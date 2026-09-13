/* ========================================
   REVEAL.JS — tiny drop-in replacement for AOS
   Handles every data-aos animation used on the
   site with one IntersectionObserver (~1 KB,
   no third-party request, no render-blocking CSS).
   Exposes window.AOS so existing init calls work.
   ======================================== */
(function () {
  'use strict';

  var SELECTOR = '[data-aos]';
  var observer = null;
  var pending = [];

  function reveal(el) {
    var delay = parseInt(el.getAttribute('data-aos-delay') || '0', 10) || 0;
    var duration = parseInt(el.getAttribute('data-aos-duration') || '700', 10) || 700;
    el.style.transitionDuration = duration + 'ms';
    if (delay) el.style.transitionDelay = delay + 'ms';
    el.classList.add('aos-animate');
  }

  function revealAll() {
    document.querySelectorAll(SELECTOR).forEach(function (el) { el.classList.add('aos-animate'); });
  }

  function scan() {
    var nodes = Array.prototype.slice.call(document.querySelectorAll(SELECTOR + ':not(.aos-animate)'));
    if (!nodes.length) return;

    if (!('IntersectionObserver' in window)) { revealAll(); return; }

    if (!observer) {
      observer = new IntersectionObserver(function (entries) {
        entries.forEach(function (entry) {
          if (!entry.isIntersecting) return;
          reveal(entry.target);
          observer.unobserve(entry.target);
        });
      }, { rootMargin: '0px 0px -8% 0px', threshold: 0.05 });
    }
    nodes.forEach(function (el) { observer.observe(el); });
  }

  window.AOS = {
    init: function () { scan(); },
    refresh: function () { scan(); },
    refreshHard: function () {
      if (observer) { observer.disconnect(); observer = null; }
      scan();
    }
  };

  /* Anything injected later (render.js) still gets animated. */
  if ('MutationObserver' in window) {
    var mo = new MutationObserver(function (muts) {
      var added = muts.some(function (m) {
        return Array.prototype.some.call(m.addedNodes, function (n) {
          return n.nodeType === 1 && (n.matches && (n.matches(SELECTOR) || n.querySelector(SELECTOR)));
        });
      });
      if (added) { clearTimeout(pending.t); pending.t = setTimeout(scan, 120); }
    });
    var start = function () { mo.observe(document.body, { childList: true, subtree: true }); };
    if (document.body) start(); else document.addEventListener('DOMContentLoaded', start);
  }

  /* Safety net: never leave content invisible. */
  setTimeout(function () {
    document.querySelectorAll(SELECTOR + ':not(.aos-animate)').forEach(function (el) {
      var r = el.getBoundingClientRect();
      if (r.top < window.innerHeight * 1.4 && r.bottom > -200) reveal(el);
    });
  }, 1800);

  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', scan);
  else scan();
})();
