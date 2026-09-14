#!/usr/bin/node
/* Regenerate the demo card thumbnails in demos/img/thumbs/.
 *
 * Every demo card on demos.html shows a real screenshot of the demo
 * ("how it looks inside") before the live preview loads. This script
 * captures the top 1280x794 of each demos/*.html page — exactly the
 * region the card iframe displays — and writes it as a 640px-wide
 * WebP (deviceScaleFactor 0.5), ~15 KB each.
 *
 * Dependencies (one-off, not needed to serve the site):
 *   npm i puppeteer-core @sparticuz/chromium @fortawesome/fontawesome-free sharp \
 *       @fontsource/inter @fontsource/playfair-display @fontsource/poppins \
 *       @fontsource/syne @fontsource/space-grotesk @fontsource/sora \
 *       @fontsource/quicksand @fontsource/plus-jakarta-sans @fontsource/lora \
 *       @fontsource/lato @fontsource/outfit @fontsource/dm-serif-display \
 *       @fontsource/nunito @fontsource/merriweather @fontsource/karla \
 *       @fontsource/marcellus @fontsource/manrope @fontsource/libre-baskerville \
 *       @fontsource/source-sans-3 @fontsource/fraunces @fontsource/nunito-sans \
 *       @fontsource/cormorant @fontsource/jost @fontsource/cormorant-garamond \
 *       @fontsource/public-sans @fontsource/montserrat @fontsource/chakra-petch \
 *       @fontsource/archivo @fontsource/barlow-condensed @fontsource/anton
 *
 * The demo pages load Google Fonts + Font Awesome from CDNs. If those are
 * unreachable (offline CI, firewalled env) the script mirrors them from the
 * local node_modules above via request interception, so thumbnails render
 * with the real fonts and icons.
 *
 * Usage:  node scripts/shoot_thumbs.js [demo.html ...]   (default: all)
 */
'use strict';
const http = require('http');
const fs = require('fs');
const path = require('path');
const puppeteer = require('puppeteer-core');
const chromium = require('@sparticuz/chromium');

const ROOT = path.join(__dirname, '..');
const OUT = path.join(ROOT, 'demos', 'img', 'thumbs');
const NM = path.join(ROOT, 'node_modules');

/* ---------- tiny static server for the repo (no external deps) ---------- */
const MIME = { '.html': 'text/html', '.css': 'text/css', '.js': 'text/javascript',
               '.webp': 'image/webp', '.png': 'image/png', '.jpg': 'image/jpeg',
               '.svg': 'image/svg+xml', '.json': 'application/json', '.ico': 'image/x-icon' };
const server = http.createServer((req, res) => {
  const rel = decodeURIComponent(req.url.split('?')[0]).replace(/^\/+/, '');
  const file = path.join(ROOT, rel);
  if (!file.startsWith(ROOT) || !fs.existsSync(file) || !fs.statSync(file).isFile()) {
    res.writeHead(404); res.end('nope'); return;
  }
  res.writeHead(200, { 'content-type': MIME[path.extname(file)] || 'application/octet-stream' });
  fs.createReadStream(file).pipe(res);
});

/* ---------- font mirror: @fontsource packages -> fonts.googleapis.com ---------- */
const fontFiles = new Map(); // basename -> abs path (latin + latin-ext only)
if (fs.existsSync(path.join(NM, '@fontsource'))) {
  for (const pkg of fs.readdirSync(path.join(NM, '@fontsource'))) {
    const dir = path.join(NM, '@fontsource', pkg, 'files');
    if (!fs.existsSync(dir)) continue;
    for (const f of fs.readdirSync(dir)) {
      if (/^([a-z0-9-]+)-(latin|latin-ext)-(\d{3,4})-(normal|italic)\.woff2$/.test(f) && !fontFiles.has(f)) {
        fontFiles.set(f, path.join(dir, f));
      }
    }
  }
}
const kebab = s => s.trim().toLowerCase().replace(/[^a-z0-9]+/g, '-').replace(/^-|-$/g, '');
function gfontsCss(urlStr) {
  const u = new URL(urlStr);
  const fams = [...u.searchParams].filter(([k]) => k === 'family').map(([, v]) => v.split(':')[0].trim());
  let css = '/* local @fontsource mirror */\n';
  for (const fam of fams) {
    const pre = kebab(fam) + '-';
    for (const [base, p] of fontFiles) {
      if (!base.startsWith(pre)) continue;
      const m = base.match(/^([a-z0-9-]+)-(latin|latin-ext)-(\d{3,4})-(normal|italic)\.woff2$/);
      if (m) css += `@font-face{font-family:'${fam}';font-style:${m[4]};font-weight:${m[3]};font-display:swap;src:url(https://fontsource.local/${base}) format('woff2');}\n`;
    }
  }
  return css;
}
const FA = path.join(NM, '@fortawesome', 'fontawesome-free');
const FONT_MIME = { '.woff2': 'font/woff2', '.woff': 'font/woff', '.ttf': 'font/ttf', '.eot': 'application/vnd.ms-fontobject' };

