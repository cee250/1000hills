#!/usr/bin/env python3
"""Regenerate the 34 small-business website demos as rich, mobile-first sites
(sticky header + drawer nav, hero with product card, marquee, services,
about, gallery, testimonials, contact form, footer, WhatsApp FAB).

Run:  python3 scripts/gen_pro_sites.py
"""
import os
import re
import sys
import random
import hashlib

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from demo_data import catalogue                                # noqa: E402
from pro_site_template import CSS, HTML, JS, TOKENS            # noqa: E402
from gen_pro_systems import (hex2rgb, rgb2hex, mix, rgba, luminance,
                             seed_of, initials)                 # noqa: E402

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "demos")
ASSETS = os.path.join(ROOT, "assets")

NAMES = [
    ("Aline Uwase", "Kigali"), ("Jean Bosco Mugabo", "Remera"), ("Divine Mukamana", "Kimironko"),
    ("Eric Nshimiyimana", "Nyarutarama"), ("Grace Ingabire", "Kicukiro"), ("Kevin Habimana", "Gisozi"),
    ("Claire Umutoni", "Kacyiru"), ("Samuel Niyonzima", "Nyamirambo"), ("Sandrine Uwera", "Gikondo"),
    ("Patrick Ndayisaba", "Musanze"), ("Josiane Mutesi", "Rubavu"), ("Thierry Rwigema", "Huye"),
]

# ------------------------------------------------------------------ categories
SERIF_CATS = {"restaurant", "hotel", "realestate", "fitness", "ngo", "events"}

