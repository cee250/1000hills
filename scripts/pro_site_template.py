#!/usr/bin/env python3
"""Shared, mobile-first template for the small-business website demos.

Shell CSS/JS live in demos/assets/ so the browser caches them once; each demo
only carries its own design tokens + content.
"""

TOKENS = r"""
:root{
  --acc:@@ACC@@;--acc-2:@@ACC2@@;--acc-ink:@@ACC_INK@@;--acc-bg:@@ACC_BG@@;--acc-line:@@ACC_LINE@@;
  --bg:@@BG@@;--bg-2:@@BG2@@;--card:@@CARD@@;--card-2:@@CARD2@@;
  --ink:@@INK@@;--muted:@@MUTED@@;--faint:@@FAINT@@;--line:@@LINE@@;--line-2:@@LINE2@@;
  --ok:#10B981;--warn:#F59E0B;
  --nav-bg:@@NAV_BG@@;
  --r:14px;--r-l:20px;--r-xl:28px;
  --sh:0 18px 44px -22px rgba(0,0,0,.55);
  --sh-l:0 34px 80px -30px rgba(0,0,0,.65);
  --bar:46px;--head:66px;
  --wrap:min(1140px,92vw);
  --font:'Inter',-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,sans-serif;
  --display:@@DISPLAY_FONT@@;
}
"""

