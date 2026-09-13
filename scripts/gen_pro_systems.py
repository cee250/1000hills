#!/usr/bin/env python3
"""Regenerate every management-system demo as a professional, fully responsive
app dashboard (sidebar drawer on mobile, KPIs, charts, tables that collapse to
cards, quick actions, toasts).

Run:  python3 scripts/gen_pro_systems.py
"""
import os
import re
import sys
import random
import hashlib

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from demo_data import catalogue                      # noqa: E402
from demo_rows_extra import EXTRA_ROWS                # noqa: E402
from pro_system_template import CSS, HTML, JS, TOKENS  # noqa: E402

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "demos")
ASSETS = os.path.join(ROOT, "assets")

PEOPLE = [
    ("Aline Uwase", "Operations lead"), ("Jean Bosco Mugabo", "Branch manager"),
    ("Divine Mukamana", "Administrator"), ("Eric Nshimiyimana", "Supervisor"),
    ("Grace Ingabire", "Finance officer"), ("Kevin Habimana", "Team lead"),
    ("Claire Umutoni", "Service manager"), ("Samuel Niyonzima", "Coordinator"),
]

MONTHS = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug"]
DAYS = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

FINANCE_WORDS = ("account", "invoic", "loan", "savings", "payroll", "subscri",
                 "loyalty", "insurance", "microfinance", "church", "coop",
                 "sacco", "fees", "procure", "contract", "analytic", "survey")

FLAVOUR_OVERRIDE = {
    "system-project.html": "kanban",
    "system-crm.html": "donut",
    "system-lms.html": "progress",
    "system-helpdesk.html": "activity",
    "system-helpdesk-it.html": "activity",
    "system-booking.html": "schedule",
    "system-spa.html": "schedule",
    "system-clinic-emr.html": "schedule",
    "system-inventory.html": "status",
    "system-coldchain.html": "status",
    "system-parking.html": "status",
    "system-energy.html": "donut",
    "system-agri.html": "progress",
    "system-construction.html": "progress",
    "system-hse.html": "status",
    "system-maintenance.html": "status",
    "system-taxi.html": "status",
    "system-delivery.html": "progress",
    "system-events-ticketing.html": "donut",
    "system-isp.html": "donut",
}


# ----------------------------------------------------------------- colour utils
def hex2rgb(h):
    h = h.strip().lstrip("#")
    if len(h) == 3:
        h = "".join(c * 2 for c in h)
    return tuple(int(h[i:i + 2], 16) for i in (0, 2, 4))


def rgb2hex(t):
    return "#" + "".join("%02X" % max(0, min(255, int(round(c)))) for c in t)


def mix(a, b, t):
    """t = 0 -> a, t = 1 -> b"""
    ra, rb = hex2rgb(a), hex2rgb(b)
    return rgb2hex(tuple(ra[i] + (rb[i] - ra[i]) * t for i in range(3)))


def rgba(h, a):
    r, g, b = hex2rgb(h)
    return "rgba(%d,%d,%d,%s)" % (r, g, b, a)


def luminance(h):
    r, g, b = [c / 255.0 for c in hex2rgb(h)]
    return 0.2126 * r + 0.7152 * g + 0.0722 * b


def seed_of(s):
    return int(hashlib.md5(s.encode()).hexdigest()[:8], 16)


# ----------------------------------------------------------------- number utils
NUM_RE = re.compile(r"^([^\d\-]*?)(-?[\d,]*\.?\d+)(.*)$")


def parse_num(value):
    """'8.2M' -> (8.2, '', 'M', 1) ; '1,842' -> (1842.0, '', '', 0)"""
    m = NUM_RE.match(str(value).strip())
    if not m:
        return None
    pre, num, suf = m.group(1), m.group(2), m.group(3)
    try:
        n = float(num.replace(",", ""))
    except ValueError:
        return None
    dec = len(num.split(".")[1]) if "." in num else 0
    # keep a space for word suffixes: "3 classes", not "3classes"
    gap = " " if (suf[:1] == " " and suf.strip()[:1].isalpha()) else ""
    return n, pre.strip(), gap + suf.strip(), dec