CAT = {
    "restaurant": dict(
        hours="Mon – Sun · 08:00 – 22:30", hours_short="08:00 – 22:30 daily",
        pay="Cash · MTN MoMo · Airtel Money · Card",
        form=("Date & time", "e.g. Friday, 19:30"), pax="Guests",
        pill="Open now · table in 10 min", gal=("Our space", "Come see it in person", "The room, the kitchen and the plate — all designed around your brand."),
        roles=["Regular guest", "Food blogger", "Corporate lunch", "Family of six"],
        strip=["Wood & charcoal grill", "MoMo and card", "Group bookings", "Takeaway in 15 min", "Kids menu", "Terrace seating"],
        gal_icons=["fa-utensils", "fa-fire-burner", "fa-mug-hot", "fa-wine-glass", "fa-cake-candles", "fa-bowl-food"],
        badge=("4.8", "Google rating"), nav_icon="fa-utensils",
        about_k="Our kitchen", cards_k="On the menu",
        addr=lambda p: "%s, Kigali — opposite the main road" % p,
    ),
    "hotel": dict(
        hours="Reception 24 hours · Check-in from 14:00", hours_short="Reception 24/7",
        pay="Cash · MoMo · Visa · Mastercard · Bank transfer",
        form=("Check-in date", "e.g. 12 Oct – 15 Oct"), pax="Guests",
        pill="Rooms available tonight", gal=("The property", "Rooms, gardens and views", "Every photo block becomes your own gallery in the live build."),
        roles=["Business traveller", "Weekend guest", "Conference organiser", "Family holiday"],
        strip=["Airport transfer", "Fibre Wi-Fi", "Restaurant & bar", "Conference room", "Laundry", "Secure parking"],
        gal_icons=["fa-bed", "fa-bath", "fa-mountain-sun", "fa-mug-saucer", "fa-person-swimming", "fa-concierge-bell"],
        badge=("24/7", "Reception"), nav_icon="fa-bed",
        about_k="The stay", cards_k="Rooms & amenities",
        addr=lambda p: "%s, Kigali — 20 min from Kigali International" % p,
    ),
    "ecommerce": dict(
        hours="Online orders 24/7 · Dispatch 08:00 – 18:00", hours_short="Orders 24/7",
        pay="MTN MoMo · Airtel Money · Card · Cash on delivery",
        form=("Delivery area", "e.g. Kimironko, Kigali"), pax="Items",
        pill="Same-day delivery in Kigali", gal=("In the shop", "Stock you can browse", "Product cards, filters and MoMo checkout — wired to your stock."),
        roles=["Repeat buyer", "Wholesale client", "Gift shopper", "New customer"],
        strip=["Kigali same-day", "Nationwide courier", "MoMo checkout", "7-day returns", "WhatsApp ordering", "Bulk prices"],
        gal_icons=["fa-box-open", "fa-basket-shopping", "fa-truck-fast", "fa-tags", "fa-shield-halved", "fa-mobile-screen"],
        badge=("24/7", "Ordering"), nav_icon="fa-basket-shopping",
        about_k="Why shop here", cards_k="What we sell",
        addr=lambda p: "Warehouse & pickup: %s, Kigali" % p,
    ),
    "education": dict(
        hours="Mon – Fri · 07:30 – 17:30 · Sat 08:00 – 13:00", hours_short="Mon – Fri 07:30 – 17:30",
        pay="Bank transfer · MoMo · Cash · Termly plans",
        form=("Preferred start", "e.g. January term"), pax="Learners",
        pill="Enrolment open for this term", gal=("Campus life", "Classrooms, labs and play", "Add your real photos and we build the gallery around them."),
        roles=["Parent of two", "Adult learner", "School governor", "Sponsor"],
        strip=["Qualified teachers", "Small classes", "Termly reports", "School bus", "Lunch programme", "Clubs & sport"],
        gal_icons=["fa-chalkboard-user", "fa-book-open-reader", "fa-flask", "fa-futbol", "fa-bus", "fa-graduation-cap"],
        badge=("98%", "Pass rate"), nav_icon="fa-graduation-cap",
        about_k="How we teach", cards_k="Programmes",
        addr=lambda p: "%s, Kigali — near the bus stop" % p,
    ),
    "health": dict(
        hours="Mon – Sat · 08:00 – 18:00 · Emergencies 24/7", hours_short="Mon – Sat 08:00 – 18:00",
        pay="Cash · MoMo · Card · RAMA & private insurance",
        form=("Preferred day", "e.g. Tuesday morning"), pax="Patients",
        pill="Bookings confirmed on WhatsApp", gal=("Our clinic", "Rooms, lab and team", "Private, calm and accessible — your photos go here."),
        roles=["Patient", "Parent", "Referred by a doctor", "Corporate wellness"],
        strip=["Licensed clinicians", "Lab on site", "Insurance accepted", "Digital records", "Home visits", "Pharmacy"],
        gal_icons=["fa-stethoscope", "fa-vial", "fa-hospital", "fa-pills", "fa-heart-pulse", "fa-user-nurse"],
        badge=("24/7", "Emergencies"), nav_icon="fa-calendar-check",
        about_k="Our care", cards_k="Services",
        addr=lambda p: "%s, Kigali — ground floor, step-free access" % p,
    ),
    "corporate": dict(
        hours="Mon – Fri · 08:00 – 17:30", hours_short="Mon – Fri 08:00 – 17:30",
        pay="Bank transfer · Purchase order · Card",
        form=("Company", "e.g. Kigali Foods Ltd"), pax="Team size",
        pill="Replies within one business hour", gal=("Our work", "Projects and people", "Case studies, logos and outcomes — the sections clients ask for."),
        roles=["Procurement lead", "Managing director", "IT manager", "Finance officer"],
        strip=["Contracts & SLAs", "Company profiles", "Multi-site teams", "Reports & invoicing", "Local references", "After-sales support"],
        gal_icons=["fa-briefcase", "fa-handshake", "fa-chart-line", "fa-building", "fa-file-contract", "fa-people-group"],
        badge=("12+ yrs", "In business"), nav_icon="fa-briefcase",
        about_k="Who we are", cards_k="What we do",
        addr=lambda p: "%s, Kigali — by appointment" % p,
    ),
    "events": dict(
        hours="Bookings daily · 09:00 – 20:00", hours_short="Bookings 09:00 – 20:00",
        pay="Deposit by MoMo · Balance on the day · Card",
        form=("Event date", "e.g. 14 December"), pax="Guests",
        pill="Weekend dates filling fast", gal=("On the day", "Sets, sound and crowds", "Your portfolio, reels and photo wall live here."),
        roles=["Bride & groom", "Corporate event", "Birthday client", "Festival organiser"],
        strip=["Sound & lighting", "MC and DJ", "Photo & video", "Venue styling", "Deposit by MoMo", "Nationwide travel"],
        gal_icons=["fa-music", "fa-microphone", "fa-camera-retro", "fa-lightbulb", "fa-champagne-glasses", "fa-calendar-days"],
        badge=("200+", "Events"), nav_icon="fa-calendar-days",
        about_k="How we work", cards_k="Packages",
        addr=lambda p: "Studio: %s, Kigali — we travel nationwide" % p,
    ),
    "fitness": dict(
        hours="Mon – Sat · 06:00 – 21:00 · Sun 08:00 – 14:00", hours_short="Mon – Sat 06:00 – 21:00",
        pay="Cash · MoMo · Card · Monthly plans",
        form=("Preferred time", "e.g. Saturday 10:00"), pax="People",
        pill="Walk-ins welcome today", gal=("The space", "Chairs, studios and gear", "Real photos of your space convert bookings — we handle the gallery."),
        roles=["Weekly regular", "Bridal client", "New member", "Couple"],
        strip=["Qualified stylists", "Walk-ins welcome", "Monthly plans", "Kids friendly", "Card & MoMo", "Gift vouchers"],
        gal_icons=["fa-scissors", "fa-dumbbell", "fa-spa", "fa-spray-can-sparkles", "fa-person-running", "fa-heart"],
        badge=("4.9", "Client rating"), nav_icon="fa-calendar-check",
        about_k="Our standards", cards_k="Services",
        addr=lambda p: "%s, Kigali — first floor, lift access" % p,
    ),
    "agriculture": dict(
        hours="Mon – Sat · 07:00 – 18:00 · Collection daily", hours_short="Mon – Sat 07:00 – 18:00",
        pay="MoMo · Bank transfer · Cash at collection",
        form=("Volume needed", "e.g. 2 tonnes / month"), pax="Units",
        pill="Harvest season — booking now", gal=("From the farm", "Fields, drying beds and packs", "Traceability, certifications and farm photos belong here."),
        roles=["Buyer / exporter", "Co-op member", "Retailer", "Restaurant chef"],
        strip=["Farm-gate prices", "Traceable lots", "Drying & grading", "Export paperwork", "Farmer payments by MoMo", "Bulk delivery"],
        gal_icons=["fa-seedling", "fa-tractor", "fa-wheat-awn", "fa-cow", "fa-leaf", "fa-boxes-packing"],
        badge=("42 ha", "Under management"), nav_icon="fa-seedling",
        about_k="How we grow", cards_k="What we produce",
        addr=lambda p: "Farm & collection point: %s" % p,
    ),
    "ngo": dict(
        hours="Mon – Fri · 08:00 – 17:00", hours_short="Mon – Fri 08:00 – 17:00",
        pay="Donations: MoMo · Bank · Card · PayPal",
        form=("How can we help?", "e.g. Partnership or donation"), pax="People",
        pill="Donations reach the field in 48h", gal=("Our impact", "Programmes and communities", "Field photos, beneficiary stories and donor reports live here."),
        roles=["Monthly donor", "Community leader", "Volunteer", "Partner NGO"],
        strip=["Registered NGO", "Audited accounts", "Donor reports", "Volunteer programme", "Community-led", "Safeguarding policy"],
        gal_icons=["fa-hand-holding-heart", "fa-people-group", "fa-school", "fa-droplet", "fa-hands-holding-child", "fa-chart-simple"],
        badge=("3,400+", "Lives reached"), nav_icon="fa-hand-holding-heart",
        about_k="Our mission", cards_k="Programmes",
        addr=lambda p: "Head office: %s, Kigali" % p,
    ),
    "realestate": dict(
        hours="Mon – Sat · 08:00 – 18:00 · Viewings by booking", hours_short="Mon – Sat 08:00 – 18:00",
        pay="Bank transfer · MoMo deposit · Escrow",
        form=("Viewing date", "e.g. Saturday 10:00"), pax="Viewers",
        pill="Viewings this week available", gal=("The property", "Interiors, plots and views", "Your listings, floor plans and site photos go here."),
        roles=["First-time buyer", "Investor", "Tenant", "Returning client"],
        strip=["Verified titles", "Viewings in 24h", "Mortgage help", "Property management", "Off-plan payment plans", "Legal support"],
        gal_icons=["fa-house-chimney", "fa-city", "fa-key", "fa-ruler-combined", "fa-tree", "fa-building"],
        badge=("86", "Live listings"), nav_icon="fa-house-chimney",
        about_k="How we sell", cards_k="Listings & services",
        addr=lambda p: "Agency: %s, Kigali" % p,
    ),
}

