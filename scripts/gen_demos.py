#!/usr/bin/env python3
"""Generate extra industry demo pages for 1000 Hills Group."""
import json
import os

ROOT = os.path.join(os.path.dirname(__file__), "..", "demos")

BAR = """
<div class="demo-bar" id="demoBar">
  <div class="db-left"><i class="fas fa-bolt"></i> <a href="../demos.html">1000 Hills Group</a> — Live {kind} Demo</div>
  <div class="db-right">
    <a class="db-cta" href="https://wa.me/250788695396?text={wa}" target="_blank" rel="noopener">{cta}</a>
    <button class="db-close" onclick="document.getElementById('demoBar').classList.add('hidden');document.body.style.paddingTop=0" aria-label="Close"><i class="fas fa-times"></i></button>
  </div>
</div>
"""

def site_html(d):
    feats = "".join(f'<div class="card"><i class="fas {ic}"></i><h3>{t}</h3><p>{p}</p></div>' for ic,t,p in d["cards"])
    nav = "".join(f'<a href="#{n.lower()}">{n}</a>' for n in d["nav"])
    stats = "".join(f'<div><strong>{s}</strong><span>{l}</span></div>' for s,l in d["stats"])
    items = "".join(f'<li><i class="fas fa-check"></i> {x}</li>' for x in d["list"])
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8"/>
<meta name="viewport" content="width=device-width, initial-scale=1.0"/>
<title>{d["name"]} | {d["tagline"]} — Demo by 1000 Hills Group</title>
<meta name="description" content="Live website demo by 1000 Hills Group — {d["desc"]}"/>
<link rel="preconnect" href="https://fonts.googleapis.com"/>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&family=Playfair+Display:wght@600;700&display=swap" rel="stylesheet"/>
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.0/css/all.min.css"/>
<style>
:root{{--bg:{d["bg"]};--ink:{d["ink"]};--muted:{d["muted"]};--acc:{d["acc"]};--acc2:{d["acc2"]};--card:{d["card"]};--line:{d["line"]};}}
*{{margin:0;padding:0;box-sizing:border-box}}body{{font-family:Inter,sans-serif;background:var(--bg);color:var(--ink);line-height:1.65;padding-top:46px}}
a{{text-decoration:none;color:inherit}}ul{{list-style:none}}h1,h2,.serif{{font-family:'Playfair Display',serif}}
.demo-bar{{position:fixed;top:0;left:0;right:0;height:46px;background:#0A1628;display:flex;align-items:center;justify-content:space-between;padding:0 16px;z-index:9999;border-bottom:1px solid rgba(201,169,110,.35)}}
.demo-bar .db-left{{display:flex;align-items:center;gap:8px;font-size:.78rem;color:#E8D5A3}}
.demo-bar .db-left i,.demo-bar .db-left a{{color:#E8D5A3;font-weight:600}}
.demo-bar .db-cta{{background:linear-gradient(135deg,#C9A96E,#E8D5A3);color:#0A1628;font-size:.72rem;font-weight:700;padding:5px 12px;border-radius:30px}}
.demo-bar .db-close{{background:none;border:0;color:#A8B9D0;cursor:pointer}}
header{{position:sticky;top:46px;z-index:50;background:{d["navbg"]};backdrop-filter:blur(12px);border-bottom:1px solid var(--line)}}
.nav{{width:min(1120px,92%);margin:0 auto;display:flex;align-items:center;justify-content:space-between;padding:14px 0;gap:16px}}
.brand{{display:flex;align-items:center;gap:10px;font-weight:800}}
.brand .ic{{width:38px;height:38px;border-radius:10px;background:linear-gradient(135deg,var(--acc),var(--acc2));display:grid;place-items:center;color:{d["iconc"]}}}
.nav-links{{display:flex;gap:22px;font-size:.86rem;font-weight:600;color:var(--muted)}}
.btn{{display:inline-flex;align-items:center;gap:8px;padding:11px 22px;border-radius:40px;font-weight:700;font-size:.84rem;background:linear-gradient(135deg,var(--acc),var(--acc2));color:{d["iconc"]}}}
.hero{{padding:88px 0 70px;background:{d["herobg"]};}}
.wrap{{width:min(1120px,92%);margin:0 auto}}
.pill{{display:inline-flex;gap:8px;align-items:center;border:1px solid var(--line);padding:7px 14px;border-radius:30px;font-size:.75rem;letter-spacing:1.5px;text-transform:uppercase;color:var(--acc);font-weight:700}}
.hero h1{{font-size:clamp(2.1rem,5vw,3.6rem);line-height:1.1;margin:16px 0;max-width:16ch}}
.hero h1 em{{color:var(--acc);font-style:normal}}
.hero p{{max-width:52ch;color:var(--muted);font-size:1.05rem}}
.hero-btns{{display:flex;gap:12px;margin-top:28px;flex-wrap:wrap}}
.btn-ghost{{background:transparent;border:1px solid var(--line);color:var(--ink)}}
.stats{{display:flex;gap:36px;margin-top:40px;flex-wrap:wrap}}
.stats strong{{display:block;font-size:1.6rem;color:var(--acc)}}
.stats span{{font-size:.78rem;color:var(--muted)}}
section{{padding:72px 0}}
.sec{{text-align:center;max-width:640px;margin:0 auto 40px}}
.sec .k{{color:var(--acc);font-size:.75rem;letter-spacing:2px;font-weight:800;text-transform:uppercase}}
.sec h2{{font-size:clamp(1.6rem,3vw,2.4rem);margin:8px 0}}
.grid{{display:grid;grid-template-columns:repeat(auto-fit,minmax(240px,1fr));gap:18px}}
.card{{background:var(--card);border:1px solid var(--line);border-radius:16px;padding:26px}}
.card i{{color:var(--acc);font-size:1.3rem;margin-bottom:12px}}
.split{{display:grid;grid-template-columns:1fr 1fr;gap:40px;align-items:center}}
.split ul li{{margin:10px 0;display:flex;gap:10px;align-items:flex-start}}
.split ul i{{color:var(--acc);margin-top:4px}}
.cta{{text-align:center;background:{d["ctabg"]};}}
footer{{border-top:1px solid var(--line);padding:40px 0;color:var(--muted);font-size:.85rem}}
.frow{{display:flex;justify-content:space-between;flex-wrap:wrap;gap:12px}}
.frow a{{color:var(--acc);font-weight:700}}
@media(max-width:800px){{.nav-links{{display:none}}.split{{grid-template-columns:1fr}}}}
</style>
</head>
<body>
{BAR.format(kind=d["kind"], wa=d["wa"], cta=d["cta"])}
<header><div class="nav">
  <a class="brand" href="#"><span class="ic"><i class="fas {d["icon"]}"></i></span>{d["name"]}</a>
  <nav class="nav-links">{nav}</nav>
  <a class="btn" href="https://wa.me/250788695396" target="_blank"><i class="fab fa-whatsapp"></i> {d["btn"]}</a>
</div></header>
<section class="hero"><div class="wrap">
  <span class="pill"><i class="fas fa-location-dot"></i> {d["place"]}</span>
  <h1>{d["h1"]}</h1>
  <p>{d["lead"]}</p>
  <div class="hero-btns">
    <a class="btn" href="#offer">{d["btn"]}</a>
    <a class="btn btn-ghost" href="#about">Learn more</a>
  </div>
  <div class="stats">{stats}</div>
</div></section>
<section id="offer"><div class="wrap">
  <div class="sec"><span class="k">{d["kicker"]}</span><h2>{d["h2"]}</h2><p>{d["desc"]}</p></div>
  <div class="grid">{feats}</div>
</div></section>
<section id="about"><div class="wrap split">
  <div>
    <span class="k" style="color:var(--acc);font-size:.75rem;letter-spacing:2px;font-weight:800;text-transform:uppercase">About</span>
    <h2 class="serif" style="font-size:2rem;margin:10px 0">{d["about_h"]}</h2>
    <p style="color:var(--muted)">{d["about"]}</p>
  </div>
  <ul>{items}</ul>
</section>
<section class="cta" id="contact"><div class="wrap">
  <h2 class="serif" style="font-size:2.1rem;margin-bottom:10px">{d["cta_h"]}</h2>
  <p style="color:var(--muted);margin-bottom:22px">{d["cta_p"]}</p>
  <a class="btn" href="https://wa.me/250788695396" target="_blank"><i class="fab fa-whatsapp"></i> WhatsApp us</a>
</div></section>
<footer><div class="wrap frow">
  <p>© 2026 {d["name"]} (fictional demo)</p>
  <p>Website demo by <a href="../demos.html">1000 Hills Group</a></p>
</div></footer>
</body></html>
'''

def sys_html(d):
    kpis = "".join(f'<div class="kpi"><span>{l}</span><strong>{v}</strong></div>' for l,v in d["kpis"])
    rows = "".join(f'<tr><td>{a}</td><td>{b}</td><td>{c}</td><td class="ok">{e}</td></tr>' for a,b,c,e in d["rows"])
    nav = "".join(('<a href="#" class="%s"><i class="fas %s"></i> %s</a>' % ("on" if i==0 else "", ic, t)) for i,(ic,t) in enumerate(d["sidenav"]))
    tpl = '''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8"/>
<meta name="viewport" content="width=device-width, initial-scale=1.0"/>
<title>{d["name"]} | {d["tagline"]} — System Demo</title>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap" rel="stylesheet"/>
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.0/css/all.min.css"/>
<style>
:root{{--side:{d["side"]};--acc:{d["acc"]};--bg:{d["bg"]};--ink:{d["ink"]}}
*{{margin:0;padding:0;box-sizing:border-box}}body{{font-family:Inter,sans-serif;background:var(--bg);color:var(--ink);padding-top:46px;font-size:14px}}
a{{text-decoration:none;color:inherit}}
.demo-bar{{position:fixed;top:0;left:0;right:0;height:46px;background:#0A1628;display:flex;align-items:center;justify-content:space-between;padding:0 16px;z-index:9999}}
.demo-bar .db-left{{color:#E8D5A3;font-size:.78rem;display:flex;gap:8px;align-items:center}}
.demo-bar .db-left a{{color:#E8D5A3;font-weight:600}}
.demo-bar .db-cta{{background:linear-gradient(135deg,#C9A96E,#E8D5A3);color:#0A1628;font-size:.72rem;font-weight:700;padding:5px 12px;border-radius:30px}}
.demo-bar .db-close{{background:none;border:0;color:#A8B9D0;cursor:pointer}}
.app{{display:flex;min-height:calc(100vh - 46px)}}
.sidebar{{width:220px;background:var(--side);color:#c9d4e4;padding:16px 12px}}
.s-logo{{display:flex;gap:10px;align-items:center;color:#fff;font-weight:800;margin-bottom:18px}}
.s-logo .ic{{width:36px;height:36px;border-radius:10px;background:var(--acc);color:#0A1628;display:grid;place-items:center}}
.sidebar a{{display:flex;gap:10px;padding:10px 12px;border-radius:8px;margin:3px 0;font-size:.84rem}}
.sidebar a.on{{background:var(--acc);color:#0A1628;font-weight:700}}
.main{{flex:1;padding:22px}}
.kpis{{display:grid;grid-template-columns:repeat(4,1fr);gap:12px;margin:16px 0}}
.kpi{{background:#fff;border-radius:12px;padding:16px;border:1px solid #e6eaf0}}
.kpi span{{font-size:.72rem;color:#6b7a90;font-weight:700}}
.kpi strong{{display:block;font-size:1.4rem;margin-top:6px}}
table{{width:100%;border-collapse:collapse;background:#fff;border-radius:12px;overflow:hidden}}
th,td{{padding:12px 14px;text-align:left;border-bottom:1px solid #eef1f5;font-size:.84rem}}
th{{background:#f6f8fb;font-size:.72rem;letter-spacing:1px;text-transform:uppercase;color:#6b7a90}}
.ok{{color:#059669;font-weight:700}}
@media(max-width:860px){{.sidebar{{display:none}}.kpis{{grid-template-columns:1fr 1fr}}}}
</style>
</head>
<body>
{BAR.format(kind="System", wa=d["wa"], cta="Get this system")}
<div class="app">
<aside class="sidebar">
  <div class="s-logo"><span class="ic"><i class="fas {d["icon"]}"></i></span>{d["name"]}</div>
  {nav}
</aside>
<main class="main">
  <h2>{d["screen"]}</h2>
  <p style="color:#6b7a90">{d["tagline"]}</p>
  <div class="kpis">{kpis}</div>
  <table>
    <thead><tr><th>{d["cols"][0]}</th><th>{d["cols"][1]}</th><th>{d["cols"][2]}</th><th>{d["cols"][3]}</th></tr></thead>
    <tbody>{rows}</tbody>
  </table>
  <p style="margin-top:18px;font-size:.78rem;color:#6b7a90">System demo by <a href="../demos.html" style="color:var(--acc);font-weight:700">1000 Hills Group</a></p>
</main>
</div>
</body></html>
'''
    # unescape doubled braces for non-f-string then inject
    html = tpl.replace('{{','{').replace('}}','}')
    html = html.replace('{BAR.format(kind="System", wa=d["wa"], cta="Get this system")}', BAR.format(kind="System", wa=d["wa"], cta="Get this system"))
    html = html.replace('{d["name"]}', d["name"]).replace('{d["tagline"]}', d["tagline"])
    html = html.replace('{d["icon"]}', d["icon"]).replace('{d["screen"]}', d["screen"])
    html = html.replace('{kpis}', kpis).replace('{nav}', nav).replace('{rows}', rows)
    html = html.replace('{d["cols"][0]}', d["cols"][0]).replace('{d["cols"][1]}', d["cols"][1])
    html = html.replace('{d["cols"][2]}', d["cols"][2]).replace('{d["cols"][3]}', d["cols"][3])
    html = html.replace('{d["side"]}', d["side"]).replace('{d["acc"]}', d["acc"])
    html = html.replace('{d["bg"]}', d["bg"]).replace('{d["ink"]}', d["ink"])
    return html

# ThemeForest-inspired niches that map to our 12 cats
SITES = [
# restaurant extras
dict(file="resto-bbq.html", cat="restaurant", category="Restaurant & Food", icon="fa-fire", name="Nyama Grill", type="Website Demo",
     tagline="Charcoal BBQ House", desc="Smoky BBQ restaurant with platters, sauce bar and weekend live grill.",
     features=["Platters","Sauce bar","Live grill","Outdoor seating"],
     bg="#1A120C", ink="#F6EDE3", muted="#C4B0A0", acc="#E85D04", acc2="#F48C06", card="#261910", line="rgba(232,93,4,.25)",
     navbg="rgba(26,18,12,.9)", herobg="radial-gradient(ellipse at 20% 20%,rgba(232,93,4,.25),transparent 50%)",
     ctabg="rgba(232,93,4,.08)", iconc="#1A120C", kind="Website",
     wa="Hi%201000%20Hills%20Group!%20I%20want%20a%20BBQ%20restaurant%20website.", cta="Get a site like this",
     place="Nyamirambo · Kigali", h1="Fire, Smoke & <em>Nyama</em>", lead="Charcoal-grilled platters, house pili-pili and cold Primus under the stars.",
     btn="Book a platter", kicker="The Grill", h2="Weekend Fire Menu",
     cards=[("fa-drumstick-bite","Beef Brochettes","Marinated overnight, charcoal finish."),("fa-pepper-hot","Sauce Bar","Six house sauces including akabanga honey."),("fa-music","Live Grill Nights","DJ + open fire every Friday.")],
     stats=[("4.8★","Guest rating"),("12","Grill stations"),("1998","Since")],
     nav=["Menu","About","Visit"], about_h="Born on the roadside grill", about="Nyama Grill grew from a single charcoal stand into Kigali’s favourite meat house.",
     list=["Family platters from 25,000 RWF","Private nyama choma courtyard","MoMo & card at the till"],
     cta_h="Hungry for fire?", cta_p="Reserve a weekend grill table."),
dict(file="resto-bakery.html", cat="restaurant", category="Restaurant & Food", icon="fa-bread-slice", name="Icyuma Bakery", type="Website Demo",
     tagline="Artisan Bakery", desc="Warm bakery site with daily breads, pastry counter and catering trays.",
     features=["Daily breads","Pastry counter","Catering","Pre-order"],
     bg="#FFF8F0", ink="#3D2A1F", muted="#8A6E5C", acc="#C2410C", acc2="#EA580C", card="#fff", line="#F3E2D4",
     navbg="#fff", herobg="linear-gradient(180deg,#FFF8F0,#FDE8D4)",
     ctabg="#FDE8D4", iconc="#fff", kind="Website",
     wa="Hi%201000%20Hills%20Group!%20I%20want%20a%20bakery%20website.", cta="Get a site like this",
     place="Kimironko Market", h1="Fresh from the <em>Oven</em>", lead="Sourdough, mandazi, croissants and wedding cakes — baked before sunrise.",
     btn="Pre-order bread", kicker="Today’s bake", h2="From the counter",
     cards=[("fa-wheat-awn","Sourdough","48-hour ferment, crackling crust."),("fa-cake-candles","Celebration cakes","Custom icing in 48 hours."),("fa-basket-shopping","Office trays","Pastry boxes for meetings.")],
     stats=[("4am","First bake"),("22","Recipes"),("0","Preservatives")],
     nav=["Bakes","Cakes","Catering"], about_h="A neighbourhood oven", about="Icyuma is a family bakery serving Kimironko since 2011.",
     list=["WhatsApp pre-orders before 7pm","Gluten-free Saturday loaves","Corporate catering"],
     cta_h="Need bread tomorrow?", cta_p="Pre-order on WhatsApp."),
dict(file="resto-fast.html", cat="restaurant", category="Restaurant & Food", icon="fa-burger", name="Kigali Bite", type="Website Demo",
     tagline="Fast Casual Burgers", desc="Bold fast-casual burger joint with combo builder and delivery zones.",
     features=["Combo builder","Delivery zones","Loyalty stamps","Dark neon"],
     bg="#0B0B0F", ink="#F4F4F5", muted="#A1A1AA", acc="#22C55E", acc2="#4ADE80", card="#18181B", line="rgba(34,197,94,.2)",
     navbg="rgba(11,11,15,.92)", herobg="radial-gradient(circle at 80% 10%,rgba(34,197,94,.2),transparent 40%)",
     ctabg="#111", iconc="#052e16", kind="Website",
     wa="Hi%201000%20Hills%20Group!%20I%20want%20a%20fast%20food%20website.", cta="Get a site like this",
     place="KN 3 Rd · Delivery citywide", h1="Smash Burgers. <em>Serious</em> fries.", lead="Build a combo, pay with MoMo, get it in 25 minutes.",
     btn="Order now", kicker="Menu", h2="Build your bite",
     cards=[("fa-burger","Smash burgers","Double smash, cheddar, pickles."),("fa-motorcycle","25-min delivery","Kigali inner ring."),("fa-stamp","Loyalty","10th burger free.")],
     stats=[("25m","Avg delivery"),("12k","Orders / mo"),("MoMo","Checkout")],
     nav=["Menu","Delivery","Loyalty"], about_h="Fast, not cheap", about="Kigali Bite is a local smash-burger kitchen with a neon storefront.",
     list=["Online combo builder","Rider tracking","Night kitchen till 1am"],
     cta_h="Craving something smashed?", cta_p="Order on WhatsApp."),
# hotel
dict(file="hotel-boutique.html", cat="hotel", category="Hotel & Tourism", icon="fa- palmtree".replace(" ",""), name="Inzira Boutique Hotel", type="Website Demo",
     tagline="Boutique City Hotel", desc="Intimate 24-room boutique hotel with spa, courtyard breakfast and rooftop.",
     features=["24 rooms","Rooftop bar","Spa","Courtyard"],
     bg="#0F1C24", ink="#E8F0F4", muted="#9BB0BC", acc="#D4A373", acc2="#E6C9A8", card="#17303C", line="rgba(212,163,115,.25)",
     navbg="rgba(15,28,36,.92)", herobg="radial-gradient(ellipse at 70% 0%,rgba(212,163,115,.2),transparent)",
     ctabg="rgba(212,163,115,.08)", iconc="#0F1C24", kind="Website",
     wa="Hi%201000%20Hills%20Group!%20I%20want%20a%20boutique%20hotel%20website.", cta="Get a site like this",
     place="Kiyovu · Kigali", h1="Sleep in the <em>quiet hills</em>", lead="Twenty-four rooms, a courtyard of jacarandas and a rooftop that watches the city.",
     btn="Check availability", kicker="Stay", h2="Rooms with a story",
     cards=[("fa-bed","Garden Suites","Private terraces."),("fa-spa","Inzira Spa","Rwandan clay rituals."),("fa-martini-glass","Rooftop","Sunset cocktails.")],
     stats=[("24","Rooms"),("4.9★","Guests"),("Spa","On site")],
     nav=["Rooms","Spa","Dine"], about_h="Small on purpose", about="Inzira is a converted colonial house — never more than 24 keys.",
     list=["Airport transfers","Workspace loft","Pet-friendly garden rooms"],
     cta_h="Plan a quiet stay", cta_p="Request dates on WhatsApp."),
]
# fix palmtree - fa-tree
SITES[3]["icon"] = "fa-tree"

SITES += [
dict(file="hotel-guesthouse.html", cat="hotel", category="Hotel & Tourism", icon="fa-house-chimney", name="Mama’s Guesthouse", type="Website Demo",
     tagline="Family Guesthouse", desc="Warm homestay guesthouse with shared kitchen, city tours and long-stay rates.",
     features=["Homestay","Long-stay rates","Tours","Shared kitchen"],
     bg="#FAF7F2", ink="#2C241B", muted="#7A6A58", acc="#B45309", acc2="#D97706", card="#fff", line="#EDE4D6",
     navbg="#fff", herobg="#FAF7F2", ctabg="#F3E8D8", iconc="#fff", kind="Website",
     wa="Hi%201000%20Hills%20Group!%20I%20want%20a%20guesthouse%20website.", cta="Get a site like this",
     place="Remera · Kigali", h1="Come stay with <em>family</em>", lead="Eight rooms, home cooking and a host who knows every bus route.",
     btn="Ask for a room", kicker="Stay", h2="Simple, kind, local",
     cards=[("fa-mug-hot","Breakfast included","Mandazi & tea."),("fa-map","City walks","Host-led tours."),("fa-wifi","Fast Wi-Fi","Remote-work desk.")],
     stats=[("8","Rooms"),("From 25k","RWF / night"),("4.9","Rating")],
     nav=["Rooms","Tours","Rates"], about_h="A house, not a hotel", about="Mama’s has hosted backpackers and consultants since 2009.",
     list=["Weekly rates","Airport pickup","Kitchen access"],
     cta_h="Need a bed this week?", cta_p="Message Mama on WhatsApp."),
dict(file="realestate-rentals.html", cat="realestate", category="Real Estate", icon="fa-key", name="Kigali Lets", type="Website Demo",
     tagline="Rental Marketplace", desc="Apartment rental marketplace with filters, landlord portal and viewing scheduler.",
     features=["Rentals","Filters","Viewings","Landlord portal"],
     bg="#F4F7FB", ink="#0F172A", muted="#64748B", acc="#2563EB", acc2="#60A5FA", card="#fff", line="#E2E8F0",
     navbg="#fff", herobg="linear-gradient(180deg,#EFF6FF,#F4F7FB)", ctabg="#EFF6FF", iconc="#fff", kind="Website",
     wa="Hi%201000%20Hills%20Group!%20I%20want%20a%20rentals%20website.", cta="Get a site like this",
     place="All Kigali districts", h1="Find a place to <em>live</em>", lead="Verified apartments, transparent deposits, WhatsApp viewings.",
     btn="Browse listings", kicker="Listings", h2="This week’s lets",
     cards=[("fa-building","Apartments","Studio to 3-bed."),("fa-shield","Verified landlords","ID-checked."),("fa-calendar","Viewings","Book a slot.")],
     stats=[("420","Live lets"),("48h","Avg match"),("0","Hidden fees")],
     nav=["Search","Landlords","Help"], about_h="Rent without the runaround", about="Kigali Lets lists only inspected units with clear photos.",
     list=["Deposit calculator","MoMo rent collection","Move-in checklist"],
     cta_h="List or let today", cta_p="Talk to an agent on WhatsApp."),
dict(file="realestate-agency.html", cat="realestate", category="Real Estate", icon="fa-handshake", name="Hillside Agency", type="Website Demo",
     tagline="Sales Agency", desc="Traditional real estate agency with sold properties, agents and valuation form.",
     features=["Valuations","Agents","Sold stamp","Lead form"],
     bg="#111827", ink="#F9FAFB", muted="#9CA3AF", acc="#F59E0B", acc2="#FBBF24", card="#1F2937", line="rgba(245,158,11,.2)",
     navbg="rgba(17,24,39,.95)", herobg="#111827", ctabg="#1F2937", iconc="#111827", kind="Website",
     wa="Hi%201000%20Hills%20Group!%20I%20want%20a%20real%20estate%20agency%20website.", cta="Get a site like this",
     place="Nyarutarama", h1="Buy, sell, <em>advise</em>", lead="Independent agency for homes, plots and commercial units.",
     btn="Free valuation", kicker="Agency", h2="Recently sold",
     cards=[("fa-house","Homes","Villas & townhouses."),("fa-map","Plots","Titled land."),("fa-store","Commercial","Retail & offices.")],
     stats=[("180","Sold 2025"),("12","Agents"),("BNR","Compliant")],
     nav=["Buy","Sell","Agents"], about_h="Advice first", about="Hillside is a boutique agency — no pressure, just numbers.",
     list=["Same-week valuations","Title due diligence","Off-plan desks"],
     cta_h="What’s your property worth?", cta_p="Request a valuation."),
dict(file="shop-grocery.html", cat="ecommerce", category="E-Commerce", icon="fa-carrot", name="Isoko Fresh", type="Website Demo",
     tagline="Online Grocery", desc="Grocery delivery shop with produce aisles, same-day slots and MoMo pay.",
     features=["Same-day slots","Produce aisles","MoMo","Min basket"],
     bg="#F0FDF4", ink="#14532D", muted="#4D7C0F", acc="#16A34A", acc2="#4ADE80", card="#fff", line="#DCFCE7",
     navbg="#fff", herobg="#ECFCCB", ctabg="#D9F99D", iconc="#fff", kind="Website",
     wa="Hi%201000%20Hills%20Group!%20I%20want%20a%20grocery%20ecommerce%20site.", cta="Get a site like this",
     place="Same-day · Kigali", h1="Market stall, <em>to your door</em>", lead="Fruits, veg, dairy and household — packed this morning.",
     btn="Shop aisles", kicker="Aisles", h2="Fresh this morning",
     cards=[("fa-apple-whole","Produce","From Nyabugogo market."),("fa-truck","Same-day","Slots till 6pm."),("fa-mobile","MoMo pay","At checkout.")],
     stats=[("2h","Pack time"),("150+","SKUs"),("Free","Over 15k")],
     nav=["Shop","Slots","Help"], about_h="A digital isoko", about="Isoko Fresh partners with traders at Nyabugogo.",
     list=["Cold-chain dairy","Substitution preferences","Rider SMS"],
     cta_h="Need groceries tonight?", cta_p="Place an order."),
dict(file="shop-pharmacy.html", cat="ecommerce", category="E-Commerce", icon="fa-pills", name="Ubuzima Pharmacy Shop", type="Website Demo",
     tagline="Online Pharmacy", desc="Regulated pharmacy e-commerce with Rx upload, OTC aisles and pharmacist chat.",
     features=["Rx upload","OTC aisles","Pharmacist chat","Delivery"],
     bg="#F8FAFC", ink="#0F172A", muted="#64748B", acc="#0EA5E9", acc2="#38BDF8", card="#fff", line="#E2E8F0",
     navbg="#fff", herobg="#E0F2FE", ctabg="#E0F2FE", iconc="#fff", kind="Website",
     wa="Hi%201000%20Hills%20Group!%20I%20want%20an%20online%20pharmacy.", cta="Get a site like this",
     place="Licensed · Rwanda FDA", h1="Medicine, <em>delivered safely</em>", lead="Upload a prescription, chat a pharmacist, pay with MoMo.",
     btn="Upload Rx", kicker="Care", h2="How it works",
     cards=[("fa-file-medical","Upload Rx","Photo or PDF."),("fa-user-nurse","Pharmacist","Verified before pack."),("fa-box","Discreet delivery","Same day Kigali.")],
     stats=[("FDA","Licensed"),("24/7","Chat"),("Cold","Chain")],
     nav=["OTC","Rx","Advice"], about_h="A real pharmacy online", about="Ubuzima is a brick-and-click pharmacy, not a marketplace.",
     list=["Controlled-drug protocol","Insurance receipts","Refill reminders"],
     cta_h="Need a refill?", cta_p="Talk to a pharmacist."),
dict(file="edu-creche.html", cat="education", category="Education", icon="fa-child", name="Little Hills Crèche", type="Website Demo",
     tagline="Early Years School", desc="Playful nursery website with programmes, fees, tours and parent portal teaser.",
     features=["Programmes","Fees","Tours","Parent notes"],
     bg="#FFF7ED", ink="#7C2D12", muted="#9A3412", acc="#F97316", acc2="#FDBA74", card="#fff", line="#FFEDD5",
     navbg="#fff", herobg="#FFEDD5", ctabg="#FED7AA", iconc="#7C2D12", kind="Website",
     wa="Hi%201000%20Hills%20Group!%20I%20want%20a%20nursery%20website.", cta="Get a site like this",
     place="Gacuriro", h1="Tiny feet, <em>big hills</em>", lead="A bilingual crèche with gardens, music and a calm daily rhythm.",
     btn="Book a tour", kicker="Ages 1–5", h2="Little programmes",
     cards=[("fa-shapes","Play rooms","Sensorial corners."),("fa-language","Kinyarwanda + English","Everyday bilingual."),("fa-leaf","Garden days","Outdoor learning.")],
     stats=[("1–5","Years"),("8:1","Ratio"),("Organic","Snacks")],
     nav=["Programmes","Fees","Visit"], about_h="A second home", about="Little Hills is licensed and inspected annually.",
     list=["Secure pickup PINs","Daily photo notes","Holiday clubs"],
     cta_h="Come see the garden", cta_p="Book a parent tour."),
dict(file="edu-training.html", cat="education", category="Education", icon="fa-chalkboard-user", name="SkillForge Institute", type="Website Demo",
     tagline="Vocational Training", desc="TVET / short-course institute with cohorts, certificates and employer partners.",
     features=["Cohorts","Certificates","Employers","Apply form"],
     bg="#0B1220", ink="#E5E7EB", muted="#9CA3AF", acc="#22D3EE", acc2="#67E8F9", card="#111827", line="rgba(34,211,238,.2)",
     navbg="rgba(11,18,32,.95)", herobg="#0B1220", ctabg="#111827", iconc="#0B1220", kind="Website",
     wa="Hi%201000%20Hills%20Group!%20I%20want%20a%20training%20institute%20website.", cta="Get a site like this",
     place="Kicukiro · TVET", h1="Skills that <em>get hired</em>", lead="12-week cohorts in digital, electrical and hospitality.",
     btn="Apply for a cohort", kicker="Courses", h2="Next intakes",
     cards=[("fa-laptop-code","Digital","Web & Excel."),("fa-bolt","Electrical","City & Guilds path."),("fa-concierge-bell","Hospitality","Hotel-ready.")],
     stats=[("92%","Placement"),("12w","Cohorts"),("MoMo","Fees")],
     nav=["Courses","Apply","Employers"], about_h="Train for the job", about="SkillForge partners with hotels and IT firms for internships.",
     list=["Evening classes","Installment fees","Graduate showcase"],
     cta_h="Join the next cohort", cta_p="Apply on WhatsApp."),
dict(file="ngo-youth.html", cat="ngo", category="NGO & Church", icon="fa-people-group", name="Urumuri Youth", type="Website Demo",
     tagline="Youth NGO", desc="Youth empowerment NGO with programmes, volunteer form and impact map.",
     features=["Programmes","Volunteers","Impact map","Donate"],
     bg="#052E16", ink="#ECFDF5", muted="#86EFAC", acc="#A3E635", acc2="#BEF264", card="#14532D", line="rgba(163,230,53,.25)",
     navbg="rgba(5,46,22,.95)", herobg="#052E16", ctabg="#14532D", iconc="#052E16", kind="Website",
     wa="Hi%201000%20Hills%20Group!%20I%20want%20a%20youth%20NGO%20website.", cta="Get a site like this",
     place="Huye · Rwanda", h1="Light for the <em>next generation</em>", lead="Mentorship, football academies and coding clubs in Southern Province.",
     btn="Volunteer", kicker="Impact", h2="What we run",
     cards=[("fa-futbol","Academies","Fair-play football."),("fa-code","Code clubs","Saturday labs."),("fa-hands-holding-child","Mentors","University volunteers.")],
     stats=[("1,200","Youth / yr"),("14","Clubs"),("RGB","Registered")],
     nav=["Work","Volunteer","Give"], about_h="Youth leading youth", about="Urumuri is youth-founded and RGB registered.",
     list=["Transparent reports","In-kind donations","School partnerships"],
     cta_h="Give time or funds", cta_p="We reply the same day."),
dict(file="church-youth.html", cat="ngo", category="NGO & Church", icon="fa-cross", name="New Dawn Chapel", type="Website Demo",
     tagline="Contemporary Church", desc="Modern church site with livestream, events calendar and giving.",
     features=["Livestream","Events","Giving","Connect card"],
     bg="#1C1917", ink="#FAFAF9", muted="#A8A29A", acc="#FBBF24", acc2="#FDE68A", card="#292524", line="rgba(251,191,36,.2)",
     navbg="rgba(28,25,23,.95)", herobg="#1C1917", ctabg="#292524", iconc="#1C1917", kind="Website",
     wa="Hi%201000%20Hills%20Group!%20I%20want%20a%20church%20website.", cta="Get a site like this",
     place="Gisozi", h1="A home for <em>hope</em>", lead="Sunday gatherings, midweek groups and a generous city church.",
     btn="Plan your visit", kicker="This week", h2="Gather with us",
     cards=[("fa-video","Livestream","9:30 & 11:30."),("fa-calendar","Events","Youth Friday."),("fa-hand-holding-heart","Give","MoMo & card.")],
     stats=[("2","Services"),("Kids","Church"),("EN/KIN","Languages")],
     nav=["Visit","Watch","Give"], about_h="Church for the city", about="New Dawn is a contemporary congregation in Gisozi.",
     list=["Connect card","Prayer request","Serve teams"],
     cta_h="Visit this Sunday", cta_p="We’ll save you a seat."),
dict(file="health-lab.html", cat="health", category="Health", icon="fa-flask", name="HillLab Diagnostics", type="Website Demo",
     tagline="Medical Lab", desc="Diagnostics lab with test catalogue, home collection and result portal.",
     features=["Test catalogue","Home collection","Results portal","MoMo"],
     bg="#F8FAFC", ink="#0F172A", muted="#64748B", acc="#7C3AED", acc2="#A78BFA", card="#fff", line="#EDE9FE",
     navbg="#fff", herobg="#EDE9FE", ctabg="#EDE9FE", iconc="#fff", kind="Website",
     wa="Hi%201000%20Hills%20Group!%20I%20want%20a%20lab%20website.", cta="Get a site like this",
     place="Accredited lab · Kigali", h1="Results you can <em>trust</em>", lead="Walk-in tests, home phlebotomy and a secure results login.",
     btn="Book a test", kicker="Diagnostics", h2="Popular panels",
     cards=[("fa-droplet","Blood panels","Same-day CBC."),("fa-house-medical","Home collection","Nurse visit."),("fa-lock","Portal","Encrypted PDFs.")],
     stats=[("ISO","15189"),("4h","Many results"),("MoMo","Pay")],
     nav=["Tests","Collect","Portal"], about_h="A serious lab", about="HillLab is independently accredited.",
     list=["Corporate wellness contracts","Doctor referral network","WhatsApp results opt-in"],
     cta_h="Need a test today?", cta_p="Book collection."),
dict(file="health-optician.html", cat="health", category="Health", icon="fa-glasses", name="ClearView Optical", type="Website Demo",
     tagline="Optician & Eyewear", desc="Optician store with eye-test booking, frames catalogue and insurance partners.",
     features=["Eye tests","Frames","Insurance","Booking"],
     bg="#F1F5F9", ink="#0F172A", muted="#475569", acc="#0F766E", acc2="#14B8A6", card="#fff", line="#CCFBF1",
     navbg="#fff", herobg="#CCFBF1", ctabg="#99F6E4", iconc="#fff", kind="Website",
     wa="Hi%201000%20Hills%20Group!%20I%20want%20an%20optician%20website.", cta="Get a site like this",
     place="Kigali Heights", h1="See the hills <em>clearly</em>", lead="Eye exams, designer frames and same-week lenses.",
     btn="Book an eye test", kicker="Vision", h2="Frames & care",
     cards=[("fa-eye","Exams","30-minute tests."),("fa-glasses","Frames","120+ styles."),("fa-file-invoice","Insurance","RSSB & RAMA.")],
     stats=[("24h","Many lenses"),("Kids","Clinic"),("4.9★","Reviews")],
     nav=["Book","Frames","Insurance"], about_h="Optometry with style", about="ClearView is an independent optical house.",
     list=["Contact lens clinic","Workplace vision plans","Repairs while you wait"],
     cta_h="Time for a check-up?", cta_p="Book on WhatsApp."),
dict(file="corp-logistics.html", cat="corporate", category="Corporate", icon="fa-truck", name="Ingabo Logistics", type="Website Demo",
     tagline="Freight & Logistics", desc="Logistics company site with lane calculator, tracking teaser and fleet stats.",
     features=["Tracking","Fleet","Lanes","Quotes"],
     bg="#0B1220", ink="#E2E8F0", muted="#94A3B8", acc="#F97316", acc2="#FB923C", card="#111827", line="rgba(249,115,22,.25)",
     navbg="rgba(11,18,32,.95)", herobg="#0B1220", ctabg="#111827", iconc="#0B1220", kind="Website",
     wa="Hi%201000%20Hills%20Group!%20I%20want%20a%20logistics%20website.", cta="Get a site like this",
     place="Dry port · Kigali", h1="Freight that <em>moves</em>", lead="Road, air and last-mile across East Africa.",
     btn="Get a quote", kicker="Network", h2="Lanes we run",
     cards=[("fa-road","Road","Kigali–Mombasa."),("fa-plane","Air cargo","Same-week."),("fa-box","Last mile","City distribution.")],
     stats=[("80","Trucks"),("EAC","Coverage"),("GPS","Fleet")],
     nav=["Services","Track","Quote"], about_h="Reliable tonnage", about="Ingabo is a RURA-licensed transporter.",
     list=["POD photos","Bonded warehouse","Customs desk"],
     cta_h="Need a lane quote?", cta_p="Share origin & destination."),
dict(file="corp-accounting.html", cat="corporate", category="Corporate", icon="fa-calculator", name="Imena Advisory", type="Website Demo",
     tagline="Accounting Firm", desc="Clean accounting firm site with services, tax calendar and client onboarding.",
     features=["Tax calendar","Services","Onboarding","RRA"],
     bg="#F8FAFC", ink="#0F172A", muted="#64748B", acc="#1D4ED8", acc2="#60A5FA", card="#fff", line="#DBEAFE",
     navbg="#fff", herobg="#EFF6FF", ctabg="#DBEAFE", iconc="#fff", kind="Website",
     wa="Hi%201000%20Hills%20Group!%20I%20want%20an%20accounting%20firm%20website.", cta="Get a site like this",
     place="CPAs · Kigali", h1="Books you can <em>defend</em>", lead="Accounting, RRA filings and CFO-on-call for SMEs.",
     btn="Book a consult", kicker="Practice", h2="How we help",
     cards=[("fa-file-invoice-dollar","Tax","VAT & CIT."),("fa-book","Bookkeeping","Monthly close."),("fa-chart-pie","CFO","Board packs.")],
     stats=[("RRA","E-tax"),("IFRS","SME"),("NDA","Standard")],
     nav=["Services","Industries","Contact"], about_h="Quiet competence", about="Imena is a licensed CPA practice.",
     list=["Xero & QuickBooks","Payroll PAYE","Audit support"],
     cta_h="Close the books properly", cta_p="Talk to a partner."),
dict(file="events-conference.html", cat="events", category="Events & Media", icon="fa-microphone", name="Kigali Summit Co", type="Website Demo",
     tagline="Conference Producer", desc="Conference production site with agenda, speakers and ticket tiers.",
     features=["Agenda","Speakers","Tickets","Sponsors"],
     bg="#0A0A0A", ink="#FAFAFA", muted="#A1A1AA", acc="#E11D48", acc2="#FB7185", card="#18181B", line="rgba(225,29,72,.25)",
     navbg="rgba(10,10,10,.95)", herobg="#0A0A0A", ctabg="#18181B", iconc="#fff", kind="Website",
     wa="Hi%201000%20Hills%20Group!%20I%20want%20an%20events%20website.", cta="Get a site like this",
     place="KCC · Annual", h1="Stages that <em>matter</em>", lead="We produce summits, expos and government forums.",
     btn="See the agenda", kicker="Production", h2="What we produce",
     cards=[("fa-users","Summits","1,000+ delegates."),("fa-tv","Broadcast","Livestream kits."),("fa-handshake","Sponsors","Tiered packages.")],
     stats=[("40","Events / yr"),("Hybrid","Ready"),("EN/FR","Host")],
     nav=["Work","Agenda","Tickets"], about_h="Production, not just AV", about="Summit Co handles content, staging and ticketing.",
     list=["Badge printing","Speaker lounge","Sponsor village"],
     cta_h="Planning a forum?", cta_p="Brief us on WhatsApp."),
dict(file="events-podcast.html", cat="events", category="Events & Media", icon="fa-podcast", name="Hillscast Studio", type="Website Demo",
     tagline="Podcast Studio", desc="Media studio site with show reels, booking calendar and rate card.",
     features=["Studios","Rate card","Show reel","Booking"],
     bg="#111827", ink="#F9FAFB", muted="#9CA3AF", acc="#A855F7", acc2="#C084FC", card="#1F2937", line="rgba(168,85,247,.25)",
     navbg="rgba(17,24,39,.95)", herobg="#111827", ctabg="#1F2937", iconc="#fff", kind="Website",
     wa="Hi%201000%20Hills%20Group!%20I%20want%20a%20podcast%20studio%20website.", cta="Get a site like this",
     place="Kimihurura studio", h1="Record something <em>worth hearing</em>", lead="Two treated rooms, video podcasts and in-house editors.",
     btn="Book a slot", kicker="Studio", h2="Rooms & rates",
     cards=[("fa-microphone-lines","Audio A","Vocal booth."),("fa-video","Video B","3-cam setup."),("fa-scissors","Edit","48h turnaround.")],
     stats=[("2","Rooms"),("4K","Video"),("MoMo","Pay")],
     nav=["Rooms","Rates","Book"], about_h="A quiet room in a loud city", about="Hillscast is an independent podcast house.",
     list=["Guest green room","Live audience nights","Distribution help"],
     cta_h="Need a room this week?", cta_p="Check the calendar."),
dict(file="fit-yoga.html", cat="fitness", category="Beauty & Fitness", icon="fa-spa", name="Amahoro Yoga", type="Website Demo",
     tagline="Yoga Studio", desc="Calm yoga studio with class timetable, intro offer and teacher bios.",
     features=["Timetable","Intro week","Teachers","Retreats"],
     bg="#FDFCFB", ink="#3F3A36", muted="#7C746C", acc="#0D9488", acc2="#5EEAD4", card="#fff", line="#CCFBF1",
     navbg="#fff", herobg="#F0FDFA", ctabg="#CCFBF1", iconc="#fff", kind="Website",
     wa="Hi%201000%20Hills%20Group!%20I%20want%20a%20yoga%20studio%20website.", cta="Get a site like this",
     place="Kiyovu loft", h1="Breathe with the <em>hills</em>", lead="Vinyasa, yin and breathwork in a sunlit loft.",
     btn="Try intro week", kicker="Practice", h2="This week’s classes",
     cards=[("fa-sun","Morning flow","6:45am."),("fa-moon","Yin evenings","Restore."),("fa-mountain","Retreats","Lake Kivu.")],
     stats=[("12","Classes / wk"),("Mats","Provided"),("All","Levels")],
     nav=["Timetable","Teachers","Retreats"], about_h="A small, serious studio", about="Amahoro is teacher-owned.",
     list=["Intro week 15,000 RWF","Private sessions","Corporate offsites"],
     cta_h="Come to the loft", cta_p="Book intro week."),
dict(file="fit-salon.html", cat="fitness", category="Beauty & Fitness", icon="fa-scissors", name="Crown & Coil Salon", type="Website Demo",
     tagline="Hair Salon", desc="Editorial hair salon with services menu, stylists and booking CTA.",
     features=["Service menu","Stylists","Lookbook","Booking"],
     bg="#1C1014", ink="#FDF2F8", muted="#F9A8D4", acc="#F472B6", acc2="#FBCFE8", card="#2A1620", line="rgba(244,114,182,.25)",
     navbg="rgba(28,16,20,.95)", herobg="#1C1014", ctabg="#2A1620", iconc="#1C1014", kind="Website",
     wa="Hi%201000%20Hills%20Group!%20I%20want%20a%20salon%20website.", cta="Get a site like this",
     place="Nyarutarama", h1="Hair that <em>holds court</em>", lead="Cuts, colour, braids and bridal — appointment only.",
     btn="Book a chair", kicker="Salon", h2="The menu",
     cards=[("fa-scissors","Cut & colour","Consultation first."),("fa-crown","Braids","Protective styles."),("fa-ring","Bridal","Trials included.")],
     stats=[("6","Stylists"),("Lookbook","IG"),("MoMo","Pay")],
     nav=["Menu","Stylists","Book"], about_h="A chair with a point of view", about="Crown & Coil is an editorial salon.",
     list=["Patch tests","Kids cuts Saturday","Gift cards"],
     cta_h="Ready for a new look?", cta_p="WhatsApp the front desk."),
dict(file="agri-coop.html", cat="agriculture", category="Agriculture", icon="fa-users", name="Ibirayi Co-op", type="Website Demo",
     tagline="Farmer Cooperative", desc="Cooperative site with produce calendar, member benefits and buyer desk.",
     features=["Produce calendar","Members","Buyer desk","Traceability"],
     bg="#14532D", ink="#ECFDF5", muted="#86EFAC", acc="#FACC15", acc2="#FDE047", card="#166534", line="rgba(250,204,21,.25)",
     navbg="rgba(20,83,45,.95)", herobg="#14532D", ctabg="#166534", iconc="#14532D", kind="Website",
     wa="Hi%201000%20Hills%20Group!%20I%20want%20a%20cooperative%20website.", cta="Get a site like this",
     place="Musanze · Potatoes", h1="Grown by <em>members</em>", lead="A potato and vegetable co-op with a buyer desk in Kigali.",
     btn="Buyer enquiry", kicker="Harvest", h2="What’s in season",
     cards=[("fa-carrot","Vegetables","Weekly crates."),("fa-truck","Aggregation","Cold store."),("fa-certificate","Traceability","Lot codes.")],
     stats=[("420","Members"),("GlobalGAP","Path"),("RAB","Partner")],
     nav=["Produce","Members","Buyers"], about_h="Owned by growers", about="Ibirayi is a registered cooperative.",
     list=["Member dividends","Input credit","Training days"],
     cta_h="Need volume this month?", cta_p="Talk to the buyer desk."),
dict(file="agri-dairy.html", cat="agriculture", category="Agriculture", icon="fa-cow", name="Inka Dairy", type="Website Demo",
     tagline="Dairy Brand", desc="Dairy brand site with products, farm story and stockists map.",
     features=["Products","Farm story","Stockists","Freshness"],
     bg="#FFFBEB", ink="#422006", muted="#92400E", acc="#D97706", acc2="#FBBF24", card="#fff", line="#FDE68A",
     navbg="#fff", herobg="#FEF3C7", ctabg="#FDE68A", iconc="#fff", kind="Website",
     wa="Hi%201000%20Hills%20Group!%20I%20want%20a%20dairy%20brand%20website.", cta="Get a site like this",
     place="Gicumbi hills", h1="Milk from the <em>high pastures</em>", lead="Pasteurised milk, yoghurt and cheese from Inka herds.",
     btn="Find stockists", kicker="Dairy", h2="From the creamery",
     cards=[("fa-bottle-water","Fresh milk","Daily runs."),("fa-ice-cream","Yoghurt","Plain & fruit."),("fa-cheese","Cheese","Aged wheels.")],
     stats=[("4am","Milking"),("Cold","Chain"),("RBS","Certified")],
     nav=["Products","Farm","Stockists"], about_h="A herd with a name", about="Inka Dairy is farm-owned.",
     list=["School milk programmes","HoReCa packs","Farm visits"],
     cta_h="Stock Inka?", cta_p="Wholesale enquiries welcome."),
]

SYSTEMS = [
dict(file="system-crm.html", cat="system", category="Management System", icon="fa-address-book", name="LeadFlow CRM", type="System Demo",
     tagline="Sales CRM for SMEs", desc="Pipeline CRM — leads, deals, follow-ups and WhatsApp logging.",
     features=["Pipeline","Deals","WhatsApp log","Reports"],
     side="#0F172A", acc="#38BDF8", bg="#F1F5F9", ink="#0F172A",
     wa="Hi%201000%20Hills%20Group!%20I%20want%20the%20LeadFlow%20CRM.",
     screen="Sales pipeline",
     sidenav=[("fa-chart-line","Dashboard"),("fa-filter","Pipeline"),("fa-users","Contacts"),("fa-file-invoice","Deals"),("fa-gear","Settings")],
     kpis=[("Open deals","24"),("Won this month","8.2M"),("Follow-ups due","11"),("Win rate","31%")],
     cols=["Deal","Company","Value","Stage"],
     rows=[("Website redesign","Lemigo Hotel","2.4M","Proposal"),("POS rollout","Isoko Fresh","1.1M","Negotiation"),("SEO retainer","Grazia","720k","Qualified")]),
dict(file="system-inventory.html", cat="system", category="Management System", icon="fa-boxes-stacked", name="StockWise WMS", type="System Demo",
     tagline="Warehouse inventory", desc="Warehouse system — SKUs, bins, stocktakes and supplier POs.",
     features=["Bins","Stocktakes","POs","Reorder"],
     side="#1E293B", acc="#F59E0B", bg="#FFF7ED", ink="#1C1917",
     wa="Hi%201000%20Hills%20Group!%20I%20want%20StockWise%20WMS.",
     screen="Warehouse overview",
     sidenav=[("fa-warehouse","Overview"),("fa-barcode","SKUs"),("fa-dolly","POs"),("fa-clipboard-check","Stocktake"),("fa-gear","Settings")],
     kpis=[("SKUs","1,842"),("Low stock","37"),("Open POs","6"),("Accuracy","99.1%")],
     cols=["SKU","Bin","On hand","Status"],
     rows=[("OIL-1L","A-12","42","OK"),("SOAP-3","B-04","9","Reorder"),("RICE-25","C-01","120","OK")]),
dict(file="system-booking.html", cat="system", category="Management System", icon="fa-calendar-check", name="SlotBook Appointments", type="System Demo",
     tagline="Appointment booking", desc="Booking system for clinics, salons and consultants — calendars and reminders.",
     features=["Calendar","Reminders","Staff","No-show"],
     side="#134E4A", acc="#2DD4BF", bg="#F0FDFA", ink="#134E4A",
     wa="Hi%201000%20Hills%20Group!%20I%20want%20SlotBook.",
     screen="Today’s appointments",
     sidenav=[("fa-calendar-day","Today"),("fa-user-clock","Staff"),("fa-bell","Reminders"),("fa-chart-simple","Reports"),("fa-gear","Settings")],
     kpis=[("Today","18"),("No-shows","1"),("Waitlist","5"),("Utilisation","86%")],
     cols=["Time","Client","Service","Staff"],
     rows=[("09:00","Aline U.","Consultation","Dr. Ineza"),("10:30","Jean P.","Follow-up","Nurse Keza"),("14:00","Nadia M.","New patient","Dr. Ineza")]),
dict(file="system-helpdesk.html", cat="system", category="Management System", icon="fa-headset", name="Ticketa Helpdesk", type="System Demo",
     tagline="Support ticketing", desc="Helpdesk — tickets, SLAs, canned replies and CSAT.",
     features=["Tickets","SLA","Canned replies","CSAT"],
     side="#1E1B4B", acc="#818CF8", bg="#EEF2FF", ink="#1E1B4B",
     wa="Hi%201000%20Hills%20Group!%20I%20want%20Ticketa%20Helpdesk.",
     screen="Open tickets",
     sidenav=[("fa-inbox","Inbox"),("fa-stopwatch","SLA"),("fa-book","KB"),("fa-face-smile","CSAT"),("fa-gear","Settings")],
     kpis=[("Open","42"),("Breaching SLA","3"),("CSAT","4.7"),("First reply","12m")],
     cols=["ID","Subject","Priority","SLA"],
     rows=[("#1041","MoMo receipt missing","High","2h left"),("#1038","Password reset","Low","OK"),("#1033","App crash Android","High","45m left")]),
dict(file="system-lms.html", cat="system", category="Management System", icon="fa-chalkboard", name="ClassCloud LMS", type="System Demo",
     tagline="Learning management", desc="LMS — courses, quizzes, attendance and certificates.",
     features=["Courses","Quizzes","Certificates","Attendance"],
     side="#312E81", acc="#A78BFA", bg="#F5F3FF", ink="#312E81",
     wa="Hi%201000%20Hills%20Group!%20I%20want%20ClassCloud%20LMS.",
     screen="Course manager",
     sidenav=[("fa-book","Courses"),("fa-user-graduate","Learners"),("fa-clipboard-question","Quizzes"),("fa-certificate","Certs"),("fa-gear","Settings")],
     kpis=[("Active courses","14"),("Learners","860"),("Completion","71%"),("Certs issued","214")],
     cols=["Course","Cohort","Progress","Status"],
     rows=[("Digital Marketing 101","Jan","82%","Live"),("Excel for Finance","Feb","54%","Live"),("Hospitality Safety","Mar","12%","Starting")]),
dict(file="system-project.html", cat="system", category="Management System", icon="fa-diagram-project", name="Hillboard Projects", type="System Demo",
     tagline="Project management", desc="Kanban / Gantt lite for agencies — tasks, time and invoices.",
     features=["Kanban","Time","Invoices","Clients"],
     side="#111827", acc="#34D399", bg="#ECFDF5", ink="#064E3B",
     wa="Hi%201000%20Hills%20Group!%20I%20want%20Hillboard%20Projects.",
     screen="Agency board",
     sidenav=[("fa-table-columns","Board"),("fa-clock","Time"),("fa-file-invoice-dollar","Invoices"),("fa-users","Clients"),("fa-gear","Settings")],
     kpis=[("Active projects","9"),("Hours this week","186"),("Unbilled","1.4M"),("On track","7")],
     cols=["Project","Client","Due","Health"],
     rows=[("MenuHub v2","Internal","12 Oct","OK"),("Lemigo booking","Lemigo","28 Sep","Watch"),("NGO donate flow","Hope RW","5 Oct","OK")]),
]

os.makedirs(ROOT, exist_ok=True)
meta = []
for d in SITES:
    path = os.path.join(ROOT, d["file"])
    with open(path, "w") as f:
        f.write(site_html(d))
    meta.append({k: d[k] for k in ["name","category","cat","type","file","icon","desc","features"]})
    meta[-1]["file"] = "demos/" + d["file"]
    meta[-1]["icon"] = "fas " + d["icon"]
for d in SYSTEMS:
    path = os.path.join(ROOT, d["file"])
    with open(path, "w") as f:
        f.write(sys_html(d))
    meta.append({k: d[k] for k in ["name","category","cat","type","file","icon","desc","features"]})
    meta[-1]["file"] = "demos/" + d["file"]
    meta[-1]["icon"] = "fas " + d["icon"]

print(json.dumps(meta, indent=2))
print("COUNT", len(meta))