def fmt_num(n, pre="", suf="", dec=0):
    txt = ("%." + str(dec) + "f") % n
    if dec == 0:
        txt = "{:,}".format(int(round(n)))
    else:
        whole, frac = txt.split(".")
        txt = "{:,}".format(int(whole)) + "." + frac
    return pre + txt + suf


def initials(name):
    txt = re.sub(r"[^A-Za-z0-9 ]", " ", str(name))
    parts = [p for p in txt.split() if p]
    if not parts:
        return "1H"
    if len(parts) == 1:
        w = parts[0]
        return (w[0] + (w[1] if len(w) > 1 and w[1].isalnum() else "")).upper()
    return (parts[0][0] + parts[-1][0]).upper()


PERSON_COLS = ("member", "client", "student", "staff", "visitor", "customer",
               "borrower", "rider", "guest", "officer", "tech", "host",
               "custodian", "owner", "patient", "user", "group", "contact",
               "driver", "foreman", "agent", "server", "therapist", "account")


# ----------------------------------------------------------------- status words
GOOD = ("ok", "paid", "cleared", "active", "online", "available", "closed", "resolved",
        "completed", "delivered", "on track", "served", "in use", "free", "fresh",
        "occupied", "approved", "awarded", "done", "back", "repaying", "resulted",
        "bank", "momo", "cash", "live", "on loan")
BAD = ("overdue", "out", "alert", "at risk", "breach", "failed", "arrears", "delayed",
       "urgent", "critical", "expiring", "offline", "dispute", "past due", "no-show",
       "investigation", "snags", "unassigned", "pending", "watch", "grid", "high",
       "p1", "major", "flag")
WARN = ("open", "in progress", "cooking", "waiting", "scheduled", "assigned", "queued",
        "proposal", "negotiation", "discovery", "reorder", "part paid", "medium",
        "sent", "evaluating", "drafting", "filed", "review", "renew", "running",
        "reserved", "assessment", "capa", "serving", "delivering", "returning",
        "on site", "on trip", "triage", "starting", "guest", "ot", "late", "renewing",
        "screening", "interview", "offer", "occupied", "due", "qualified", "viewing")


def status_class(text):
    t = str(text).strip().lower()
    if not t or t in ("—", "-"):
        return "p-mute"
    for w in BAD:
        if w in t:
            return "p-bad"
    for w in WARN:
        if w in t:
            return "p-warn"
    for w in GOOD:
        if w in t:
            return "p-ok"
    return "p-info"


def plural(word):
    w = str(word).strip()
    if w.isupper() and len(w) <= 4:
        return w + "s"
    if w.lower().endswith("s"):
        return w.lower()
    if w.lower().endswith("y"):
        return w[:-1].lower() + "ies"
    return w.lower() + "s"


# ----------------------------------------------------------------- chart
def build_chart(rnd, kpis, fname, tagline):
    finance = any(w in (fname + tagline).lower() for w in FINANCE_WORDS)
    labels = MONTHS if finance else DAYS
    n = len(labels)

    # pick the most "chartable" KPI as the series
    pick = None
    for label, value in kpis:
        p = parse_num(value)
        if p and "%" not in p[2] and p[0] > 0:
            pick = (label, p)
            break
    if not pick:
        pick = (kpis[0][0], (100.0, "", "", 0))
    label, (base, pre, suf, dec) = pick

    period = "months" if finance else "days"
    vals = []
    drift = rnd.uniform(0.82, 1.0)
    for i in range(n):
        noise = rnd.uniform(0.68, 1.24)
        v = base * drift * noise
        drift *= rnd.uniform(1.0, 1.06)
        vals.append(max(v, base * 0.18))
    peak = max(vals)
    hi = vals.index(peak)

    cols = []
    for i, (lab, v) in enumerate(zip(labels, vals)):
        h = max(6, round(v / peak * 100))
        cls = ' class="col hi"' if i == hi else ' class="col"'
        cols.append(
            '<div%s><div class="bar" data-h="%d" data-v="%s"></div><small>%s</small></div>'
            % (cls, h, fmt_num(v, pre, suf, dec), lab)
        )

    total = sum(vals)
    avg = total / n
    mini = (
        '<div>Peak<b>%s</b></div><div>Average<b>%s</b></div><div>Total<b>%s</b></div>'
        % (fmt_num(peak, pre, suf, dec), fmt_num(avg, pre, suf, dec), fmt_num(total, pre, suf, dec))
    )
    title = "%s — last %d %s" % (label, n, period)
    sub = "Demo series for a Rwandan team · updates automatically in the live build"
    return "".join(cols), mini, title, sub, label