DEFAULT = CAT["corporate"]


def cfg(d):
    return CAT.get(d.get("cat", ""), DEFAULT)


def phone_for(seed):
    """Well-formed (fictional) Rwandan mobile number: +250 7XX XXX XXX."""
    rnd = random.Random(seed)
    prefix = rnd.choice(["72", "73", "78", "79"]) + str(rnd.randint(0, 9))
    return "+250 %s %03d %03d" % (prefix, rnd.randint(100, 999), rnd.randint(100, 999))


def slug(t):
    return re.sub(r"[^a-z0-9]+", "-", str(t).lower()).strip("-") or "section"


def build(d):
    fname = d["file"]
    rnd = random.Random(seed_of(fname))
    c = cfg(d)

    bg = d.get("bg", "#0F172A")
    card = d.get("card", "#FFFFFF")
    ink = d.get("ink", "#F8FAFC")
    acc = d.get("acc", "#38BDF8")
    acc2 = d.get("acc2", mix(acc, "#FFFFFF", .3))
    muted = d.get("muted", mix(ink, bg, .42))
    iconc = d.get("iconc", "#0B1220" if luminance(acc) > .62 else "#FFFFFF")

    dark = luminance(bg) < .45
    if card.lower() in ("#fff", "#ffffff", "white"):
        card = "#FFFFFF" if not dark else mix(bg, "#FFFFFF", .07)
    bg2 = mix(bg, card, .45)
    card2 = mix(card, bg, .45)
    faint = mix(muted, bg, .38)
    if dark:
        line, line2 = rgba("#FFFFFF", .1), rgba("#FFFFFF", .19)
    else:
        line, line2 = rgba(ink, .1), rgba(ink, .18)

    navbg = d.get("navbg") or (rgba(bg, .92) if dark else rgba("#FFFFFF", .92))
    if navbg.lower().startswith("#") and len(navbg) < 9:
        navbg = rgba(navbg, .93)
    herobg = d.get("herobg") or (bg2 if not dark else mix(bg, acc, .05))

    display = "'Playfair Display', Georgia, serif" if d.get("cat") in SERIF_CATS else "var(--font)"
    if display.startswith("'Playfair"):
        font_url = ("https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800"
                    "&family=Playfair+Display:wght@600;700;800&display=swap")
    else:
        font_url = "https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&display=swap"

    name = d["name"]
    place = d.get("place", "Kigali")
    nav_labels = list(d.get("nav", ["Services", "About", "Contact"]))
    while len(nav_labels) < 3:
        nav_labels.append("Gallery")
    ids = ["services", "about", "gallery", "contact"]
    nav_full = nav_labels[:3] + ["Contact"]
    nav_icons = [c["nav_icon"], "fa-circle-info", "fa-images", "fa-paper-plane"]

    nav_html = "".join('<a href="#%s">%s</a>' % (ids[i], nav_full[i]) for i in range(len(nav_full)))
    drawer_html = "".join(
        '<a href="#%s"><i class="fas %s" aria-hidden="true"></i> %s</a>' % (ids[i], nav_icons[i], nav_full[i])
        for i in range(len(nav_full)))
    foot_nav = "".join('<li><a href="#%s"><i class="fas fa-chevron-right" aria-hidden="true"></i> %s</a></li>'
                       % (ids[i], nav_full[i]) for i in range(len(nav_full)))

    stats = "".join('<div><strong>%s</strong><span>%s</span></div>' % (v, l) for v, l in d.get("stats", []))

    cards_src = list(d.get("cards", []))
    features = list(d.get("features", []))
    cards_html = "".join(
        '<article class="card rv" data-delay="%d"><span class="cic"><i class="fas %s" aria-hidden="true"></i></span>'
        '<h3>%s</h3><p>%s</p></article>' % (i * 70, ic, t, p) for i, (ic, t, p) in enumerate(cards_src[:4]))

    vrows = "".join(
        '<div class="vrow"><i class="fas %s" aria-hidden="true"></i><span><b>%s</b><small>%s</small></span>'
        '<span class="tagm">%s</span></div>'
        % (ic, t, p, (features[i] if i < len(features) else "Included"))
        for i, (ic, t, p) in enumerate(list(d.get("cards", []))[:3]))

    strip_items = list(features) + list(c["strip"])
    seen, strip = set(), []
    for s in strip_items:
        k = s.lower()
        if k in seen:
            continue
        seen.add(k)
        strip.append(s)
    strip_html = "".join('<span><i class="fas fa-circle-check" aria-hidden="true"></i> %s</span>' % s
                         for s in strip[:8])

    list_html = "".join('<li><i class="fas fa-check" aria-hidden="true"></i> %s</li>' % x
                        for x in d.get("list", []))

    arts_src = list(d.get("cards", []))[:3]
    arts = []
    for i, (ic, t, p) in enumerate(arts_src):
        cls = "art alt rv" if i == 1 else "art rv"
        arts.append('<div class="%s" data-delay="%d"><i class="fas %s big" aria-hidden="true"></i>'
                    '<div><h4>%s</h4><p>%s</p></div></div>' % (cls, i * 90, ic, t, p))
    while len(arts) < 3:
        arts.append('<div class="art rv"><i class="fas %s big" aria-hidden="true"></i>'
                    '<div><h4>%s</h4><p>Built and branded for you by 1000 Hills Group.</p></div></div>'
                    % (c["gal_icons"][len(arts) % len(c["gal_icons"])], name))
    arts_html = "".join(arts)

    gal_captions = [t for _, t, _ in list(d.get("cards", []))] + features + nav_labels
    seen2, caps = set(), []
    for g in gal_captions:
        if g.lower() in seen2:
            continue
        seen2.add(g.lower())
        caps.append(g)
    gal_html = "".join(
        '<figure class="gtile rv" data-delay="%d" data-toast="Photo block — we drop in your own photography.">'
        '<i class="fas %s" aria-hidden="true"></i><figcaption>%s</figcaption></figure>'
        % ((i % 3) * 80, c["gal_icons"][i % len(c["gal_icons"])], caps[i % len(caps)] if caps else name)
        for i in range(6))

    quotes_tpl = [
        "Booked through the website on a Sunday night and got a WhatsApp confirmation in two minutes. %s is now the only place we go in %s.",
        "I compared four places in Kigali — %s won on price and on how fast they answered. The whole booking took one message.",
        "As a %s I need reliability. %s has never let me down, and the online form means I stop calling around.",
        "The team remembered every preference from last time. That is rare in Kigali, and it is why we keep coming back to %s.",
        "Paid with MoMo, got a receipt instantly, and the service was exactly as described online. Highly recommended.",
    ]
    quotes = []
    for i in range(3):
        person, town = NAMES[(seed_of(fname) + i * 5) % len(NAMES)]
        role = c["roles"][i % len(c["roles"])]
        tpl = quotes_tpl[(seed_of(fname) + i * 3) % len(quotes_tpl)]
        text = _fill(tpl, [name, place, role, place])
        quotes.append(
            '<figure class="quote rv" data-delay="%d"><div class="qm"><i class="fas fa-quote-left" aria-hidden="true"></i></div>'
            '<p>%s</p><div class="who"><span class="av">%s</span><span><b>%s</b><small>%s · %s</small></span>'
            '<span class="stars">%s</span></div></figure>'
            % (i * 90, text, initials(person), person, role, town,
               '<i class="fas fa-star"></i>' * 5))
    quotes_html = "".join(quotes)

    phone = phone_for(seed_of(fname))
    wa = "https://wa.me/250788695396?text=" + d.get("wa", "")
    pax_opts = "".join('<option>%d</option>' % n for n in (1, 2, 3, 4, 5, 6, 8, 10, 12, 20))

    big, small = c["badge"]
    rating = "%.1f" % (4.6 + (seed_of(fname) % 4) / 10.0)

    footer_about = ("%s — %s in %s. This is a fictional demo business created by 1000 Hills Group to show "
                    "what your own website could look like." % (name, d.get("tagline", "").lower(), place))

    lead = d.get("lead") or d.get("desc", "")
    about = d.get("about", "")
    if about and len(about) < 90:
        about = about + " Every detail — colours, photos, wording and forms — is rebuilt around your brand."

    tokens = {
        "@@TOKENS@@": TOKENS,
        "@@TITLE@@": "%s | %s in %s — Website Demo by 1000 Hills Group" % (name, d.get("tagline", "Business"), place),
        "@@META_DESC@@": ("Live website demo by 1000 Hills Group: %s — %s Fully responsive on phone, tablet and desktop."
                          % (name, d.get("desc", ""))),
        "@@NAME@@": name, "@@ICON@@": d.get("icon", "fa-star"),
        "@@TAGLINE@@": d.get("tagline", ""), "@@PLACE@@": place,
        "@@H1@@": d.get("h1", name), "@@LEAD@@": lead,
        "@@H2@@": d.get("h2", c["cards_k"]), "@@BTN@@": d.get("btn", "Book now"),
        "@@STATS@@": stats, "@@NAV@@": nav_html, "@@DRAWER@@": drawer_html, "@@FOOT_NAV@@": foot_nav,
        "@@NAV1@@": nav_labels[0], "@@NAV1_ID@@": "services", "@@NAV1_ICON@@": c["nav_icon"],
        "@@VISUAL_ROWS@@": vrows, "@@STRIP@@": strip_html,
        "@@PILL_TEXT@@": c["pill"], "@@BADGE_BIG@@": big, "@@BADGE_SMALL@@": small,
        "@@RATING@@": rating, "@@REVIEW_COUNT@@": str(60 + seed_of(fname) % 240),
        "@@CARDS@@": cards_html, "@@CARDS_ID@@": "services",
        "@@CARDS_KICKER@@": c["cards_k"], "@@CARDS_SUB@@": d.get("desc", ""),
        "@@ABOUT_KICKER@@": c["about_k"], "@@ABOUT_H@@": d.get("about_h", "Why %s" % name),
        "@@ABOUT@@": about, "@@LIST@@": list_html, "@@ARTS@@": arts_html,
        "@@GAL_KICKER@@": c["gal"][0], "@@GAL_H@@": c["gal"][1], "@@GAL_SUB@@": c["gal"][2],
        "@@GALLERY@@": gal_html, "@@QUOTES@@": quotes_html,
        "@@CTA_H@@": d.get("cta_h", "Ready when you are"),
        "@@CTA_P@@": ("%s Message us on WhatsApp and we will confirm within minutes — "
                      "or send the form and we will call you back." % d.get("cta_p", "")),
        "@@ADDRESS@@": c["addr"](place), "@@HOURS@@": c["hours"], "@@HOURS_SHORT@@": c["hours_short"],
        "@@PHONE@@": phone, "@@PAYMENTS@@": c["pay"],
        "@@FORM_FIELD@@": c["form"][0], "@@FORM_PLACEHOLDER@@": c["form"][1], "@@PAX@@": pax_opts,
        "@@FOOTER_ABOUT@@": footer_about, "@@YEAR@@": "2026",
        "@@WA_URL@@": wa,
        "@@HERO_BG@@": herobg, "@@NAV_BG@@": navbg, "@@BG@@": bg, "@@BG2@@": bg2,
        "@@CARD@@": card, "@@CARD2@@": card2, "@@INK@@": ink, "@@MUTED@@": muted, "@@FAINT@@": faint,
        "@@LINE@@": line, "@@LINE2@@": line2,
        "@@ACC@@": acc, "@@ACC2@@": acc2, "@@ACC_INK@@": iconc, "@@ACC_BG@@": rgba(acc, .13),
        "@@ACC_LINE@@": rgba(acc, .32), "@@BRAND_ICON_COLOR@@": iconc,
        "@@DISPLAY_FONT@@": display, "@@FONT_URL@@": font_url,
    }

    html = HTML
    for k, v in tokens.items():
        html = html.replace(k, v)

    letter = name[0].upper()
    fav = ("data:image/svg+xml," + ("<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 64 64'>"
           "<rect width='64' height='64' rx='14' fill='%s'/><text x='32' y='45' font-family='Inter,Arial' "
           "font-size='34' font-weight='800' text-anchor='middle' fill='%s'>%s</text></svg>"
           % (acc.replace("#", "%23"), iconc.replace("#", "%23"), letter)).replace("#", "%23"))
    return html.replace("@@FAVICON@@", fav)