CSS = r"""
*,*::before,*::after{margin:0;padding:0;box-sizing:border-box}
html{-webkit-text-size-adjust:100%;scroll-behavior:smooth;scroll-padding-top:calc(var(--bar) + var(--head) + 14px)}
body{
  font-family:var(--font);background:var(--bg);color:var(--ink);
  line-height:1.65;font-size:16px;padding-top:var(--bar);overflow-x:hidden;
  -webkit-font-smoothing:antialiased;
}
a{text-decoration:none;color:inherit}
ul{list-style:none}
img,svg{display:block;max-width:100%}
button,input,select,textarea{font-family:inherit;font-size:inherit;color:inherit}
h1,h2,h3,h4{font-family:var(--display);line-height:1.14;letter-spacing:-.5px;font-weight:700}
:focus-visible{outline:2px solid var(--acc);outline-offset:3px;border-radius:6px}
::selection{background:var(--acc);color:var(--acc-ink)}
.wrap{width:var(--wrap);margin-inline:auto}
section{padding:clamp(48px,7vw,86px) 0;position:relative}
.sr{position:absolute;width:1px;height:1px;overflow:hidden;clip:rect(0 0 0 0);white-space:nowrap}

/* ---------- 1000 Hills demo bar ---------- */
.demo-bar{
  position:fixed;top:0;left:0;right:0;height:var(--bar);z-index:9999;
  background:#0A1628;color:#E8D5A3;display:flex;align-items:center;justify-content:space-between;
  gap:10px;padding:0 clamp(10px,2.4vw,20px);border-bottom:1px solid rgba(201,169,110,.35);
  transition:transform .3s ease;
}
.demo-bar.hidden{transform:translateY(-100%)}
.db-left{display:flex;align-items:center;gap:8px;font-size:.76rem;font-weight:600;min-width:0}
.db-left i{color:#C9A96E;flex:none}
.db-left a:hover{color:#fff}
.db-left .sep{color:rgba(232,213,163,.5);flex:none}
.db-left .kind{color:rgba(232,213,163,.72);font-weight:500;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.db-right{display:flex;align-items:center;gap:8px;flex:none}
.db-cta{
  background:linear-gradient(135deg,#C9A96E,#E8D5A3);color:#0A1628;font-size:.72rem;font-weight:800;
  padding:7px 14px;border-radius:30px;white-space:nowrap;box-shadow:0 4px 14px rgba(201,169,110,.28);transition:.2s;
}
.db-cta:hover{transform:translateY(-1px);box-shadow:0 8px 20px rgba(201,169,110,.4)}
.db-close{
  background:rgba(255,255,255,.07);border:0;color:#A8B9D0;cursor:pointer;width:28px;height:28px;
  border-radius:8px;display:grid;place-items:center;font-size:.8rem;transition:.2s;
}
.db-close:hover{background:rgba(255,255,255,.16);color:#fff}

/* ---------- header ---------- */
.site-head{
  position:sticky;top:var(--bar);z-index:900;background:var(--nav-bg);
  backdrop-filter:blur(14px);-webkit-backdrop-filter:blur(14px);
  border-bottom:1px solid var(--line);transition:box-shadow .3s,padding .3s;
}
.site-head.stuck{box-shadow:0 12px 34px -20px rgba(0,0,0,.8)}
.head-in{width:var(--wrap);margin-inline:auto;display:flex;align-items:center;gap:16px;min-height:var(--head)}
.brand{display:flex;align-items:center;gap:11px;font-weight:800;font-family:var(--display);font-size:1.02rem;letter-spacing:-.3px;min-width:0}
.brand .bic{
  width:40px;height:40px;flex:none;border-radius:12px;display:grid;place-items:center;font-size:1rem;
  background:linear-gradient(135deg,var(--acc),var(--acc-2));color:@@BRAND_ICON_COLOR@@;
  box-shadow:0 10px 24px -12px var(--acc);
}
.brand b{white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.site-nav{display:flex;align-items:center;gap:clamp(14px,2vw,28px);margin-left:auto}
.site-nav a{font-size:.9rem;font-weight:600;color:var(--muted);position:relative;padding:6px 0;transition:.2s}
.site-nav a::after{content:'';position:absolute;left:0;right:100%;bottom:0;height:2px;background:var(--acc);transition:.28s;border-radius:2px}
.site-nav a:hover{color:var(--ink)}
.site-nav a:hover::after{right:0}
.head-cta{display:flex;align-items:center;gap:10px;margin-left:8px}
.btn{
  display:inline-flex;align-items:center;justify-content:center;gap:9px;
  padding:12px 22px;border-radius:40px;font-weight:700;font-size:.88rem;border:1px solid transparent;
  cursor:pointer;transition:.24s;white-space:nowrap;
}
.btn i{font-size:.86rem}
.btn-a{background:linear-gradient(135deg,var(--acc),var(--acc-2));color:var(--acc-ink);box-shadow:0 14px 30px -14px var(--acc)}
.btn-a:hover{transform:translateY(-2px);box-shadow:0 20px 40px -16px var(--acc)}
.btn-b{border-color:var(--line-2);color:var(--ink);background:transparent}
.btn-b:hover{border-color:var(--acc);color:var(--acc);background:var(--acc-bg)}
.burger{
  display:none;width:44px;height:44px;border-radius:12px;border:1px solid var(--line);
  background:var(--card);cursor:pointer;place-items:center;flex:none;margin-left:auto;
}
.burger span{display:block;width:19px;height:2px;background:var(--ink);border-radius:2px;transition:.28s;position:relative}
.burger span+span{margin-top:5px}
body.menu-open .burger span:nth-child(1){transform:translateY(7px) rotate(45deg)}
body.menu-open .burger span:nth-child(2){opacity:0}
body.menu-open .burger span:nth-child(3){transform:translateY(-7px) rotate(-45deg)}
.drawer{
  position:fixed;top:var(--bar);right:0;bottom:0;width:min(340px,86vw);z-index:950;
  background:var(--bg-2);border-left:1px solid var(--line);padding:22px;
  transform:translateX(103%);transition:transform .34s cubic-bezier(.22,1,.36,1);
  display:flex;flex-direction:column;gap:6px;overflow-y:auto;box-shadow:var(--sh-l);
}
body.menu-open .drawer{transform:none}
.drawer a{
  display:flex;align-items:center;gap:12px;padding:14px 14px;border-radius:12px;
  font-weight:700;font-size:1rem;color:var(--ink);border:1px solid transparent;transition:.2s;
}
.drawer a i{color:var(--acc);width:20px;text-align:center;font-size:.95rem}
.drawer a:hover,.drawer a:active{background:var(--acc-bg);border-color:var(--acc-line)}
.drawer .d-foot{margin-top:auto;padding-top:20px;display:grid;gap:10px}
.drawer .d-foot small{color:var(--muted);font-size:.76rem;text-align:center}
.scrim{
  position:fixed;inset:var(--bar) 0 0;background:rgba(4,10,20,.6);backdrop-filter:blur(3px);
  z-index:940;opacity:0;visibility:hidden;transition:.3s;
}
body.menu-open .scrim{opacity:1;visibility:visible}

/* ---------- hero ---------- */
.hero{padding:clamp(44px,7vw,84px) 0 clamp(48px,7vw,88px);background:var(--herobg,var(--bg));overflow:hidden}
.hero::before{
  content:'';position:absolute;inset:-20% -10% auto auto;width:min(620px,80vw);aspect-ratio:1;
  background:radial-gradient(circle at 50% 50%,var(--acc-bg),transparent 62%);pointer-events:none;
}
.hero-grid{display:grid;grid-template-columns:1.05fr .95fr;gap:clamp(26px,4vw,54px);align-items:center;position:relative}
.kicker{
  display:inline-flex;align-items:center;gap:9px;padding:7px 15px;border-radius:40px;
  border:1px solid var(--acc-line);background:var(--acc-bg);color:var(--acc);
  font-size:.72rem;font-weight:800;letter-spacing:1.4px;text-transform:uppercase;
}
.hero h1{font-size:clamp(2.1rem,6.1vw,3.7rem);margin:18px 0 14px;max-width:17ch}
.hero h1 em{font-style:normal;color:var(--acc);position:relative}
.hero .lead{color:var(--muted);font-size:clamp(.98rem,2.2vw,1.09rem);max-width:52ch}
.hero-cta{display:flex;gap:12px;flex-wrap:wrap;margin-top:28px}
.hero-stats{display:flex;gap:clamp(18px,3.4vw,40px);flex-wrap:wrap;margin-top:34px;padding-top:26px;border-top:1px solid var(--line)}
.hero-stats div{min-width:0}
.hero-stats strong{display:block;font-family:var(--display);font-size:clamp(1.25rem,3.4vw,1.7rem);color:var(--acc);line-height:1.1;letter-spacing:-.6px}
.hero-stats span{font-size:.74rem;color:var(--muted);letter-spacing:.4px;text-transform:uppercase;font-weight:700}

/* hero visual */
.visual{position:relative;min-height:clamp(280px,42vw,420px)}
.vcard{
  position:absolute;background:var(--card);border:1px solid var(--line);border-radius:var(--r-l);
  padding:18px;box-shadow:var(--sh-l);
}
.vmain{inset:0 8% 12% 0;display:flex;flex-direction:column;gap:14px;overflow:hidden}
.vmain .vhead{display:flex;align-items:center;gap:12px}
.vmain .vhead .bic{width:44px;height:44px;border-radius:13px;display:grid;place-items:center;background:linear-gradient(135deg,var(--acc),var(--acc-2));color:@@BRAND_ICON_COLOR@@;font-size:1.05rem;flex:none}
.vmain .vhead h4{font-size:.98rem;font-family:var(--font);font-weight:800;letter-spacing:-.2px}
.vmain .vhead small{color:var(--muted);font-size:.72rem;display:flex;align-items:center;gap:6px}
.vmain .vhead small i{color:var(--warn)}
.vrow{display:flex;align-items:center;gap:11px;padding:11px 13px;border-radius:12px;background:var(--card-2);border:1px solid var(--line)}
.vrow i{color:var(--acc);width:18px;text-align:center;flex:none}
.vrow b{font-size:.82rem;display:block;line-height:1.3}
.vrow small{color:var(--muted);font-size:.68rem}
.vrow .tagm{margin-left:auto;font-size:.62rem;font-weight:800;padding:4px 10px;border-radius:20px;background:var(--acc-bg);color:var(--acc);white-space:nowrap}
.vbadge{
  right:-2%;bottom:2%;width:min(200px,52%);padding:14px 16px;
  background:linear-gradient(135deg,var(--acc),var(--acc-2));color:var(--acc-ink);border:0;
}
.vbadge strong{font-family:var(--display);font-size:1.5rem;display:block;letter-spacing:-.6px;line-height:1}
.vbadge span{font-size:.7rem;font-weight:700;opacity:.9}
.vpill{left:-4%;top:12%;padding:10px 15px;display:flex;align-items:center;gap:9px;font-size:.76rem;font-weight:700}
.vpill i{color:var(--ok)}

/* ---------- marquee strip ---------- */
.strip{background:var(--card);border-block:1px solid var(--line);padding:16px 0;overflow:hidden}
.strip-in{display:flex;gap:clamp(24px,5vw,58px);align-items:center;width:max-content;animation:slide 34s linear infinite}
.strip:hover .strip-in{animation-play-state:paused}
.strip span{display:inline-flex;align-items:center;gap:9px;font-size:.8rem;font-weight:700;color:var(--muted);white-space:nowrap}
.strip span i{color:var(--acc)}
@keyframes slide{to{transform:translateX(-50%)}}

/* ---------- section heads ---------- */
.shead{max-width:640px;margin-bottom:clamp(26px,4vw,44px)}
.shead.center{margin-inline:auto;text-align:center}
.shead h2{font-size:clamp(1.6rem,4.4vw,2.4rem);margin:14px 0 10px}
.shead p{color:var(--muted);font-size:clamp(.92rem,2.2vw,1rem)}
.rule{width:56px;height:3px;border-radius:3px;background:linear-gradient(90deg,var(--acc),var(--acc-2));margin-bottom:14px}
.shead.center .rule{margin-inline:auto}

/* ---------- cards ---------- */
.cards{display:grid;grid-template-columns:repeat(auto-fit,minmax(min(250px,100%),1fr));gap:18px}
.card{
  background:var(--card);border:1px solid var(--line);border-radius:var(--r-l);padding:26px;
  transition:.3s;position:relative;overflow:hidden;
}
.card::after{content:'';position:absolute;inset:auto 0 0 0;height:3px;background:linear-gradient(90deg,var(--acc),var(--acc-2));transform:scaleX(0);transform-origin:left;transition:.35s}
.card:hover{transform:translateY(-6px);border-color:var(--acc-line);box-shadow:var(--sh)}
.card:hover::after{transform:scaleX(1)}
.card .cic{
  width:50px;height:50px;border-radius:15px;display:grid;place-items:center;font-size:1.15rem;
  background:var(--acc-bg);color:var(--acc);border:1px solid var(--acc-line);margin-bottom:16px;
}
.card h3{font-size:1.06rem;margin-bottom:7px;font-family:var(--font);font-weight:800}
.card p{color:var(--muted);font-size:.9rem}

/* ---------- split / about ---------- */
.split{display:grid;grid-template-columns:1fr 1fr;gap:clamp(24px,4.4vw,56px);align-items:center}
.checklist{display:grid;gap:12px;margin-top:24px}
.checklist li{display:flex;gap:12px;align-items:flex-start;font-size:.94rem;font-weight:600}
.checklist i{
  width:24px;height:24px;flex:none;border-radius:8px;display:grid;place-items:center;
  background:var(--acc-bg);color:var(--acc);font-size:.66rem;margin-top:2px;
}
.artstack{display:grid;gap:14px}
.art{
  border-radius:var(--r-l);border:1px solid var(--line);background:var(--card);
  padding:22px;display:flex;align-items:center;gap:16px;box-shadow:var(--sh);position:relative;overflow:hidden;
}
.art::before{
  content:'';position:absolute;inset:0 auto 0 0;width:4px;
  background:linear-gradient(180deg,var(--acc),var(--acc-2));
}
.art i.big{
  width:56px;height:56px;flex:none;border-radius:16px;display:grid;place-items:center;font-size:1.35rem;
  background:var(--acc-bg);color:var(--acc);border:1px solid var(--acc-line);
}
.art h4{font-size:1rem;font-family:var(--font);font-weight:800}
.art p{color:var(--muted);font-size:.85rem;margin-top:3px}
.art.alt{background:linear-gradient(135deg,var(--acc),var(--acc-2));border:0;color:var(--acc-ink)}
.art.alt::before{background:rgba(255,255,255,.4)}
.art.alt i.big{background:rgba(255,255,255,.2);color:var(--acc-ink);border-color:rgba(255,255,255,.3)}
.art.alt p{color:rgba(255,255,255,.82)}

/* ---------- gallery ---------- */
.gal{display:grid;grid-template-columns:repeat(auto-fit,minmax(min(210px,100%),1fr));gap:14px}
.gtile{
  position:relative;border-radius:var(--r-l);overflow:hidden;border:1px solid var(--line);
  aspect-ratio:4/3;background:var(--card-2);display:grid;place-items:center;transition:.3s;cursor:pointer;
}
.gtile::before{
  content:'';position:absolute;inset:0;
  background:
    radial-gradient(circle at 22% 18%,var(--acc-bg),transparent 55%),
    repeating-linear-gradient(135deg,rgba(255,255,255,.035) 0 12px,transparent 12px 24px);
}
.gtile i{font-size:2.1rem;color:var(--acc);position:relative;transition:.35s}
.gtile figcaption{
  position:absolute;left:0;right:0;bottom:0;padding:14px;font-size:.8rem;font-weight:700;
  background:linear-gradient(transparent,rgba(0,0,0,.62));color:#fff;text-align:left;
}
.gtile:hover{transform:translateY(-5px);border-color:var(--acc-line);box-shadow:var(--sh)}
.gtile:hover i{transform:scale(1.14)}

/* ---------- testimonials ---------- */
.quotes{display:grid;grid-template-columns:repeat(auto-fit,minmax(min(280px,100%),1fr));gap:18px}
.quote{background:var(--card);border:1px solid var(--line);border-radius:var(--r-l);padding:26px;position:relative;transition:.3s}
.quote:hover{transform:translateY(-5px);box-shadow:var(--sh);border-color:var(--acc-line)}
.quote .qm{color:var(--acc);opacity:.25;font-size:2.1rem;line-height:1;margin-bottom:8px}
.quote p{font-size:.94rem;color:var(--ink)}
.quote .who{display:flex;align-items:center;gap:12px;margin-top:18px;padding-top:16px;border-top:1px solid var(--line)}
.quote .av{width:40px;height:40px;border-radius:50%;display:grid;place-items:center;background:linear-gradient(135deg,var(--acc),var(--acc-2));color:var(--acc-ink);font-weight:800;font-size:.8rem;flex:none}
.quote .who b{font-size:.86rem;display:block}
.quote .who small{color:var(--muted);font-size:.72rem}
.stars{margin-left:auto;color:var(--warn);font-size:.68rem;display:flex;gap:2px}

/* ---------- hours + form ---------- */
.contact{display:grid;grid-template-columns:.9fr 1.1fr;gap:clamp(20px,3.6vw,40px);align-items:start}
.infobox{background:var(--card);border:1px solid var(--line);border-radius:var(--r-l);padding:26px;display:grid;gap:18px}
.irow{display:flex;gap:14px;align-items:flex-start}
.irow i{width:40px;height:40px;flex:none;border-radius:12px;display:grid;place-items:center;background:var(--acc-bg);color:var(--acc);font-size:.95rem}
.irow b{font-size:.9rem;display:block}
.irow span{color:var(--muted);font-size:.84rem}
.map{
  border-radius:var(--r);height:132px;border:1px solid var(--line);position:relative;overflow:hidden;background:var(--card-2);
  background-image:linear-gradient(var(--line) 1px,transparent 1px),linear-gradient(90deg,var(--line) 1px,transparent 1px);
  background-size:26px 26px;
}
.map::after{
  content:'';position:absolute;left:50%;top:46%;width:16px;height:16px;border-radius:50%;
  background:var(--acc);transform:translate(-50%,-50%);box-shadow:0 0 0 6px var(--acc-bg),0 0 0 14px var(--acc-bg);
}
.map span{position:absolute;left:50%;bottom:12px;transform:translateX(-50%);font-size:.7rem;font-weight:800;background:var(--card);border:1px solid var(--line);padding:4px 11px;border-radius:20px}
form.book{background:var(--card);border:1px solid var(--line);border-radius:var(--r-l);padding:26px;display:grid;gap:14px}
.f2{display:grid;grid-template-columns:1fr 1fr;gap:14px}
label.fl{display:grid;gap:7px;font-size:.78rem;font-weight:700;color:var(--muted)}
label.fl input,label.fl select,label.fl textarea{
  background:var(--card-2);border:1px solid var(--line);border-radius:11px;padding:12px 14px;
  font-size:.9rem;outline:none;transition:.2s;width:100%;color:var(--ink);
}
label.fl textarea{min-height:96px;resize:vertical}
label.fl input:focus,label.fl select:focus,label.fl textarea:focus{border-color:var(--acc);box-shadow:0 0 0 3px var(--acc-bg);background:var(--card)}
.form-note{font-size:.74rem;color:var(--muted);display:flex;gap:8px;align-items:flex-start}
.form-note i{color:var(--acc);margin-top:3px}

/* ---------- CTA ---------- */
.cta{background:var(--card-2);border-block:1px solid var(--line);text-align:center}
.cta h2{font-size:clamp(1.7rem,5vw,2.6rem);margin-bottom:12px}
.cta p{color:var(--muted);max-width:52ch;margin:0 auto 26px}
.cta-btns{display:flex;gap:12px;justify-content:center;flex-wrap:wrap}

/* ---------- footer ---------- */
.site-foot{background:var(--bg-2);border-top:1px solid var(--line);padding:clamp(38px,6vw,60px) 0 26px}
.foot-grid{display:grid;grid-template-columns:1.5fr 1fr 1fr;gap:clamp(22px,4vw,44px)}
.foot-grid p{color:var(--muted);font-size:.88rem;margin-top:14px;max-width:42ch}
.foot-grid h5{font-size:.76rem;letter-spacing:1.6px;text-transform:uppercase;color:var(--acc);margin-bottom:14px;font-family:var(--font);font-weight:800}
.foot-grid ul{display:grid;gap:9px}
.foot-grid ul a,.foot-grid ul span{color:var(--muted);font-size:.88rem;display:inline-flex;gap:9px;align-items:center;transition:.2s}
.foot-grid ul a:hover{color:var(--acc)}
.foot-grid ul i{width:16px;color:var(--acc);font-size:.8rem}
.socials{display:flex;gap:9px;margin-top:18px}
.socials a{width:38px;height:38px;border-radius:11px;border:1px solid var(--line);display:grid;place-items:center;color:var(--muted);transition:.24s}
.socials a:hover{background:var(--acc);border-color:var(--acc);color:var(--acc-ink);transform:translateY(-3px)}
.foot-bot{
  margin-top:clamp(26px,4vw,42px);padding-top:20px;border-top:1px solid var(--line);
  display:flex;justify-content:space-between;gap:12px;flex-wrap:wrap;color:var(--muted);font-size:.8rem;
}
.foot-bot a{color:var(--acc);font-weight:700}

/* ---------- floating whatsapp + top ---------- */
.fab{
  position:fixed;right:clamp(14px,3vw,26px);bottom:clamp(14px,3vw,26px);z-index:800;
  width:54px;height:54px;border-radius:50%;display:grid;place-items:center;
  background:#25D366;color:#fff;font-size:1.4rem;box-shadow:0 16px 34px -12px rgba(37,211,102,.75);
  transition:.25s;
}
.fab:hover{transform:translateY(-4px) scale(1.05)}
.fab::after{content:'';position:absolute;inset:0;border-radius:50%;border:2px solid #25D366;animation:ring 2.4s ease-out infinite}
@keyframes ring{0%{transform:scale(1);opacity:.7}100%{transform:scale(1.6);opacity:0}}
.totop{
  position:fixed;left:clamp(14px,3vw,26px);bottom:clamp(14px,3vw,26px);z-index:800;
  width:44px;height:44px;border-radius:50%;display:grid;place-items:center;border:1px solid var(--line);
  background:var(--card);color:var(--muted);cursor:pointer;opacity:0;visibility:hidden;transition:.28s;
}
.totop.show{opacity:1;visibility:visible}
.totop:hover{color:var(--acc);border-color:var(--acc)}

/* ---------- toast ---------- */
.toast{
  position:fixed;left:50%;bottom:24px;transform:translate(-50%,150%);z-index:10000;
  background:#0A1628;color:#fff;font-size:.82rem;font-weight:600;padding:13px 20px;border-radius:13px;
  box-shadow:var(--sh-l);display:flex;align-items:center;gap:10px;max-width:calc(100vw - 28px);
  transition:transform .38s cubic-bezier(.22,1,.36,1);border:1px solid rgba(201,169,110,.4);
}
.toast.show{transform:translate(-50%,0)}
.toast i{color:#E8D5A3}

/* ---------- reveal ---------- */
.rv{opacity:0;transform:translateY(18px);transition:opacity .6s ease,transform .6s cubic-bezier(.22,1,.36,1)}
.rv.in{opacity:1;transform:none}

/* ---------- responsive ---------- */
@media (max-width:1024px){
  .hero-grid{grid-template-columns:1fr;gap:34px}
  .visual{min-height:320px;max-width:520px}
  .vmain{inset:0 4% 14% 0}
  .contact{grid-template-columns:1fr}
  .foot-grid{grid-template-columns:1fr 1fr}
}
@media (max-width:900px){
  .site-nav,.head-cta{display:none}
  .burger{display:grid}
}
@media (max-width:760px){
  .split{grid-template-columns:1fr}
  .foot-grid{grid-template-columns:1fr;gap:26px}
  .hero-stats{gap:20px}
  .hero-stats div{flex:1 1 30%}
}
@media (max-width:560px){
  body{font-size:15px}
  .f2{grid-template-columns:1fr}
  .card,.infobox,form.book,.quote{padding:20px}
  .visual{min-height:300px}
  .vmain{inset:0 0 16% 0;padding:15px}
  .vmain > :nth-child(4){display:none}
  .vrow{padding:9px 11px}
  .vpill{left:0;top:4%}
  .vbadge{right:0;width:60%}
  .db-left .kind{display:none}
  .db-cta{padding:6px 11px;font-size:.68rem}
  .btn{padding:12px 18px;font-size:.85rem;width:100%}
  .hero-cta .btn,.cta-btns .btn{width:100%}
  .cta-btns{flex-direction:column}
  .gal{grid-template-columns:1fr 1fr;gap:10px}
  .gtile{aspect-ratio:1}
  .gtile i{font-size:1.6rem}
  .fab{width:50px;height:50px;font-size:1.25rem}
}
@media (max-width:380px){
  .gal{grid-template-columns:1fr}
  .hero-stats div{flex:1 1 100%}
}
@media (prefers-reduced-motion:reduce){
  *,*::before,*::after{animation-duration:.001ms!important;animation-iteration-count:1!important;transition-duration:.001ms!important}
  html{scroll-behavior:auto}
  .rv{opacity:1;transform:none}
  .strip-in{animation:none}
}
"""

