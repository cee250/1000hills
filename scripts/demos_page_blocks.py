#!/usr/bin/env python3
"""Replacement <style> block, filter-bar markup, modal markup and page script
for demos.html. Kept in one module so scripts/patch_demos_page.py can splice
them in without touching the 130-entry DEMOS array.
"""

CSS = r"""
    <style>
        /* ======================================== */
        /* DEMOS PAGE — mobile-first, poster previews */
        /* ======================================== */
        :root {
            --hdr: 62px;
            --bar-bg: rgba(10, 22, 40, 0.92);
        }

        /* ---- Hero ---- */
        .demo-hero {
            padding: clamp(112px, 15vw, 172px) 0 clamp(44px, 6vw, 72px);
            background:
                radial-gradient(ellipse 55% 45% at 82% 8%, rgba(201, 169, 110, 0.10), transparent 62%),
                radial-gradient(ellipse 45% 40% at 8% 92%, rgba(201, 169, 110, 0.07), transparent 62%),
                var(--black);
            position: relative;
            overflow: hidden;
        }
        .demo-hero::before {
            content: '';
            position: absolute;
            inset: 0;
            background-image:
                linear-gradient(rgba(255, 255, 255, .025) 1px, transparent 1px),
                linear-gradient(90deg, rgba(255, 255, 255, .025) 1px, transparent 1px);
            background-size: 52px 52px;
            -webkit-mask-image: radial-gradient(ellipse 65% 60% at 50% 25%, black, transparent);
            mask-image: radial-gradient(ellipse 65% 60% at 50% 25%, black, transparent);
            pointer-events: none;
        }
        .demo-hero .container { position: relative; z-index: 2; }
        .demo-hero h1 {
            font-size: clamp(2rem, 6.4vw, 3.6rem);
            font-weight: 900;
            line-height: 1.1;
            margin: 16px 0 14px;
            letter-spacing: -1px;
            text-wrap: balance;
        }
        .demo-hero h1 .highlight { color: var(--gold); }
        .demo-hero p {
            color: var(--grey);
            max-width: 62ch;
            font-size: clamp(.94rem, 2.4vw, 1.05rem);
            font-weight: 300;
        }
        .demo-hero-stats {
            display: grid;
            grid-template-columns: repeat(3, minmax(0, 1fr));
            gap: 14px;
            margin-top: clamp(26px, 4vw, 38px);
            max-width: 560px;
        }
        .demo-hero-stats > div {
            background: rgba(22, 45, 80, .55);
            border: 1px solid rgba(255, 255, 255, .07);
            border-radius: 14px;
            padding: 13px 15px;
        }
        .demo-hero-stats strong {
            font-size: clamp(1.2rem, 4vw, 1.6rem);
            font-weight: 800;
            color: var(--gold);
            display: block;
            line-height: 1.15;
            letter-spacing: -.5px;
        }
        .demo-hero-stats span { font-size: .72rem; color: var(--grey); letter-spacing: .3px; }

        /* ---- Filter bar ---- */
        .filter-bar {
            position: sticky;
            top: var(--hdr);
            z-index: 500;
            background: var(--bar-bg);
            -webkit-backdrop-filter: blur(16px);
            backdrop-filter: blur(16px);
            border-top: 1px solid rgba(255, 255, 255, .06);
            border-bottom: 1px solid rgba(255, 255, 255, .07);
            padding: 12px 0;
            box-shadow: 0 14px 34px -26px rgba(0, 0, 0, .9);
        }
        .filter-inner { display: flex; align-items: center; gap: 14px; }
        .filter-scroll { position: relative; flex: 1 1 auto; min-width: 0; }
        .filter-pills {
            display: flex;
            gap: 9px;
            overflow-x: auto;
            overscroll-behavior-x: contain;
            scroll-snap-type: x proximity;
            scrollbar-width: none;
            -ms-overflow-style: none;
            padding: 3px 2px;
            scroll-padding-inline: 8px;
        }
        .filter-pills::-webkit-scrollbar { display: none; height: 0; }
        .pill {
            flex: none;
            scroll-snap-align: start;
            display: inline-flex;
            align-items: center;
            gap: 8px;
            border: 1px solid rgba(255, 255, 255, .11);
            background: var(--dark-card);
            color: var(--grey-light);
            font-size: .82rem;
            font-weight: 600;
            font-family: var(--font);
            padding: 10px 17px;
            border-radius: 40px;
            cursor: pointer;
            transition: transform .2s ease, background .25s ease, border-color .25s ease, color .25s ease;
            white-space: nowrap;
            -webkit-tap-highlight-color: transparent;
        }
        .pill i { font-size: .76rem; color: var(--gold); }
        .pill:hover { border-color: rgba(201, 169, 110, .6); color: var(--white); transform: translateY(-1px); }
        .pill:active { transform: scale(.97); }
        .pill.active {
            background: linear-gradient(135deg, #C9A96E, #E8D5A3);
            color: #0A1628;
            border-color: transparent;
            box-shadow: 0 10px 24px -12px rgba(201, 169, 110, .8);
        }
        .pill.active i { color: #0A1628; }
        .pill .pill-n {
            font-size: .66rem;
            font-weight: 800;
            background: rgba(255, 255, 255, .1);
            border-radius: 20px;
            padding: 2px 8px;
            letter-spacing: .2px;
        }
        .pill.active .pill-n { background: rgba(10, 22, 40, .18); }

        /* scroll affordances: fades + arrow rails */
        .rail-fade {
            position: absolute; top: 0; bottom: 0; width: 46px;
            pointer-events: none; opacity: 0; transition: opacity .25s ease; z-index: 2;
        }
        .rail-fade.l { left: 0; background: linear-gradient(90deg, #0A1628 8%, rgba(10, 22, 40, 0)); }
        .rail-fade.r { right: 0; background: linear-gradient(270deg, #0A1628 8%, rgba(10, 22, 40, 0)); }
        .rail-fade.on { opacity: 1; }
        .rail-btn {
            position: absolute; top: 50%; transform: translateY(-50%);
            width: 34px; height: 34px; border-radius: 50%;
            display: none; place-items: center;
            border: 1px solid rgba(201, 169, 110, .35);
            background: rgba(10, 22, 40, .92);
            color: var(--gold-light);
            cursor: pointer; z-index: 3; font-size: .72rem;
            transition: .2s ease;
        }
        .rail-btn:hover { background: var(--gold); color: #0A1628; border-color: transparent; }
        .rail-btn.prev { left: -4px; }
        .rail-btn.next { right: -4px; }
        .rail-btn.on { display: grid; }
        .rail-btn[disabled] { opacity: .3; cursor: default; }

        .filter-side { display: flex; align-items: center; gap: 10px; flex: none; }
        .demo-search {
            display: flex; align-items: center; gap: 10px;
            background: var(--dark-card);
            border: 1px solid rgba(255, 255, 255, .11);
            border-radius: 40px;
            padding: 9px 16px;
            width: 250px;
            transition: .25s ease;
        }
        .demo-search:focus-within { border-color: var(--gold); box-shadow: 0 0 0 3px rgba(201, 169, 110, .16); }
        .demo-search i { color: var(--gold); font-size: .85rem; flex: none; }
        .demo-search input {
            background: none; border: 0; outline: none; color: var(--white);
            font-family: var(--font); font-size: .86rem; width: 100%; min-width: 0;
        }
        .demo-search input::placeholder { color: var(--grey); }
        .search-clear {
            background: none; border: 0; color: var(--grey); cursor: pointer;
            font-size: .8rem; padding: 4px; display: none; flex: none;
        }
        .search-clear.on { display: block; }
        .search-clear:hover { color: var(--white); }

        /* "All categories" expander — replaces sideways hunting on small screens */
        .pill-toggle {
            display: none;
            align-items: center; gap: 9px;
            background: linear-gradient(135deg, rgba(201, 169, 110, .18), rgba(201, 169, 110, .06));
            border: 1px solid rgba(201, 169, 110, .4);
            color: var(--gold-light);
            font-family: var(--font); font-size: .8rem; font-weight: 700;
            padding: 10px 15px; border-radius: 40px; cursor: pointer;
            white-space: nowrap; transition: .2s ease; flex: none;
        }
        .pill-toggle .caret { transition: transform .3s ease; font-size: .68rem; }
        .pill-toggle[aria-expanded="true"] { background: linear-gradient(135deg, #C9A96E, #E8D5A3); color: #0A1628; border-color: transparent; }
        .pill-toggle[aria-expanded="true"] .caret { transform: rotate(180deg); }

        @media (max-width: 899px) {
            .filter-inner { flex-direction: column-reverse; align-items: stretch; gap: 10px; }
            .filter-side { width: 100%; }
            .demo-search { flex: 1; width: auto; }
            .pill-toggle { display: inline-flex; }
            .rail-btn { display: none !important; }
            /* expanded: every category visible at once, no sideways scrolling */
            .filter-pills.expanded {
                display: grid;
                grid-template-columns: repeat(2, minmax(0, 1fr));
                overflow: visible;
                gap: 8px;
            }
            .filter-pills.expanded .pill { width: 100%; justify-content: flex-start; scroll-snap-align: none; }
            .rail-fade { display: none; }
        }
        @media (max-width: 400px) {
            .filter-pills.expanded { grid-template-columns: 1fr; }
            .filter-side { flex-wrap: wrap; }
            .pill-toggle { flex: 1; justify-content: center; }
        }

        /* ---- Demos grid ---- */
        .demos-section { padding: clamp(44px, 6vw, 72px) 0 clamp(56px, 8vw, 92px); background: var(--black); }
        .demo-count {
            color: var(--grey); font-size: .88rem; margin-bottom: 26px;
            display: flex; align-items: center; gap: 10px; flex-wrap: wrap;
        }
        .demo-count strong { color: var(--gold); }
        .demo-count .live-dot {
            width: 7px; height: 7px; border-radius: 50%; background: #10B981; flex: none;
            box-shadow: 0 0 0 4px rgba(16, 185, 129, .18);
        }
        .demos-grid {
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(min(340px, 100%), 1fr));
            gap: clamp(16px, 2.4vw, 26px);
        }
        .demo-card {
            background: var(--dark-card);
            border: 1px solid rgba(255, 255, 255, .07);
            border-radius: var(--radius-lg);
            overflow: hidden;
            display: flex;
            flex-direction: column;
            transition: transform .3s ease, border-color .3s ease, box-shadow .3s ease;
            content-visibility: auto;
            contain-intrinsic-size: auto 540px;
        }
        .demo-card:hover { transform: translateY(-6px); border-color: rgba(201, 169, 110, .45); box-shadow: 0 26px 60px -24px rgba(0, 0, 0, .8); }
        .demo-card.hidden { display: none; }

        /* ---- preview viewport ---- */
        .demo-viewport {
            position: relative;
            aspect-ratio: 1280 / 820;
            background: #0B1729;
            overflow: hidden;
            cursor: pointer;
            border-bottom: 1px solid rgba(255, 255, 255, .06);
            container-type: inline-size;
            -webkit-tap-highlight-color: transparent;
        }
        .chrome-bar {
            position: absolute; top: 0; left: 0; right: 0; height: 26px;
            background: #0D1B2F; display: flex; align-items: center; gap: 6px;
            padding: 0 12px; z-index: 5; border-bottom: 1px solid rgba(255, 255, 255, .05);
        }
        .chrome-bar .dot { width: 9px; height: 9px; border-radius: 50%; flex: none; }
        .chrome-bar .d1 { background: #FF5F57; } .chrome-bar .d2 { background: #FEBC2E; } .chrome-bar .d3 { background: #28C840; }
        .chrome-bar .url {
            margin-left: 8px; font-size: 9px; color: #7E93AF;
            background: rgba(255, 255, 255, .06); border-radius: 20px; padding: 3px 12px;
            letter-spacing: .3px; max-width: 62%; overflow: hidden; white-space: nowrap; text-overflow: ellipsis;
        }
        .demo-frame {
            position: absolute; top: 26px; left: 0; width: 1280px; height: 794px;
            border: 0; transform-origin: top left; opacity: 0;
            transition: opacity .5s ease; pointer-events: none; background: #fff; z-index: 4;
        }
        .demo-frame.loaded { opacity: 1; }

        /* poster: an instant "screenshot" of the demo */
        .poster {
            position: absolute; inset: 26px 0 0 0; z-index: 1;
            padding: 5% 5% 6%;
            display: flex; flex-direction: column;
            background:
                radial-gradient(120% 90% at 88% 0%, rgba(255, 255, 255, .10), transparent 58%),
                linear-gradient(155deg, var(--pc-1), var(--pc-2));
            overflow: hidden;
        }
        /* real screenshot of the demo — the card face before the live preview loads */
        .p-shot {
            position: absolute; inset: 0; z-index: 3;
            width: 100%; height: 100%;
            object-fit: cover; object-position: top center;
            background: #fff;
        }
        .p-shot[src=""], .p-shot:not([src]) { visibility: hidden; }
        .poster::after {
            content: ''; position: absolute; inset: 0;
            background: linear-gradient(200deg, rgba(255, 255, 255, .07), transparent 42%);
            pointer-events: none;
        }
        .p-mark {
            position: absolute; right: 5%; bottom: 6%; z-index: 2;
            color: rgba(255, 255, 255, .22); font-size: 3.4rem;
            transition: transform .4s cubic-bezier(.22, 1, .36, 1), color .4s ease;
        }
        .p-mark { font-size: 26cqi; }
        .demo-card:hover .p-mark { transform: scale(1.08) rotate(-4deg); color: rgba(255, 255, 255, .34); }
        .p-line { display: block; height: 2.4%; border-radius: 99px; background: rgba(255, 255, 255, .42); }
        .p-line.soft { background: rgba(255, 255, 255, .22); }
        .p-line.thick { height: 4.4%; background: rgba(255, 255, 255, .72); }
        .w95 { width: 95%; } .w90 { width: 90%; } .w85 { width: 85%; } .w80 { width: 80%; }
        .w70 { width: 70%; } .w60 { width: 60%; } .w55 { width: 55%; } .w50 { width: 50%; }
        .w45 { width: 45%; } .w40 { width: 40%; } .w30 { width: 30%; } .w22 { width: 22%; } .w15 { width: 15%; }
        .p-nav { display: flex; align-items: center; gap: 3.4%; height: 7%; margin-bottom: 5%; }
        .p-nav .p-dot { width: 5.4%; aspect-ratio: 1; border-radius: 50%; background: rgba(255, 255, 255, .82); flex: none; }
        .p-nav .p-line { flex: none; }
        .p-nav .p-cta {
            margin-left: auto; width: 15%; height: 62%; border-radius: 99px;
            background: rgba(255, 255, 255, .88); flex: none;
        }
        .p-hero { display: grid; gap: 3.2%; align-content: start; }
        .p-btns { display: flex; gap: 3%; margin-top: 4%; }
        .p-btns span { width: 22%; height: 5.2%; border-radius: 99px; background: rgba(255, 255, 255, .9); }
        .p-btns span.ghost { background: rgba(255, 255, 255, .2); border: 1px solid rgba(255, 255, 255, .45); }
        .p-cards { display: flex; gap: 3.4%; margin-top: auto; }
        .p-cards span {
            flex: 1; height: 26%; border-radius: 8px;
            background: rgba(255, 255, 255, .16);
            border: 1px solid rgba(255, 255, 255, .22);
        }
        /* dashboard poster */
        .p-body { display: flex; gap: 4%; flex: 1; min-height: 0; }
        .p-side { width: 20%; display: grid; gap: 6%; align-content: start; padding-top: 1%; }
        .p-side .p-logo { height: 5%; border-radius: 6px; background: rgba(255, 255, 255, .8); }
        .p-side .p-line { height: 3.4%; }
        .p-main { flex: 1; min-width: 0; display: grid; gap: 5%; align-content: start; }
        .p-kpis { display: flex; gap: 3.4%; }
        .p-kpis span { flex: 1; height: 13%; border-radius: 7px; background: rgba(255, 255, 255, .17); border: 1px solid rgba(255, 255, 255, .24); }
        .p-chart { display: flex; align-items: flex-end; gap: 2.6%; height: 30%; padding: 4% 4% 0; border-radius: 8px; background: rgba(255, 255, 255, .1); border: 1px solid rgba(255, 255, 255, .18); }
        .p-chart i { flex: 1; border-radius: 3px 3px 0 0; background: rgba(255, 255, 255, .78); height: var(--h, 50%); }
        .p-chart i:nth-child(even) { background: rgba(255, 255, 255, .42); }
        .p-table { display: grid; gap: 4%; padding: 4%; border-radius: 8px; background: rgba(255, 255, 255, .1); border: 1px solid rgba(255, 255, 255, .18); }
        .p-table span { height: 4%; border-radius: 99px; background: rgba(255, 255, 255, .34); }
        .p-table span:first-child { background: rgba(255, 255, 255, .6); width: 42%; }

        .demo-badges { position: absolute; top: 38px; left: 12px; right: 12px; display: flex; justify-content: space-between; gap: 8px; z-index: 6; pointer-events: none; }
        .demo-badges span {
            font-size: .62rem; font-weight: 700; letter-spacing: 1.1px; text-transform: uppercase;
            padding: 5px 11px; border-radius: 30px;
            -webkit-backdrop-filter: blur(6px); backdrop-filter: blur(6px); white-space: nowrap;
        }
        .badge-cat { background: rgba(10, 22, 40, .78); color: var(--gold-light); border: 1px solid rgba(201, 169, 110, .4); }
        .badge-live { background: rgba(16, 185, 129, .9); color: #fff; display: inline-flex; align-items: center; gap: 6px; }
        .badge-live::before { content: ''; width: 6px; height: 6px; background: #fff; border-radius: 50%; animation: livePulse 1.8s infinite; }
        @keyframes livePulse { 0%, 100% { box-shadow: 0 0 0 0 rgba(255, 255, 255, .7); } 50% { box-shadow: 0 0 0 5px rgba(255, 255, 255, 0); } }

        .demo-view {
            position: absolute; inset: 26px 0 0 0; z-index: 6;
            display: flex; align-items: center; justify-content: center; gap: 10px;
            background: rgba(6, 14, 28, .55);
            opacity: 0; transition: opacity .3s ease;
            -webkit-backdrop-filter: blur(2px); backdrop-filter: blur(2px);
        }
        .demo-view span {
            background: linear-gradient(135deg, #C9A96E, #E8D5A3); color: #0A1628;
            font-size: .8rem; font-weight: 700; padding: 11px 22px; border-radius: 40px;
            display: inline-flex; align-items: center; gap: 8px;
            box-shadow: 0 14px 30px -12px rgba(0, 0, 0, .8);
        }
        @media (hover: hover) {
            .demo-viewport:hover .demo-view, .demo-viewport:focus-visible .demo-view { opacity: 1; }
        }
        @media (hover: none) {
            .demo-view { display: none; }
        }

        /* ---- card body ---- */
        .demo-body { padding: clamp(16px, 2.4vw, 22px); display: flex; flex-direction: column; gap: 11px; flex: 1; }
        .demo-title-row { display: flex; align-items: center; gap: 12px; }
        .demo-title-row .demo-ic {
            width: 44px; height: 44px; flex: none; border-radius: 13px;
            background: linear-gradient(135deg, rgba(201, 169, 110, .22), rgba(201, 169, 110, .06));
            border: 1px solid rgba(201, 169, 110, .32);
            display: grid; place-items: center; color: var(--gold); font-size: 1.05rem;
        }
        .demo-title-row > div { min-width: 0; }
        .demo-title-row h3 {
            font-size: clamp(1rem, 2.6vw, 1.08rem); font-weight: 700; line-height: 1.3;
            overflow: hidden; text-overflow: ellipsis; white-space: nowrap;
        }
        .demo-title-row .type { font-size: .68rem; color: var(--grey); font-weight: 600; letter-spacing: 1px; text-transform: uppercase; }
        .demo-desc { font-size: .87rem; color: var(--grey); font-weight: 300; line-height: 1.6; }
        .demo-feats { display: flex; flex-wrap: wrap; gap: 7px; }
        .demo-feats span {
            font-size: .68rem; border: 1px solid rgba(255, 255, 255, .11); padding: 4px 11px;
            border-radius: 30px; color: var(--grey-light); background: rgba(255, 255, 255, .03);
        }
        .demo-actions { display: flex; gap: 9px; margin-top: auto; padding-top: 6px; }
        .btn-preview {
            flex: 1; min-height: 44px;
            display: inline-flex; align-items: center; justify-content: center; gap: 8px;
            background: linear-gradient(135deg, #C9A96E, #E8D5A3); color: #0A1628;
            font-size: .82rem; font-weight: 700; padding: 11px 16px; border-radius: 40px;
            cursor: pointer; border: 0; transition: .25s ease; font-family: var(--font);
        }
        .btn-preview:hover { transform: translateY(-2px); box-shadow: 0 12px 28px -12px rgba(201, 169, 110, .8); }
        .btn-icon {
            width: 44px; height: 44px; flex: none; display: grid; place-items: center;
            border-radius: 50%; border: 1px solid rgba(255, 255, 255, .15);
            color: var(--grey-light); transition: .25s ease; background: none; cursor: pointer;
        }
        .btn-icon:hover { border-color: var(--gold); color: var(--gold); transform: translateY(-2px); }
        .btn-wa:hover { border-color: #25D366; color: #25D366; }

        .no-results { text-align: center; padding: 56px 20px; color: var(--grey); display: none; }
        .no-results i { font-size: 2.4rem; color: var(--gold); margin-bottom: 16px; display: block; }
        .no-results strong { color: var(--gold); }
        .no-results .btn-primary { margin-top: 22px; }

        /* ---- How it works ---- */
        .how-section { background: var(--dark); border-top: 1px solid rgba(255, 255, 255, .05); border-bottom: 1px solid rgba(255, 255, 255, .05); padding: clamp(48px, 7vw, 74px) 0; }
        .how-grid { display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); gap: clamp(18px, 3vw, 28px); margin-top: 10px; }
        .how-card {
            text-align: center; padding: 26px 18px; position: relative;
            background: rgba(22, 45, 80, .4); border: 1px solid rgba(255, 255, 255, .06); border-radius: var(--radius-lg);
            transition: .3s ease;
        }
        .how-card:hover { transform: translateY(-5px); border-color: rgba(201, 169, 110, .35); }
        .how-card .n {
            width: 56px; height: 56px; margin: 0 auto 16px; border-radius: 50%;
            background: linear-gradient(135deg, #C9A96E, #E8D5A3); color: #0A1628;
            font-weight: 800; font-size: 1.15rem; display: grid; place-items: center;
            box-shadow: 0 14px 30px -12px rgba(201, 169, 110, .7);
        }
        .how-card h4 { font-size: 1.02rem; margin-bottom: 8px; }
        .how-card p { font-size: .85rem; color: var(--grey); font-weight: 300; }

        /* ---- Preview modal ---- */
        .demo-modal {
            position: fixed; inset: 0; z-index: 10000;
            background: rgba(4, 10, 20, .94);
            -webkit-backdrop-filter: blur(8px); backdrop-filter: blur(8px);
            display: none; flex-direction: column;
        }
        .demo-modal.open { display: flex; }
        .modal-top {
            display: flex; align-items: center; gap: 12px;
            padding: 12px clamp(12px, 2.4vw, 22px);
            padding-top: calc(12px + env(safe-area-inset-top));
            background: #0A1628; border-bottom: 1px solid rgba(201, 169, 110, .25);
            flex-wrap: wrap; flex: none;
        }
        .modal-top .m-title { font-weight: 700; font-size: .98rem; min-width: 0; }
        .modal-top .m-title small { display: block; font-size: .66rem; color: var(--gold); letter-spacing: 1.4px; text-transform: uppercase; font-weight: 700; }
        .device-group { display: flex; gap: 5px; margin-left: auto; background: rgba(255, 255, 255, .06); padding: 4px; border-radius: 40px; }
        .device-btn {
            border: 0; background: none; color: var(--grey);
            font-size: .78rem; font-family: var(--font); font-weight: 600;
            padding: 8px 14px; border-radius: 30px; cursor: pointer; transition: .25s ease;
            display: inline-flex; align-items: center; gap: 7px;
        }
        .device-btn:hover { color: var(--white); }
        .device-btn.active { background: linear-gradient(135deg, #C9A96E, #E8D5A3); color: #0A1628; font-weight: 700; }
        .modal-actions { display: flex; gap: 8px; }
        .modal-actions a, .modal-actions button {
            width: 42px; height: 42px; display: grid; place-items: center; border-radius: 12px;
            border: 1px solid rgba(255, 255, 255, .15); background: none; color: var(--grey-light);
            cursor: pointer; transition: .25s ease; font-size: .95rem;
        }
        .modal-actions a:hover { border-color: var(--gold); color: var(--gold); }
        .modal-actions button:hover { border-color: #FF5F57; color: #FF5F57; }
        .modal-stage {
            flex: 1; display: flex; align-items: stretch; justify-content: center;
            background: #060D1A; overflow: hidden; min-height: 0; position: relative;
        }
        .modal-frame { background: #fff; width: 100%; height: 100%; transition: width .4s cubic-bezier(.25, .46, .45, .94), margin .4s; overflow: hidden; position: relative; }
        .modal-frame iframe { width: 100%; height: 100%; border: 0; display: block; }
        .modal-frame.dev-tablet { width: min(768px, calc(100% - 24px)); margin: 14px auto; height: calc(100% - 28px); border-radius: 14px; box-shadow: 0 30px 80px rgba(0, 0, 0, .6); }
        .modal-frame.dev-mobile { width: min(402px, calc(100% - 20px)); margin: 14px auto; height: calc(100% - 28px); border-radius: 20px; box-shadow: 0 30px 80px rgba(0, 0, 0, .6); }
        .modal-loading {
            position: absolute; inset: 0; display: grid; place-items: center; gap: 14px;
            background: #0B1729; color: var(--grey); font-size: .84rem; z-index: 2;
            align-content: center; justify-items: center; transition: opacity .35s ease;
        }
        .modal-loading.hide { opacity: 0; pointer-events: none; }
        .spinner { width: 34px; height: 34px; border-radius: 50%; border: 3px solid rgba(201, 169, 110, .25); border-top-color: var(--gold); animation: spin .8s linear infinite; }
        @keyframes spin { to { transform: rotate(360deg); } }

        /* ---- CTA band ---- */
        .demos-cta { text-align: center; }
        .demos-cta .mini-cards { display: flex; justify-content: center; gap: 12px; flex-wrap: wrap; margin: 8px 0 32px; }
        .demos-cta .mini-card {
            display: inline-flex; align-items: center; gap: 10px;
            background: var(--dark-card); border: 1px solid rgba(255, 255, 255, .08);
            color: var(--grey-light); font-size: .82rem; font-weight: 600;
            padding: 10px 18px; border-radius: 40px; transition: .25s ease;
        }
        .demos-cta .mini-card:hover { border-color: rgba(201, 169, 110, .45); transform: translateY(-2px); }
        .demos-cta .mini-card i { color: var(--gold); }

        /* ---- back to top ---- */
        .back-top {
            position: fixed; right: clamp(14px, 3vw, 26px);
            bottom: calc(clamp(14px, 3vw, 26px) + env(safe-area-inset-bottom));
            width: 46px; height: 46px; border-radius: 50%; z-index: 900;
            display: grid; place-items: center; cursor: pointer;
            background: linear-gradient(135deg, #C9A96E, #E8D5A3); color: #0A1628;
            border: 0; font-size: .95rem; box-shadow: 0 16px 34px -14px rgba(201, 169, 110, .8);
            opacity: 0; visibility: hidden; transform: translateY(14px); transition: .3s ease;
        }
        .back-top.show { opacity: 1; visibility: visible; transform: none; }

        /* ---- breakpoints ---- */
        @media (max-width: 1024px) {
            .how-grid { grid-template-columns: repeat(2, minmax(0, 1fr)); }
            .how-card:last-child { grid-column: 1 / -1; }
            .demo-search { width: 210px; }
        }
        @media (max-width: 768px) {
            :root { --hdr: 58px; }
            .demo-hero-stats { grid-template-columns: repeat(3, minmax(0, 1fr)); gap: 10px; max-width: none; }
            .demo-hero-stats > div { padding: 11px 12px; }
            .how-grid { grid-template-columns: 1fr; }
            .how-card:last-child { grid-column: auto; }
            .device-group { order: 3; margin-left: 0; width: 100%; justify-content: center; }
            .modal-actions { margin-left: auto; }
            .modal-top { gap: 10px; }
            .demo-count { font-size: .82rem; }
        }
        @media (max-width: 560px) {
            :root { --hdr: 54px; }
            .demos-grid { grid-template-columns: 1fr; gap: 14px; }
            .demo-card { border-radius: 16px; }
            .device-btn span { display: none; }
            .device-btn { padding: 9px 13px; }
            .modal-frame.dev-tablet, .modal-frame.dev-mobile { margin: 0 auto; height: 100%; border-radius: 0; width: 100%; }
            .demo-hero-stats span { font-size: .66rem; }
            .back-top { width: 42px; height: 42px; }
        }
        @media (max-width: 380px) {
            .pill { padding: 9px 14px; font-size: .78rem; }
            .demo-feats span { font-size: .64rem; padding: 4px 9px; }
        }
        @media (prefers-reduced-motion: reduce) {
            .demo-card:hover { transform: none; }
            .badge-live::before, .spinner { animation: none; }
        }
    </style>
"""