def sparkline(rnd, tone_color):
    pts = [rnd.uniform(0.28, 0.95) for _ in range(12)]
    pts[-1] = min(1.0, pts[-1] + 0.12)
    w, h = 100, 30
    step = w / (len(pts) - 1)
    coords = [(i * step, h - p * (h - 4) - 2) for i, p in enumerate(pts)]
    line = " ".join("%.1f,%.1f" % c for c in coords)
    area = "0,%.1f %s %.1f,%.1f" % (h, line, w, h)
    return ('<svg viewBox="0 0 %d %d" preserveAspectRatio="none" aria-hidden="true">'
            '<path class="ar" d="M%s Z"/><path class="ln" d="M%s"/>'
            '<circle cx="%.1f" cy="%.1f" r="2.6" fill="%s"/></svg>'
            % (w, h, area, line, coords[-1][0], coords[-1][1], tone_color))


# ----------------------------------------------------------------- side panels
def panel_activity(d, rnd, rows, acc):
    verbs = ["updated", "closed", "flagged", "assigned", "approved", "created"]
    items = []
    pool = list(rows) + list(rows)
    rnd.shuffle(pool)
    tones = ["", "ok", "warn", "bad", ""]
    icons = ["fa-pen", "fa-check", "fa-flag", "fa-user-plus", "fa-shield-halved", "fa-plus"]
    times = ["2 minutes ago", "18 minutes ago", "1 hour ago", "Today, 09:12", "Yesterday, 16:40"]
    for i in range(min(5, len(pool))):
        r = pool[i]
        who = PEOPLE[rnd.randrange(len(PEOPLE))][0].split()[0]
        tone = tones[i % len(tones)]
        items.append(
            '<li><span class="fav %s"><i class="fas %s" aria-hidden="true"></i></span>'
            '<div><p><b>%s</b> %s <b>%s</b> — %s</p><time>%s</time></div></li>'
            % (tone, icons[i % len(icons)], who, verbs[i % len(verbs)], r[0], r[-1], times[i])
        )
    return (
        '<div class="panel"><div class="p-head"><div><h3>Activity</h3>'
        '<small>Everything your team did, in one audit trail</small></div>'
        '<button class="p-link" type="button" data-toast="Full audit log with filters and export.">View all <i class="fas fa-arrow-right" aria-hidden="true"></i></button></div>'
        '<div class="p-body"><ul class="feed">%s</ul></div></div>' % "".join(items)
    )


def panel_progress(d, rnd, rows, acc):
    items = []
    tones = ["", "ok", "warn", "bad"]
    for i, r in enumerate(rows[:5]):
        pct = rnd.randint(12, 98)
        tone = tones[0] if pct > 75 else (tones[2] if pct > 40 else tones[3])
        items.append(
            '<div class="row"><div class="top"><span style="color:var(--ink);font-weight:700">%s</span>'
            '<span>%d%%</span></div><div class="meter"><i class="%s" data-w="%d"></i></div></div>'
            % (r[0], pct, tone, pct)
        )
    return (
        '<div class="panel"><div class="p-head"><div><h3>%s</h3>'
        '<small>Live completion tracked per record</small></div></div>'
        '<div class="p-body"><div class="plist">%s</div></div></div>'
        % ("Progress by %s" % d["cols"][0].lower(), "".join(items))
    )