JS = r"""
(function () {
  'use strict';
  var body = document.body;

  /* ---- mobile drawer ---- */
  var burger = document.getElementById('burger');
  var scrim = document.getElementById('scrim');
  function setMenu(open) {
    body.classList.toggle('menu-open', open);
    if (burger) burger.setAttribute('aria-expanded', String(open));
    body.style.overflow = open ? 'hidden' : '';
  }
  if (burger) burger.addEventListener('click', function () { setMenu(!body.classList.contains('menu-open')); });
  if (scrim) scrim.addEventListener('click', function () { setMenu(false); });
  document.querySelectorAll('.drawer a').forEach(function (a) {
    a.addEventListener('click', function () { setMenu(false); });
  });
  document.addEventListener('keydown', function (e) { if (e.key === 'Escape') setMenu(false); });

  /* ---- demo bar close ---- */
  var dbClose = document.getElementById('dbClose');
  if (dbClose) dbClose.addEventListener('click', function () {
    document.getElementById('demoBar').classList.add('hidden');
    body.style.paddingTop = '0';
    document.documentElement.style.setProperty('--bar', '0px');
  });

  /* ---- sticky header shadow + back to top ---- */
  var head = document.getElementById('siteHead');
  var top = document.getElementById('toTop');
  var ticking = false;
  function onScroll() {
    var y = window.pageYOffset || document.documentElement.scrollTop;
    if (head) head.classList.toggle('stuck', y > 12);
    if (top) top.classList.toggle('show', y > 600);
    ticking = false;
  }
  window.addEventListener('scroll', function () {
    if (!ticking) { ticking = true; window.requestAnimationFrame(onScroll); }
  }, { passive: true });
  onScroll();
  if (top) top.addEventListener('click', function () {
    window.scrollTo({ top: 0, behavior: window.matchMedia('(prefers-reduced-motion: reduce)').matches ? 'auto' : 'smooth' });
  });

  /* ---- toast ---- */
  var toastEl = document.getElementById('toast'), toastMsg = document.getElementById('toastMsg'), tTimer;
  function toast(msg) {
    if (!toastEl) return;
    toastMsg.textContent = msg;
    toastEl.classList.add('show');
    clearTimeout(tTimer);
    tTimer = setTimeout(function () { toastEl.classList.remove('show'); }, 2800);
  }
  document.addEventListener('click', function (e) {
    var t = e.target.closest('[data-toast]');
    if (t) toast(t.getAttribute('data-toast'));
  });

  /* ---- demo enquiry form ---- */
  var form = document.getElementById('bookForm');
  if (form) form.addEventListener('submit', function (e) {
    e.preventDefault();
    var name = (form.querySelector('[name=name]') || {}).value || '';
    toast('Thanks ' + (name ? name.split(' ')[0] : '') + '! In the live site this sends to your inbox + WhatsApp.');
    form.reset();
  });

  /* ---- reveal on scroll ---- */
  var rvs = document.querySelectorAll('.rv');
  if ('IntersectionObserver' in window) {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) {
        if (en.isIntersecting) {
          var d = parseInt(en.target.getAttribute('data-delay') || '0', 10);
          setTimeout(function () { en.target.classList.add('in'); }, d);
          io.unobserve(en.target);
        }
      });
    }, { rootMargin: '0px 0px -6% 0px', threshold: 0.06 });
    rvs.forEach(function (el) { io.observe(el); });
  } else {
    rvs.forEach(function (el) { el.classList.add('in'); });
  }

  /* ---- duplicate marquee content for a seamless loop ---- */
  var strip = document.querySelector('.strip-in');
  if (strip) strip.innerHTML += strip.innerHTML;

  /* ---- active nav link while scrolling ---- */
  var links = Array.prototype.slice.call(document.querySelectorAll('.site-nav a[href^="#"]'));
  var targets = links.map(function (a) { return document.querySelector(a.getAttribute('href')); });
  if ('IntersectionObserver' in window && targets.some(Boolean)) {
    var no = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) {
        if (!en.isIntersecting) return;
        var i = targets.indexOf(en.target);
        if (i < 0) return;
        links.forEach(function (l) { l.style.color = ''; });
        links[i].style.color = 'var(--acc)';
      });
    }, { rootMargin: '-45% 0px -50% 0px' });
    targets.forEach(function (t) { if (t) no.observe(t); });
  }
})();
"""

