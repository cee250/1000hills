#!/usr/bin/env python3
"""Bulk extra demos — especially management systems."""
import json, os, html as htmlmod

ROOT = os.path.join(os.path.dirname(__file__), "..", "demos")

def bar(kind, wa, cta):
    return f'''<div class="demo-bar" id="demoBar">
  <div class="db-left"><i class="fas fa-bolt"></i> <a href="../demos.html">1000 Hills Group</a> — Live {kind} Demo</div>
  <div class="db-right">
    <a class="db-cta" href="https://wa.me/250788695396?text={wa}" target="_blank" rel="noopener">{cta}</a>
    <button class="db-close" onclick="document.getElementById('demoBar').classList.add('hidden');document.body.style.paddingTop='0'" aria-label="Close"><i class="fas fa-times"></i></button>
  </div>
</div>'''

def site(d):
    cards = "".join(
        f'<div class="card"><i class="fas {ic}"></i><h3>{t}</h3><p>{p}</p></div>'
        for ic, t, p in d["cards"]
    )
    nav = "".join(f'<a href="#{n.lower()}">{n}</a>' for n in d["nav"])
    stats = "".join(f'<div><strong>{s}</strong><span>{l}</span></div>' for s, l in d["stats"])
    items = "".join(f'<li><i class="fas fa-check"></i> {x}</li>' for x in d["list"])
    return f'''<!DOCTYPE html>
<html lang="en"><head>
<meta charset="UTF-8"/><meta name="viewport" content="width=device-width, initial-scale=1.0"/>
<title>{d["name"]} | {d["tagline"]} — Demo by 1000 Hills Group</title>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600;800&family=Playfair+Display:wght@700&display=swap" rel="stylesheet"/>
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.0/css/all.min.css"/>
<style>
:root{{--bg:{d["bg"]};--ink:{d["ink"]};--muted:{d["muted"]};--acc:{d["acc"]};--acc2:{d["acc2"]};--card:{d["card"]};--line:{d["line"]};}}
*{{margin:0;padding:0;box-sizing:border-box}}body{{font-family:Inter,sans-serif;background:var(--bg);color:var(--ink);line-height:1.65;padding-top:46px}}
a{{text-decoration:none;color:inherit}}ul{{list-style:none}}h1,h2{{font-family:'Playfair Display',serif}}
.demo-bar{{position:fixed;top:0;left:0;right:0;height:46px;background:#0A1628;display:flex;align-items:center;justify-content:space-between;padding:0 16px;z-index:9999}}
.demo-bar .db-left,.demo-bar .db-left a{{color:#E8D5A3;font-size:.78rem;font-weight:600;display:flex;gap:8px;align-items:center}}
.demo-bar .db-cta{{background:linear-gradient(135deg,#C9A96E,#E8D5A3);color:#0A1628;font-size:.72rem;font-weight:700;padding:5px 12px;border-radius:30px}}
.demo-bar .db-close{{background:none;border:0;color:#A8B9D0;cursor:pointer}}
header{{position:sticky;top:46px;background:{d["navbg"]};border-bottom:1px solid var(--line);z-index:40}}
.nav{{width:min(1100px,92%);margin:auto;display:flex;justify-content:space-between;align-items:center;padding:14px 0;gap:12px}}
.brand{{display:flex;gap:10px;align-items:center;font-weight:800}}
.brand .ic{{width:38px;height:38px;border-radius:10px;background:linear-gradient(135deg,var(--acc),var(--acc2));display:grid;place-items:center;color:{d["iconc"]}}}
.nav-links{{display:flex;gap:18px;color:var(--muted);font-size:.86rem;font-weight:600}}
.btn{{display:inline-flex;gap:8px;align-items:center;padding:11px 22px;border-radius:40px;font-weight:700;font-size:.84rem;background:linear-gradient(135deg,var(--acc),var(--acc2));color:{d["iconc"]}}}
.hero{{padding:80px 0 64px;background:{d["herobg"]}}}
.wrap{{width:min(1100px,92%);margin:auto}}
.pill{{display:inline-flex;gap:8px;border:1px solid var(--line);padding:6px 14px;border-radius:30px;font-size:.72rem;letter-spacing:1px;text-transform:uppercase;color:var(--acc);font-weight:800}}
.hero h1{{font-size:clamp(2rem,5vw,3.4rem);line-height:1.1;margin:14px 0;max-width:16ch}}
.hero h1 em{{color:var(--acc);font-style:normal}}
.hero p{{max-width:50ch;color:var(--muted)}}
.stats{{display:flex;gap:28px;margin-top:32px;flex-wrap:wrap}}
.stats strong{{display:block;font-size:1.5rem;color:var(--acc)}}
.stats span{{font-size:.75rem;color:var(--muted)}}
section{{padding:64px 0}}
.grid{{display:grid;grid-template-columns:repeat(auto-fit,minmax(230px,1fr));gap:16px}}
.card{{background:var(--card);border:1px solid var(--line);border-radius:16px;padding:24px}}
.card i{{color:var(--acc);font-size:1.2rem;margin-bottom:10px}}
.split{{display:grid;grid-template-columns:1fr 1fr;gap:32px}}
.split li{{margin:10px 0;display:flex;gap:8px}}
.split i{{color:var(--acc)}}
.cta{{text-align:center;background:{d["ctabg"]}}}
footer{{border-top:1px solid var(--line);padding:32px 0;color:var(--muted);font-size:.84rem}}
.frow{{display:flex;justify-content:space-between;flex-wrap:wrap;gap:8px}}
.frow a{{color:var(--acc);font-weight:700}}
@media(max-width:800px){{.nav-links{{display:none}}.split{{grid-template-columns:1fr}}}}
</style></head><body>
{bar("Website", d["wa"], "Get a site like this")}
<header><div class="nav">
<a class="brand" href="#"><span class="ic"><i class="fas {d["icon"]}"></i></span>{d["name"]}</a>
<nav class="nav-links">{nav}</nav>
<a class="btn" href="https://wa.me/250788695396" target="_blank"><i class="fab fa-whatsapp"></i> {d["btn"]}</a>
</div></header>
<section class="hero"><div class="wrap">
<span class="pill"><i class="fas fa-location-dot"></i> {d["place"]}</span>
<h1>{d["h1"]}</h1>
<p>{d["lead"]}</p>
<div class="stats">{stats}</div>
</div></section>
<section><div class="wrap">
<h2 style="margin-bottom:24px">{d["h2"]}</h2>
<div class="grid">{cards}</div>
</div></section>
<section><div class="wrap split">
<div><h2>{d["about_h"]}</h2><p style="color:var(--muted);margin-top:10px">{d["about"]}</p></div>
<ul>{items}</ul>
</div></section>
<section class="cta"><div class="wrap">
<h2>{d["cta_h"]}</h2>
<p style="color:var(--muted);margin:10px 0 20px">{d["cta_p"]}</p>
<a class="btn" href="https://wa.me/250788695396" target="_blank"><i class="fab fa-whatsapp"></i> WhatsApp</a>
</div></section>
<footer><div class="wrap frow"><p>© 2026 {d["name"]} (fictional demo)</p><p>Demo by <a href="../demos.html">1000 Hills Group</a></p></div></footer>
</body></html>'''

def system(d):
    kpis = "".join(f'<div class="kpi"><span>{l}</span><strong>{v}</strong></div>' for l, v in d["kpis"])
    rows = "".join(
        f"<tr><td>{a}</td><td>{b}</td><td>{c}</td><td class='ok'>{e}</td></tr>"
        for a, b, c, e in d["rows"]
    )
    sidenav = "".join(
        f'<a href="#" class="{"on" if i==0 else ""}"><i class="fas {ic}"></i> {t}</a>'
        for i, (ic, t) in enumerate(d["sidenav"])
    )
    return f'''<!DOCTYPE html>
<html lang="en"><head>
<meta charset="UTF-8"/><meta name="viewport" content="width=device-width, initial-scale=1.0"/>
<title>{d["name"]} | {d["tagline"]} — System Demo</title>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600;800&display=swap" rel="stylesheet"/>
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.0/css/all.min.css"/>
<style>
:root{{--side:{d["side"]};--acc:{d["acc"]};--bg:{d["bg"]};--ink:{d["ink"]};}}
*{{margin:0;padding:0;box-sizing:border-box}}body{{font-family:Inter,sans-serif;background:var(--bg);color:var(--ink);padding-top:46px;font-size:14px}}
a{{text-decoration:none;color:inherit}}
.demo-bar{{position:fixed;top:0;left:0;right:0;height:46px;background:#0A1628;display:flex;align-items:center;justify-content:space-between;padding:0 16px;z-index:9999}}
.demo-bar .db-left,.demo-bar .db-left a{{color:#E8D5A3;font-size:.78rem;display:flex;gap:8px;align-items:center;font-weight:600}}
.demo-bar .db-cta{{background:linear-gradient(135deg,#C9A96E,#E8D5A3);color:#0A1628;font-size:.72rem;font-weight:700;padding:5px 12px;border-radius:30px}}
.demo-bar .db-close{{background:none;border:0;color:#A8B9D0;cursor:pointer}}
.app{{display:flex;min-height:calc(100vh - 46px)}}
.sidebar{{width:220px;background:var(--side);color:#c9d4e4;padding:16px 12px}}
.s-logo{{display:flex;gap:10px;align-items:center;color:#fff;font-weight:800;margin-bottom:16px}}
.s-logo .ic{{width:36px;height:36px;border-radius:10px;background:var(--acc);color:#0A1628;display:grid;place-items:center}}
.sidebar a{{display:flex;gap:10px;padding:10px 12px;border-radius:8px;margin:3px 0;font-size:.84rem}}
.sidebar a.on{{background:var(--acc);color:#0A1628;font-weight:700}}
.main{{flex:1;padding:22px}}
.kpis{{display:grid;grid-template-columns:repeat(4,1fr);gap:12px;margin:16px 0}}
.kpi{{background:#fff;border-radius:12px;padding:16px;border:1px solid #e6eaf0}}
.kpi span{{font-size:.72rem;color:#6b7a90;font-weight:700}}
.kpi strong{{display:block;font-size:1.35rem;margin-top:6px}}
table{{width:100%;border-collapse:collapse;background:#fff;border-radius:12px;overflow:hidden}}
th,td{{padding:12px 14px;text-align:left;border-bottom:1px solid #eef1f5;font-size:.84rem}}
th{{background:#f6f8fb;font-size:.72rem;letter-spacing:1px;text-transform:uppercase;color:#6b7a90}}
.ok{{color:#059669;font-weight:700}}
.note{{margin-top:18px;font-size:.78rem;color:#6b7a90}}
.note a{{color:var(--acc);font-weight:700}}
@media(max-width:860px){{.sidebar{{display:none}}.kpis{{grid-template-columns:1fr 1fr}}}}
</style></head><body>
{bar("System", d["wa"], "Get this system")}
<div class="app">
<aside class="sidebar">
<div class="s-logo"><span class="ic"><i class="fas {d["icon"]}"></i></span>{d["name"]}</div>
{sidenav}
</aside>
<main class="main">
<h2>{d["screen"]}</h2>
<p style="color:#6b7a90">{d["tagline"]} · demo data for Rwanda SMEs</p>
<div class="kpis">{kpis}</div>
<table>
<thead><tr><th>{d["cols"][0]}</th><th>{d["cols"][1]}</th><th>{d["cols"][2]}</th><th>{d["cols"][3]}</th></tr></thead>
<tbody>{rows}</tbody>
</table>
<p class="note">System demo by <a href="../demos.html">1000 Hills Group</a> — we build yours custom (roles, MoMo, reports).</p>
</main></div>
</body></html>'''

