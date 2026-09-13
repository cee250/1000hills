#!/usr/bin/env python3
"""Give the 36 hand-built ("rich") demos a working mobile navigation.

Several of them ship a hamburger button with no script behind it, or hide the
dashboard sidebar on small screens with nothing to replace it. This injects a
small, self-contained drawer (CSS + JS) so navigation works on every phone and
tablet. Files that already have a working drawer are left untouched.

Run:  python3 scripts/patch_rich_mobile.py
"""
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from demo_data import catalogue                                  # noqa: E402

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "demos")
MARK = "/* 1000hills-mobile-nav */"

SITE_CSS = MARK + """
.mh-scrim,.mh-panel,.mh-burger{display:none}
@media (max-width:960px){
  .nav-links{display:none !important}
  .hamburger{display:none !important}
  .mh-burger{
    display:grid !important;place-items:center;width:42px;height:42px;flex:none;
    border-radius:12px;border:1px solid rgba(201,169,110,.4);background:rgba(201,169,110,.14);
    color:#E8D5A3;font-size:1rem;cursor:pointer;margin-left:auto;transition:.2s;
  }
  .mh-burger:hover{background:rgba(201,169,110,.26)}
  .mh-scrim{
    display:block;position:fixed;inset:0;background:rgba(4,10,20,.62);
    backdrop-filter:blur(3px);-webkit-backdrop-filter:blur(3px);
    z-index:9990;opacity:0;visibility:hidden;transition:opacity .3s ease,visibility .3s ease;
  }
  .mh-panel{
    display:flex;flex-direction:column;gap:5px;position:fixed;top:0;right:0;bottom:0;
    width:min(330px,88vw);z-index:9995;background:#0A1628;
    border-left:1px solid rgba(201,169,110,.35);
    padding:18px 18px calc(20px + env(safe-area-inset-bottom));
    overflow-y:auto;transform:translateX(103%);
    transition:transform .34s cubic-bezier(.22,1,.36,1);box-shadow:-24px 0 70px rgba(0,0,0,.55);
  }
  body.mh-open .mh-scrim{opacity:1;visibility:visible}
  body.mh-open .mh-panel{transform:none}
  body.mh-open{overflow:hidden}
  .mh-head{display:flex;align-items:center;justify-content:space-between;gap:10px;margin-bottom:12px}
  .mh-brand{color:#E8D5A3;font-weight:800;font-size:.95rem;display:flex;align-items:center;gap:9px;min-width:0}
  .mh-brand span{overflow:hidden;text-overflow:ellipsis;white-space:nowrap}
  .mh-x{background:rgba(255,255,255,.08);border:0;color:#A8B9D0;width:34px;height:34px;flex:none;border-radius:10px;cursor:pointer;font-size:.85rem}
  .mh-x:hover{background:rgba(255,255,255,.16);color:#fff}
  a.mh-link{
    display:flex;align-items:center;gap:12px;padding:14px 13px;border-radius:12px;
    color:#CCD9E8;font-weight:600;font-size:.95rem;border:1px solid transparent;transition:.2s;
  }
  a.mh-link:hover,a.mh-link:active{background:rgba(201,169,110,.13);border-color:rgba(201,169,110,.35);color:#fff}
  a.mh-link i{color:#C9A96E;width:18px;text-align:center;font-size:.82rem;flex:none}
  .mh-cta{margin-top:auto;padding-top:18px;display:grid;gap:10px}
  .mh-cta a{
    display:flex;align-items:center;justify-content:center;gap:9px;padding:13px 18px;border-radius:40px;
    font-weight:800;font-size:.85rem;background:linear-gradient(135deg,#C9A96E,#E8D5A3);color:#0A1628;
  }
  .mh-cta a.ghost{background:none;border:1px solid rgba(255,255,255,.18);color:#CCD9E8}
  .mh-note{color:#7E93AF;font-size:.68rem;text-align:center;margin-top:4px}
}
@media (prefers-reduced-motion:reduce){.mh-panel,.mh-scrim{transition:none}}
"""