FILTER = r"""    <!-- ======================================== -->
    <!-- FILTER BAR                               -->
    <!-- ======================================== -->
    <div class="filter-bar" id="filterBar">
        <div class="container filter-inner">
            <div class="filter-scroll" id="filterScroll">
                <span class="rail-fade l" id="railFadeL"></span>
                <span class="rail-fade r" id="railFadeR"></span>
                <div class="filter-pills" id="filterPills" role="tablist" aria-label="Demo categories">
                    <button class="pill active" role="tab" aria-selected="true" data-filter="all"><i class="fas fa-grip"></i> All Demos <b class="pill-n" data-count-for="all">0</b></button>
                    <button class="pill" role="tab" aria-selected="false" data-filter="restaurant"><i class="fas fa-utensils"></i> Restaurant <b class="pill-n" data-count-for="restaurant">0</b></button>
                    <button class="pill" role="tab" aria-selected="false" data-filter="hotel"><i class="fas fa-hotel"></i> Hotel &amp; Tourism <b class="pill-n" data-count-for="hotel">0</b></button>
                    <button class="pill" role="tab" aria-selected="false" data-filter="realestate"><i class="fas fa-city"></i> Real Estate <b class="pill-n" data-count-for="realestate">0</b></button>
                    <button class="pill" role="tab" aria-selected="false" data-filter="ecommerce"><i class="fas fa-cart-shopping"></i> E-Commerce <b class="pill-n" data-count-for="ecommerce">0</b></button>
                    <button class="pill" role="tab" aria-selected="false" data-filter="education"><i class="fas fa-graduation-cap"></i> Education <b class="pill-n" data-count-for="education">0</b></button>
                    <button class="pill" role="tab" aria-selected="false" data-filter="ngo"><i class="fas fa-hand-holding-heart"></i> NGO &amp; Church <b class="pill-n" data-count-for="ngo">0</b></button>
                    <button class="pill" role="tab" aria-selected="false" data-filter="health"><i class="fas fa-heart-pulse"></i> Health <b class="pill-n" data-count-for="health">0</b></button>
                    <button class="pill" role="tab" aria-selected="false" data-filter="corporate"><i class="fas fa-briefcase"></i> Corporate <b class="pill-n" data-count-for="corporate">0</b></button>
                    <button class="pill" role="tab" aria-selected="false" data-filter="events"><i class="fas fa-calendar-days"></i> Events &amp; Media <b class="pill-n" data-count-for="events">0</b></button>
                    <button class="pill" role="tab" aria-selected="false" data-filter="fitness"><i class="fas fa-dumbbell"></i> Beauty &amp; Fitness <b class="pill-n" data-count-for="fitness">0</b></button>
                    <button class="pill" role="tab" aria-selected="false" data-filter="agriculture"><i class="fas fa-tractor"></i> Agriculture <b class="pill-n" data-count-for="agriculture">0</b></button>
                    <button class="pill" role="tab" aria-selected="false" data-filter="system"><i class="fas fa-gauge-high"></i> Systems <b class="pill-n" data-count-for="system">0</b></button>
                </div>
                <button class="rail-btn prev" id="railPrev" type="button" aria-label="Scroll categories left"><i class="fas fa-chevron-left"></i></button>
                <button class="rail-btn next" id="railNext" type="button" aria-label="Scroll categories right"><i class="fas fa-chevron-right"></i></button>
            </div>
            <div class="filter-side">
                <label class="demo-search">
                    <i class="fas fa-magnifying-glass"></i>
                    <input type="search" id="demoSearch" placeholder="Search demos… e.g. hotel, school" aria-label="Search demos" autocomplete="off" />
                    <button class="search-clear" id="searchClear" type="button" aria-label="Clear search"><i class="fas fa-circle-xmark"></i></button>
                </label>
                <button class="pill-toggle" id="pillToggle" type="button" aria-expanded="false" aria-controls="filterPills">
                    <i class="fas fa-layer-group"></i> <span>All categories</span> <i class="fas fa-chevron-down caret"></i>
                </button>
            </div>
        </div>
    </div>
"""