def _fill(tpl, values):
    """Fill %s placeholders in order, tolerating templates with fewer slots."""
    out, i = [], 0
    parts = tpl.split("%s")
    for n, part in enumerate(parts):
        out.append(part)
        if n < len(parts) - 1:
            out.append(str(values[i % len(values)]))
            i += 1
    return "".join(out)


def write_assets():
    os.makedirs(ASSETS, exist_ok=True)
    with open(os.path.join(ASSETS, "pro-site.css"), "w", encoding="utf-8") as f:
        f.write("/* 1000 Hills Group — shared website-demo shell.\n"
                "   Generated by scripts/gen_pro_sites.py — do not edit by hand. */\n"
                + CSS.strip() + "\n")
    with open(os.path.join(ASSETS, "pro-site.js"), "w", encoding="utf-8") as f:
        f.write("/* 1000 Hills Group — shared website-demo behaviour.\n"
                "   Generated by scripts/gen_pro_sites.py — do not edit by hand. */\n"
                + JS.strip() + "\n")


def main():
    _, sites = catalogue()
    os.makedirs(ROOT, exist_ok=True)
    write_assets()
    for d in sites:
        with open(os.path.join(ROOT, d["file"]), "w", encoding="utf-8") as f:
            f.write(build(d))
    print("wrote %d pro website demos" % len(sites))


if __name__ == "__main__":
    main()