SITE_JS = """
<script>
/* 1000hills-mobile-nav */
(function () {
  if (window.__mhSite) return;
  window.__mhSite = true;
  var links = Array.prototype.slice.call(document.querySelectorAll('.nav-links a'));
  if (!links.length) return;
  var brandEl = document.querySelector('.brand, .logo, header a');
  var brandName = brandEl ? brandEl.textContent.trim().split('\\n')[0] : 'Menu';
  var cta = document.querySelector('header .btn, .nav .btn, .hero .btn');

  var scrim = document.createElement('div');
  scrim.className = 'mh-scrim';
  document.body.appendChild(scrim);

  var panel = document.createElement('nav');
  panel.className = 'mh-panel';
  panel.setAttribute('aria-label', 'Mobile menu');
  var items = links.map(function (a) {
    return '<a class="mh-link" href="' + a.getAttribute('href') + '"><i class="fas fa-angle-right"></i> ' +
      a.textContent.trim() + '</a>';
  }).join('');
  var ctaHtml = cta
    ? '<a href="' + cta.getAttribute('href') + '"' +
      (cta.getAttribute('target') ? ' target="' + cta.getAttribute('target') + '" rel="noopener"' : '') + '>' +
      '<i class="fab fa-whatsapp"></i> ' + cta.textContent.trim() + '</a>'
    : '';
  panel.innerHTML =
    '<div class="mh-head"><span class="mh-brand"><i class="fas fa-bolt"></i><span>' + brandName + '</span></span>' +
    '<button class="mh-x" type="button" aria-label="Close menu"><i class="fas fa-times"></i></button></div>' +
    items +
    '<div class="mh-cta">' + ctaHtml +
    '<a class="ghost" href="../demos.html"><i class="fas fa-layer-group"></i> All demos</a>' +
    '<p class="mh-note">Fictional demo business · built by 1000 Hills Group</p></div>';
  document.body.appendChild(panel);

  var host = document.querySelector('header .container, header .nav, .nav, header');
  var burger = document.createElement('button');
  burger.className = 'mh-burger';
  burger.type = 'button';
  burger.setAttribute('aria-label', 'Open menu');
  burger.setAttribute('aria-expanded', 'false');
  burger.innerHTML = '<i class="fas fa-bars"></i>';
  if (host) host.appendChild(burger); else document.body.appendChild(burger);

  function setOpen(open) {
    document.body.classList.toggle('mh-open', open);
    burger.setAttribute('aria-expanded', String(open));
  }
  burger.addEventListener('click', function () { setOpen(!document.body.classList.contains('mh-open')); });
  scrim.addEventListener('click', function () { setOpen(false); });
  panel.querySelector('.mh-x').addEventListener('click', function () { setOpen(false); });
  panel.querySelectorAll('a').forEach(function (a) { a.addEventListener('click', function () { setOpen(false); }); });
  document.addEventListener('keydown', function (e) { if (e.key === 'Escape') setOpen(false); });
  window.addEventListener('resize', function () { if (window.innerWidth > 960) setOpen(false); });
})();
</script>
"""

