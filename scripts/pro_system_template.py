#!/usr/bin/env python3
"""Professional, fully-responsive app-shell template used for every
management-system demo page.

Shared CSS/JS live in demos/assets/ so the browser downloads them once and
caches them across all 60 system demos. Only the design tokens are inlined.
"""

TOKENS = r"""/* Per-demo design tokens — injected inline by the generator. */
:root{
  --acc:@@ACC@@;--acc-2:@@ACC2@@;--acc-ink:@@ACC_INK@@;
  --side:@@SIDE@@;--side-2:@@SIDE2@@;--side-ink:@@SIDE_INK@@;--side-muted:@@SIDE_MUTED@@;
  --bg:@@BG@@;--card:#FFFFFF;--card-2:@@CARD2@@;
  --ink:@@INK@@;--muted:@@MUTED@@;--faint:@@FAINT@@;
  --line:@@LINE@@;--line-2:@@LINE2@@;
  --ok:@@OK@@;--warn:@@WARN@@;--bad:@@BAD@@;--info:@@INFO@@;
  --ok-bg:@@OK_BG@@;--warn-bg:@@WARN_BG@@;--bad-bg:@@BAD_BG@@;--info-bg:@@INFO_BG@@;
  --acc-bg:@@ACC_BG@@;
  --acc-light:@@ACC_LIGHT@@;--acc-fade:@@ACC_FADE@@;
  --ok-light:@@OK_LIGHT@@;--warn-light:@@WARN_LIGHT@@;--bad-light:@@BAD_LIGHT@@;
  --r-s:8px;--r:12px;--r-l:16px;--r-xl:22px;
  --sh-s:0 1px 2px rgba(15,23,42,.05),0 1px 3px rgba(15,23,42,.05);
  --sh:0 6px 18px -8px rgba(15,23,42,.18),0 2px 6px -2px rgba(15,23,42,.08);
  --sh-l:0 22px 48px -20px rgba(15,23,42,.32);
  --bar:46px;--font:'Inter',-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,sans-serif;
}
"""