# palette helper
def pal(side, acc, bg="#F8FAFC", ink="#0F172A"):
    return dict(side=side, acc=acc, bg=bg, ink=ink)

SYSTEMS = [
# extra systems — lots
dict(file="system-restaurant-pos.html", name="TablePay POS", icon="fa-utensils", tagline="Restaurant POS & tables", desc="Restaurant POS — tables, KOT kitchen tickets, splits and MoMo.", features=["Tables","KOT","Splits","MoMo"],
     screen="Floor & tickets", sidenav=[("fa-chair","Floor"),("fa-receipt","Tickets"),("fa-fire-burner","Kitchen"),("fa-chart-line","Reports"),("fa-gear","Settings")],
     kpis=[("Open tables","11"),("Today sales","842k"),("Avg ticket","18.4k"),("KOT wait","4m")],
     cols=["Table","Server","Items","Status"], rows=[("T4","Keza","3","Cooking"),("T9","Jean","7","Served"),("T12","Aline","2","Bill")],
     **pal("#3F1D0F","#F97316","#FFF7ED","#431407"),
     wa="Hi%201000%20Hills%20Group!%20I%20want%20TablePay%20restaurant%20POS."),
dict(file="system-bar.html", name="TapLine Bar POS", icon="fa-beer-mug-empty", tagline="Bar & nightclub POS", desc="Bar POS — tabs, happy-hour pricing, stock pours and VIP rooms.", features=["Tabs","Happy hour","Pours","VIP"],
     screen="Open tabs", sidenav=[("fa-martini-glass","POS"),("fa-users","Tabs"),("fa-boxes","Cellar"),("fa-music","Events"),("fa-gear","Settings")],
     kpis=[("Open tabs","19"),("Tonight","1.1M"),("Pour variance","1.8%"),("VIP rooms","3")],
     cols=["Tab","Guest","Spend","Status"], rows=[("VIP-1","Private","186k","Open"),("B12","Walk-in","24k","Settling"),("T7","Hotel guest","41k","Open")],
     **pal("#1C1917","#F59E0B","#FAFAF9","#1C1917"),
     wa="Hi%201000%20Hills%20Group!%20I%20want%20TapLine%20bar%20POS."),
dict(file="system-spa.html", name="SereniSpa Book", icon="fa-spa", tagline="Spa & salon booking", desc="Spa system — rooms, therapists, packages and gift cards.", features=["Rooms","Therapists","Packages","Gifts"],
     screen="Today’s treatments", sidenav=[("fa-calendar","Diary"),("fa-user-nurse","Therapists"),("fa-gift","Cards"),("fa-boxes","Retail"),("fa-gear","Settings")],
     kpis=[("Bookings","22"),("Utilisation","81%"),("Retail add-on","19%"),("No-shows","0")],
     cols=["Time","Guest","Ritual","Therapist"], rows=[("09:00","Nadia","Hot stone 90m","Ineza"),("11:00","Patrick","Couples","Keza + Aline"),("15:30","Claire","Facial","Ineza")],
     **pal("#4A1942","#E879F9","#FDF4FF","#4A044E"),
     wa="Hi%201000%20Hills%20Group!%20I%20want%20SereniSpa%20booking."),
dict(file="system-gym.html", name="ForgeClub Gym OS", icon="fa-dumbbell", tagline="Gym memberships & classes", desc="Gym OS — members, access, class packs and PT diaries.", features=["Access","Classes","PT","Billing"],
     screen="Check-ins today", sidenav=[("fa-id-card","Members"),("fa-calendar","Classes"),("fa-person-running","PT"),("fa-credit-card","Billing"),("fa-gear","Settings")],
     kpis=[("Active members","640"),("Check-ins","186"),("PT sessions","14"),("Overdue","9")],
     cols=["Member","Plan","Check-in","Status"], rows=[("Jean M.","Gold","06:12","OK"),("Aline K.","Class pack","07:40","OK"),("Patrick N.","PT","08:05","Session")],
     **pal("#7F1D1D","#F87171","#FEF2F2","#450A0A"),
     wa="Hi%201000%20Hills%20Group!%20I%20want%20ForgeClub%20gym%20OS."),
dict(file="system-church.html", name="ParishSoft", icon="fa-church", tagline="Church & giving admin", desc="Church admin — members, giving, groups and events.", features=["Giving","Groups","Events","Members"],
     screen="Giving this month", sidenav=[("fa-users","Members"),("fa-hand-holding-heart","Giving"),("fa-people-group","Groups"),("fa-calendar","Events"),("fa-gear","Settings")],
     kpis=[("Members","1,240"),("Giving","4.8M"),("Groups","18"),("Volunteers","96")],
     cols=["Date","Type","Amount","Method"], rows=[("12 Sep","Tithe","25,000","MoMo"),("12 Sep","Missions","10,000","Cash"),("11 Sep","Building","50,000","Bank")],
     **pal("#1E3A5F","#FBBF24","#FFFBEB","#1C1917"),
     wa="Hi%201000%20Hills%20Group!%20I%20want%20ParishSoft."),
dict(file="system-ngo.html", name="GrantTrack NGO", icon="fa-hand-holding-heart", tagline="NGO grants & M&E", desc="NGO system — grants, beneficiaries, M&E indicators and donor reports.", features=["Grants","M&E","Beneficiaries","Donors"],
     screen="Active grants", sidenav=[("fa-sack-dollar","Grants"),("fa-users","Beneficiaries"),("fa-chart-simple","M&E"),("fa-file","Reports"),("fa-gear","Settings")],
     kpis=[("Active grants","7"),("Burn rate","64%"),("Beneficiaries","3,412"),("Due reports","2")],
     cols=["Grant","Donor","Budget","Status"], rows=[("Youth code clubs","EU","48M","On track"),("School meals","WFP","22M","Watch"),("Girls STEM","USAID","15M","On track")],
     **pal("#14532D","#84CC16","#F7FEE7","#14532D"),
     wa="Hi%201000%20Hills%20Group!%20I%20want%20GrantTrack%20NGO."),
dict(file="system-realestate.html", name="PlotDesk CRM", icon="fa-city", tagline="Property listings CRM", desc="Real estate CRM — listings, viewings, offers and commissions.", features=["Listings","Viewings","Offers","Commission"],
     screen="Active listings", sidenav=[("fa-building","Listings"),("fa-calendar","Viewings"),("fa-file-signature","Offers"),("fa-percent","Commission"),("fa-gear","Settings")],
     kpis=[("Live listings","86"),("Viewings this week","41"),("Offers","9"),("Pipeline","1.2B")],
     cols=["Property","Agent","Price","Stage"], rows=[("Nyarutarama villa","Ineza","420M","Offer"),("Kicukiro 2-bed","Jean","85M","Viewing"),("Plot Gahanga","Aline","32M","New")],
     **pal("#1E3A8A","#60A5FA","#EFF6FF","#1E3A8A"),
     wa="Hi%201000%20Hills%20Group!%20I%20want%20PlotDesk%20CRM."),
dict(file="system-construction.html", name="SiteLog Build", icon="fa-helmet-safety", tagline="Construction site logs", desc="Construction PM — BOQ, snags, daily logs and materials.", features=["BOQ","Snags","Daily logs","Materials"],
     screen="Active sites", sidenav=[("fa-map","Sites"),("fa-list-check","BOQ"),("fa-triangle-exclamation","Snags"),("fa-truck","Materials"),("fa-gear","Settings")],
     kpis=[("Open sites","5"),("Snags","23"),("This week spend","18M"),("Safety days","41")],
     cols=["Site","Foreman","Progress","Health"], rows=[("Kicukiro apartments","Mugisha","62%","OK"),("Huye school block","Uwase","28%","Watch"),("Kivu lodge villa","Patrick","81%","OK")],
     **pal("#78350F","#F59E0B","#FFFBEB","#78350F"),
     wa="Hi%201000%20Hills%20Group!%20I%20want%20SiteLog%20Build."),
dict(file="system-legal.html", name="CaseVault Legal", icon="fa-scale-balanced", tagline="Law firm case manager", desc="Legal practice — matters, billable hours, court dates and retainers.", features=["Matters","Hours","Court dates","Retainers"],
     screen="Open matters", sidenav=[("fa-folder-open","Matters"),("fa-clock","Time"),("fa-gavel","Hearings"),("fa-file-invoice","Bills"),("fa-gear","Settings")],
     kpis=[("Open matters","34"),("Hours this week","126"),("Unbilled","3.1M"),("Hearings","6")],
     cols=["Matter","Client","Next date","Status"], rows=[("Land dispute Gisenyi","Ndoli Ltd","18 Sep","Hearing"),("Employment","Inzozi","22 Sep","Drafting"),("Company set-up","VoltHub","—","Filing")],
     **pal("#4C0519","#FB7185","#FFF1F2","#4C0519"),
     wa="Hi%201000%20Hills%20Group!%20I%20want%20CaseVault%20Legal."),
dict(file="system-accounting.html", name="Ikirenga Books", icon="fa-book", tagline="SME accounting & VAT", desc="Accounting — invoices, expenses, VAT (RRA) and bank rec.", features=["Invoices","VAT","Bank rec","P&L"],
     screen="This month", sidenav=[("fa-file-invoice","Sales"),("fa-receipt","Purchases"),("fa-building-columns","Bank"),("fa-percent","VAT"),("fa-gear","Settings")],
     kpis=[("Invoiced","12.4M"),("Collected","9.1M"),("VAT due","1.6M"),("Unpaid","3.3M")],
     cols=["Invoice","Client","Amount","Status"], rows=[("INV-1042","Lemigo","2.4M","Paid"),("INV-1043","Hope RW","720k","Due"),("INV-1044","Grazia","1.1M","Overdue")],
     **pal("#1E3A8A","#3B82F6","#EFF6FF","#1E3A8A"),
     wa="Hi%201000%20Hills%20Group!%20I%20want%20Ikirenga%20Books."),
dict(file="system-invoicing.html", name="QuoteBill", icon="fa-file-invoice-dollar", tagline="Quotes & invoicing", desc="Lightweight quoting — proposals, e-sign, invoices and reminders.", features=["Quotes","E-sign","Invoices","Reminders"],
     screen="Open quotes", sidenav=[("fa-file","Quotes"),("fa-signature","E-sign"),("fa-file-invoice","Invoices"),("fa-bell","Reminders"),("fa-gear","Settings")],
     kpis=[("Open quotes","17"),("Win rate","38%"),("Awaiting sign","5"),("Overdue inv","4")],
     cols=["Quote","Client","Value","Stage"], rows=[("Q-221","Nyungwe Lodge","4.8M","Sent"),("Q-222","Excel Academy","1.9M","Signed"),("Q-223","Ubumwe","860k","Draft")],
     **pal("#0F766E","#2DD4BF","#F0FDFA","#134E4A"),
     wa="Hi%201000%20Hills%20Group!%20I%20want%20QuoteBill."),
dict(file="system-field.html", name="FieldForce", icon="fa-clipboard-list", tagline="Field service jobs", desc="Field jobs — dispatch, GPS techs, parts and SLAs.", features=["Dispatch","GPS","Parts","SLA"],
     screen="Jobs today", sidenav=[("fa-list","Jobs"),("fa-location-dot","Map"),("fa-screwdriver-wrench","Parts"),("fa-stopwatch","SLA"),("fa-gear","Settings")],
     kpis=[("Open jobs","28"),("On site","9"),("SLA risk","3"),("First-time fix","84%")],
     cols=["Job","Client","Tech","SLA"], rows=[("GEN-12","Hotel generator","Eric","2h left"),("AC-09","Clinic HVAC","Diane","OK"),("NET-04","Office Wi-Fi","Patrick","OK")],
     **pal("#0C4A6E","#38BDF8","#F0F9FF","#0C4A6E"),
     wa="Hi%201000%20Hills%20Group!%20I%20want%20FieldForce."),
dict(file="system-maintenance.html", name="PlantCare CMMS", icon="fa-gears", tagline="Maintenance CMMS", desc="CMMS — assets, work orders, PM schedules and spare parts.", features=["Assets","WO","PM","Spares"],
     screen="Work orders", sidenav=[("fa-industry","Assets"),("fa-wrench","Work orders"),("fa-calendar-check","PM"),("fa-boxes","Spares"),("fa-gear","Settings")],
     kpis=[("Assets","412"),("Open WO","19"),("Overdue PM","4"),("MTBF","118d")],
     cols=["WO","Asset","Priority","Status"], rows=[("WO-881","Boiler 2","High","In progress"),("WO-879","Lift A","Med","Queued"),("WO-870","Generator","Low","Done")],
     **pal("#334155","#94A3B8","#F1F5F9","#0F172A"),
     wa="Hi%201000%20Hills%20Group!%20I%20want%20PlantCare%20CMMS."),
dict(file="system-energy.html", name="KiloWatch Energy", icon="fa-bolt", tagline="Energy & solar monitoring", desc="Energy OS — meters, solar yield, outages and tenant billing.", features=["Meters","Solar","Outages","Billing"],
     screen="Site yield", sidenav=[("fa-solar-panel","Solar"),("fa-gauge","Meters"),("fa-plug","Outages"),("fa-file-invoice","Billing"),("fa-gear","Settings")],
     kpis=[("Today kWh","1,842"),("Solar share","61%"),("Outages 7d","2"),("Tenants billed","48")],
     cols=["Site","kWh today","Solar %","Status"], rows=[("Kacyiru HQ","420","72%","OK"),("Warehouse","610","54%","Watch"),("Clinic","180","81%","OK")],
     **pal("#713F12","#FACC15","#FEFCE8","#713F12"),
     wa="Hi%201000%20Hills%20Group!%20I%20want%20KiloWatch."),
dict(file="system-water.html", name="Amazi Utility", icon="fa-droplet", tagline="Water utility billing", desc="Utility billing — meters, readings, bills and disconnections.", features=["Meters","Readings","Bills","Cut-off"],
     screen="Billing cycle Sep", sidenav=[("fa-gauge","Meters"),("fa-pen","Readings"),("fa-file-invoice","Bills"),("fa-ban","Cut-off"),("fa-gear","Settings")],
     kpis=[("Accounts","2,140"),("Read this cycle","91%"),("Collected","78%"),("Disputes","11")],
     cols=["Account","Zone","m³","Status"], rows=[("W-10421","Kicukiro","18","Billed"),("W-10488","Gikondo","42","Unread"),("W-10502","Kanombe","9","Paid")],
     **pal("#164E63","#22D3EE","#ECFEFF","#164E63"),
     wa="Hi%201000%20Hills%20Group!%20I%20want%20Amazi%20Utility."),
dict(file="system-isp.html", name="NetPulse ISP", icon="fa-wifi", tagline="ISP billing & RADIUS", desc="ISP — packages, RADIUS, tickets and hotspot vouchers.", features=["RADIUS","Packages","Hotspot","Tickets"],
     screen="Subscribers", sidenav=[("fa-users","Subs"),("fa-signal","RADIUS"),("fa-ticket","Hotspot"),("fa-headset","Tickets"),("fa-gear","Settings")],
     kpis=[("Active","1,086"),("Online now","742"),("ARPU","18.4k"),("Churn 30d","2.1%")],
     cols=["Customer","Plan","Status","Last seen"], rows=[("Inzozi Café","50 Mbps","Online","now"),("Mama Guest","20 Mbps","Online","2m"),("Plot 12","Fibre 100","Suspended","3d")],
     **pal("#312E81","#818CF8","#EEF2FF","#312E81"),
     wa="Hi%201000%20Hills%20Group!%20I%20want%20NetPulse%20ISP."),
dict(file="system-school-fees.html", name="FeeFlow School", icon="fa-money-bill-wave", tagline="School fees & SMS", desc="School fees — invoices, MoMo, SMS reminders and statements.", features=["Invoices","MoMo","SMS","Statements"],
     screen="Fee collection", sidenav=[("fa-file-invoice","Invoices"),("fa-mobile","MoMo"),("fa-comment-sms","SMS"),("fa-user-graduate","Students"),("fa-gear","Settings")],
     kpis=[("Expected","86M"),("Collected","61M"),("Arrears","25M"),("SMS queued","340")],
     cols=["Student","Class","Balance","Status"], rows=[("Keza U.","S3A","0","Clear"),("Jean P.","P5","45k","Partial"),("Nadia M.","S1B","120k","Arrears")],
     **pal("#1E3A8A","#60A5FA","#EFF6FF","#1E3A8A"),
     wa="Hi%201000%20Hills%20Group!%20I%20want%20FeeFlow."),
dict(file="system-exam.html", name="MarkBook Exams", icon="fa-clipboard-check", tagline="Exams & report cards", desc="Exams — mark entry, ranking, report cards and parent portal.", features=["Marks","Ranking","Reports","Parents"],
     screen="Term 2 entry", sidenav=[("fa-pen","Marks"),("fa-ranking-star","Ranks"),("fa-file","Reports"),("fa-user","Parents"),("fa-gear","Settings")],
     kpis=[("Subjects","14"),("Entered","72%"),("Mean","68.4"),("Pending reports","3 classes")],
     cols=["Class","Subject","Entered","Mean"], rows=[("S3A","Maths","40/40","71"),("S3A","English","38/40","66"),("S2B","Physics","12/42","—")],
     **pal("#4C1D95","#C4B5FD","#F5F3FF","#4C1D95"),
     wa="Hi%201000%20Hills%20Group!%20I%20want%20MarkBook."),
dict(file="system-library.html", name="LibraNest", icon="fa-book-open", tagline="Library & catalogue", desc="Library — catalogue, loans, fines and ISBN intake.", features=["Catalogue","Loans","Fines","ISBN"],
     screen="Loans today", sidenav=[("fa-book","Catalogue"),("fa-right-left","Loans"),("fa-coins","Fines"),("fa-barcode","Intake"),("fa-gear","Settings")],
     kpis=[("Titles","8,420"),("On loan","312"),("Overdue","27"),("Fines due","84k")],
     cols=["Title","Borrower","Due","Status"], rows=[("Things Fall Apart","S3A Keza","18 Sep","OK"),("Intro Physics","S5 Jean","12 Sep","Overdue"),("Kinyarwanda Reader","P4 Aline","20 Sep","OK")],
     **pal("#44403C","#D6D3D1","#FAFAF9","#1C1917"),
     wa="Hi%201000%20Hills%20Group!%20I%20want%20LibraNest."),
dict(file="system-hostel.html", name="DormKeeper", icon="fa-bed", tagline="Hostel & boarding", desc="Boarding — rooms, leave passes, meals and discipline.", features=["Rooms","Leave","Meals","Discipline"],
     screen="Boarding house", sidenav=[("fa-bed","Rooms"),("fa-door-open","Leave"),("fa-utensils","Meals"),("fa-flag","Incidents"),("fa-gear","Settings")],
     kpis=[("Boarders","186"),("Out on leave","12"),("Vacancies","4"),("Incidents 7d","2")],
     cols=["Room","Student","Status","Leave"], rows=[("B12","Mugisha","In","—"),("B12","Patrick","Leave","Sun 18:00"),("G04","Keza","In","—")],
     **pal("#3F3F46","#A1A1AA","#FAFAFA","#18181B"),
     wa="Hi%201000%20Hills%20Group!%20I%20want%20DormKeeper."),
dict(file="system-clinic-emr.html", name="PulseEMR", icon="fa-notes-medical", tagline="Clinic electronic records", desc="Clinic EMR — visits, Rx, labs and billing in one chart.", features=["Charts","Rx","Labs","Billing"],
     screen="Today’s clinic", sidenav=[("fa-user-injured","Patients"),("fa-stethoscope","Encounters"),("fa-pills","Rx"),("fa-flask","Labs"),("fa-gear","Settings")],
     kpis=[("Waiting","14"),("Seen","31"),("Labs pending","6"),("Revenue","1.2M")],
     cols=["Time","Patient","Reason","Status"], rows=[("08:40","UWASE, 34F","ANC","In consult"),("09:10","MUGISHA, 8M","Fever","Waiting"),("09:25","NDAYISABA, 51M","HTN review","Lab")],
     **pal("#0F766E","#5EEAD4","#F0FDFA","#134E4A"),
     wa="Hi%201000%20Hills%20Group!%20I%20want%20PulseEMR."),
dict(file="system-lab.html", name="LabQueue LIS", icon="fa-vials", tagline="Lab information system", desc="LIS — sample accession, analysers, QC and result release.", features=["Accession","Analysers","QC","Release"],
     screen="Sample queue", sidenav=[("fa-vial","Accession"),("fa-microscope","Analysers"),("fa-check-double","QC"),("fa-file-medical","Release"),("fa-gear","Settings")],
     kpis=[("Samples today","186"),("TAT <4h","91%"),("QC flags","2"),("Criticals","1")],
     cols=["SID","Test","TAT","Status"], rows=[("L-9041","CBC","32m","Released"),("L-9042","Malaria","18m","Critical"),("L-9048","LFT","—","Analyser")],
     **pal("#5B21B6","#C4B5FD","#F5F3FF","#4C1D95"),
     wa="Hi%201000%20Hills%20Group!%20I%20want%20LabQueue%20LIS."),
dict(file="system-bloodbank.html", name="Drops Blood Bank", icon="fa-heart-circle-plus", tagline="Blood bank inventory", desc="Blood bank — donors, units, crossmatch and expiry.", features=["Donors","Units","Crossmatch","Expiry"],
     screen="Fridge inventory", sidenav=[("fa-hand-holding-droplet","Donors"),("fa-droplet","Units"),("fa-vial-circle-check","Crossmatch"),("fa-clock","Expiry"),("fa-gear","Settings")],
     kpis=[("Units","214"),("Expiring 7d","6"),("O-neg","11"),("Drives this month","3")],
     cols=["Unit","Type","Collected","Status"], rows=[("RW-10021","O+","10 Sep","Available"),("RW-10018","A-","04 Sep","Reserved"),("RW-09991","O-","28 Aug","Expire 18 Sep")],
     **pal("#7F1D1D","#F87171","#FEF2F2","#450A0A"),
     wa="Hi%201000%20Hills%20Group!%20I%20want%20Drops%20blood%20bank."),
dict(file="system-insurance.html", name="ClaimWise", icon="fa-file-shield", tagline="Insurance claims desk", desc="Claims — FNOL, assessments, approvals and payouts.", features=["FNOL","Assess","Approve","Payout"],
     screen="Open claims", sidenav=[("fa-file","Claims"),("fa-car-burst","Motor"),("fa-house","Property"),("fa-money-check","Payouts"),("fa-gear","Settings")],
     kpis=[("Open","64"),("SLA risk","7"),("Paid MTD","42M"),("Fraud flags","2")],
     cols=["Claim","Type","Amount","Stage"], rows=[("CL-4412","Motor","3.2M","Assess"),("CL-4408","Health","180k","Approve"),("CL-4399","Fire","12M","Investigate")],
     **pal("#1E3A8A","#93C5FD","#EFF6FF","#1E3A8A"),
     wa="Hi%201000%20Hills%20Group!%20I%20want%20ClaimWise."),
dict(file="system-microfinance.html", name="Intego Loans", icon="fa-coins", tagline="Microfinance loans", desc="MFI — groups, loans, collections and PAR reports.", features=["Groups","Loans","Collections","PAR"],
     screen="Collections today", sidenav=[("fa-people-group","Groups"),("fa-file-invoice-dollar","Loans"),("fa-hand-holding-dollar","Collect"),("fa-chart-line","PAR"),("fa-gear","Settings")],
     kpis=[("Active loans","860"),("PAR 30","4.2%"),("Collected today","2.1M"),("Disbursed MTD","18M")],
     cols=["Group","Officer","Due","PAR"], rows=[("Twiyubake","Ineza","140k","OK"),("Abahizi","Jean","95k","Watch"),("Dufatanye","Aline","210k","OK")],
     **pal("#14532D","#86EFAC","#F0FDF4","#14532D"),
     wa="Hi%201000%20Hills%20Group!%20I%20want%20Intego%20Loans."),
dict(file="system-savings.html", name="Ibimina VSLA", icon="fa-piggy-bank", tagline="Village savings groups", desc="VSLA — shares, social fund, loans and meeting minutes.", features=["Shares","Social fund","Loans","Meetings"],
     screen="Group meeting", sidenav=[("fa-users","Groups"),("fa-coins","Shares"),("fa-heart","Social"),("fa-handshake","Loans"),("fa-gear","Settings")],
     kpis=[("Groups","48"),("Shares this cycle","9.4M"),("Loans out","3.1M"),("Attendance","94%")],
     cols=["Member","Shares","Loan","Status"], rows=[("Mukamana","24","120k","OK"),("Habimana","18","—","OK"),("Uwase","12","80k","Late 1w")],
     **pal("#365314","#A3E635","#F7FEE7","#365314"),
     wa="Hi%201000%20Hills%20Group!%20I%20want%20Ibimina%20VSLA."),
dict(file="system-payroll-sme.html", name="PayLite SME", icon="fa-wallet", tagline="Simple SME payroll", desc="Lightweight payroll — staff, PAYE, RSSB and payslips.", features=["PAYE","RSSB","Payslips","MoMo"],
     screen="September run", sidenav=[("fa-users","Staff"),("fa-calculator","Run"),("fa-building-columns","RSSB"),("fa-file","Payslips"),("fa-gear","Settings")],
     kpis=[("Staff","22"),("Gross","8.4M"),("PAYE","1.1M"),("RSSB","0.6M")],
     cols=["Staff","Gross","Net","Pay"], rows=[("Ineza D.","450k","362k","MoMo"),("Jean M.","320k","268k","Bank"),("Keza A.","280k","241k","MoMo")],
     **pal("#1E293B","#38BDF8","#F8FAFC","#0F172A"),
     wa="Hi%201000%20Hills%20Group!%20I%20want%20PayLite."),
dict(file="system-attendance.html", name="ClockIn Biometric", icon="fa-fingerprint", tagline="Attendance & shifts", desc="Attendance — biometric/QR, shifts, overtime and leave.", features=["Biometric","Shifts","OT","Leave"],
     screen="Live clock-ins", sidenav=[("fa-fingerprint","Live"),("fa-calendar","Shifts"),("fa-clock","Overtime"),("fa-umbrella-beach","Leave"),("fa-gear","Settings")],
     kpis=[("On site","86"),("Late","4"),("OT hours","31"),("Leave today","3")],
     cols=["Staff","In","Out","Flag"], rows=[("Mugisha","07:52","—","OK"),("Aline","08:21","—","Late"),("Patrick","07:48","—","OK")],
     **pal("#111827","#A78BFA","#F5F3FF","#111827"),
     wa="Hi%201000%20Hills%20Group!%20I%20want%20ClockIn."),
dict(file="system-recruit.html", name="HireHills ATS", icon="fa-user-plus", tagline="Recruitment ATS", desc="ATS — jobs, pipeline, scorecards and offer letters.", features=["Jobs","Pipeline","Scorecards","Offers"],
     screen="Open roles", sidenav=[("fa-briefcase","Jobs"),("fa-filter","Pipeline"),("fa-star","Score"),("fa-file-signature","Offers"),("fa-gear","Settings")],
     kpis=[("Open roles","8"),("Candidates","142"),("Interviews","11"),("Offers out","2")],
     cols=["Role","Stage","Count","Owner"], rows=[("Front-end","Onsite","4","Cipher"),("Accountant","Screen","18","Ineza"),("Driver","Offer","1","Ops")],
     **pal("#0F172A","#F472B6","#FDF2F8","#831843"),
     wa="Hi%201000%20Hills%20Group!%20I%20want%20HireHills%20ATS."),
dict(file="system-visitor.html", name="GatePass Visitors", icon="fa-id-badge", tagline="Visitor management", desc="Front desk — visitors, badges, host alerts and watchlist.", features=["Badges","Hosts","Watchlist","Logs"],
     screen="Lobby now", sidenav=[("fa-door-open","Check-in"),("fa-id-badge","Badges"),("fa-bell","Hosts"),("fa-shield","Watchlist"),("fa-gear","Settings")],
     kpis=[("On site","23"),("Expected","9"),("Overstay","1"),("Deliveries","6")],
     cols=["Visitor","Host","In","Badge"], rows=[("Eric N.","Finance","09:12","V-104"),("DHL","Reception","09:40","DEL"),("Aline K.","CEO","10:05","V-105")],
     **pal("#1F2937","#FBBF24","#FFFBEB","#1F2937"),
     wa="Hi%201000%20Hills%20Group!%20I%20want%20GatePass."),
dict(file="system-assets.html", name="TagTrack Assets", icon="fa-tags", tagline="Asset register", desc="Assets — tags, assignments, depreciation and audits.", features=["Tags","Assign","Depreciation","Audit"],
     screen="Register", sidenav=[("fa-laptop","IT"),("fa-car","Vehicles"),("fa-chair","Furniture"),("fa-clipboard-check","Audit"),("fa-gear","Settings")],
     kpis=[("Assets","1,240"),("Unassigned","18"),("Due audit","42"),("NBV","186M")],
     cols=["Tag","Item","Custodian","Status"], rows=[("IT-221","ThinkPad","Cipher","OK"),("VH-04","Hilux","Ops","Service due"),("FN-88","Desk","HR","OK")],
     **pal("#334155","#38BDF8","#F1F5F9","#0F172A"),
     wa="Hi%201000%20Hills%20Group!%20I%20want%20TagTrack."),
dict(file="system-documents.html", name="VaultDocs DMS", icon="fa-folder-tree", tagline="Document management", desc="DMS — folders, versions, approvals and e-sign.", features=["Versions","Approvals","E-sign","Search"],
     screen="Pending approvals", sidenav=[("fa-folder","Library"),("fa-code-branch","Versions"),("fa-stamp","Approvals"),("fa-signature","E-sign"),("fa-gear","Settings")],
     kpis=[("Files","4,812"),("Pending","11"),("Expiring contracts","6"),("Storage","38 GB")],
     cols=["Doc","Owner","Version","Status"], rows=[("Lease Nyarutarama","Legal","v4","Approve"),("Staff handbook","HR","v2","Signed"),("ISO SOP-12","Ops","v7","Draft")],
     **pal("#1E293B","#94A3B8","#F8FAFC","#0F172A"),
     wa="Hi%201000%20Hills%20Group!%20I%20want%20VaultDocs."),
dict(file="system-contracts.html", name="ClauseKeep", icon="fa-file-contract", tagline="Contract lifecycle", desc="CLM — templates, obligations, renewals and alerts.", features=["Templates","Obligations","Renewals","Alerts"],
     screen="Renewals 60 days", sidenav=[("fa-file","Contracts"),("fa-bell","Alerts"),("fa-list-check","Obligations"),("fa-rotate","Renewals"),("fa-gear","Settings")],
     kpis=[("Active","128"),("Renew 60d","9"),("Value","2.1B"),("Missed obl.","1")],
     cols=["Contract","Counterparty","End","Action"], rows=[("Fibre ISP","NetPulse","12 Oct","Renew"),("Office lease","Ubumwe","01 Nov","Review"),("Cleaning","Spark","30 Sep","Renegotiate")],
     **pal("#312E81","#A78BFA","#F5F3FF","#312E81"),
     wa="Hi%201000%20Hills%20Group!%20I%20want%20ClauseKeep."),
dict(file="system-procurement.html", name="BidDesk Procure", icon="fa-gavel", tagline="Procurement & tenders", desc="Procurement — RFQs, bids, evaluations and POs.", features=["RFQ","Bids","Eval","POs"],
     screen="Open RFQs", sidenav=[("fa-file","RFQs"),("fa-scale-balanced","Eval"),("fa-file-invoice","POs"),("fa-truck","Deliveries"),("fa-gear","Settings")],
     kpis=[("Open RFQs","6"),("Bids in","19"),("Savings YTD","12%"),("Late PO","2")],
     cols=["RFQ","Category","Bids","Status"], rows=[("RFQ-88","Laptops","5","Eval"),("RFQ-87","Fuel","3","Awarded"),("RFQ-86","Printing","4","Open")],
     **pal("#7C2D12","#FB923C","#FFF7ED","#7C2D12"),
     wa="Hi%201000%20Hills%20Group!%20I%20want%20BidDesk."),
dict(file="system-warehouse-retail.html", name="AisleOps Retail", icon="fa-store", tagline="Multi-store retail ops", desc="Multi-branch retail — transfers, shrinkage and planograms.", features=["Transfers","Shrink","Stores","Planogram"],
     screen="Stores today", sidenav=[("fa-store","Stores"),("fa-right-left","Transfers"),("fa-chart-pie","Shrink"),("fa-boxes","Replenish"),("fa-gear","Settings")],
     kpis=[("Stores","7"),("Transfers","12"),("Shrink 30d","1.1%"),("OOS SKUs","23")],
     cols=["Store","Sales","Shrink","Status"], rows=[("Kimironko","420k","0.6%","OK"),("Nyabugogo","610k","1.8%","Watch"),("Remera","280k","0.4%","OK")],
     **pal("#9A3412","#FDBA74","#FFF7ED","#9A3412"),
     wa="Hi%201000%20Hills%20Group!%20I%20want%20AisleOps."),
dict(file="system-ecommerce-admin.html", name="CartAdmin", icon="fa-bag-shopping", tagline="E-commerce back office", desc="Shop admin — orders, stock, coupons and MoMo recon.", features=["Orders","Stock","Coupons","MoMo"],
     screen="Orders inbox", sidenav=[("fa-bag-shopping","Orders"),("fa-boxes","Stock"),("fa-ticket","Coupons"),("fa-mobile","MoMo"),("fa-gear","Settings")],
     kpis=[("Orders today","64"),("To pick","18"),("Failed pay","3"),("GMV","2.8M")],
     cols=["Order","Customer","Total","Status"], rows=[("#5521","Aline","24,500","Pick"),("#5520","Jean","8,200","Paid"),("#5518","Nadia","61,000","Ship")],
     **pal("#0F172A","#34D399","#ECFDF5","#064E3B"),
     wa="Hi%201000%20Hills%20Group!%20I%20want%20CartAdmin."),
dict(file="system-delivery.html", name="RiderHub Last Mile", icon="fa-motorcycle", tagline="Delivery dispatch", desc="Last-mile — riders, batches, COD and proof of delivery.", features=["Riders","Batches","COD","POD"],
     screen="Live riders", sidenav=[("fa-motorcycle","Riders"),("fa-boxes","Batches"),("fa-money-bill","COD"),("fa-camera","POD"),("fa-gear","Settings")],
     kpis=[("On shift","22"),("Stops left","148"),("COD held","1.1M"),("SLA 45m","88%")],
     cols=["Rider","Zone","Stops","Status"], rows=[("Eric","Kacyiru","7","On route"),("Diane","Remera","11","At pickup"),("Patrick","Gikondo","4","Returning")],
     **pal("#7C2D12","#FB923C","#FFF7ED","#7C2D12"),
     wa="Hi%201000%20Hills%20Group!%20I%20want%20RiderHub."),
dict(file="system-taxi.html", name="RideHills Dispatch", icon="fa-taxi", tagline="Taxi / moto dispatch", desc="Dispatch — jobs, drivers, fares and settlements.", features=["Jobs","Drivers","Fares","Settle"],
     screen="Live jobs", sidenav=[("fa-map","Map"),("fa-car","Drivers"),("fa-receipt","Fares"),("fa-wallet","Settle"),("fa-gear","Settings")],
     kpis=[("Online drivers","86"),("Open jobs","14"),("Completed today","410"),("GMV","3.4M")],
     cols=["Job","From–To","Driver","Status"], rows=[("R-901","Airport→Kiyovu","Eric","En route"),("R-902","Nyabugogo→Remera","—","Unassigned"),("R-888","Kacyiru→Gisozi","Diane","Done")],
     **pal("#365314","#A3E635","#F7FEE7","#365314"),
     wa="Hi%201000%20Hills%20Group!%20I%20want%20RideHills."),
dict(file="system-parking.html", name="BayWatch Parking", icon="fa-square-parking", tagline="Parking & ANPR", desc="Parking — bays, tickets, season passes and ANPR.", features=["Bays","Tickets","Season","ANPR"],
     screen="Car park A", sidenav=[("fa-square-parking","Bays"),("fa-ticket","Tickets"),("fa-id-card","Season"),("fa-camera","ANPR"),("fa-gear","Settings")],
     kpis=[("Occupancy","78%"),("Tickets open","42"),("Season","186"),("Overstay","5")],
     cols=["Bay","Plate","In","Status"], rows=[("A12","RAB 432 A","08:11","OK"),("B04","RAD 110 C","07:40","Season"),("C19","RAE 009 B","06:02","Overstay")],
     **pal("#1E3A8A","#93C5FD","#EFF6FF","#1E3A8A"),
     wa="Hi%201000%20Hills%20Group!%20I%20want%20BayWatch."),
dict(file="system-events-ticketing.html", name="GateTix", icon="fa-ticket", tagline="Event ticketing", desc="Ticketing — events, QR tickets, door scanners and settlements.", features=["QR tickets","Door","Tiers","Settle"],
     screen="Tonight’s door", sidenav=[("fa-calendar","Events"),("fa-ticket","Tickets"),("fa-qrcode","Scan"),("fa-wallet","Settle"),("fa-gear","Settings")],
     kpis=[("Sold","1,240"),("Scanned","410"),("Comp","22"),("GMV","18.6M")],
     cols=["Tier","Price","Sold","Left"], rows=[("Early bird","8,000","400","0"),("Regular","12,000","640","160"),("VIP","35,000","200","40")],
     **pal("#4A044E","#E879F9","#FDF4FF","#4A044E"),
     wa="Hi%201000%20Hills%20Group!%20I%20want%20GateTix."),
dict(file="system-membership.html", name="Memberly Clubs", icon="fa-id-card", tagline="Club memberships", desc="Clubs — members, dues, events and access cards.", features=["Dues","Cards","Events","Benefits"],
     screen="Members", sidenav=[("fa-users","Members"),("fa-credit-card","Dues"),("fa-calendar","Events"),("fa-id-card","Access"),("fa-gear","Settings")],
     kpis=[("Members","540"),("Dues overdue","18"),("Events 30d","4"),("Renewals","31")],
     cols=["Member","Plan","Dues","Status"], rows=[("Ineza D.","Gold","Paid","OK"),("Jean M.","Silver","Overdue","Hold"),("Aline K.","Gold","Paid","OK")],
     **pal("#1C1917","#D6D3D1","#FAFAF9","#1C1917"),
     wa="Hi%201000%20Hills%20Group!%20I%20want%20Memberly."),
dict(file="system-agri.html", name="ShambaOS Farm", icon="fa-seedling", tagline="Farm records", desc="Farm OS — plots, inputs, harvests and traceability lots.", features=["Plots","Inputs","Harvest","Lots"],
     screen="Season dashboard", sidenav=[("fa-map","Plots"),("fa-flask","Inputs"),("fa-wheat-awn","Harvest"),("fa-barcode","Lots"),("fa-gear","Settings")],
     kpis=[("Ha planted","42"),("Input cost","6.1M"),("Est. yield","118t"),("Lots open","9")],
     cols=["Plot","Crop","Stage","Health"], rows=[("P-04","Potato","Tuber fill","OK"),("P-07","Maize","Flowering","Watch"),("P-12","Beans","Harvest","OK")],
     **pal("#14532D","#86EFAC","#F0FDF4","#14532D"),
     wa="Hi%201000%20Hills%20Group!%20I%20want%20ShambaOS."),
dict(file="system-coop.html", name="CoopBooks", icon="fa-handshake", tagline="Cooperative accounts", desc="Co-op — members, shares, produce intake and dividends.", features=["Members","Shares","Intake","Dividends"],
     screen="Intake today", sidenav=[("fa-users","Members"),("fa-scale-balanced","Intake"),("fa-coins","Shares"),("fa-chart-pie","Dividends"),("fa-gear","Settings")],
     kpis=[("Members","420"),("Intake kg","8,640"),("Paid today","3.2M"),("Unpaid lots","4")],
     cols=["Member","Crop","Kg","Pay"], rows=[("Habimana","Potato","420","Paid"),("Mukamana","Potato","280","Pending"),("Uwase","Cabbage","110","Paid")],
     **pal("#365314","#FACC15","#FEFCE8","#365314"),
     wa="Hi%201000%20Hills%20Group!%20I%20want%20CoopBooks."),
dict(file="system-vet.html", name="HerdVet", icon="fa-cow", tagline="Livestock & vet records", desc="Herd — animals, treatments, milk and vaccinations.", features=["Herd","Treatments","Milk","Vaccines"],
     screen="Herd health", sidenav=[("fa-cow","Animals"),("fa-syringe","Vet"),("fa-bottle-droplet","Milk"),("fa-calendar","Vaccines"),("fa-gear","Settings")],
     kpis=[("Animals","186"),("Milk today","640 L"),("Treatments","3"),("Due vaccines","12")],
     cols=["Tag","Breed","Status","Next vax"], rows=[("RW-021","Ankole","Lactating","20 Sep"),("RW-044","Friesian","Dry","18 Sep"),("RW-081","Ankole","Calf","01 Oct")],
     **pal("#78350F","#FBBF24","#FFFBEB","#78350F"),
     wa="Hi%201000%20Hills%20Group!%20I%20want%20HerdVet."),
dict(file="system-coldchain.html", name="FrostLink Cold", icon="fa-snowflake", tagline="Cold-chain monitoring", desc="Cold chain — loggers, alerts, vehicles and HACCP logs.", features=["Loggers","Alerts","Vehicles","HACCP"],
     screen="Live temperatures", sidenav=[("fa-snowflake","Chambers"),("fa-truck","Vehicles"),("fa-bell","Alerts"),("fa-clipboard","HACCP"),("fa-gear","Settings")],
     kpis=[("Chambers","8"),("Out of range","1"),("Vehicles","5"),("Alerts 24h","3")],
     cols=["Point","Temp","Range","Status"], rows=[("Chamber A","3.2°C","2–8","OK"),("Chamber B","9.1°C","2–8","Alert"),("Truck 3","4.0°C","2–8","OK")],
     **pal("#0E7490","#67E8F9","#ECFEFF","#164E63"),
     wa="Hi%201000%20Hills%20Group!%20I%20want%20FrostLink."),
dict(file="system-quality.html", name="QMS Hills", icon="fa-certificate", tagline="Quality management", desc="QMS — NCs, CAPA, audits and document control.", features=["NC","CAPA","Audits","Docs"],
     screen="Open NCs", sidenav=[("fa-triangle-exclamation","NCs"),("fa-list-check","CAPA"),("fa-clipboard-check","Audits"),("fa-folder","Docs"),("fa-gear","Settings")],
     kpis=[("Open NC","9"),("Overdue CAPA","2"),("Audits YTD","6"),("On-time close","88%")],
     cols=["NC","Process","Severity","Status"], rows=[("NC-104","Packing","Major","CAPA"),("NC-101","Receiving","Minor","Closed"),("NC-099","Lab","Major","Investigate")],
     **pal("#1E3A8A","#60A5FA","#EFF6FF","#1E3A8A"),
     wa="Hi%201000%20Hills%20Group!%20I%20want%20QMS%20Hills."),
dict(file="system-hse.html", name="SafeSite HSE", icon="fa-hard-hat", tagline="HSE incidents & PTW", desc="HSE — incidents, permits to work, inspections and toolbox talks.", features=["Incidents","PTW","Inspections","Talks"],
     screen="Permits today", sidenav=[("fa-file-circle-exclamation","Incidents"),("fa-stamp","PTW"),("fa-clipboard","Inspect"),("fa-comments","Toolbox"),("fa-gear","Settings")],
     kpis=[("Open PTW","6"),("LTI-free days","124"),("Inspections","8"),("Near misses","3")],
     cols=["Permit","Type","Area","Status"], rows=[("PTW-12","Hot work","Roof","Active"),("PTW-11","Confined","Tank 2","Closed"),("PTW-10","Electrical","Substation","Active")],
     **pal("#7F1D1D","#F87171","#FEF2F2","#450A0A"),
     wa="Hi%201000%20Hills%20Group!%20I%20want%20SafeSite%20HSE."),
dict(file="system-helpdesk-it.html", name="ITSM Desk", icon="fa-computer", tagline="IT service management", desc="ITSM — incidents, assets, changes and SLA.", features=["Incidents","CMDB","Changes","SLA"],
     screen="IT queue", sidenav=[("fa-ticket","Incidents"),("fa-server","CMDB"),("fa-code-branch","Changes"),("fa-stopwatch","SLA"),("fa-gear","Settings")],
     kpis=[("Open","27"),("P1","1"),("Changes this week","4"),("SLA","96%")],
     cols=["ID","Issue","Priority","Status"], rows=[("INC-441","VPN down HQ","P1","Working"),("INC-438","Laptop slow","P3","Queued"),("CHG-12","Firewall rule","—","CAB")],
     **pal("#0F172A","#38BDF8","#F1F5F9","#0F172A"),
     wa="Hi%201000%20Hills%20Group!%20I%20want%20ITSM%20Desk."),
dict(file="system-chatbot.html", name="Hillbot Inbox", icon="fa-comments", tagline="WhatsApp inbox & bots", desc="Omnichannel inbox — WhatsApp, bots, canned replies and handoff.", features=["WhatsApp","Bots","Handoff","Canned"],
     screen="Live inbox", sidenav=[("fa-inbox","Inbox"),("fa-robot","Bots"),("fa-user","Agents"),("fa-chart-simple","Reports"),("fa-gear","Settings")],
     kpis=[("Open chats","34"),("Bot resolved","61%"),("Avg reply","48s"),("CSAT","4.6")],
     cols=["Channel","Contact","Intent","Status"], rows=[("WA","+250 788 …","Order status","Bot"),("WA","+250 789 …","Human","Agent Keza"),("Web","guest-12","Quote","Queued")],
     **pal("#14532D","#4ADE80","#F0FDF4","#14532D"),
     wa="Hi%201000%20Hills%20Group!%20I%20want%20Hillbot%20inbox."),
dict(file="system-survey.html", name="PulseSurvey", icon="fa-square-poll-vertical", tagline="Surveys & CSAT", desc="Surveys — CSAT, NPS, kiosk and WhatsApp forms.", features=["NPS","CSAT","Kiosk","WA forms"],
     screen="NPS this month", sidenav=[("fa-square-poll-vertical","Surveys"),("fa-face-smile","CSAT"),("fa-mobile","WhatsApp"),("fa-store","Kiosk"),("fa-gear","Settings")],
     kpis=[("NPS","48"),("Responses","612"),("CSAT","4.5"),("Detractors","9%")],
     cols=["Touchpoint","NPS","Responses","Trend"], rows=[("Checkout","52","210","Up"),("Support","41","180","Flat"),("Delivery","46","222","Up")],
     **pal("#4C1D95","#C4B5FD","#F5F3FF","#4C1D95"),
     wa="Hi%201000%20Hills%20Group!%20I%20want%20PulseSurvey."),
dict(file="system-loyalty.html", name="StampCard Loyalty", icon="fa-stamp", tagline="Loyalty & stamps", desc="Loyalty — stamps, points, tiers and WhatsApp wallets.", features=["Stamps","Points","Tiers","WA wallet"],
     screen="Members", sidenav=[("fa-stamp","Stamps"),("fa-coins","Points"),("fa-crown","Tiers"),("fa-gift","Rewards"),("fa-gear","Settings")],
     kpis=[("Members","4,210"),("Redeemed MTD","186"),("Active 30d","61%"),("Points issued","92k")],
     cols=["Member","Tier","Points","Last visit"], rows=[("Aline K.","Gold","1,240","Yesterday"),("Jean M.","Silver","420","5d"),("Nadia","Bronze","80","12d")],
     **pal("#9A3412","#FDBA74","#FFF7ED","#9A3412"),
     wa="Hi%201000%20Hills%20Group!%20I%20want%20StampCard."),
dict(file="system-subscription.html", name="RecurPay", icon="fa-rotate", tagline="Subscriptions & billing", desc="Subscriptions — plans, dunning, MoMo mandates and pauses.", features=["Plans","Dunning","MoMo","Pause"],
     screen="MRR snapshot", sidenav=[("fa-layer-group","Plans"),("fa-users","Subs"),("fa-triangle-exclamation","Dunning"),("fa-chart-line","MRR"),("fa-gear","Settings")],
     kpis=[("MRR","6.8M"),("Active","412"),("Past due","18"),("Churn","2.4%")],
     cols=["Customer","Plan","Next bill","Status"], rows=[("Isoko Fresh","Pro","18 Sep","OK"),("Hope RW","NGO","01 Oct","OK"),("VoltHub","Pro","12 Sep","Dunning")],
     **pal("#0F172A","#22D3EE","#ECFEFF","#164E63"),
     wa="Hi%201000%20Hills%20Group!%20I%20want%20RecurPay."),
dict(file="system-analytics.html", name="HillMetrics BI", icon="fa-chart-area", tagline="Business intelligence", desc="BI — dashboards, SQL lite, scheduled PDFs and row-level access.", features=["Dashboards","SQL","PDF","RLS"],
     screen="Exec pack", sidenav=[("fa-chart-area","Boards"),("fa-database","Datasets"),("fa-file-pdf","Schedules"),("fa-lock","Access"),("fa-gear","Settings")],
     kpis=[("Boards","12"),("Refreshed","08:00"),("Alerts","2"),("Viewers","28")],
     cols=["Board","Owner","Refresh","Status"], rows=[("Sales","CEO","Hourly","OK"),("Ops","COO","15m","OK"),("Finance","CFO","Nightly","Late")],
     **pal("#111827","#60A5FA","#F8FAFC","#0F172A"),
     wa="Hi%201000%20Hills%20Group!%20I%20want%20HillMetrics."),
dict(file="system-kiosk.html", name="Q-Kiosk Queue", icon="fa-tv", tagline="Queue management", desc="Queue — tickets, counters, displays and SMS call.", features=["Tickets","Counters","Display","SMS"],
     screen="Bank hall", sidenav=[("fa-ticket","Tickets"),("fa-desktop","Counters"),("fa-tv","Display"),("fa-comment-sms","SMS"),("fa-gear","Settings")],
     kpis=[("Waiting","23"),("Avg wait","11m"),("Serving","6"),("No-show","2")],
     cols=["Ticket","Service","Wait","Status"], rows=[("A042","Teller","8m","Called"),("A043","Loans","14m","Waiting"),("B011","SACCO","3m","Serving")],
     **pal("#1E3A8A","#93C5FD","#EFF6FF","#1E3A8A"),
     wa="Hi%201000%20Hills%20Group!%20I%20want%20Q-Kiosk."),
]

