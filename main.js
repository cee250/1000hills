// ======================================== //
// MAIN.JS - SITE BEHAVIOUR + OPTIONAL FIREBASE
// Firebase is only needed by client-portal.html, so the SDK
// is initialised defensively: pages that do not load it still
// get the header, menu and preloader behaviour.
// ======================================== //

// Deliberately NOT named `firebaseConfig`: firebase-config.js declares a
// top-level `const firebaseConfig` too, so loading both files on one page is a
// fatal "Identifier 'firebaseConfig' has already been declared" SyntaxError
// that kills every script on the page.
const siteFirebaseConfig = {
    apiKey: "AIzaSyABeFEPPKjKVFU14cx4s__uwWLRpHa5J2c",
    authDomain: "luxury-properties-36554.firebaseapp.com",
    projectId: "luxury-properties-36554",
    storageBucket: "luxury-properties-36554.firebasestorage.app",
    messagingSenderId: "214959691683",
    appId: "1:214959691683:web:864ba0f961cfefd7baac16"
};

let db = null;
let auth = null;

(function initFirebase() {
    if (typeof firebase === 'undefined') return;          // SDK not loaded on this page
    try {
        if (!firebase.apps || !firebase.apps.length) firebase.initializeApp(siteFirebaseConfig);
        db = firebase.firestore();
        auth = firebase.auth();
    } catch (err) {
        console.warn('Firebase unavailable on this page:', err.message);
    }
})();

// Replace legacy team names in rendered markup while preserving existing image
// filenames and URLs. This keeps the home and About pages consistent with the
// canonical team data in content.json.
function updateTeamNames() {
    const replacements = [
        ['MUGISHA GILBERT', 'ISHIMWE GILBERT'],
        ['Mugisha Gilbert', 'Ishimwe Gilbert'],
        ['MUGISHA', 'ISHIMWE'],
        ['CIPHERFOX', 'UWACU EDDY CARNETTY'],
        ['Cipherfox', 'Uwacu Eddy Carnetty']
    ];
    const walker = document.createTreeWalker(document.body, NodeFilter.SHOW_TEXT);
    const textNodes = [];
    while (walker.nextNode()) textNodes.push(walker.currentNode);
    textNodes.forEach(node => {
        let value = node.nodeValue || '';
        replacements.forEach(([oldName, newName]) => { value = value.replaceAll(oldName, newName); });
        node.nodeValue = value;
    });
    document.querySelectorAll('img[alt]').forEach(image => {
        replacements.forEach(([oldName, newName]) => {
            image.alt = image.alt.replaceAll(oldName, newName);
        });
    });
}

// ======================================== //
// DOM READY                                //
// ======================================== //
document.addEventListener('DOMContentLoaded', function () {

    updateTeamNames();

    // ======================================== //
    // HEADER SCROLL EFFECT (rAF-throttled)     //
    // ======================================== //
    const header = document.getElementById('header');
    if (header) {
        let ticking = false;
        const update = function () {
            header.classList.toggle('scrolled', (window.pageYOffset || document.documentElement.scrollTop) > 50);
            ticking = false;
        };
        window.addEventListener('scroll', function () {
            if (!ticking) { ticking = true; window.requestAnimationFrame(update); }
        }, { passive: true });
        update();
    }

    // ======================================== //
    // HAMBURGER MENU                           //
    // ======================================== //
    const hamburger = document.getElementById('hamburger');
    const navLinks = document.getElementById('navLinks');

    if (hamburger && navLinks) {
        const setMenu = function (open) {
            hamburger.classList.toggle('active', open);
            navLinks.classList.toggle('open', open);
            hamburger.setAttribute('aria-expanded', String(open));
            document.body.style.overflow = open ? 'hidden' : '';
        };
        hamburger.addEventListener('click', function () {
            setMenu(!navLinks.classList.contains('open'));
        });
        navLinks.querySelectorAll('a').forEach(link => {
            link.addEventListener('click', () => setMenu(false));
        });
        document.addEventListener('keydown', e => { if (e.key === 'Escape') setMenu(false); });
        window.addEventListener('resize', () => { if (window.innerWidth > 992) setMenu(false); });
    }

    // ======================================== //
    // PRELOADER                                //
    // ======================================== //
    const preloader = document.getElementById('preloader');
    if (preloader) {
        const hide = function () {
            preloader.classList.add('hide');
            setTimeout(() => { preloader.style.display = 'none'; }, 700);
        };
        window.addEventListener('load', function () { setTimeout(hide, 350); });
        setTimeout(hide, 3500);   // never trap the visitor behind a spinner
    }

    // ======================================== //
    // REVEAL ANIMATIONS (local, no CDN)        //
    // ======================================== //
    if (typeof AOS !== 'undefined') {
        AOS.init({ duration: 700, once: true, offset: 40 });
    }

    // ======================================== //
    // BACK TO TOP                              //
    // ======================================== //
    const toTop = document.getElementById('backToTop');
    if (toTop) {
        window.addEventListener('scroll', function () {
            toTop.classList.toggle('show', (window.pageYOffset || 0) > 700);
        }, { passive: true });
        toTop.addEventListener('click', function () {
            const reduce = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
            window.scrollTo({ top: 0, behavior: reduce ? 'auto' : 'smooth' });
        });
    }
});