HTML = r"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8"/>
<meta name="viewport" content="width=device-width, initial-scale=1.0, viewport-fit=cover"/>
<title>@@TITLE@@</title>
<meta name="description" content="@@META_DESC@@"/>
<meta name="robots" content="index, follow"/>
<meta name="theme-color" content="@@BG@@"/>
<link rel="icon" href="@@FAVICON@@"/>
<link rel="preconnect" href="https://fonts.googleapis.com"/>
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin/>
<link rel="preconnect" href="https://cdnjs.cloudflare.com" crossorigin/>
<link href="@@FONT_URL@@" rel="stylesheet"/>
<link rel="preload" as="style" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.0/css/all.min.css" onload="this.rel='stylesheet'"/>
<noscript><link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.0/css/all.min.css"/></noscript>
<link rel="stylesheet" href="assets/pro-site.css"/>
<style>@@TOKENS@@</style>
</head>
<body>

<!-- 1000 Hills Group demo bar -->
<div class="demo-bar" id="demoBar">
  <div class="db-left">
    <i class="fas fa-bolt" aria-hidden="true"></i>
    <a href="../demos.html">1000 Hills Group</a>
    <span class="sep">·</span>
    <span class="kind">Live website demo — @@NAME@@</span>
  </div>
  <div class="db-right">
    <a class="db-cta" href="@@WA_URL@@" target="_blank" rel="noopener">Get a site like this</a>
    <button class="db-close" id="dbClose" type="button" aria-label="Close demo bar"><i class="fas fa-times" aria-hidden="true"></i></button>
  </div>