def panel_donut(d, rnd, rows, acc):
    labels = [str(r[-1]) for r in rows] or ["Active", "Pending", "Closed"]
    seen, uniq = [], []
    for l in labels:
        if l not in seen:
            seen.append(l)
            uniq.append(l)
    while len(uniq) < 3:
        uniq.append(["Pending", "Closed", "Other"][len(uniq) - len(uniq) + 1] if False else "Other")
    uniq = uniq[:4]
    weights = [rnd.randint(18, 52) for _ in uniq]
    total = sum(weights)
    palette = [acc, mix(acc, "#FFFFFF", 0.42), mix(acc, "#0F172A", 0.3), "#94A3B8"]
    stops, cur = [], 0
    for i, w in enumerate(weights):
        deg = w / total * 360
        stops.append("%s %.1fdeg %.1fdeg" % (palette[i % len(palette)], cur, cur + deg))
        cur += deg
    legend = "".join(
        '<div><i style="background:%s"></i><span>%s</span><b>%d%%</b></div>'
        % (palette[i % len(palette)], uniq[i], round(w / total * 100))
        for i, w in enumerate(weights)
    )
    return (
        '<div class="panel"><div class="p-head"><div><h3>Breakdown</h3>'
        '<small>Share of %s by status</small></div></div>'
        '<div class="p-body"><div class="donut-wrap">'
        '<div class="donut" style="background:conic-gradient(%s)"><b>%d<em>records</em></b></div>'
        '<div class="dlist">%s</div></div></div></div>'
        % (plural(d["cols"][0]), ", ".join(stops), total * rnd.randint(9, 40), legend)
    )


def panel_schedule(d, rnd, rows, acc):
    times = ["08:30", "09:15", "10:00", "11:30", "14:00", "15:45", "16:30"]
    items = []
    pool = list(rows)
    rnd.shuffle(pool)
    tones = ["", "w", "b", ""]
    words = ["Confirmed", "Waiting", "Cancelled", "Checked in"]
    for i in range(min(5, max(3, len(pool)))):
        r = pool[i % len(pool)]
        title = " · ".join(str(x) for x in r[:3] if x)
        items.append(
            '<div class="slot"><span class="t">%s</span><div class="w"><h6>%s</h6>'
            '<small>%s</small></div><span class="st %s">%s</span></div>'
            % (times[i % len(times)], title[:46], r[-1], tones[i % len(tones)], words[i % len(words)])
        )
    return (
        '<div class="panel"><div class="p-head"><div><h3>Today&rsquo;s schedule</h3>'
        '<small>Reminders go out by SMS and WhatsApp automatically</small></div>'
        '<button class="p-link" type="button" data-toast="Calendar sync with Google and Outlook is included.">Calendar <i class="fas fa-calendar-days" aria-hidden="true"></i></button></div>'
        '<div class="p-body"><div class="sched">%s</div></div></div>' % "".join(items)
    )


def panel_kanban(d, rnd, rows, acc):
    cols3 = ["To do", "In progress", "Done"]
    pool = list(rows)
    rnd.shuffle(pool)
    out = []
    for c, colname in enumerate(cols3):
        cards = []
        for i in range(2):
            r = pool[(c * 2 + i) % len(pool)]
            who = PEOPLE[rnd.randrange(len(PEOPLE))][0]
            cards.append(
                '<div class="bcard" data-toast="Open “%s” — full detail view in the live build.">'
                '<h6>%s</h6><div class="meta"><span class="av">%s</span>'
                '<small style="font-size:.64rem;color:var(--muted)">%s</small>'
                '<time>%s</time></div></div>'
                % (r[0], r[0], initials(who), who.split()[0], r[-1])
            )
        out.append('<div class="bcol"><h5>%s <b>%d</b></h5>%s</div>'
                   % (colname, len(cards) + rnd.randint(0, 4), "".join(cards)))
    return (
        '<div class="panel"><div class="p-head"><div><h3>Board</h3>'
        '<small>Drag-and-drop in the live build · permissions per column</small></div></div>'
        '<div class="p-body"><div class="board">%s</div></div></div>' % "".join(out)
    )