SYS_CSS = MARK + """
.mh-scrim,.mh-btn{display:none}
@media (max-width:1024px){
  .sidebar{
    position:fixed !important;top:46px;left:0;bottom:0;height:auto !important;
    width:min(272px,84vw) !important;display:flex !important;flex-direction:column;
    z-index:9995;transform:translateX(-103%);
    transition:transform .3s cubic-bezier(.22,1,.36,1);
    box-shadow:0 24px 60px rgba(0,0,0,.5);overflow-y:auto;
  }
  body.mh-open .sidebar{transform:none}
  body.mh-open{overflow:hidden}
  .mh-btn{
    display:grid;place-items:center;width:36px;height:36px;flex:none;border-radius:10px;
    border:1px solid var(--line,rgba(15,23,42,.14));background:var(--card,#fff);
    color:var(--muted,#475569);cursor:pointer;font-size:.9rem;transition:.2s;
  }
  .mh-btn:hover{color:var(--green,#0EA5E9);border-color:currentColor}
  .mh-scrim{
    display:block;position:fixed;inset:46px 0 0;background:rgba(6,13,26,.58);
    backdrop-filter:blur(2px);-webkit-backdrop-filter:blur(2px);
    z-index:9990;opacity:0;visibility:hidden;transition:opacity .28s ease,visibility .28s ease;
  }
  body.mh-open .mh-scrim{opacity:1;visibility:visible}
  .app{display:block}
  .main,.content,main{min-width:0}
  .kpis{grid-template-columns:repeat(2,1fr) !important}
  .panels,.grid-2,.grid-3,.pos{grid-template-columns:1fr !important}
  .topbar{padding:10px 14px !important;gap:10px !important}
  .content,.main > div{padding-left:14px !important;padding-right:14px !important}
  .tscroll,.table-panel{overflow-x:auto;-webkit-overflow-scrolling:touch}
}
@media (max-width:620px){
  .kpis{grid-template-columns:1fr !important}
  .tb-search{display:none !important}
}
@media (prefers-reduced-motion:reduce){.sidebar,.mh-scrim{transition:none}}
"""

SYS_JS = """
<script>
/* 1000hills-mobile-nav */
(function () {
  if (window.__mhSys) return;
  window.__mhSys = true;
  var sidebar = document.querySelector('.sidebar');
  if (!sidebar) return;

  var scrim = document.createElement('div');
  scrim.className = 'mh-scrim';
  document.body.appendChild(scrim);

  var btn = document.createElement('button');
  btn.className = 'mh-btn';
  btn.type = 'button';
  btn.setAttribute('aria-label', 'Open menu');
  btn.setAttribute('aria-expanded', 'false');
  btn.innerHTML = '<i class="fas fa-bars"></i>';
  var host = document.querySelector('.topbar') || document.querySelector('.main') || document.body;
  if (host.firstChild) host.insertBefore(btn, host.firstChild); else host.appendChild(btn);

  function setOpen(open) {
    document.body.classList.toggle('mh-open', open);
    btn.setAttribute('aria-expanded', String(open));
  }
  btn.addEventListener('click', function () { setOpen(!document.body.classList.contains('mh-open')); });
  scrim.addEventListener('click', function () { setOpen(false); });
  sidebar.addEventListener('click', function (e) {
    if (e.target.closest('a')) setOpen(false);
  });
  document.addEventListener('keydown', function (e) { if (e.key === 'Escape') setOpen(false); });
  window.addEventListener('resize', function () { if (window.innerWidth > 1024) setOpen(false); });
})();
</script>
"""


def already_works(src):
    """True when the page already wires up its own mobile nav (script or inline handler)."""
    if MARK in src:
        return True
    return bool(re.search(r"classList\.toggle\(\s*['\"](?:open|nav-open|menu-open)['\"]", src) or
                re.search(r"classList\.(?:add|contains)\(\s*['\"]open['\"]", src))


def patch(path):
    src = open(path, encoding="utf-8").read()
    if already_works(src):
        return "skip (already has mobile nav)"

    is_system = ("class=\"sidebar\"" in src or re.search(r"\.sidebar\s*\{", src)) and "<aside" in src
    if is_system:
        css, js, name = SYS_CSS, SYS_JS, "system"
    elif ".nav-links" in src:
        css, js, name = SITE_CSS, SITE_JS, "site"
    else:
        return "skip (no recognisable nav)"

    src = src.replace("</style>", css + "\n</style>", 1)
    src = src.replace("</body>", js + "\n</body>", 1)
    open(path, "w", encoding="utf-8").write(src)
    return "patched (" + name + ")"


def main():
    systems, sites = catalogue()
    regenerated = {d["file"] for d in systems} | {d["file"] for d in sites}
    files = sorted(f for f in os.listdir(ROOT) if f.endswith(".html"))
    counts = {}
    for f in files:
        if f in regenerated:
            continue
        res = patch(os.path.join(ROOT, f))
        counts[res] = counts.get(res, 0) + 1
        print("%-28s %s" % (f, res))
    print("\nsummary:", counts)


if __name__ == "__main__":
    main()