</div>

<!-- header -->
<header class="site-head" id="siteHead">
  <div class="head-in">
    <a class="brand" href="#top"><span class="bic"><i class="fas @@ICON@@" aria-hidden="true"></i></span><b>@@NAME@@</b></a>
    <nav class="site-nav" aria-label="Main">@@NAV@@</nav>
    <div class="head-cta">
      <a class="btn btn-a" href="@@WA_URL@@" target="_blank" rel="noopener"><i class="fab fa-whatsapp" aria-hidden="true"></i> @@BTN@@</a>
    </div>
    <button class="burger" id="burger" type="button" aria-label="Open menu" aria-expanded="false" aria-controls="drawer">
      <span></span><span></span><span></span>
    </button>
  </div>
</header>

<div class="scrim" id="scrim"></div>
<nav class="drawer" id="drawer" aria-label="Mobile">
  @@DRAWER@@
  <div class="d-foot">
    <a class="btn btn-a" href="@@WA_URL@@" target="_blank" rel="noopener"><i class="fab fa-whatsapp" aria-hidden="true"></i> @@BTN@@</a>
    <a class="btn btn-b" href="#contact"><i class="fas fa-phone" aria-hidden="true"></i> Call @@PHONE@@</a>
    <small>@@NAME@@ · @@PLACE@@ — fictional demo by 1000 Hills Group</small>
  </div>
