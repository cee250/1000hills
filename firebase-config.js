// ========================================
// FIREBASE CONFIG - 1000 HILLS GROUP
// ========================================

// Wrapped in an IIFE on purpose. This file used to declare `firebaseConfig`,
// `db`, `auth` and `storage` as top-level consts, which collide with the same
// names in main.js and crash the page with
// "Identifier 'x' has already been declared" if both files are ever loaded
// together. Everything is still exported on `window`, so existing code keeps
// working.
(function () {
    var firebaseConfig = {
        apiKey: "AIzaSyABeFEPPKjKVFU14cx4s__uwWLRpHa5J2c",
        authDomain: "luxury-properties-36554.firebaseapp.com",
        projectId: "luxury-properties-36554",
        storageBucket: "luxury-properties-36554.firebasestorage.app",
        messagingSenderId: "214959691683",
        appId: "1:214959691683:web:864ba0f961cfefd7baac16"
    };

    if (typeof firebase === 'undefined') {
        console.warn('firebase-config.js: Firebase SDK not loaded — skipping initialisation.');
        return;
    }

    // Initialize Firebase
    if (!firebase.apps || !firebase.apps.length) firebase.initializeApp(firebaseConfig);
    var db = firebase.firestore();
    var auth = firebase.auth();
    var storage = firebase.storage();

    // Collection references
    var SERVICES_COLLECTION = 'services';
    var TEAM_COLLECTION = 'team';
    var PORTFOLIO_COLLECTION = 'portfolio';
    var TESTIMONIALS_COLLECTION = 'testimonials';
    var CLIENTS_COLLECTION = 'clients';

    // Export for use in other files
    window.db = db;
    window.auth = auth;
    window.storage = storage;
    window.firebaseCollections = {
        services: SERVICES_COLLECTION,
        team: TEAM_COLLECTION,
        portfolio: PORTFOLIO_COLLECTION,
        testimonials: TESTIMONIALS_COLLECTION,
        clients: CLIENTS_COLLECTION
    };
})();
