// ======================================== //
// MAIN.JS - FIREBASE CONFIG & INIT        //
// ======================================== //

// ======================================== //
// FIREBASE CONFIG                          //
// ======================================== //
const firebaseConfig = {
    apiKey: "AIzaSyABeFEPPKjKVFU14cx4s__uwWLRpHa5J2c",
    authDomain: "luxury-properties-36554.firebaseapp.com",
    projectId: "luxury-properties-36554",
    storageBucket: "luxury-properties-36554.firebasestorage.app",
    messagingSenderId: "214959691683",
    appId: "1:214959691683:web:864ba0f961cfefd7baac16"
};

// Initialize Firebase
firebase.initializeApp(firebaseConfig);
const db = firebase.firestore();
const auth = firebase.auth();

// ======================================== //
// DOM READY                                //
// ======================================== //
document.addEventListener('DOMContentLoaded', function() {
    
    // ======================================== //
    // HEADER SCROLL EFFECT                    //
    // ======================================== //
    const header = document.getElementById('header');
    if (header) {
        window.addEventListener('scroll', function() {
            if (window.pageYOffset > 50) {
                header.classList.add('scrolled');
            } else {
                header.classList.remove('scrolled');
            }
        });
    }

    // ======================================== //
    // HAMBURGER MENU                          //
    // ======================================== //
    const hamburger = document.getElementById('hamburger');
    const navLinks = document.getElementById('navLinks');
    
    if (hamburger && navLinks) {
        hamburger.addEventListener('click', function() {
            this.classList.toggle('active');
            navLinks.classList.toggle('open');
            const isOpen = navLinks.classList.contains('open');
            if (this) this.setAttribute('aria-expanded', isOpen);
        });

        navLinks.querySelectorAll('a').forEach(link => {
            link.addEventListener('click', function() {
                hamburger.classList.remove('active');
                navLinks.classList.remove('open');
                if (hamburger) hamburger.setAttribute('aria-expanded', 'false');
            });
        });
    }

    // ======================================== //
    // PRELOADER                               //
    // ======================================== //
    const preloader = document.getElementById('preloader');
    if (preloader) {
        window.addEventListener('load', function() {
            setTimeout(() => {
                preloader.classList.add('hide');
            }, 800);
        });
    }

    // ======================================== //
    // AOS INIT                                 //
    // ======================================== //
    if (typeof AOS !== 'undefined') {
        AOS.init({
            duration: 800,
            once: true,
            offset: 50,
            easing: 'ease-out-cubic'
        });
    }

    console.log('🚀 1000 Hills Group - Website Loaded Successfully!');
    console.log('🔥 Connected to Firebase Firestore');
});