</nav>

<main id="top">

  <!-- hero -->
  <section class="hero" style="--herobg:@@HERO_BG@@">
    <div class="wrap hero-grid">
      <div class="rv">
        <span class="kicker"><i class="fas fa-location-dot" aria-hidden="true"></i> @@PLACE@@ · @@TAGLINE@@</span>
        <h1>@@H1@@</h1>
        <p class="lead">@@LEAD@@</p>
        <div class="hero-cta">
          <a class="btn btn-a" href="@@WA_URL@@" target="_blank" rel="noopener"><i class="fab fa-whatsapp" aria-hidden="true"></i> @@BTN@@</a>
          <a class="btn btn-b" href="#@@NAV1_ID@@"><i class="fas @@NAV1_ICON@@" aria-hidden="true"></i> @@NAV1@@</a>
        </div>
        <div class="hero-stats">@@STATS@@</div>
      </div>
      <div class="visual rv" data-delay="120">
        <div class="vcard vmain">
          <div class="vhead">
            <span class="bic"><i class="fas @@ICON@@" aria-hidden="true"></i></span>
            <div>
              <h4>@@NAME@@</h4>
              <small><i class="fas fa-star" aria-hidden="true"></i> @@RATING@@ · @@REVIEW_COUNT@@ reviews · @@PLACE@@</small>
            </div>
          </div>
          @@VISUAL_ROWS@@
        </div>
        <div class="vcard vpill"><i class="fas fa-circle-check" aria-hidden="true"></i> @@PILL_TEXT@@</div>
        <div class="vcard vbadge"><strong>@@BADGE_BIG@@</strong><span>@@BADGE_SMALL@@</span></div>
      </div>
    </div>
  </section>

  <!-- marquee -->
  <div class="strip" aria-hidden="true"><div class="strip-in">@@STRIP@@</div></div>

  <!-- cards -->
  <section id="@@CARDS_ID@@">
    <div class="wrap">
      <div class="shead center rv">
        <div class="rule"></div>
        <span class="kicker"><i class="fas @@ICON@@" aria-hidden="true"></i> @@CARDS_KICKER@@</span>
        <h2>@@H2@@</h2>
        <p>@@CARDS_SUB@@</p>
      </div>
      <div class="cards">@@CARDS@@</div>
    </div>
  </section>

  <!-- about -->
  <section id="about" style="background:var(--bg-2)">
    <div class="wrap split">
      <div class="rv">
        <div class="rule"></div>
        <span class="kicker"><i class="fas fa-heart" aria-hidden="true"></i> @@ABOUT_KICKER@@</span>
        <h2 style="font-size:clamp(1.55rem,4.2vw,2.3rem);margin:14px 0 12px">@@ABOUT_H@@</h2>
        <p style="color:var(--muted)">@@ABOUT@@</p>
        <ul class="checklist">@@LIST@@</ul>
        <div class="hero-cta" style="margin-top:26px">
          <a class="btn btn-b" href="#contact"><i class="fas fa-calendar-check" aria-hidden="true"></i> @@BTN@@</a>
        </div>
      </div>
      <div class="artstack rv" data-delay="120">@@ARTS@@</div>
    </div>
  </section>

  <!-- gallery -->
  <section id="gallery">
    <div class="wrap">
      <div class="shead rv">
        <div class="rule"></div>
        <span class="kicker"><i class="fas fa-images" aria-hidden="true"></i> @@GAL_KICKER@@</span>
        <h2>@@GAL_H@@</h2>
        <p>@@GAL_SUB@@</p>
      </div>
      <div class="gal">@@GALLERY@@</div>
    </div>
  </section>

  <!-- testimonials -->
  <section style="background:var(--bg-2)">
    <div class="wrap">
      <div class="shead center rv">
        <div class="rule"></div>
        <span class="kicker"><i class="fas fa-quote-left" aria-hidden="true"></i> Reviews</span>
        <h2>What people say</h2>
        <p>Sample testimonials — we wire in your real Google and WhatsApp reviews.</p>
      </div>
      <div class="quotes">@@QUOTES@@</div>
    </div>
  </section>

  <!-- contact -->
  <section id="contact">
    <div class="wrap">
      <div class="shead rv">
        <div class="rule"></div>
        <span class="kicker"><i class="fas fa-paper-plane" aria-hidden="true"></i> Get in touch</span>
        <h2>@@CTA_H@@</h2>
        <p>@@CTA_P@@</p>
      </div>
      <div class="contact">
        <div class="infobox rv">
          <div class="irow"><i class="fas fa-location-dot" aria-hidden="true"></i><div><b>Find us</b><span>@@ADDRESS@@</span></div></div>
          <div class="irow"><i class="fas fa-clock" aria-hidden="true"></i><div><b>Opening hours</b><span>@@HOURS@@</span></div></div>
          <div class="irow"><i class="fas fa-phone" aria-hidden="true"></i><div><b>Call or WhatsApp</b><span>@@PHONE@@</span></div></div>
          <div class="irow"><i class="fas fa-credit-card" aria-hidden="true"></i><div><b>We accept</b><span>@@PAYMENTS@@</span></div></div>
          <div class="map"><span>@@PLACE@@, Kigali</span></div>
        </div>
        <form class="book rv" id="bookForm" data-delay="120" novalidate>
          <div class="f2">
            <label class="fl">Your name<input type="text" name="name" placeholder="e.g. Aline Uwase" required/></label>
            <label class="fl">Phone<input type="tel" name="phone" placeholder="+250 7XX XXX XXX" required/></label>
          </div>
          <div class="f2">
            <label class="fl">@@FORM_FIELD@@<input type="text" name="when" placeholder="@@FORM_PLACEHOLDER@@"/></label>
            <label class="fl">People<select name="pax">@@PAX@@</select></label>
          </div>
          <label class="fl">Message<textarea name="msg" placeholder="Tell us what you need…"></textarea></label>
          <button class="btn btn-a" type="submit"><i class="fas fa-paper-plane" aria-hidden="true"></i> Send request</button>
          <p class="form-note"><i class="fas fa-circle-info" aria-hidden="true"></i> Demo form — in your live site this delivers to your email, WhatsApp and admin dashboard instantly.</p>
        </form>
      </div>
    </div>
  </section>

  <!-- cta -->
  <section class="cta">
    <div class="wrap rv">
      <h2>@@CTA_H@@</h2>
      <p>@@CTA_P@@</p>
      <div class="cta-btns">
        <a class="btn btn-a" href="@@WA_URL@@" target="_blank" rel="noopener"><i class="fab fa-whatsapp" aria-hidden="true"></i> @@BTN@@</a>
        <a class="btn btn-b" href="../demos.html"><i class="fas fa-layer-group" aria-hidden="true"></i> See more demos</a>
      </div>
    </div>
  </section>