def panel_status(d, rnd, rows, acc):
    tiles = []
    tones = ["", "w", "b", ""]
    icons = ["fa-circle-check", "fa-triangle-exclamation", "fa-bell", "fa-circle-check", "fa-gauge-high"]
    pool = list(rows)
    for i in range(min(6, len(pool))):
        r = pool[i]
        tiles.append(
            '<div class="tile" data-toast="%s — %s"><div class="th">'
            '<i class="fas %s lead" aria-hidden="true"></i><span class="pip %s"></span></div>'
            '<h6>%s</h6><small>%s</small></div>'
            % (r[0], r[-1], icons[i % len(icons)], tones[i % len(tones)], r[0], " · ".join(str(x) for x in r[1:]))
        )
    return (
        '<div class="panel"><div class="p-head"><div><h3>Live status</h3>'
        '<small>Alerts fire by SMS, WhatsApp and email the moment something goes wrong</small></div></div>'
        '<div class="p-body"><div class="tiles">%s</div></div></div>' % "".join(tiles)
    )


PANELS = {
    "activity": panel_activity, "progress": panel_progress, "donut": panel_donut,
    "schedule": panel_schedule, "kanban": panel_kanban, "status": panel_status,
}


def pick_flavour(d, rnd):
    f = d["file"]
    if f in FLAVOUR_OVERRIDE:
        return FLAVOUR_OVERRIDE[f]
    cols = " ".join(d["cols"]).lower()
    if cols.startswith("time") or "time" == d["cols"][0].lower():
        return "schedule"
    keys = list(PANELS.keys())
    return keys[seed_of(f) % len(keys)]


# ----------------------------------------------------------------- KPI icons
KPI_ICONS = [
    "fa-chart-line", "fa-coins", "fa-clock", "fa-percent", "fa-users", "fa-box",
    "fa-triangle-exclamation", "fa-check-double", "fa-bolt", "fa-calendar",
]


def kpi_tone(i, value, label):
    txt = (str(label) + " " + str(value)).lower()
    if any(w in txt for w in ("overdue", "breach", "risk", "fail", "alert", "arrears", "critical", "no-show", "out of")):
        return "k-bad"
    if any(w in txt for w in ("pending", "watch", "late", "due", "dispute", "snag", "wait")):
        return "k-warn"
    return ["k-ok", "k-info", "", "k-ok"][i % 4]


def tone_color(tone, acc):
    return {"k-bad": "#DC2626", "k-warn": "#D97706", "k-ok": "#0E9F6E", "k-info": "#2563EB"}.get(tone, acc)