# extra websites (lighter volume, still many)
def wpal(bg, ink, muted, acc, acc2, card, line, navbg, herobg, ctabg, iconc):
    return dict(bg=bg, ink=ink, muted=muted, acc=acc, acc2=acc2, card=card, line=line, navbg=navbg, herobg=herobg, ctabg=ctabg, iconc=iconc)

SITES = [
dict(file="resto-pizza.html", cat="restaurant", category="Restaurant & Food", icon="fa-pizza-slice", name="Forno Kigali", type="Website Demo",
     tagline="Wood-fired pizza", desc="Pizzeria with wood oven, slices and delivery zones.", features=["Wood oven","Delivery","Slices","MoMo"],
     place="Kimihurura", h1="Fire, dough & <em>Kigali nights</em>", lead="90-second pies from a 450° oven.", btn="Order a pie", h2="The oven menu",
     cards=[("fa-fire","Wood fire","Birch & mango wood."),("fa-motorcycle","Delivery","35 minutes."),("fa-wine-glass","Natural wine","Small list.")],
     stats=[("90s","Bake"),("12","Pies"),("4.8","Stars")], nav=["Menu","About","Order"],
     about_h="A small oven with a queue", about="Forno is a 28-seat pizzeria.", list=["Gluten-free dough Fridays","Private oven hire","Lunch slices"],
     cta_h="Hungry?", cta_p="WhatsApp a pie.", wa="Hi%201000%20Hills%20Group!%20I%20want%20a%20pizzeria%20website.",
     **wpal("#1C1917","#FAFAF9","#A8A29A","#EF4444","#F87171","#292524","rgba(239,68,68,.25)","rgba(28,25,23,.95)","#1C1917","#292524","#fff")),
dict(file="hotel-apart.html", cat="hotel", category="Hotel & Tourism", icon="fa-building", name="Kigali Serviced Suites", type="Website Demo",
     tagline="Serviced apartments", desc="Long-stay suites with kitchens, laundry and coworking.", features=["Kitchens","Laundry","Cowork","Weekly rates"],
     place="Kacyiru", h1="Stay longer, <em>live lighter</em>", lead="Studios and 1-beds for consultants and families.", btn="See suites", h2="The building",
     cards=[("fa-kitchen-set","Full kitchen","Cook in."),("fa-wifi","Fibre","Dedicated desk."),("fa-shirt","Laundry","Twice a week.")],
     stats=[("42","Keys"),("From 55k","/ night"),("Weekly","Rates")], nav=["Suites","Work","Stay"],
     about_h="A hotel that behaves like a flat", about="Serviced suites for 3–90 night stays.", list=["Airport pickup","Housekeeping","Parking"],
     cta_h="Need a month?", cta_p="Ask for long-stay.", wa="Hi%201000%20Hills%20Group!%20I%20want%20a%20serviced%20apartment%20site.",
     **wpal("#0F172A","#E2E8F0","#94A3B8","#38BDF8","#7DD3FC","#1E293B","rgba(56,189,248,.2)","rgba(15,23,42,.95)","#0F172A","#1E293B","#0F172A")),
dict(file="shop-furniture.html", cat="ecommerce", category="E-Commerce", icon="fa-couch", name="Imigongo Home", type="Website Demo",
     tagline="Furniture store", desc="Furniture shop with rooms, custom orders and delivery.", features=["Rooms","Custom","Delivery","MoMo"],
     place="Gikondo", h1="Rooms that <em>feel like home</em>", lead="Sofas, tables and lighting made in Rwanda.", btn="Shop rooms", h2="This season",
     cards=[("fa-couch","Living","Modular sofas."),("fa-bed","Sleep","Oak frames."),("fa-truck","Delivery","Kigali 5 days.")],
     stats=[("Showroom","Open"),("Custom","14 days"),("MoMo","Pay")], nav=["Shop","Showroom","Custom"],
     about_h="Made nearby", about="Imigongo Home works with Kigali workshops.", list=["Trade programme","3D room planner","Warranty 2y"],
     cta_h="Visit the showroom", cta_p="Book a slot.", wa="Hi%201000%20Hills%20Group!%20I%20want%20a%20furniture%20store.",
     **wpal("#FFF7ED","#431407","#9A3412","#C2410C","#FB923C","#fff","#FFEDD5","#fff","#FFEDD5","#FED7AA","#fff")),
dict(file="edu-language.html", cat="education", category="Education", icon="fa-language", name="Ikinyarwanda Lab", type="Website Demo",
     tagline="Language school", desc="Language school with group classes, tutors and visas.", features=["Groups","Tutors","Visa","Online"],
     place="Kiyovu", h1="Speak the <em>hills</em>", lead="Kinyarwanda, English and French for work and life.", btn="Join a class", h2="Programmes",
     cards=[("fa-users","Groups","8 per class."),("fa-video","Online","Zoom evenings."),("fa-passport","Visa English","IELTS path.")],
     stats=[("8","Max group"),("A1–C1","Levels"),("MoMo","Fees")], nav=["Courses","Tutors","Fees"],
     about_h="A lab, not a lecture", about="Ikinyarwanda Lab is conversation-first.", list=["Placement test","Corporate classes","Study club"],
     cta_h="Start this Monday", cta_p="Book a placement.", wa="Hi%201000%20Hills%20Group!%20I%20want%20a%20language%20school%20site.",
     **wpal("#EEF2FF","#312E81","#6366F1","#4F46E5","#818CF8","#fff","#C7D2FE","#fff","#E0E7FF","#C7D2FE","#fff")),
dict(file="health-physio.html", cat="health", category="Health", icon="fa-person-walking", name="Stride Physio", type="Website Demo",
     tagline="Physiotherapy clinic", desc="Physio clinic with sports rehab, booking and home visits.", features=["Rehab","Home visits","Sports","Booking"],
     place="Nyarutarama", h1="Move well <em>again</em>", lead="Sports physio, post-op rehab and workplace assessments.", btn="Book a session", h2="How we treat",
     cards=[("fa-dumbbell","Sports","Return-to-play."),("fa-house","Home visits","Kigali inner."),("fa-briefcase","Workplace","Ergonomics.")],
     stats=[("45m","Sessions"),("RSSB","Partner"),("4.9","Rating")], nav=["Treat","Book","Team"],
     about_h="Hands-on, evidence-led", about="Stride is a small physio practice.", list=["Referral letters","Gym next door","MoMo"],
     cta_h="In pain?", cta_p="Same-week slots.", wa="Hi%201000%20Hills%20Group!%20I%20want%20a%20physio%20website.",
     **wpal("#ECFDF5","#064E3B","#047857","#059669","#34D399","#fff","#A7F3D0","#fff","#D1FAE5","#A7F3D0","#fff")),
dict(file="corp-it.html", cat="corporate", category="Corporate", icon="fa-server", name="RidgeTech MSP", type="Website Demo",
     tagline="Managed IT", desc="MSP site with support plans, cybersecurity and on-site SLAs.", features=["SLAs","Security","Cloud","Helpdesk"],
     place="Kigali", h1="IT that <em>stays up</em>", lead="Helpdesk, cloud and security for Rwanda SMEs.", btn="Get a plan", h2="Plans",
     cards=[("fa-headset","Helpdesk","15-min first reply."),("fa-shield","Security","EDR + backup."),("fa-cloud","Cloud","M365 & Google.")],
     stats=[("15m","Reply"),("24/7","Watch"),("RURA","Aware")], nav=["Plans","Security","Contact"],
     about_h="Your in-house IT, outsourced", about="RidgeTech is a local MSP.", list=["On-site engineers","vCIO","Fixed monthly"],
     cta_h="Need a desk?", cta_p="Talk to us.", wa="Hi%201000%20Hills%20Group!%20I%20want%20an%20IT%20company%20website.",
     **wpal("#020617","#E2E8F0","#94A3B8","#22D3EE","#67E8F9","#0F172A","rgba(34,211,238,.2)","rgba(2,6,23,.95)","#020617","#0F172A","#020617")),
dict(file="events-dj.html", cat="events", category="Events & Media", icon="fa-headphones", name="Amplitudes DJ", type="Website Demo",
     tagline="DJ & production", desc="DJ site with mixes, packages and date hold.", features=["Mixes","Packages","Date hold","Tech rider"],
     place="Kigali / touring", h1="Nights that <em>move</em>", lead="Weddings, clubs and brand launches.", btn="Hold a date", h2="Packages",
     cards=[("fa-ring","Weddings","Full reception."),("fa-champagne-glasses","Clubs","Resident sets."),("fa-briefcase","Brands","Launch nights.")],
     stats=[("120","Events / yr"),("4h","Typical set"),("Rider","On request")], nav=["Mixes","Packages","Book"],
     about_h="Vinyl + USB", about="Amplitudes is a Kigali DJ collective.", list=["MC add-on","Lighting","Backup decks"],
     cta_h="Date still free?", cta_p="Hold it today.", wa="Hi%201000%20Hills%20Group!%20I%20want%20a%20DJ%20website.",
     **wpal("#0A0A0A","#FAFAFA","#A1A1AA","#A3E635","#BEF264","#18181B","rgba(163,230,53,.25)","#0A0A0A","#0A0A0A","#18181B","#0A0A0A")),
dict(file="fit-barber.html", cat="fitness", category="Beauty & Fitness", icon="fa-scissors", name="Fade Republic", type="Website Demo",
     tagline="Barbershop", desc="Barbershop with chair booking, memberships and walk-in board.", features=["Chairs","Membership","Walk-ins","Looks"],
     place="Remera", h1="Fades, <em>not guesses</em>", lead="Four chairs, skin fades and beard work.", btn="Book a chair", h2="The shop",
     cards=[("fa-scissors","Cuts","Skin to scissor."),("fa-crown","Beards","Hot towel."),("fa-id-card","Members","2 cuts / month.")],
     stats=[("4","Chairs"),("Walk-in","Board"),("MoMo","Pay")], nav=["Book","Looks","Members"],
     about_h="A proper shop", about="Fade Republic is appointment-first.", list=["Kids Saturdays","Student rate","After 7pm"],
     cta_h="Need a fade?", cta_p="Book now.", wa="Hi%201000%20Hills%20Group!%20I%20want%20a%20barbershop%20website.",
     **wpal("#18181B","#FAFAFA","#A1A1AA","#F59E0B","#FBBF24","#27272A","rgba(245,158,11,.25)","#18181B","#18181B","#27272A","#18181B")),
dict(file="agri-coffee.html", cat="agriculture", category="Agriculture", icon="fa-mug-hot", name="Thousand Hills Coffee", type="Website Demo",
     tagline="Coffee exporter", desc="Coffee estate with lots, cupping notes and wholesale.", features=["Lots","Cupping","Export","Wholesale"],
     place="Nyamasheke", h1="Washed, <em>traceable</em> lots", lead="Smallholder lots from the western slopes.", btn="Request a sample", h2="This harvest",
     cards=[("fa-seedling","Washed","Fully washed AA."),("fa-flask","Cupping","84+ lots."),("fa-ship","Export","Mombasa FCL.")],
     stats=[("84+","Cup"),("Q","Graders"),("EU","Ready")], nav=["Lots","Farm","Trade"],
     about_h="A mill with a name", about="Thousand Hills Coffee is farmer-owned.", list=["QR traceability","Roaster visits","Sample packs"],
     cta_h="Roasting our lots?", cta_p="Ask for samples.", wa="Hi%201000%20Hills%20Group!%20I%20want%20a%20coffee%20exporter%20site.",
     **wpal("#1C1917","#FAFAF9","#A8A29A","#D97706","#FBBF24","#292524","rgba(217,119,6,.25)","#1C1917","#1C1917","#292524","#1C1917")),
dict(file="ngo-health.html", cat="ngo", category="NGO & Church", icon="fa-heart-pulse", name="Ubuzima Outreach", type="Website Demo",
     tagline="Health NGO", desc="Health NGO with clinics, campaigns and donate.", features=["Clinics","Campaigns","Donate","Reports"],
     place="Nyagatare", h1="Care that <em>travels</em>", lead="Mobile clinics and maternal health in the east.", btn="Support a clinic", h2="Programmes",
     cards=[("fa-truck-medical","Mobile clinics","Weekly."),("fa-baby","Maternal","ANC packs."),("fa-book-medical","CHWs","Training.")],
     stats=[("12","Clinics / mo"),("RGB","Reg."),("Open","Books")], nav=["Work","Give","Reports"],
     about_h="Community first", about="Ubuzima Outreach is a local health NGO.", list=["MoMo donate","Volunteer clinicians","Annual audit"],
     cta_h="Fund a clinic day", cta_p="Give today.", wa="Hi%201000%20Hills%20Group!%20I%20want%20a%20health%20NGO%20website.",
     **wpal("#134E4A","#F0FDFA","#5EEAD4","#2DD4BF","#99F6E4","#115E59","rgba(45,212,191,.25)","rgba(19,78,74,.95)","#134E4A","#115E59","#134E4A")),
dict(file="realestate-offplan.html", cat="realestate", category="Real Estate", icon="fa-city", name="Skyline Off-Plan", type="Website Demo",
     tagline="Off-plan developments", desc="Off-plan sales with unit picker, payment plans and site cam.", features=["Unit picker","Plans","Site cam","Escrow"],
     place="Kigali skyline", h1="Buy the <em>view</em> early", lead="Studios to penthouses with staged payments.", btn="See the tower", h2="The scheme",
     cards=[("fa-layer-group","Phases","Two towers."),("fa-percent","Plans","20 / 40 / 40."),("fa-video","Site cam","Weekly.")],
     stats=[("240","Units"),("2027","Handover"),("Escrow","Bank")], nav=["Units","Plans","Visit"],
     about_h="A serious developer site", about="Skyline sells off-plan with escrow.", list=["Show apartment","Mortgage desk","WhatsApp sales"],
     cta_h="Reserve a unit", cta_p="Talk to sales.", wa="Hi%201000%20Hills%20Group!%20I%20want%20an%20off-plan%20website.",
     **wpal("#020617","#F8FAFC","#94A3B8","#F59E0B","#FCD34D","#111827","rgba(245,158,11,.25)","rgba(2,6,23,.95)","#020617","#111827","#020617")),
]

os.makedirs(ROOT, exist_ok=True)
meta = []
for d in SYSTEMS:
    d.setdefault("type", "System Demo")
    d.setdefault("cat", "system")
    d.setdefault("category", "Management System")
    path = os.path.join(ROOT, d["file"])
    with open(path, "w") as f:
        f.write(system(d))
    meta.append(dict(name=d["name"], category=d["category"], cat=d["cat"], type=d["type"],
                     file="demos/"+d["file"], icon="fas "+d["icon"], desc=d["desc"], features=d["features"]))
for d in SITES:
    path = os.path.join(ROOT, d["file"])
    with open(path, "w") as f:
        f.write(site(d))
    meta.append(dict(name=d["name"], category=d["category"], cat=d["cat"], type=d["type"],
                     file="demos/"+d["file"], icon="fas "+d["icon"], desc=d["desc"], features=d["features"]))
print(json.dumps(meta))
print("COUNT", len(meta), "sys", len(SYSTEMS), "sites", len(SITES))