</main>

<!-- footer -->
<footer class="site-foot">
  <div class="wrap">
    <div class="foot-grid">
      <div>
        <a class="brand" href="#top"><span class="bic"><i class="fas @@ICON@@" aria-hidden="true"></i></span><b>@@NAME@@</b></a>
        <p>@@FOOTER_ABOUT@@</p>
        <div class="socials">
          <a href="#" aria-label="Instagram" data-toast="Instagram feed embeds are available on every site we build."><i class="fab fa-instagram" aria-hidden="true"></i></a>
          <a href="#" aria-label="Facebook" data-toast="Facebook page integration + pixel included."><i class="fab fa-facebook-f" aria-hidden="true"></i></a>
          <a href="@@WA_URL@@" target="_blank" rel="noopener" aria-label="WhatsApp"><i class="fab fa-whatsapp" aria-hidden="true"></i></a>
        </div>
      </div>
      <div>
        <h5>Explore</h5>
        <ul>@@FOOT_NAV@@</ul>
      </div>
      <div>
        <h5>Visit</h5>
        <ul>
          <li><span><i class="fas fa-location-dot" aria-hidden="true"></i> @@ADDRESS@@</span></li>
          <li><span><i class="fas fa-phone" aria-hidden="true"></i> @@PHONE@@</span></li>
          <li><span><i class="fas fa-clock" aria-hidden="true"></i> @@HOURS_SHORT@@</span></li>
        </ul>
      </div>
    </div>
    <div class="foot-bot">
      <span>© @@YEAR@@ @@NAME@@ — fictional demo business</span>
      <span>Designed &amp; built by <a href="../demos.html">1000 Hills Group</a></span>
    </div>
  </div>
</footer>

<a class="fab" href="@@WA_URL@@" target="_blank" rel="noopener" aria-label="Chat on WhatsApp"><i class="fab fa-whatsapp" aria-hidden="true"></i></a>
<button class="totop" id="toTop" type="button" aria-label="Back to top"><i class="fas fa-arrow-up" aria-hidden="true"></i></button>
<div class="toast" id="toast" role="status" aria-live="polite"><i class="fas fa-circle-info" aria-hidden="true"></i><span id="toastMsg"></span></div>

<script src="assets/pro-site.js" defer></script>
</body>
</html>
"""