# ----------------------------------------------------------------- build page
def build(d):
    fname = d["file"]
    rnd = random.Random(seed_of(fname))

    acc = d.get("acc", "#3B82F6")
    side = d.get("side", "#0F172A")
    bg = d.get("bg", "#F6F8FB")
    ink = d.get("ink", "#0F172A")
    if luminance(bg) < 0.45:            # demo data is light-theme; normalise dark bg
        bg = mix(bg, "#FFFFFF", 0.9)
    if luminance(ink) > 0.6:
        ink = mix(ink, "#0B1220", 0.75)

    light_on_acc = luminance(acc) > 0.62
    acc_ink = "#0B1220" if light_on_acc else "#FFFFFF"
    acc2 = mix(acc, "#FFFFFF", 0.34) if light_on_acc else mix(acc, "#FFFFFF", 0.22)
    acc_light = mix(acc, "#FFFFFF", 0.45)
    acc_bg = rgba(acc, 0.1)
    acc_fade = rgba(acc, 0.55)

    side2 = mix(side, "#000000", 0.22)
    side_ink = "#DCE5F1"
    side_muted = mix(side_ink, side, 0.52)

    card2 = mix(bg, "#FFFFFF", 0.55)
    muted = mix(ink, bg, 0.46)
    faint = mix(ink, bg, 0.66)
    line = rgba(ink, 0.09)
    line2 = rgba(ink, 0.16)

    ok, warn, bad, info = "#0E9F6E", "#D97706", "#DC2626", "#2563EB"

    rows = list(d.get("rows", [])) + list(EXTRA_ROWS.get(fname, []))
    cols = d["cols"]
    kpis = d["kpis"]
    nav = d.get("sidenav", [("fa-gauge-high", "Dashboard"), ("fa-gear", "Settings")])
    features = d.get("features", [])

    who_name, who_role = PEOPLE[seed_of(fname) % len(PEOPLE)]

    # ---- side nav split
    main_nav = nav[:3] if len(nav) > 3 else nav
    sub_nav = nav[3:] if len(nav) > 3 else [("fa-gear", "Settings")]
    badges = ["", "", ""]

    def nav_html(items, first_active=True):
        out = []
        for i, (ic, t) in enumerate(items):
            on = ' class="on"' if (first_active and i == 0) else ""
            badge = ""
            if i == 0 and rnd.random() > 0.45:
                badge = '<span class="n-badge">%d</span>' % rnd.randint(2, 14)
            out.append('<a href="#"%s><i class="fas %s" aria-hidden="true"></i> %s%s</a>' % (on, ic, t, badge))
        return "".join(out)

    # ---- KPI cards
    kpi_html = []
    for i, (label, value) in enumerate(kpis):
        tone = kpi_tone(i, value, label)
        parsed = parse_num(value)
        if parsed:
            n, pre, suf, dec = parsed
            val_html = ('<b><span data-count="%s" data-pre="%s" data-suf="%s" data-dec="%d">%s</span></b>'
                        % (n, pre, suf, dec, value))
        else:
            val_html = "<b>%s</b>" % value
        deltas = [("+12%", "up"), ("-4%", "down"), ("+8%", "up"), ("+2.1%", "up")]
        dtxt, dcls = deltas[i % len(deltas)]
        if tone == "k-bad":
            dtxt, dcls = ("+2", "down")
        kpi_html.append(
            '<article class="kpi %s"><div class="kpi-top">'
            '<span class="kpi-ic"><i class="fas %s" aria-hidden="true"></i></span>'
            '<span class="delta %s"><i class="fas fa-%s" aria-hidden="true"></i> %s</span></div>'
            '%s<span>%s</span><div class="spark">%s</div></article>'
            % (tone, KPI_ICONS[(i * 3 + seed_of(fname)) % len(KPI_ICONS)], dcls,
               "arrow-trend-up" if dcls == "up" else "arrow-trend-down", dtxt,
               val_html, label, sparkline(rnd, tone_color(tone, acc)))
        )

    # ---- chart
    chart_cols, mini_stats, chart_title, chart_sub, series = build_chart(rnd, kpis, fname, d.get("tagline", ""))

    # ---- side panel
    flavour = pick_flavour(d, rnd)
    side_panel = PANELS[flavour](d, rnd, rows, acc)

    # ---- table
    NOUN_OVERRIDE = {"system-booking.html": "appointments",
                   "system-payroll-sme.html": "payslips"}
    noun = NOUN_OVERRIDE.get(fname, plural(cols[0]))
    thead = "".join("<th>%s</th>" % c for c in cols)
    tbody = []
    for r in rows:
        cells = list(r) + [""] * (len(cols) - len(r))
        tds = []
        for ci, c in enumerate(cells[:len(cols)]):
            val = str(c)
            if ci == 0:
                if cols[0].lower() in PERSON_COLS:
                    lead = '<span class="av">%s</span>' % initials(val)
                else:
                    lead = '<span class="av ai"><i class="fas %s" aria-hidden="true"></i></span>' % d.get("icon", "fa-cube")
                tds.append('<td class="strong" data-l="%s"><span class="who">%s'
                           '<span><b>%s</b></span></span></td>' % (cols[0], lead, val))
            elif ci == len(cols) - 1:
                tds.append('<td data-l="%s"><span class="pill %s">%s</span></td>'
                           % (cols[ci], status_class(val), val))
            else:
                tds.append('<td data-l="%s">%s</td>' % (cols[ci], val))
        tbody.append("<tr>%s</tr>" % "".join(tds))

    statuses = []
    for r in rows:
        s = str(r[-1]).strip()
        if s and s not in statuses:
            statuses.append(s)
    tabs = '<button type="button" class="on">All</button>' + "".join(
        '<button type="button">%s</button>' % s for s in statuses[:5]
    )

    chip_words = ["Kigali", "This week", "MoMo paid", "My team", "Needs action", "High value"]
    rnd.shuffle(chip_words)
    chips = '<button type="button" class="chip on">All %s</button>' % noun + "".join(
        '<button type="button" class="chip" data-nofilter data-toast="%s filter — configured per business in the live build.">%s</button>'
        % (w, w) for w in chip_words[:4]
    )

    # ---- quick actions
    qa_src = [(ic, t) for ic, t in nav if t.lower() != "settings"][:4]
    quick = "".join(
        '<button class="qa" type="button" data-toast="%s module — fully customisable to your workflow.">'
        '<i class="fas %s" aria-hidden="true"></i><span><b>Open %s</b><small>%s</small></span></button>'
        % (t, ic, t, "Live module") for ic, t in qa_src
    )

    mods = "".join('<span><i class="fas fa-check" aria-hidden="true"></i> %s</span>' % f for f in features)

    total = rnd.randint(140, 980)
    LABEL_OVERRIDE = {"system-booking.html": "Add appointment",
                      "system-payroll-sme.html": "Run payroll"}
    primary_label = LABEL_OVERRIDE.get(fname) or (
        "Add %s" % (cols[0].lower() if len(cols[0]) < 12 else "record"))
    wa = d.get("wa", "")
    if not wa.startswith("http"):          # legacy data stores only the message text
        wa = "https://wa.me/250788695396?text=" + wa

    head_base = (d.get("desc") or d.get("tagline", "")).strip().rstrip(". ")
    head_sub = ("%s. Demo data for a Rwandan team — in your build every number, "
                "role and workflow is yours." % head_base)

    tokens = {
        "@@TOKENS@@": TOKENS,          # must be first: it carries the colour tokens
        "@@TITLE@@": "%s | %s — System Demo by 1000 Hills Group" % (d["name"], d.get("tagline", "Management system")),
        "@@META_DESC@@": ("Live %s system demo by 1000 Hills Group (Rwanda): %s "
                          "Works on phone, tablet and desktop." % (d["name"], d.get("desc", ""))),
        "@@NAME@@": d["name"],
        "@@ICON@@": d.get("icon", "fa-gauge-high"),
        "@@TAGLINE@@": d.get("tagline", ""),
        "@@SCREEN@@": d.get("screen", "Dashboard"),
        "@@SCREEN_SHORT@@": (d.get("tagline", "")[:22] or "System").upper(),
        "@@ACC@@": acc, "@@ACC2@@": acc2, "@@ACC_INK@@": acc_ink,
        "@@ACC_LIGHT@@": acc_light, "@@ACC_BG@@": acc_bg, "@@ACC_FADE@@": acc_fade,
        "@@SIDE@@": side, "@@SIDE2@@": side2, "@@SIDE_INK@@": side_ink, "@@SIDE_MUTED@@": side_muted,
        "@@BG@@": bg, "@@CARD2@@": card2, "@@INK@@": ink, "@@MUTED@@": muted, "@@FAINT@@": faint,
        "@@LINE@@": line, "@@LINE2@@": line2,
        "@@OK@@": ok, "@@WARN@@": warn, "@@BAD@@": bad, "@@INFO@@": info,
        "@@OK_BG@@": rgba(ok, .12), "@@WARN_BG@@": rgba(warn, .13),
        "@@BAD_BG@@": rgba(bad, .1), "@@INFO_BG@@": rgba(info, .1),
        "@@OK_LIGHT@@": mix(ok, "#FFFFFF", .45), "@@WARN_LIGHT@@": mix(warn, "#FFFFFF", .45),
        "@@BAD_LIGHT@@": mix(bad, "#FFFFFF", .45),
        "@@SIDENAV@@": nav_html(main_nav),
        "@@SIDENAV2@@": nav_html(sub_nav, first_active=False),
        "@@KPIS@@": "".join(kpi_html),
        "@@CHART@@": chart_cols, "@@MINI_STATS@@": mini_stats,
        "@@CHART_TITLE@@": chart_title, "@@CHART_SUB@@": chart_sub, "@@CHART_SERIES@@": series,
        "@@SIDE_PANEL@@": side_panel,
        "@@THEAD@@": thead, "@@TBODY@@": "".join(tbody),
        "@@TABS@@": tabs, "@@CHIPS@@": chips,
        "@@TABLE_TITLE@@": "%s overview" % noun.title(),
        "@@TABLE_SUB@@": "%s · sorted by %s · demo data" % (d.get("tagline", "").capitalize(), cols[-1].lower()),
        "@@TABLE_NOUN@@": noun, "@@ROW_COUNT@@": str(len(rows)), "@@TOTAL@@": "{:,}".format(total),
        "@@QUICK@@": quick, "@@MODS@@": mods,
        "@@SEARCH_NOUN@@": noun,
        "@@USER_NAME@@": who_name, "@@USER_SHORT@@": who_name.split()[0],
        "@@USER_ROLE@@": who_role, "@@INITIALS@@": initials(who_name),
        "@@WA@@": wa,
        "@@PRIMARY_LABEL@@": primary_label.title(),
        "@@PRIMARY_ICON@@": "fa-plus",
        "@@PRIMARY_TOAST@@": "Demo form — in the live build this opens your %s form with validation and MoMo payment." % primary_label.split()[-1].lower(),
        "@@HEAD_SUB@@": head_sub,
        "@@ALERT_TEXT@@": "%d items need your attention today — demo notifications." % rnd.randint(2, 9),
        "@@PLAN_TEXT@@": "%s demo workspace" % d["name"],
        "@@PLAN_PCT@@": str(rnd.randint(38, 78)),
    }

    html = HTML
    for k, v in tokens.items():
        html = html.replace(k, v)

    # favicon: accent tile with the brand initial (no external request)
    letter = d["name"][0].upper()
    fav = ("data:image/svg+xml," + ("<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 64 64'>"
           "<rect width='64' height='64' rx='14' fill='%s'/><text x='32' y='45' font-family='Inter,Arial' "
           "font-size='36' font-weight='800' text-anchor='middle' fill='%s'>%s</text></svg>"
           % (acc.replace("#", "%23"), acc_ink.replace("#", "%23"), letter)).replace("#", "%23"))
    html = html.replace('@@FAVICON@@', fav)
    return html


def write_assets():
    """Shared shell CSS/JS — downloaded once and cached across every demo."""
    os.makedirs(ASSETS, exist_ok=True)
    banner_css = ("/* 1000 Hills Group — shared management-system demo shell.\n"
                  "   Generated by scripts/gen_pro_systems.py — do not edit by hand. */\n")
    banner_js = ("/* 1000 Hills Group — shared management-system demo behaviour.\n"
                 "   Generated by scripts/gen_pro_systems.py — do not edit by hand. */\n")
    with open(os.path.join(ASSETS, "pro-system.css"), "w", encoding="utf-8") as f:
        f.write(banner_css + CSS.strip() + "\n")
    with open(os.path.join(ASSETS, "pro-system.js"), "w", encoding="utf-8") as f:
        f.write(banner_js + "'use strict';\n" + JS.strip() + "\n")


def main():
    systems, _ = catalogue()
    os.makedirs(ROOT, exist_ok=True)
    write_assets()
    written = 0
    for d in systems:
        out = os.path.join(ROOT, d["file"])
        with open(out, "w", encoding="utf-8") as f:
            f.write(build(d))
        written += 1
    print("wrote %d pro system demos" % written)


if __name__ == "__main__":
    main()