MODAL = r"""    <!-- ======================================== -->
    <!-- PREVIEW MODAL                            -->
    <!-- ======================================== -->
    <div class="demo-modal" id="demoModal" role="dialog" aria-modal="true" aria-label="Demo preview">
        <div class="modal-top">
            <div class="m-title" id="modalTitle">Demo<small id="modalCat">Category</small></div>
            <div class="device-group" role="group" aria-label="Preview size">
                <button class="device-btn active" type="button" data-device="desktop" title="Desktop view"><i class="fas fa-desktop"></i> <span>Desktop</span></button>
                <button class="device-btn" type="button" data-device="tablet" title="Tablet view"><i class="fas fa-tablet-screen-button"></i> <span>Tablet</span></button>
                <button class="device-btn" type="button" data-device="mobile" title="Mobile view"><i class="fas fa-mobile-screen-button"></i> <span>Mobile</span></button>
            </div>
            <div class="modal-actions">
                <a href="#" id="modalOpen" target="_blank" rel="noopener" title="Open in new tab" aria-label="Open demo in a new tab"><i class="fas fa-arrow-up-right-from-square"></i></a>
                <a href="#" id="modalWa" target="_blank" rel="noopener" title="Get a quote on WhatsApp" aria-label="Get a quote on WhatsApp" style="color:#25D366;border-color:rgba(37,211,102,.45)"><i class="fab fa-whatsapp"></i></a>
                <button id="modalClose" type="button" title="Close preview" aria-label="Close preview"><i class="fas fa-times"></i></button>
            </div>
        </div>
        <div class="modal-stage">
            <div class="modal-frame" id="modalFrame">
                <div class="modal-loading" id="modalLoading">
                    <span class="spinner"></span>
                    <span>Loading live demo…</span>
                </div>
                <iframe id="modalIframe" title="Demo preview" src="about:blank"></iframe>
            </div>
        </div>
    </div>

    <button class="back-top" id="backTop" type="button" aria-label="Back to top"><i class="fas fa-arrow-up"></i></button>
"""