CSS = r"""*,*::before,*::after{margin:0;padding:0;box-sizing:border-box}
html{-webkit-text-size-adjust:100%}
body{
  font-family:var(--font);background:var(--bg);color:var(--ink);
  font-size:14px;line-height:1.55;padding-top:var(--bar);
  -webkit-font-smoothing:antialiased;overflow-x:hidden;
}
a{text-decoration:none;color:inherit}
ul{list-style:none}
button,input,select{font-family:inherit;font-size:inherit;color:inherit}
img,svg{display:block;max-width:100%}
:focus-visible{outline:2px solid var(--acc);outline-offset:2px;border-radius:4px}
::selection{background:var(--acc);color:var(--acc-ink)}

/* ---------- 1000 Hills demo bar ---------- */
.demo-bar{
  position:fixed;top:0;left:0;right:0;height:var(--bar);z-index:9999;
  background:#0A1628;color:#E8D5A3;
  display:flex;align-items:center;justify-content:space-between;gap:10px;
  padding:0 clamp(10px,2.4vw,20px);
  border-bottom:1px solid rgba(201,169,110,.35);
  transition:transform .3s ease;
}
.demo-bar.hidden{transform:translateY(-100%)}
.db-left{display:flex;align-items:center;gap:8px;font-size:.76rem;font-weight:600;min-width:0}
.db-left i{color:#C9A96E;flex:none}
.db-left a{color:#E8D5A3;white-space:nowrap}
.db-left a:hover{color:#fff}
.db-left .sep{color:rgba(232,213,163,.5);flex:none}
.db-left .kind{color:rgba(232,213,163,.72);font-weight:500;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.db-right{display:flex;align-items:center;gap:8px;flex:none}
.db-cta{
  background:linear-gradient(135deg,#C9A96E,#E8D5A3);color:#0A1628;
  font-size:.72rem;font-weight:800;padding:7px 14px;border-radius:30px;white-space:nowrap;
  box-shadow:0 4px 14px rgba(201,169,110,.28);transition:.2s;
}
.db-cta:hover{transform:translateY(-1px);box-shadow:0 8px 20px rgba(201,169,110,.4)}
.db-close{
  background:rgba(255,255,255,.07);border:0;color:#A8B9D0;cursor:pointer;
  width:28px;height:28px;border-radius:8px;display:grid;place-items:center;font-size:.8rem;transition:.2s;
}
.db-close:hover{background:rgba(255,255,255,.16);color:#fff}

/* ---------- shell ---------- */
.app{display:flex;align-items:flex-start;min-height:calc(100vh - var(--bar))}
.scrim{
  position:fixed;inset:var(--bar) 0 0;background:rgba(8,15,28,.55);
  backdrop-filter:blur(2px);z-index:80;opacity:0;visibility:hidden;transition:.28s ease;
}
body.nav-open .scrim{opacity:1;visibility:visible}

.sidebar{
  width:246px;flex:none;background:linear-gradient(180deg,var(--side),var(--side-2));
  color:var(--side-ink);position:sticky;top:var(--bar);
  height:calc(100vh - var(--bar));display:flex;flex-direction:column;z-index:90;
  border-right:1px solid rgba(255,255,255,.06);
}
.s-logo{display:flex;align-items:center;gap:11px;padding:18px 16px;border-bottom:1px solid rgba(255,255,255,.07)}
.s-logo .ic{
  width:38px;height:38px;flex:none;border-radius:11px;display:grid;place-items:center;font-size:1rem;
  background:linear-gradient(135deg,var(--acc),var(--acc-2));color:var(--acc-ink);
  box-shadow:0 6px 16px -6px var(--acc);
}
.s-logo h4{font-size:.94rem;font-weight:800;color:#fff;line-height:1.2;letter-spacing:-.2px}
.s-logo small{display:block;font-size:.58rem;letter-spacing:1.8px;text-transform:uppercase;color:var(--side-muted);font-weight:700;margin-top:2px}
.s-nav{padding:12px 10px;flex:1;overflow-y:auto;overscroll-behavior:contain;scrollbar-width:thin}
.s-nav::-webkit-scrollbar{width:5px}
.s-nav::-webkit-scrollbar-thumb{background:rgba(255,255,255,.14);border-radius:9px}
.s-label{font-size:.58rem;letter-spacing:1.9px;text-transform:uppercase;color:var(--side-muted);font-weight:800;padding:14px 12px 7px}
.s-nav a{
  display:flex;align-items:center;gap:11px;padding:10px 12px;border-radius:10px;
  font-size:.84rem;font-weight:500;color:var(--side-ink);margin-bottom:2px;transition:.2s;position:relative;
}
.s-nav a i{width:18px;text-align:center;font-size:.88rem;opacity:.85;flex:none}
.s-nav a:hover{background:rgba(255,255,255,.07);color:#fff}
.s-nav a.on{background:linear-gradient(90deg,var(--acc),var(--acc-fade));color:var(--acc-ink);font-weight:700;box-shadow:0 8px 20px -10px var(--acc)}
.s-nav a.on i{opacity:1}
.s-nav a .n-badge{
  margin-left:auto;background:rgba(255,255,255,.16);color:inherit;
  font-size:.6rem;font-weight:800;padding:2px 7px;border-radius:20px;
}
.s-nav a.on .n-badge{background:rgba(0,0,0,.18)}
.s-plan{margin:10px;padding:14px;border-radius:var(--r);background:rgba(255,255,255,.06);border:1px solid rgba(255,255,255,.09)}
.s-plan p{font-size:.7rem;color:var(--side-ink);font-weight:600;line-height:1.45}
.s-plan .meter{height:5px;border-radius:6px;background:rgba(255,255,255,.14);margin:9px 0 7px;overflow:hidden}
.s-plan .meter i{display:block;height:100%;border-radius:6px;background:linear-gradient(90deg,var(--acc),var(--acc-2))}
.s-plan small{font-size:.62rem;color:var(--side-muted)}
.s-plan a{
  display:block;margin-top:11px;text-align:center;background:var(--acc);color:var(--acc-ink);
  font-size:.7rem;font-weight:800;padding:8px;border-radius:8px;transition:.2s;
}
.s-plan a:hover{filter:brightness(1.08)}
.s-user{display:flex;align-items:center;gap:10px;padding:13px 15px;border-top:1px solid rgba(255,255,255,.07)}
.s-user .av{
  width:34px;height:34px;flex:none;border-radius:50%;display:grid;place-items:center;
  background:linear-gradient(135deg,var(--acc),var(--acc-2));color:var(--acc-ink);font-weight:800;font-size:.74rem;
}
.s-user h6{font-size:.78rem;color:#fff;font-weight:700;line-height:1.2}
.s-user span{font-size:.64rem;color:var(--side-muted)}

/* ---------- main ---------- */
.main{flex:1;min-width:0;display:flex;flex-direction:column}
.topbar{
  position:sticky;top:var(--bar);z-index:70;
  background:rgba(255,255,255,.86);backdrop-filter:blur(12px);-webkit-backdrop-filter:blur(12px);
  border-bottom:1px solid var(--line);
  display:flex;align-items:center;gap:12px;padding:11px clamp(14px,2.2vw,24px);
}
.icon-btn{
  width:36px;height:36px;flex:none;border-radius:10px;border:1px solid var(--line);
  background:var(--card);color:var(--muted);cursor:pointer;display:grid;place-items:center;
  font-size:.9rem;transition:.2s;position:relative;
}
.icon-btn:hover{color:var(--acc);border-color:var(--acc);background:var(--acc-bg)}
.menu-btn{display:none}
.dot-alert::after{
  content:'';position:absolute;top:7px;right:8px;width:7px;height:7px;border-radius:50%;
  background:var(--bad);border:2px solid var(--card);
}
.tb-title{min-width:0}
.tb-title h1{font-size:1rem;font-weight:800;letter-spacing:-.3px;line-height:1.2;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.tb-title .crumb{font-size:.66rem;color:var(--muted);display:flex;align-items:center;gap:5px;margin-top:2px}
.tb-title .crumb i{font-size:.5rem;color:var(--faint)}
.tb-search{
  margin-left:auto;display:flex;align-items:center;gap:9px;background:var(--card-2);
  border:1px solid var(--line);border-radius:30px;padding:8px 15px;width:min(280px,32vw);transition:.2s;
}
.tb-search:focus-within{border-color:var(--acc);box-shadow:0 0 0 3px var(--acc-bg);background:var(--card)}
.tb-search i{color:var(--faint);font-size:.8rem;flex:none}
.tb-search input{border:0;background:none;outline:none;width:100%;font-size:.8rem;min-width:0}
.tb-search input::placeholder{color:var(--faint)}
.tb-search kbd{
  font-family:inherit;font-size:.6rem;color:var(--faint);border:1px solid var(--line);
  border-radius:5px;padding:1px 5px;background:var(--card);flex:none;
}
.tb-right{display:flex;align-items:center;gap:8px;margin-left:auto}
.tb-search+.tb-right{margin-left:0}
.tb-me{display:flex;align-items:center;gap:9px;padding:4px 10px 4px 4px;border-radius:30px;border:1px solid var(--line);background:var(--card);cursor:pointer;transition:.2s}
.tb-me:hover{border-color:var(--acc)}
.tb-me .av{width:28px;height:28px;border-radius:50%;background:linear-gradient(135deg,var(--acc),var(--acc-2));color:var(--acc-ink);display:grid;place-items:center;font-size:.66rem;font-weight:800;flex:none}
.tb-me b{font-size:.76rem;font-weight:700;display:block;line-height:1.15}
.tb-me span{font-size:.62rem;color:var(--muted)}

.content{padding:clamp(14px,2.2vw,24px);display:flex;flex-direction:column;gap:16px;flex:1}
.page-head{display:flex;align-items:flex-end;justify-content:space-between;gap:14px;flex-wrap:wrap}
.page-head .ph-l{min-width:0}
.page-head h2{font-size:clamp(1.15rem,2.6vw,1.5rem);font-weight:800;letter-spacing:-.5px;line-height:1.2}
.page-head p{font-size:.82rem;color:var(--muted);margin-top:4px;max-width:62ch}
.page-head .ph-r{display:flex;gap:8px;flex-wrap:wrap;align-items:center}
.btn{
  display:inline-flex;align-items:center;justify-content:center;gap:8px;
  padding:10px 17px;border-radius:10px;font-size:.8rem;font-weight:700;border:1px solid transparent;
  cursor:pointer;transition:.2s;white-space:nowrap;
}
.btn i{font-size:.78rem}
.btn-a{background:linear-gradient(135deg,var(--acc),var(--acc-2));color:var(--acc-ink);box-shadow:0 8px 20px -10px var(--acc)}
.btn-a:hover{transform:translateY(-1px);box-shadow:0 12px 26px -10px var(--acc)}
.btn-b{background:var(--card);border-color:var(--line);color:var(--ink)}
.btn-b:hover{border-color:var(--acc);color:var(--acc);background:var(--acc-bg)}
.seg{display:inline-flex;background:var(--card);border:1px solid var(--line);border-radius:10px;padding:3px;gap:2px}
.seg button{border:0;background:none;padding:7px 13px;border-radius:8px;font-size:.74rem;font-weight:700;color:var(--muted);cursor:pointer;transition:.2s}
.seg button.on{background:var(--acc-bg);color:var(--acc)}

/* ---------- KPI cards ---------- */
.kpis{display:grid;grid-template-columns:repeat(4,1fr);gap:14px}
.kpi{
  background:var(--card);border:1px solid var(--line);border-radius:var(--r-l);padding:16px;
  position:relative;overflow:hidden;box-shadow:var(--sh-s);transition:.25s;
}
.kpi:hover{transform:translateY(-3px);box-shadow:var(--sh);border-color:var(--line-2)}
.kpi::after{content:'';position:absolute;inset:0 auto 0 0;width:3px;background:var(--acc);opacity:.85}
.kpi.k-warn::after{background:var(--warn)}.kpi.k-bad::after{background:var(--bad)}.kpi.k-ok::after{background:var(--ok)}.kpi.k-info::after{background:var(--info)}
.kpi-top{display:flex;align-items:center;justify-content:space-between;gap:10px}
.kpi-ic{width:36px;height:36px;border-radius:11px;display:grid;place-items:center;font-size:.9rem;background:var(--acc-bg);color:var(--acc)}
.k-warn .kpi-ic{background:var(--warn-bg);color:var(--warn)}
.k-bad .kpi-ic{background:var(--bad-bg);color:var(--bad)}
.k-ok .kpi-ic{background:var(--ok-bg);color:var(--ok)}
.k-info .kpi-ic{background:var(--info-bg);color:var(--info)}
.delta{font-size:.66rem;font-weight:800;padding:3px 8px;border-radius:20px;display:inline-flex;align-items:center;gap:4px;white-space:nowrap}
.delta.up{background:var(--ok-bg);color:var(--ok)}
.delta.down{background:var(--bad-bg);color:var(--bad)}
.delta.flat{background:var(--card-2);color:var(--muted)}
.kpi b{display:block;font-size:clamp(1.3rem,2.5vw,1.65rem);font-weight:800;letter-spacing:-.7px;line-height:1.15;margin-top:11px}
.kpi span{font-size:.72rem;color:var(--muted);font-weight:600}
.spark{margin-top:10px;height:30px}
.spark svg{width:100%;height:30px;overflow:visible}
.spark path.ln{fill:none;stroke:var(--acc);stroke-width:2;stroke-linecap:round;stroke-linejoin:round}
.k-warn .spark path.ln{stroke:var(--warn)}.k-bad .spark path.ln{stroke:var(--bad)}
.k-ok .spark path.ln{stroke:var(--ok)}.k-info .spark path.ln{stroke:var(--info)}
.spark path.ar{stroke:none;opacity:.16}
.k-warn .spark path.ar{fill:var(--warn)}.k-bad .spark path.ar{fill:var(--bad)}
.k-ok .spark path.ar{fill:var(--ok)}.k-info .spark path.ar{fill:var(--info)}
.spark path.ar{fill:var(--acc)}

/* ---------- panels ---------- */
.grid-2{display:grid;grid-template-columns:1.6fr 1fr;gap:16px;align-items:start}
.grid-3{display:grid;grid-template-columns:repeat(3,1fr);gap:16px;align-items:start}
.panel{background:var(--card);border:1px solid var(--line);border-radius:var(--r-l);box-shadow:var(--sh-s);overflow:hidden}
.p-head{display:flex;align-items:center;justify-content:space-between;gap:12px;padding:15px 18px;border-bottom:1px solid var(--line);flex-wrap:wrap}
.p-head h3{font-size:.92rem;font-weight:800;letter-spacing:-.2px}
.p-head small{display:block;font-size:.68rem;color:var(--muted);font-weight:500;margin-top:2px}
.p-head .p-tools{display:flex;align-items:center;gap:8px}
.p-link{font-size:.72rem;font-weight:700;color:var(--acc);background:none;border:0;cursor:pointer;display:inline-flex;align-items:center;gap:6px}
.p-link:hover{text-decoration:underline}
.p-body{padding:18px}

/* bar chart */
.chart{display:flex;align-items:flex-end;gap:clamp(5px,1.2vw,12px);height:190px;padding-top:6px}
.col{flex:1;display:flex;flex-direction:column;align-items:center;gap:8px;min-width:0;height:100%;justify-content:flex-end;position:relative}
.col .bar{
  width:100%;max-width:34px;border-radius:7px 7px 4px 4px;position:relative;
  background:linear-gradient(180deg,var(--acc),var(--acc-light));
  height:0;transition:height .8s cubic-bezier(.22,1,.36,1);cursor:pointer;
}
.col.hi .bar{background:linear-gradient(180deg,var(--acc-2),var(--acc))}
.col .bar:hover{filter:brightness(1.06)}
.col .bar::after{
  content:attr(data-v);position:absolute;bottom:calc(100% + 7px);left:50%;transform:translateX(-50%) translateY(4px);
  background:var(--ink);color:#fff;font-size:.62rem;font-weight:700;padding:3px 8px;border-radius:6px;
  white-space:nowrap;opacity:0;pointer-events:none;transition:.2s;
}
.col .bar:hover::after{opacity:1;transform:translateX(-50%) translateY(0)}
.col small{font-size:.62rem;color:var(--muted);font-weight:600;white-space:nowrap;overflow:hidden;text-overflow:ellipsis;max-width:100%}
.chart-foot{display:flex;align-items:center;justify-content:space-between;gap:12px;margin-top:14px;padding-top:13px;border-top:1px dashed var(--line-2);flex-wrap:wrap}
.legend{display:flex;gap:14px;flex-wrap:wrap}
.legend span{display:inline-flex;align-items:center;gap:6px;font-size:.68rem;color:var(--muted);font-weight:600}
.legend i{width:9px;height:9px;border-radius:3px;background:var(--acc)}
.legend i.b{background:var(--acc-2)}
.mini-stats{display:flex;gap:18px;flex-wrap:wrap}
.mini-stats div{font-size:.68rem;color:var(--muted);font-weight:600}
.mini-stats b{display:block;font-size:.92rem;color:var(--ink);font-weight:800;letter-spacing:-.3px}

/* donut */
.donut-wrap{display:flex;align-items:center;gap:20px;flex-wrap:wrap}
.donut{
  width:132px;height:132px;flex:none;border-radius:50%;position:relative;
  background:conic-gradient(var(--acc) 0 100%);
}
.donut::after{content:'';position:absolute;inset:17px;border-radius:50%;background:var(--card);box-shadow:inset 0 0 0 1px var(--line)}
.donut b{position:absolute;inset:0;display:grid;place-items:center;font-size:1.25rem;font-weight:800;letter-spacing:-.6px;z-index:1}
.donut b em{display:block;font-size:.58rem;font-style:normal;color:var(--muted);font-weight:700;text-align:center;letter-spacing:.4px}
.dlist{flex:1;min-width:150px;display:grid;gap:10px}
.dlist div{display:flex;align-items:center;gap:9px;font-size:.76rem;font-weight:600}
.dlist i{width:9px;height:9px;border-radius:3px;flex:none}
.dlist b{margin-left:auto;font-weight:800}
.dlist span{color:var(--muted)}

/* progress list */
.plist{display:grid;gap:15px}
.plist .row{display:grid;gap:7px}
.plist .top{display:flex;align-items:center;justify-content:space-between;gap:10px;font-size:.78rem;font-weight:700}
.plist .top span{color:var(--muted);font-weight:600;font-size:.7rem}
.meter{height:7px;border-radius:8px;background:var(--card-2);overflow:hidden;border:1px solid var(--line)}
.meter i{display:block;height:100%;width:0;border-radius:8px;background:linear-gradient(90deg,var(--acc),var(--acc-2));transition:width 1s cubic-bezier(.22,1,.36,1)}
.meter i.ok{background:linear-gradient(90deg,var(--ok),var(--ok-light))}
.meter i.warn{background:linear-gradient(90deg,var(--warn),var(--warn-light))}
.meter i.bad{background:linear-gradient(90deg,var(--bad),var(--bad-light))}

/* activity */
.feed{display:grid;gap:2px}
.feed li{display:flex;gap:12px;padding:11px 0;border-bottom:1px dashed var(--line);position:relative}
.feed li:last-child{border-bottom:0;padding-bottom:0}
.feed .fav{width:32px;height:32px;flex:none;border-radius:10px;display:grid;place-items:center;font-size:.76rem;background:var(--acc-bg);color:var(--acc)}
.feed .fav.ok{background:var(--ok-bg);color:var(--ok)}
.feed .fav.warn{background:var(--warn-bg);color:var(--warn)}
.feed .fav.bad{background:var(--bad-bg);color:var(--bad)}
.feed p{font-size:.78rem;line-height:1.45}
.feed p b{font-weight:700}
.feed time{font-size:.64rem;color:var(--faint);font-weight:600;display:block;margin-top:2px}

/* kanban */
.board{display:grid;grid-template-columns:repeat(3,1fr);gap:12px}
.bcol{background:var(--card-2);border:1px solid var(--line);border-radius:var(--r);padding:11px;min-width:0}
.bcol h5{font-size:.68rem;letter-spacing:1.2px;text-transform:uppercase;color:var(--muted);font-weight:800;display:flex;align-items:center;gap:7px;margin-bottom:10px}
.bcol h5 b{margin-left:auto;background:var(--card);border:1px solid var(--line);border-radius:20px;padding:1px 8px;font-size:.62rem;color:var(--ink)}
.bcard{background:var(--card);border:1px solid var(--line);border-radius:10px;padding:11px;margin-bottom:9px;box-shadow:var(--sh-s);transition:.2s;cursor:pointer}
.bcard:last-child{margin-bottom:0}
.bcard:hover{border-color:var(--acc);transform:translateY(-2px);box-shadow:var(--sh)}
.bcard h6{font-size:.78rem;font-weight:700;line-height:1.35;margin-bottom:6px}
.bcard .meta{display:flex;align-items:center;gap:8px;flex-wrap:wrap}
.bcard .av{width:22px;height:22px;border-radius:50%;background:var(--acc-bg);color:var(--acc);display:grid;place-items:center;font-size:.55rem;font-weight:800}
.bcard time{font-size:.62rem;color:var(--faint);font-weight:600;margin-left:auto}

/* schedule */
.sched{display:grid;gap:9px}
.slot{display:flex;align-items:center;gap:12px;padding:11px 13px;border:1px solid var(--line);border-radius:var(--r);background:var(--card-2);transition:.2s}
.slot:hover{border-color:var(--acc);background:var(--acc-bg)}
.slot .t{font-size:.74rem;font-weight:800;color:var(--acc);width:52px;flex:none;letter-spacing:-.2px}
.slot .w{min-width:0;flex:1}
.slot h6{font-size:.8rem;font-weight:700;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.slot small{font-size:.66rem;color:var(--muted);display:block;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.slot .st{font-size:.6rem;font-weight:800;padding:4px 10px;border-radius:20px;white-space:nowrap;background:var(--ok-bg);color:var(--ok)}
.slot .st.w{background:var(--warn-bg);color:var(--warn)}
.slot .st.b{background:var(--bad-bg);color:var(--bad)}

/* status tiles */
.tiles{display:grid;grid-template-columns:repeat(auto-fill,minmax(140px,1fr));gap:11px}
.tile{border:1px solid var(--line);border-radius:var(--r);padding:13px;background:var(--card-2);transition:.2s;cursor:pointer;min-width:0}
.tile:hover{transform:translateY(-2px);box-shadow:var(--sh);border-color:var(--acc)}
.tile .th{display:flex;align-items:center;justify-content:space-between;gap:8px}
.tile i.lead{font-size:.9rem;color:var(--acc)}
.tile .pip{width:8px;height:8px;border-radius:50%;background:var(--ok);box-shadow:0 0 0 3px var(--ok-bg)}
.tile .pip.w{background:var(--warn);box-shadow:0 0 0 3px var(--warn-bg)}
.tile .pip.b{background:var(--bad);box-shadow:0 0 0 3px var(--bad-bg)}
.tile h6{font-size:.8rem;font-weight:800;margin-top:9px;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.tile small{font-size:.66rem;color:var(--muted);display:block;margin-top:2px;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}

/* ---------- table ---------- */
.tabs{display:flex;gap:4px;overflow-x:auto;scrollbar-width:none;padding:0 18px;border-bottom:1px solid var(--line);background:var(--card)}
.tabs::-webkit-scrollbar{display:none}
.tabs button{
  border:0;background:none;padding:12px 14px;font-size:.78rem;font-weight:700;color:var(--muted);
  cursor:pointer;white-space:nowrap;position:relative;transition:.2s;
}
.tabs button:hover{color:var(--ink)}
.tabs button.on{color:var(--acc)}
.tabs button.on::after{content:'';position:absolute;left:12px;right:12px;bottom:-1px;height:2px;background:var(--acc);border-radius:3px 3px 0 0}
.chips{display:flex;gap:7px;flex-wrap:wrap;padding:14px 18px 0}
.chip{
  font-size:.68rem;font-weight:700;padding:5px 12px;border-radius:20px;cursor:pointer;
  border:1px solid var(--line);background:var(--card-2);color:var(--muted);transition:.2s;
}
.chip:hover{border-color:var(--acc);color:var(--acc)}
.chip.on{background:var(--acc);border-color:var(--acc);color:var(--acc-ink)}
.tscroll{overflow-x:auto;-webkit-overflow-scrolling:touch}
table{width:100%;border-collapse:collapse;font-size:.8rem;min-width:520px}
th{
  text-align:left;font-size:.62rem;letter-spacing:1.3px;text-transform:uppercase;color:var(--muted);
  font-weight:800;padding:12px 18px;background:var(--card-2);border-bottom:1px solid var(--line);white-space:nowrap;
}
td{padding:13px 18px;border-bottom:1px solid var(--line);vertical-align:middle}
tbody tr{transition:.15s}
tbody tr:hover{background:var(--acc-bg)}
tbody tr:last-child td{border-bottom:0}
td.strong{font-weight:700}
.who{display:flex;align-items:center;gap:10px;min-width:0}
.who .av{width:30px;height:30px;flex:none;border-radius:9px;background:var(--acc-bg);color:var(--acc);display:grid;place-items:center;font-size:.66rem;font-weight:800}
.who .av.ai{font-size:.72rem;background:var(--card-2);border:1px solid var(--line)}
.who b{font-size:.8rem;font-weight:700;display:block;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.who small{font-size:.64rem;color:var(--muted)}
.pill{font-size:.62rem;font-weight:800;padding:4px 11px;border-radius:20px;white-space:nowrap;display:inline-flex;align-items:center;gap:5px}
.pill::before{content:'';width:5px;height:5px;border-radius:50%;background:currentColor}
.p-ok{background:var(--ok-bg);color:var(--ok)}
.p-warn{background:var(--warn-bg);color:var(--warn)}
.p-bad{background:var(--bad-bg);color:var(--bad)}
.p-info{background:var(--info-bg);color:var(--info)}
.p-mute{background:var(--card-2);color:var(--muted)}
.t-foot{display:flex;align-items:center;justify-content:space-between;gap:12px;padding:13px 18px;border-top:1px solid var(--line);flex-wrap:wrap;background:var(--card)}
.t-foot small{font-size:.7rem;color:var(--muted);font-weight:600}
.pager{display:flex;gap:5px;align-items:center}
.pager button{
  min-width:30px;height:30px;border-radius:8px;border:1px solid var(--line);background:var(--card);
  color:var(--muted);font-size:.72rem;font-weight:700;cursor:pointer;transition:.2s;padding:0 8px;
}
.pager button:hover:not(:disabled){border-color:var(--acc);color:var(--acc)}
.pager button.on{background:var(--acc);border-color:var(--acc);color:var(--acc-ink)}
.pager button:disabled{opacity:.4;cursor:not-allowed}

/* ---------- quick actions / modules ---------- */
.quick{display:grid;grid-template-columns:repeat(auto-fit,minmax(160px,1fr));gap:12px}
.qa{
  display:flex;align-items:center;gap:12px;padding:14px;border-radius:var(--r);
  background:var(--card);border:1px solid var(--line);cursor:pointer;transition:.22s;text-align:left;width:100%;
}
.qa:hover{transform:translateY(-3px);box-shadow:var(--sh);border-color:var(--acc)}
.qa i{width:34px;height:34px;flex:none;border-radius:10px;display:grid;place-items:center;background:var(--acc-bg);color:var(--acc);font-size:.85rem}
.qa b{display:block;font-size:.8rem;font-weight:700}
.qa small{font-size:.66rem;color:var(--muted)}
.mods{display:flex;gap:8px;flex-wrap:wrap}
.mods span{
  font-size:.7rem;font-weight:700;padding:7px 14px;border-radius:20px;
  background:var(--card);border:1px solid var(--line);color:var(--muted);display:inline-flex;align-items:center;gap:7px;
}
.mods span i{color:var(--acc);font-size:.68rem}

/* ---------- footer ---------- */
.sys-foot{
  margin-top:4px;padding:20px;border-radius:var(--r-l);
  background:linear-gradient(135deg,var(--side),var(--side-2));color:var(--side-ink);
  display:flex;align-items:center;justify-content:space-between;gap:16px;flex-wrap:wrap;
}
.sys-foot .fl{min-width:0}
.sys-foot h4{font-size:.95rem;color:#fff;font-weight:800;display:flex;align-items:center;gap:9px}
.sys-foot h4 i{color:var(--acc)}
.sys-foot p{font-size:.76rem;color:var(--side-muted);margin-top:5px;max-width:58ch}
.sys-foot p a{color:var(--acc);font-weight:700}
.sys-foot .fr{display:flex;gap:9px;flex-wrap:wrap}
.sys-foot .btn-a{box-shadow:none}

/* toast */
.toast{
  position:fixed;left:50%;bottom:22px;transform:translate(-50%,140%);z-index:10000;
  background:var(--ink);color:#fff;font-size:.78rem;font-weight:600;
  padding:12px 20px;border-radius:12px;box-shadow:var(--sh-l);
  display:flex;align-items:center;gap:10px;max-width:calc(100vw - 32px);transition:transform .35s cubic-bezier(.22,1,.36,1);
}
.toast.show{transform:translate(-50%,0)}
.toast i{color:var(--acc)}

/* reveal */
.rv{opacity:0;transform:translateY(14px);transition:opacity .55s ease,transform .55s cubic-bezier(.22,1,.36,1)}
.rv.in{opacity:1;transform:none}

/* ---------- responsive ---------- */
@media (max-width:1180px){
  .kpis{grid-template-columns:repeat(2,1fr)}
  .grid-2{grid-template-columns:1fr}
  .grid-3{grid-template-columns:1fr}
}
@media (max-width:1024px){
  .menu-btn{display:grid}
  .sidebar{
    position:fixed;top:var(--bar);left:0;bottom:0;height:auto;width:min(272px,84vw);
    transform:translateX(-102%);transition:transform .3s cubic-bezier(.22,1,.36,1);
    box-shadow:var(--sh-l);
  }
  body.nav-open .sidebar{transform:none}
  .tb-search{width:min(220px,30vw)}
  .board{grid-template-columns:1fr 1fr}
}
@media (max-width:860px){
  .tb-search{display:none}
  .tb-me b,.tb-me span{display:none}
  .tb-me{padding:4px}
  .board{grid-template-columns:1fr}
}
@media (max-width:700px){
  .kpis{grid-template-columns:1fr 1fr;gap:10px}
  .kpi{padding:13px}
  .spark{display:none}
  .content{gap:13px}
  .p-body{padding:14px}
  .p-head{padding:13px 14px}
  th,td{padding:11px 13px}
  .tabs{padding:0 12px}
  .chips{padding:12px 12px 0}
  .t-foot{padding:12px 14px}
  .page-head .ph-r{width:100%}
  .page-head .ph-r .btn{flex:1}
  /* stacked card table */
  .tscroll{overflow:visible}
  table{min-width:0}
  thead{position:absolute;width:1px;height:1px;overflow:hidden;clip:rect(0 0 0 0);white-space:nowrap}
  tbody tr{display:grid;grid-template-columns:1fr;gap:8px;padding:14px;border-bottom:1px solid var(--line)}
  tbody tr:hover{background:transparent}
  td{border:0;padding:0;display:flex;align-items:center;justify-content:space-between;gap:12px;text-align:right;min-width:0}
  td:first-child{text-align:left;justify-content:flex-start;border-bottom:1px dashed var(--line);padding-bottom:10px;margin-bottom:2px}
  td::before{content:attr(data-l);font-size:.6rem;letter-spacing:1.1px;text-transform:uppercase;color:var(--faint);font-weight:800;text-align:left;flex:none}
  td:first-child::before{display:none}
  .sys-foot{padding:16px}
  .sys-foot .fr{width:100%}
  .sys-foot .fr .btn{flex:1}
}
@media (max-width:430px){
  .kpis{grid-template-columns:1fr}
  .db-left .kind{display:none}
  .db-cta{padding:6px 11px;font-size:.68rem}
  .donut{width:112px;height:112px}
  .quick{grid-template-columns:1fr}
}
@media (prefers-reduced-motion:reduce){
  *,*::before,*::after{animation-duration:.001ms!important;transition-duration:.001ms!important}
  .rv{opacity:1;transform:none}
}
"""

