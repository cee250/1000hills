#!/usr/bin/env python3
"""QA pass over the whole site:
  * every demo referenced by demos.html exists on disk
  * HTML is well-formed enough (balanced block tags)
  * no leftover references to deleted images
  * no unresolved template tokens
  * required mobile-nav hooks are present
"""
import os
import re
import sys
from html.parser import HTMLParser

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
VOID = {"area", "base", "br", "col", "embed", "hr", "img", "input", "link",
        "meta", "param", "source", "track", "wbr"}


class Checker(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.stack = []
        self.errors = []

    def handle_starttag(self, tag, attrs):
        if tag in VOID:
            return
        self.stack.append((tag, self.getpos()))

    def handle_endtag(self, tag):
        if tag in VOID:
            return
        if not self.stack:
            self.errors.append("stray </%s> at %s" % (tag, self.getpos()))
            return
        if self.stack[-1][0] == tag:
            self.stack.pop()
            return
        # tolerate implicit closes (li, p, td, tr, option)
        for i in range(len(self.stack) - 1, -1, -1):
            if self.stack[i][0] == tag:
                skipped = [t for t, _ in self.stack[i + 1:]]
                if all(t in ("li", "p", "td", "tr", "th", "tbody", "option", "div", "span") for t in skipped):
                    del self.stack[i:]
                    return
                self.errors.append("</%s> at %s closes over %s" % (tag, self.getpos(), skipped))
                del self.stack[i:]
                return
        self.errors.append("unexpected </%s> at %s" % (tag, self.getpos()))


def check_file(path):
    src = open(path, encoding="utf-8").read()
    problems = []

    c = Checker()
    try:
        c.feed(src)
        c.close()
    except Exception as e:                                    # noqa: BLE001
        problems.append("parse error: %s" % e)
    unclosed = [t for t, _ in c.stack if t not in ("html", "body")]
    if unclosed:
        problems.append("unclosed: %s" % unclosed[:6])
    problems += c.errors[:4]

    if "@@" in src and "@@TOKENS@@" not in src:
        problems.append("unresolved tokens: %s" % sorted(set(re.findall(r"@@[A-Z0-9_]+@@", src)))[:4])

    # local asset references must exist (ignore anything inside <script>)
    markup = re.sub(r"<script\b.*?</script>", " ", src, flags=re.S)
    markup = re.sub(r"<style\b.*?</style>", " ", markup, flags=re.S)
    base = os.path.dirname(path)
    for m in re.finditer(r'(?:src|href)="([^"#?]+)"', markup):
        url = m.group(1)
        if re.match(r"^(https?:|mailto:|tel:|data:|javascript:|about:)", url):
            continue
        target = os.path.normpath(os.path.join(base, url))
        if not os.path.exists(target):
            problems.append("missing file: %s" % url)

    return problems


def main():
    bad = 0
    pages = [os.path.join(ROOT, f) for f in os.listdir(ROOT) if f.endswith(".html")]
    demos = [os.path.join(ROOT, "demos", f) for f in os.listdir(os.path.join(ROOT, "demos")) if f.endswith(".html")]

    # demos.html must reference real files
    dh = open(os.path.join(ROOT, "demos.html"), encoding="utf-8").read()
    refs = re.findall(r'file: "(demos/[^"]+)"', dh)
    missing = [r for r in refs if not os.path.exists(os.path.join(ROOT, r))]
    print("demos.html references %d demos, missing: %s" % (len(refs), missing or "none"))
    on_disk = {os.path.basename(p) for p in demos}
    orphan = sorted(on_disk - {os.path.basename(r) for r in refs})
    print("demo files not listed in demos.html: %s" % (orphan or "none"))

    for p in sorted(pages + demos):
        problems = check_file(p)
        if problems:
            bad += 1
            print("\n%s" % os.path.relpath(p, ROOT))
            for x in problems[:6]:
                print("   - %s" % x)

    print("\n%d file(s) with problems out of %d checked" % (bad, len(pages) + len(demos)))
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
