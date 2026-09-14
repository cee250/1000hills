#!/usr/bin/env python3
"""Replacement inline <script> body for demos.html (everything after the
DEMOS array). Poster previews instead of 130 iframes, a proper category rail,
accessible modal, search and back-to-top."""

JS = r"""
    const WA_NUMBER = "250788695396";

    const grid = document.getElementById('demosGrid');
    const countEl = document.getElementById('demoCount');
    const noResults = document.getElementById('noResults');
    const pillsEl = document.getElementById('filterPills');
    const searchInput = document.getElementById('demoSearch');
    const searchClear = document.getElementById('searchClear');
    const pillToggle = document.getElementById('pillToggle');
    const railFadeL = document.getElementById('railFadeL');
    const railFadeR = document.getElementById('railFadeR');
    const railPrev = document.getElementById('railPrev');
    const railNext = document.getElementById('railNext');
    const backTop = document.getElementById('backTop');

    let activeFilter = 'all';
    let searchQuery = '';
    let cards = [];

    const finePointer = window.matchMedia('(hover: hover) and (pointer: fine)').matches;

    /* Category colours for the instant CSS poster preview */
    const CAT_TINT = {
        restaurant:  ['#5B1E0C', '#C2571A'],
        hotel:       ['#0C3B3E', '#15807A'],
        realestate:  ['#152238', '#3B6FA8'],
        ecommerce:   ['#3D0F35', '#A21C6B'],
        education:   ['#1B1A4B', '#4F46E5'],
        ngo:         ['#0A3A2B', '#15803D'],
        health:      ['#450518', '#BE123C'],
        corporate:   ['#0D1526', '#3A4A63'],
        events:      ['#2A0F5E', '#7C3AED'],
        fitness:     ['#3A1B0A', '#B45309'],
        agriculture: ['#12280A', '#4D7C0F'],
        system:      ['#062B45', '#0E7490']
    };
    function tint(cat) { return CAT_TINT[cat] || CAT_TINT.corporate; }

    /* ---- poster: a real screenshot of the demo so the grid paints instantly ----
       The wireframe below is the fallback while the shot loads (or if it 404s);
       the live iframe takes over on top once it loads.
       Thumbnails are generated into demos/img/thumbs/<demo>.webp — see
       scripts/shoot_thumbs.js (headless Chromium, 1280x794 @0.5dsf). */
    function poster(d) {
        const mark = '<i class="' + d.icon + ' p-mark" aria-hidden="true"></i>';
        const shot = d.file ? d.file.replace(/^.*\//, '').replace(/\.html$/, '') : '';
        const shotImg = shot
            ? '<img class="p-shot" src="demos/img/thumbs/' + shot + '.webp" alt="" aria-hidden="true" loading="lazy" decoding="async" onerror="this.remove()">'
            : '';
        if (d.cat === 'system') {
            const bars = [38, 62, 47, 84, 55, 92, 44].map(h => '<i style="--h:' + h + '%"></i>').join('');
            return '<div class="p-body">' +
                '<div class="p-side"><span class="p-logo"></span>' +
                '<span class="p-line w85"></span><span class="p-line w60 soft"></span>' +
                '<span class="p-line w70 soft"></span><span class="p-line w45 soft"></span>' +
                '<span class="p-line w60 soft"></span></div>' +
                '<div class="p-main"><div class="p-kpis"><span></span><span></span><span></span><span></span></div>' +
                '<div class="p-chart">' + bars + '</div>' +
                '<div class="p-table"><span></span><span></span><span></span></div></div>' +
                '</div>' + mark + shotImg;
        }
        return '<div class="p-nav"><span class="p-dot"></span><span class="p-line w22"></span>' +
            '<span class="p-line w15 soft"></span><span class="p-line w15 soft"></span><span class="p-cta"></span></div>' +
            '<div class="p-hero"><span class="p-line thick w70"></span><span class="p-line thick w50"></span>' +
            '<span class="p-line soft w85"></span><span class="p-line soft w60"></span>' +
            '<div class="p-btns"><span></span><span class="ghost"></span></div></div>' +
            '<div class="p-cards"><span></span><span></span><span></span></div>' + mark + shotImg;
    }

    function waLink(d) {
        return 'https://wa.me/' + WA_NUMBER + '?text=' + encodeURIComponent(
            'Hi 1000 Hills Group! I want a ' + (d.cat === 'system' ? 'system' : 'website') +
            ' like the ' + d.name + ' demo (' + d.category + ').');
    }

    /* ---- render ---- */
    function renderCards() {
        grid.innerHTML = DEMOS.map((d, i) => {
            const t = tint(d.cat);
            const slug = d.name.toLowerCase().replace(/[^a-z0-9]+/g, '');
            return '<article class="demo-card" data-cat="' + d.cat + '" data-idx="' + i + '" data-aos="fade-up" data-aos-delay="' + ((i % 3) * 80) + '"' +
                ' data-search="' + (d.name + ' ' + d.category + ' ' + d.type + ' ' + d.desc + ' ' + d.features.join(' ')).toLowerCase().replace(/"/g, '') + '">' +
                '<div class="demo-viewport" data-preview="' + i + '" role="button" tabindex="0" aria-label="Preview the ' + d.name + ' demo">' +
                '<div class="chrome-bar"><span class="dot d1"></span><span class="dot d2"></span><span class="dot d3"></span>' +
                '<span class="url">1000hills · ' + slug + '.rw</span></div>' +
                '<div class="poster" style="--pc-1:' + t[0] + ';--pc-2:' + t[1] + '">' + poster(d) + '</div>' +
                '<iframe class="demo-frame" data-src="' + d.file + '" scrolling="no" title="' + d.name + ' live preview" tabindex="-1" aria-hidden="true"></iframe>' +
                '<div class="demo-badges"><span class="badge-cat">' + d.category + '</span><span class="badge-live">Live</span></div>' +
                '<div class="demo-view"><span><i class="fas fa-play"></i> Live Preview</span></div>' +
                '</div>' +
                '<div class="demo-body">' +
                '<div class="demo-title-row"><span class="demo-ic"><i class="' + d.icon + '" aria-hidden="true"></i></span>' +
                '<div><h3>' + d.name + '</h3><span class="type">' + d.type + '</span></div></div>' +
                '<p class="demo-desc">' + d.desc + '</p>' +
                '<div class="demo-feats">' + d.features.map(f => '<span>' + f + '</span>').join('') + '</div>' +
                '<div class="demo-actions">' +
                '<button class="btn-preview" type="button" data-preview="' + i + '"><i class="fas fa-play"></i> Live Preview</button>' +
                '<a class="btn-icon" href="' + d.file + '" target="_blank" rel="noopener" title="Open ' + d.name + ' in a new tab" aria-label="Open in a new tab"><i class="fas fa-arrow-up-right-from-square"></i></a>' +
                '<a class="btn-icon btn-wa" href="' + waLink(d) + '" target="_blank" rel="noopener" title="Ask for this on WhatsApp" aria-label="Ask for this on WhatsApp"><i class="fab fa-whatsapp"></i></a>' +
                '</div></div></article>';
        }).join('');

        cards = Array.prototype.slice.call(grid.querySelectorAll('.demo-card'));
        fitPreviews();
        countPills();
        applyFilters();
        if (typeof AOS !== 'undefined') AOS.refresh();
    }

    /* ---- live iframe on hover (desktop only, capped so memory stays sane) ---- */
    const liveStack = [];
    const LIVE_MAX = 6;

    function goLive(frame) {
        if (!frame || frame.dataset.live === '1') return;
        frame.dataset.live = '1';
        frame.addEventListener('load', () => frame.classList.add('loaded'), { once: true });
        frame.src = frame.dataset.src;
        liveStack.push(frame);
        while (liveStack.length > LIVE_MAX) {
            const old = liveStack.shift();
            old.classList.remove('loaded');
            old.removeAttribute('src');
            old.dataset.live = '0';
        }
    }

    function fitPreviews() {
        document.querySelectorAll('.demo-viewport').forEach(v => {
            const f = v.querySelector('.demo-frame');
            if (f) f.style.transform = 'scale(' + (v.clientWidth / 1280) + ')';
        });
    }
    let resizeT;
    window.addEventListener('resize', () => {
        clearTimeout(resizeT);
        resizeT = setTimeout(fitPreviews, 140);
    });

    if (finePointer) {
        let hoverT;
        grid.addEventListener('mouseover', e => {
            const vp = e.target.closest('.demo-viewport');
            if (!vp || hoverT) return;
            hoverT = setTimeout(() => {
                goLive(vp.querySelector('.demo-frame'));
                hoverT = null;
            }, 260);
        });
        grid.addEventListener('mouseout', e => {
            if (e.target.closest('.demo-viewport') && hoverT) { clearTimeout(hoverT); hoverT = null; }
        });
    }

    /* ---- counts on the category pills ---- */
    function countPills() {
        const totals = { all: DEMOS.length };
        DEMOS.forEach(d => { totals[d.cat] = (totals[d.cat] || 0) + 1; });
        document.querySelectorAll('.pill-n').forEach(b => {
            b.textContent = totals[b.dataset.countFor] || 0;
        });
    }

    /* ---- filtering + search ---- */
    function applyFilters() {
        let visible = 0;
        cards.forEach(card => {
            const matchCat = activeFilter === 'all' || card.dataset.cat === activeFilter;
            const matchSearch = !searchQuery || card.dataset.search.indexOf(searchQuery) > -1;
            const show = matchCat && matchSearch;
            card.classList.toggle('hidden', !show);
            if (show) visible++;
        });
        const label = activeFilter === 'all' ? 'demos' :
            (document.querySelector('.pill[data-filter="' + activeFilter + '"]').textContent.trim().replace(/\d+$/, '').trim());
        countEl.innerHTML = '<span class="live-dot"></span> Showing <strong>' + visible + '</strong> of <strong>' +
            DEMOS.length + '</strong> ' + label + (searchQuery ? ' for “<strong>' + searchQuery + '</strong>”' : '') +
            ' — tap any card for a live preview';
        noResults.style.display = visible === 0 ? 'block' : 'none';
    }

    function selectPill(pill, scroll) {
        document.querySelectorAll('.pill').forEach(p => {
            const on = p === pill;
            p.classList.toggle('active', on);
            p.setAttribute('aria-selected', String(on));
        });
        activeFilter = pill.dataset.filter;
        applyFilters();
        if (scroll) centerPill(pill);
    }

    function centerPill(pill) {
        if (pillsEl.classList.contains('expanded')) return;
        const target = pill.offsetLeft - (pillsEl.clientWidth - pill.offsetWidth) / 2;
        pillsEl.scrollTo({ left: Math.max(0, target), behavior: finePointer ? 'smooth' : 'auto' });
    }

    pillsEl.addEventListener('click', e => {
        const pill = e.target.closest('.pill');
        if (!pill) return;
        selectPill(pill, true);
        if (window.innerWidth < 900 && pillsEl.classList.contains('expanded')) setExpanded(false);
        const top = document.getElementById('demosGrid').getBoundingClientRect().top + window.pageYOffset - 150;
        if (window.pageYOffset > top) window.scrollTo({ top: top, behavior: finePointer ? 'smooth' : 'auto' });
    });

    pillsEl.addEventListener('keydown', e => {
        if (e.key !== 'ArrowRight' && e.key !== 'ArrowLeft') return;
        const all = Array.prototype.slice.call(pillsEl.querySelectorAll('.pill'));
        const i = all.indexOf(document.activeElement);
        if (i < 0) return;
        e.preventDefault();
        const next = all[(i + (e.key === 'ArrowRight' ? 1 : all.length - 1)) % all.length];
        next.focus();
        centerPill(next);
    });

    let searchT;
    searchInput.addEventListener('input', () => {
        searchClear.classList.toggle('on', !!searchInput.value);
        clearTimeout(searchT);
        searchT = setTimeout(() => {
            searchQuery = searchInput.value.toLowerCase().trim();
            applyFilters();
        }, 130);
    });
    searchClear.addEventListener('click', () => {
        searchInput.value = '';
        searchQuery = '';
        searchClear.classList.remove('on');
        applyFilters();
        searchInput.focus();
    });

    /* ---- category rail: fades, arrows, expander ---- */
    function updateRail() {
        const expanded = pillsEl.classList.contains('expanded');
        const max = pillsEl.scrollWidth - pillsEl.clientWidth;
        const scrollable = !expanded && max > 6;
        const desktop = window.innerWidth >= 900;
        railFadeL.classList.toggle('on', scrollable && pillsEl.scrollLeft > 6);
        railFadeR.classList.toggle('on', scrollable && pillsEl.scrollLeft < max - 6);
        railPrev.classList.toggle('on', scrollable && desktop);
        railNext.classList.toggle('on', scrollable && desktop);
    }
    function nudge(dir) {
        pillsEl.scrollBy({ left: dir * Math.max(180, pillsEl.clientWidth * 0.75), behavior: 'smooth' });
    }
    railPrev.addEventListener('click', () => nudge(-1));
    railNext.addEventListener('click', () => nudge(1));
    pillsEl.addEventListener('scroll', updateRail, { passive: true });
    window.addEventListener('resize', updateRail);

    function setExpanded(open) {
        pillsEl.classList.toggle('expanded', open);
        pillToggle.setAttribute('aria-expanded', String(open));
        pillToggle.querySelector('span').textContent = open ? 'Show less' : 'All categories';
        updateRail();
    }
    pillToggle.addEventListener('click', () => setExpanded(!pillsEl.classList.contains('expanded')));

    /* ---- preview modal ---- */
    const modal = document.getElementById('demoModal');
    const modalIframe = document.getElementById('modalIframe');
    const modalFrame = document.getElementById('modalFrame');
    const modalTitle = document.getElementById('modalTitle');
    const modalCat = document.getElementById('modalCat');
    const modalOpen = document.getElementById('modalOpen');
    const modalWa = document.getElementById('modalWa');
    const modalLoading = document.getElementById('modalLoading');
    let lastTrigger = null;
    let scrollLock = 0;

    function openPreview(idx, trigger) {
        const d = DEMOS[idx];
        if (!d) return;
        lastTrigger = trigger || null;
        modalTitle.childNodes[0].textContent = d.name;
        modalCat.textContent = d.category + ' · ' + d.type;
        modalOpen.href = d.file;
        modalWa.href = waLink(d);
        modalLoading.classList.remove('hide');
        modalIframe.src = d.file;
        setDevice(window.innerWidth < 768 ? 'desktop' : 'desktop');
        modal.classList.add('open');
        scrollLock = window.innerWidth - document.documentElement.clientWidth;
        document.body.style.overflow = 'hidden';
        if (scrollLock > 0) document.body.style.paddingRight = scrollLock + 'px';
        document.getElementById('modalClose').focus({ preventScroll: true });
    }

    function closePreview() {
        if (!modal.classList.contains('open')) return;
        modal.classList.remove('open');
        modalIframe.src = 'about:blank';
        document.body.style.overflow = '';
        document.body.style.paddingRight = '';
        if (lastTrigger && lastTrigger.focus) lastTrigger.focus({ preventScroll: true });
    }

    function setDevice(dev) {
        document.querySelectorAll('.device-btn').forEach(b => b.classList.toggle('active', b.dataset.device === dev));
        modalFrame.className = 'modal-frame' + (dev !== 'desktop' ? ' dev-' + dev : '');
    }

    modalIframe.addEventListener('load', () => modalLoading.classList.add('hide'));
    document.getElementById('modalClose').addEventListener('click', closePreview);
    document.querySelectorAll('.device-btn').forEach(b => b.addEventListener('click', () => setDevice(b.dataset.device)));
    modal.addEventListener('click', e => { if (e.target === modal || e.target.classList.contains('modal-stage')) closePreview(); });

    document.addEventListener('keydown', e => {
        if (!modal.classList.contains('open')) return;
        if (e.key === 'Escape') { closePreview(); return; }
        if (e.key !== 'Tab') return;
        const f = modal.querySelectorAll('a[href], button:not([disabled]), iframe');
        const list = Array.prototype.filter.call(f, el => el.offsetParent !== null || el === modalIframe);
        if (!list.length) return;
        const first = list[0], last = list[list.length - 1];
        if (e.shiftKey && document.activeElement === first) { e.preventDefault(); last.focus(); }
        else if (!e.shiftKey && document.activeElement === last) { e.preventDefault(); first.focus(); }
    });

    document.addEventListener('click', e => {
        const trigger = e.target.closest('[data-preview]');
        if (!trigger) return;
        e.preventDefault();
        openPreview(parseInt(trigger.dataset.preview, 10), trigger);
    });
    document.addEventListener('keydown', e => {
        if (e.key !== 'Enter' && e.key !== ' ') return;
        const vp = e.target.closest && e.target.closest('.demo-viewport');
        if (!vp) return;
        e.preventDefault();
        openPreview(parseInt(vp.dataset.preview, 10), vp);
    });

    /* ---- back to top ---- */
    let topTicking = false;
    window.addEventListener('scroll', () => {
        if (topTicking) return;
        topTicking = true;
        requestAnimationFrame(() => {
            backTop.classList.toggle('show', window.pageYOffset > 700);
            topTicking = false;
        });
    }, { passive: true });
    backTop.addEventListener('click', () => {
        window.scrollTo({ top: 0, behavior: finePointer ? 'smooth' : 'auto' });
    });

    renderCards();
    updateRail();

    /* ---- deep link: demos.html#system pre-selects that category ---- */
    (function () {
        const hash = window.location.hash.replace('#', '');
        if (!hash) return;
        const pill = document.querySelector('.pill[data-filter="' + hash + '"]');
        if (!pill) return;
        selectPill(pill, false);
        requestAnimationFrame(() => {
            centerPill(pill);
            updateRail();
        });
    })();
    """