JS = r"""
(function () {
  'use strict';
  var body = document.body;
  var sidebar = document.getElementById('sidebar');
  var menuBtn = document.getElementById('menuBtn');
  var scrim = document.getElementById('scrim');

  /* ---- mobile drawer ---- */
  function setNav(open) {
    body.classList.toggle('nav-open', open);
    if (menuBtn) menuBtn.setAttribute('aria-expanded', String(open));
  }
  if (menuBtn) menuBtn.addEventListener('click', function () { setNav(!body.classList.contains('nav-open')); });
  if (scrim) scrim.addEventListener('click', function () { setNav(false); });
  sidebar.addEventListener('click', function (e) {
    var a = e.target.closest('a');
    if (!a) return;
    e.preventDefault();
    sidebar.querySelectorAll('a').forEach(function (x) { x.classList.remove('on'); });
    a.classList.add('on');
    var t = document.querySelector('.tb-title h1');
    if (t) t.textContent = a.textContent.trim();
    setNav(false);
    toast('“' + a.textContent.trim() + '” module — demo navigation');
  });

  /* ---- demo bar close ---- */
  var dbClose = document.getElementById('dbClose');
  if (dbClose) dbClose.addEventListener('click', function () {
    document.getElementById('demoBar').classList.add('hidden');
    body.style.paddingTop = '0';
    document.documentElement.style.setProperty('--bar', '0px');
  });

  /* ---- toast ---- */
  var toastEl = document.getElementById('toast'), toastMsg = document.getElementById('toastMsg'), tTimer;
  function toast(msg) {
    if (!toastEl) return;
    toastMsg.textContent = msg;
    toastEl.classList.add('show');
    clearTimeout(tTimer);
    tTimer = setTimeout(function () { toastEl.classList.remove('show'); }, 2600);
  }
  window.toast = toast;
  document.addEventListener('click', function (e) {
    var t = e.target.closest('[data-toast]');
    if (t) toast(t.getAttribute('data-toast'));
  });

  /* ---- keyboard: ESC closes, "/" focuses search ---- */
  document.addEventListener('keydown', function (e) {
    if (e.key === 'Escape') setNav(false);
    if (e.key === '/' && document.activeElement.tagName !== 'INPUT') {
      var s = document.getElementById('globalSearch');
      if (s && s.offsetParent !== null) { e.preventDefault(); s.focus(); }
    }
  });

  /* ---- reveal on scroll ---- */
  var rvs = document.querySelectorAll('.rv');
  if ('IntersectionObserver' in window) {
    var io = new IntersectionObserver(function (en) {
      en.forEach(function (x) { if (x.isIntersecting) { x.target.classList.add('in'); io.unobserve(x.target); } });
    }, { rootMargin: '0px 0px -8% 0px', threshold: 0.05 });
    rvs.forEach(function (el) { io.observe(el); });
  } else { rvs.forEach(function (el) { el.classList.add('in'); }); }

  /* ---- animate chart bars when visible ---- */
  var chart = document.getElementById('chart');
  if (chart) {
    var run = function () {
      chart.querySelectorAll('.bar').forEach(function (b, i) {
        setTimeout(function () { b.style.height = b.getAttribute('data-h') + '%'; }, i * 55);
      });
    };
    if ('IntersectionObserver' in window) {
      var co = new IntersectionObserver(function (en) {
        if (en[0].isIntersecting) { run(); co.disconnect(); }
      }, { threshold: 0.2 });
      co.observe(chart);
    } else run();
  }

  /* ---- animate meters ---- */
  document.querySelectorAll('.meter i[data-w]').forEach(function (m) {
    var set = function () { m.style.width = m.getAttribute('data-w') + '%'; };
    if ('IntersectionObserver' in window) {
      var mo = new IntersectionObserver(function (en) { if (en[0].isIntersecting) { set(); mo.disconnect(); } }, { threshold: 0.3 });
      mo.observe(m);
    } else set();
  });

  /* ---- count-up KPI numbers ---- */
  var reduce = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  document.querySelectorAll('[data-count]').forEach(function (el) {
    var target = parseFloat(el.getAttribute('data-count'));
    var pre = el.getAttribute('data-pre') || '', suf = el.getAttribute('data-suf') || '';
    var dec = (el.getAttribute('data-dec') | 0);
    if (reduce || isNaN(target)) { el.textContent = pre + target.toFixed(dec) + suf; return; }
    var start = null, dur = 900;
    function step(ts) {
      if (!start) start = ts;
      var p = Math.min((ts - start) / dur, 1);
      var e = 1 - Math.pow(1 - p, 3);
      el.textContent = pre + (target * e).toFixed(dec).replace(/\B(?=(\d{3})+(?!\d))/g, ',') + suf;
      if (p < 1) requestAnimationFrame(step);
    }
    if ('IntersectionObserver' in window) {
      var ko = new IntersectionObserver(function (en) { if (en[0].isIntersecting) { requestAnimationFrame(step); ko.disconnect(); } }, { threshold: 0.4 });
      ko.observe(el);
    } else requestAnimationFrame(step);
  });

  /* ---- table: tabs + chips + search all filter together ---- */
  var table = document.getElementById('dataTable');
  var info = document.getElementById('tInfo');
  var TOTAL = (table && table.getAttribute('data-total')) || '0';
  var NOUN = (table && table.getAttribute('data-noun')) || 'records';

  function bindGroup(sel) {
    var wrap = document.querySelector(sel);
    if (!wrap) return;
    wrap.addEventListener('click', function (e) {
      var b = e.target.closest('button');
      if (!b) return;
      wrap.querySelectorAll('button').forEach(function (x) { x.classList.remove('on'); });
      b.classList.add('on');
      applyFilters();
    });
  }
  function activeText(sel) {
    var el = document.querySelector(sel + ' .on');
    return el ? el.textContent.trim().toLowerCase() : '';
  }
  function match(key, txt) {
    if (!key) return true;
    var words = key.split(/\s+/).filter(function (w) { return w.length > 1 && w !== 'all' && w !== NOUN; });
    if (!words.length) return true;
    return words.every(function (w) { return txt.indexOf(w) > -1; });
  }
  function applyFilters() {
    if (!table) return;
    var gs = document.getElementById('globalSearch');
    var q = gs ? gs.value.toLowerCase().trim() : '';
    var tabKey = activeText('.tabs');
    var chipKey = activeText('#chips .chip.on:not([data-nofilter])');
    var shown = 0;
    table.querySelectorAll('tbody tr').forEach(function (tr) {
      var txt = tr.textContent.toLowerCase();
      var ok = (!q || txt.indexOf(q) > -1) && match(tabKey, txt) && match(chipKey, txt);
      tr.style.display = ok ? '' : 'none';
      if (ok) shown++;
    });
    if (info) info.textContent = 'Showing ' + shown + ' of ' + TOTAL + ' ' + NOUN +
      (shown === 0 ? ' — nothing matches that filter' : '');
  }
  bindGroup('.tabs');
  bindGroup('#chips');
  var gs0 = document.getElementById('globalSearch');
  if (gs0) gs0.addEventListener('input', applyFilters);

  /* ---- segmented date ranges: visual only ---- */
  document.querySelectorAll('.seg').forEach(function (seg) {
    seg.addEventListener('click', function (e) {
      var b = e.target.closest('button');
      if (!b) return;
      seg.querySelectorAll('button').forEach(function (x) { x.classList.remove('on'); });
      b.classList.add('on');
    });
  });
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
<meta name="theme-color" content="@@SIDE@@"/>
<link rel="icon" href="@@FAVICON@@"/>
<link rel="preconnect" href="https://fonts.googleapis.com"/>
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin/>
<link rel="preconnect" href="https://cdnjs.cloudflare.com" crossorigin/>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap" rel="stylesheet"/>
<link rel="preload" as="style" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.0/css/all.min.css" onload="this.rel='stylesheet'"/>
<noscript><link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.0/css/all.min.css"/></noscript>
<link rel="stylesheet" href="assets/pro-system.css"/>
<style>@@TOKENS@@</style>
</head>
<body>

<!-- 1000 Hills Group demo bar -->
<div class="demo-bar" id="demoBar">
  <div class="db-left">
    <i class="fas fa-bolt" aria-hidden="true"></i>
    <a href="../demos.html">1000 Hills Group</a>
    <span class="sep">·</span>
    <span class="kind">Live system demo — @@NAME@@</span>
  </div>
  <div class="db-right">
    <a class="db-cta" href="@@WA@@" target="_blank" rel="noopener">Get this system</a>
    <button class="db-close" id="dbClose" type="button" aria-label="Close demo bar"><i class="fas fa-times" aria-hidden="true"></i></button>
  </div>
</div>

<div class="app">
  <div class="scrim" id="scrim"></div>

  <!-- sidebar / mobile drawer -->
  <aside class="sidebar" id="sidebar" aria-label="@@NAME@@ navigation">
    <div class="s-logo">
      <span class="ic"><i class="fas @@ICON@@" aria-hidden="true"></i></span>
      <div><h4>@@NAME@@</h4><small>@@SCREEN_SHORT@@</small></div>
    </div>
    <nav class="s-nav">
      <div class="s-label">Workspace</div>
      @@SIDENAV@@
      <div class="s-label">Insights</div>
      @@SIDENAV2@@
    </nav>
    <div class="s-plan">
      <p>@@PLAN_TEXT@@</p>
      <div class="meter"><i style="width:@@PLAN_PCT@@%"></i></div>
      <small>@@PLAN_PCT@@% of monthly quota used</small>
      <a href="@@WA@@" target="_blank" rel="noopener">Talk to us</a>
    </div>
    <div class="s-user">
      <span class="av">@@INITIALS@@</span>
      <div><h6>@@USER_NAME@@</h6><span>@@USER_ROLE@@</span></div>
    </div>
  </aside>

  <div class="main">
    <!-- topbar -->
    <header class="topbar">
      <button class="icon-btn menu-btn" id="menuBtn" type="button" aria-label="Open menu" aria-expanded="false" aria-controls="sidebar"><i class="fas fa-bars" aria-hidden="true"></i></button>
      <div class="tb-title">
        <h1>@@SCREEN@@</h1>
        <div class="crumb"><span>@@NAME@@</span><i class="fas fa-chevron-right" aria-hidden="true"></i><span>@@SCREEN@@</span></div>
      </div>
      <label class="tb-search">
        <i class="fas fa-magnifying-glass" aria-hidden="true"></i>
        <input type="search" id="globalSearch" placeholder="Search @@SEARCH_NOUN@@…" aria-label="Search"/>
        <kbd>/</kbd>
      </label>
      <div class="tb-right">
        <button class="icon-btn dot-alert" type="button" data-toast="@@ALERT_TEXT@@" aria-label="Notifications"><i class="fas fa-bell" aria-hidden="true"></i></button>
        <button class="icon-btn" type="button" data-toast="Reports export to PDF, Excel and WhatsApp — included in every build." aria-label="Reports"><i class="fas fa-chart-pie" aria-hidden="true"></i></button>
        <div class="tb-me" role="button" tabindex="0" data-toast="Signed in as @@USER_NAME@@ · @@USER_ROLE@@">
          <span class="av">@@INITIALS@@</span>
          <div><b>@@USER_SHORT@@</b><span>@@USER_ROLE@@</span></div>
        </div>
      </div>
    </header>

    <div class="content">
      <!-- page head -->
      <div class="page-head rv">
        <div class="ph-l">
          <h2>@@SCREEN@@</h2>
          <p>@@HEAD_SUB@@</p>
        </div>
        <div class="ph-r">
          <div class="seg" role="group" aria-label="Date range">
            <button type="button" data-toast="Showing today’s live demo data.">Today</button>
            <button type="button" class="on" data-toast="Showing the last 7 days of demo data.">7 days</button>
            <button type="button" data-toast="Showing this month’s demo data.">Month</button>
          </div>
          <button class="btn btn-b" type="button" data-toast="Export ready — PDF, Excel or WhatsApp delivery."><i class="fas fa-download" aria-hidden="true"></i> Export</button>
          <button class="btn btn-a" type="button" data-toast="@@PRIMARY_TOAST@@"><i class="fas @@PRIMARY_ICON@@" aria-hidden="true"></i> @@PRIMARY_LABEL@@</button>
        </div>
      </div>

      <!-- KPIs -->
      <section class="kpis rv" aria-label="Key metrics">@@KPIS@@</section>

      <!-- chart + side panel -->
      <section class="grid-2 rv">
        <div class="panel">
          <div class="p-head">
            <div><h3>@@CHART_TITLE@@</h3><small>@@CHART_SUB@@</small></div>
            <div class="p-tools">
              <div class="seg" role="group" aria-label="Chart series">
                <button type="button" class="on" data-toast="@@CHART_TITLE@@ — demo series.">@@CHART_SERIES@@</button>
                <button type="button" data-toast="Comparative series is available in the live build.">vs last</button>
              </div>
            </div>
          </div>
          <div class="p-body">
            <div class="chart" id="chart">@@CHART@@</div>
            <div class="chart-foot">
              <div class="legend"><span><i></i> @@CHART_SERIES@@</span><span><i class="b"></i> Peak</span></div>
              <div class="mini-stats">@@MINI_STATS@@</div>
            </div>
          </div>
        </div>
        @@SIDE_PANEL@@
      </section>

      <!-- table -->
      <section class="panel rv">
        <div class="p-head">
          <div><h3>@@TABLE_TITLE@@</h3><small>@@TABLE_SUB@@</small></div>
          <div class="p-tools">
            <button class="btn btn-b" type="button" data-toast="Filters: date, status, owner and amount — all configurable."><i class="fas fa-sliders" aria-hidden="true"></i> Filters</button>
            <button class="btn btn-a" type="button" data-toast="@@PRIMARY_TOAST@@"><i class="fas fa-plus" aria-hidden="true"></i> New</button>
          </div>
        </div>
        <div class="tabs" role="tablist" aria-label="Views">@@TABS@@</div>
        <div class="chips" id="chips">@@CHIPS@@</div>
        <div class="tscroll">
          <table id="dataTable" data-total="@@TOTAL@@" data-noun="@@TABLE_NOUN@@">
            <caption class="sr-only" style="position:absolute;width:1px;height:1px;overflow:hidden;clip:rect(0 0 0 0)">@@TABLE_TITLE@@</caption>
            <thead><tr>@@THEAD@@</tr></thead>
            <tbody>@@TBODY@@</tbody>
          </table>
        </div>
        <div class="t-foot">
          <small id="tInfo">Showing @@ROW_COUNT@@ of @@TOTAL@@ @@TABLE_NOUN@@</small>
          <div class="pager">
            <button type="button" disabled aria-label="Previous page"><i class="fas fa-chevron-left" aria-hidden="true"></i></button>
            <button type="button" class="on">1</button>
            <button type="button" data-toast="Pagination is wired to the live database.">2</button>
            <button type="button" data-toast="Pagination is wired to the live database.">3</button>
            <button type="button" data-toast="Pagination is wired to the live database."><i class="fas fa-chevron-right" aria-hidden="true"></i></button>
          </div>
        </div>
      </section>

      <!-- quick actions -->
      <section class="panel rv">
        <div class="p-head"><div><h3>Quick actions</h3><small>Every module is tailored to how your team actually works</small></div></div>
        <div class="p-body"><div class="quick">@@QUICK@@</div></div>
      </section>

      <!-- footer -->
      <footer class="sys-foot rv">
        <div class="fl">
          <h4><i class="fas fa-cube" aria-hidden="true"></i> Built for Rwandan businesses</h4>
          <p>@@NAME@@ is a demo by <a href="../demos.html">1000 Hills Group</a>. We ship it with your roles, MoMo &amp; bank payments, SMS/WhatsApp reminders, offline support and training — live in 2–3 weeks.</p>
        </div>
        <div class="fr">
          <a class="btn btn-b" href="../demos.html" style="background:rgba(255,255,255,.08);border-color:rgba(255,255,255,.16);color:#fff"><i class="fas fa-arrow-left" aria-hidden="true"></i> All demos</a>
          <a class="btn btn-a" href="@@WA@@" target="_blank" rel="noopener"><i class="fab fa-whatsapp" aria-hidden="true"></i> Get @@NAME@@</a>
        </div>
      </footer>
    </div>
  </div>
</div>

<div class="toast" id="toast" role="status" aria-live="polite"><i class="fas fa-circle-info" aria-hidden="true"></i><span id="toastMsg"></span></div>

<script src="assets/pro-system.js" defer></script>
</body>
</html>
"""
