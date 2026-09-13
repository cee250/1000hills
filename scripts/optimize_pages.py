#!/usr/bin/env python3
"""Page-level performance surgery for the marketing pages.

  * drops the AOS CDN (render-blocking CSS + JS) in favour of assets/js/reveal.js
  * drops the three Firebase compat bundles from pages that never use them
    (only client-portal.html touches auth/firestore)
  * preconnects to the icon CDN
  * marks <html class="js"> so reveal animations never hide content without JS
  * lazy-loads below-the-fold images and marks the hero image high priority

Run:  python3 scripts/optimize_pages.py
"""
import os
import re

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
PAGES = ["index.html", "about.html", "services.html", "contact.html",
         "companies.html", "demos.html", "client-portal.html"]

AOS_CSS = '<link href="https://unpkg.com/aos@2.3.1/dist/aos.css" rel="stylesheet" />'
AOS_JS = '<script src="https://unpkg.com/aos@2.3.1/dist/aos.js"></script>'
FIREBASE = [
    '<script src="https://www.gstatic.com/firebasejs/9.22.0/firebase-app-compat.js"></script>',
    '<script src="https://www.gstatic.com/firebasejs/9.22.0/firebase-firestore-compat.js"></script>',
    '<script src="https://www.gstatic.com/firebasejs/9.22.0/firebase-auth-compat.js"></script>',
]
JS_FLAG = "<script>document.documentElement.className += ' js';</script>"
REVEAL = '<script src="assets/js/reveal.js" defer></script>'
PRECONNECT = '<link rel="preconnect" href="https://cdnjs.cloudflare.com" crossorigin />'


def drop(src, literal):
    """Remove every line that contains `literal` (indentation included)."""
    if literal not in src:
        return src, 0
    out, n = [], 0
    for line in src.split("\n"):
        if literal in line:
            n += 1
            continue
        out.append(line)
    return "\n".join(out), n


def tidy(src):
    """Collapse blank lines left behind by removed tags."""
    return re.sub(r"\n[ \t]*\n[ \t]*\n+", "\n\n", src)


def patch(page):
    path = os.path.join(ROOT, page)
    src = open(path, encoding="utf-8").read()
    orig = src
    notes = []

    uses_aos = "data-aos" in src

    # --- AOS -> local reveal shim
    src, n = drop(src, "unpkg.com/aos@2.3.1/dist/aos.css")
    if n:
        notes.append("-aos.css")
    src, n = drop(src, "unpkg.com/aos@2.3.1/dist/aos.js")
    if n:
        notes.append("-aos.js")
    if uses_aos and REVEAL not in src:
        src = src.replace("</body>", "    " + REVEAL + "\n</body>", 1)
        notes.append("+reveal.js")

    # --- Firebase (client-portal is the only real consumer)
    if page != "client-portal.html":
        removed = 0
        for tag in FIREBASE:
            src, n = drop(src, tag)
            removed += n
        if removed:
            notes.append("-firebase x%d" % removed)

    # --- preconnect for the icon CDN
    if "font-awesome" in src and PRECONNECT not in src:
        anchor = '<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />'
        if anchor in src:
            src = src.replace(anchor, anchor + "\n    " + PRECONNECT, 1)
        else:
            src = src.replace("<head>", "<head>\n    " + PRECONNECT, 1)
        notes.append("+preconnect")

    # --- html.js flag (must run before paint)
    if uses_aos and JS_FLAG not in src:
        src = re.sub(r"(<head>)", r"\1\n    " + JS_FLAG, src, count=1)
        notes.append("+js-flag")

    # --- images: lazy + async decoding, except the first (hero) image
    imgs = list(re.finditer(r"<img\b[^>]*>", src))
    if imgs:
        for i, m in enumerate(reversed(imgs)):
            tag = m.group(0)
            new = tag
            if 'decoding=' not in new:
                new = new.replace("<img ", '<img decoding="async" ', 1)
            if 'loading=' not in new:
                idx = len(imgs) - 1 - i
                if idx == 0:                      # header logo / hero — above the fold
                    new = new.replace("<img ", '<img fetchpriority="high" ', 1)
                elif idx >= 2:                    # everything below the fold
                    new = new.replace("<img ", '<img loading="lazy" ', 1)
            if new != tag:
                src = src[:m.start()] + new + src[m.end():]
        notes.append("+img-attrs")

    src = tidy(src)
    if src != orig:
        open(path, "w", encoding="utf-8").write(src)
    return notes


def main():
    for page in PAGES:
        if not os.path.exists(os.path.join(ROOT, page)):
            continue
        print("%-20s %s" % (page, " ".join(patch(page)) or "unchanged"))


if __name__ == "__main__":
    main()
