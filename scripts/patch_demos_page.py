#!/usr/bin/env python3
"""Splice the new demos-page CSS / filter bar / modal / script into demos.html
without touching the 130-entry DEMOS array.

Run:  python3 scripts/patch_demos_page.py
"""
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from demos_page_blocks import CSS, FILTER, MODAL        # noqa: E402
from demos_page_js import JS                            # noqa: E402

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
PAGE = os.path.join(ROOT, "demos.html")

NO_RESULTS_NEW = """            <div class="no-results" id="noResults">
                <i class="fas fa-face-frown"></i>
                <p>No demos match that search — but we can still <strong>build it custom</strong> for you.</p>
                <a class="btn-primary" href="https://wa.me/250788695396?text=Hi%201000%20Hills%20Group!%20I%20need%20a%20custom%20website%20or%20system." target="_blank" rel="noopener"><i class="fab fa-whatsapp"></i> Request it on WhatsApp</a>
            </div>
"""


def cut(src, start_marker, end_marker, replacement, keep_end=False):
    i = src.index(start_marker)
    j = src.index(end_marker, i)
    if not keep_end:
        j += len(end_marker)
    return src[:i] + replacement + src[j:]


def main():
    src = open(PAGE, encoding="utf-8").read()

    # 1. page stylesheet
    src = cut(src, "    <style>\n", "    </style>\n", CSS.strip("\n") + "\n")

    # 2. filter bar (up to the DEMOS GRID comment)
    src = cut(src,
              '    <div class="filter-bar"',
              '    <!-- ======================================== -->\n    <!-- DEMOS GRID',
              FILTER.rstrip("\n") + "\n\n",
              keep_end=True)

    # 3. empty state
    src = re.sub(r'            <div class="no-results" id="noResults">.*?\n            </div>\n',
                 NO_RESULTS_NEW, src, count=1, flags=re.S)

    # 4. modal + back-to-top
    src = cut(src,
              '    <!-- ======================================== -->\n    <!-- PREVIEW MODAL',
              '    <!-- ======================================== -->\n    <!-- FOOTER',
              MODAL.rstrip("\n") + "\n\n",
              keep_end=True)

    # 5. inline script (keeps the DEMOS array above it untouched)
    src = cut(src,
              '    const WA_NUMBER = "250788695396";',
              '    })();\n    </script>',
              JS.rstrip("\n") + "\n</script>",
              keep_end=False)

    open(PAGE, "w", encoding="utf-8").write(src)

    left = set(re.findall(r"@@[A-Z_]+@@", src))
    print("demos.html patched — %d lines, unresolved tokens: %s" % (src.count("\n"), left or "none"))
    for probe in ['id="filterPills"', 'id="pillToggle"', 'class="rail-btn prev"', 'id="backTop"',
                  'id="modalLoading"', 'poster(', 'CAT_TINT', 'id="demosGrid"', "const DEMOS = ["]:
        print("   %-24s %s" % (probe, "ok" if probe in src else "MISSING"))


if __name__ == "__main__":
    main()