async function makePage(browser, origin) {
  const page = await browser.newPage();
  await page.setRequestInterception(true);
  page.on('request', req => {
    const url = req.url();
    try {
      if (url.startsWith(origin + '/') || url.startsWith('data:') || url.startsWith('blob:')) {
        req.continue();
      } else if (url.startsWith('https://fonts.googleapis.com/css2')) {
        req.respond({ status: 200, contentType: 'text/css', body: gfontsCss(url) });
      } else if (url.startsWith('https://fontsource.local/')) {
        const p = fontFiles.get(url.replace('https://fontsource.local/', ''));
        p ? req.respond({ status: 200, contentType: 'font/woff2', body: fs.readFileSync(p) }) : req.abort();
      } else if (url.includes('/font-awesome/') && url.endsWith('/css/all.min.css') && fs.existsSync(path.join(FA, 'css/all.min.css'))) {
        req.respond({ status: 200, contentType: 'text/css', body: fs.readFileSync(path.join(FA, 'css/all.min.css')) });
      } else if (url.includes('/font-awesome/') && url.includes('/webfonts/') && fs.existsSync(FA)) {
        const f = url.split('/webfonts/')[1];
        const p = path.join(FA, 'webfonts', f);
        fs.existsSync(p) ? req.respond({ status: 200, contentType: FONT_MIME[path.extname(p)] || 'font/woff2', body: fs.readFileSync(p) }) : req.abort();
      } else if (url.startsWith('https://') || url.startsWith('http://')) {
        req.continue(); // let it through when the network allows the real CDNs
      } else {
        req.continue();
      }
    } catch (e) { /* page closed */ }
  });
  return page;
}

async function shoot(page, origin, file) {
  const base = path.basename(file, '.html');
  const out = path.join(OUT, base + '.webp');
  await page.setViewport({ width: 1280, height: 794, deviceScaleFactor: 0.5 });
  await page.goto(origin + '/demos/' + path.basename(file), { waitUntil: 'networkidle0', timeout: 45000 });
  await page.addStyleTag({ content: '*,*::before,*::after{animation:none !important;transition:none !important;scroll-behavior:auto !important}' });
  await page.evaluate(() => document.fonts.ready);
  await new Promise(r => setTimeout(r, 350));
  await page.screenshot({ path: out, type: 'webp', quality: 75 });
  return fs.statSync(out).size;
}

(async () => {
  await new Promise(r => server.listen(0, '127.0.0.1', r));
  const origin = 'http://127.0.0.1:' + server.address().port;
  fs.mkdirSync(OUT, { recursive: true });

  const all = fs.readdirSync(path.join(ROOT, 'demos')).filter(f => f.endsWith('.html'));
  const wanted = process.argv.slice(2).length ? process.argv.slice(2) : all;
  const list = wanted.filter(f => all.includes(f));
  console.log('capturing', list.length, 'demo thumbnails ->', path.relative(ROOT, OUT));

  const browser = await puppeteer.launch({ executablePath: await chromium.executablePath(), args: [...chromium.args, '--no-sandbox', '--disable-dev-shm-usage'], headless: true });
  const CONC = 5;
  const results = [], errors = [];
  let idx = 0;
  async function worker() {
    const page = await makePage(browser, origin);
    while (idx < list.length) {
      const f = list[idx++];
      try { results.push({ file: f, bytes: await shoot(page, origin, f) }); }
      catch (e) { errors.push({ file: f, err: String(e.message).slice(0, 200) }); }
    }
    await page.close();
  }
  await Promise.all(Array.from({ length: CONC }, worker));
  await browser.close();
  server.close();

  const total = results.reduce((s, r) => s + r.bytes, 0);
  console.log(`OK: ${results.length}  FAILED: ${errors.length}  total: ${(total / 1048576).toFixed(2)} MB`);
  if (errors.length) { console.error(JSON.stringify(errors, null, 2)); process.exit(1); }
})().catch(e => { console.error(e); process.exit(1); });
