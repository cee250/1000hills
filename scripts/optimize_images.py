#!/usr/bin/env python3
"""Image pipeline: recompress + resize every photo/logo to WebP, rewrite all
references, and drop the multi-megabyte originals.

  cipherfox.jpeg 3500x2333 3.6 MB  ->  ~90 KB webp
  Lemigo.png     3168x1985 1.0 MB  ->  ~40 KB webp
  menuhub.png    1254x1254 1.2 MB  ->  ~60 KB webp

The brand logo stays a PNG (og:image + favicon compatibility) and a WebP copy
is used for the on-page <img> tags.

Run:  python3 scripts/optimize_images.py
"""
import json
import os
import re
import subprocess
import sys

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
IMG_OUT = os.path.join(ROOT, "assets", "img")

# source -> (max width, quality, keep original?)
PLAN = {
    "1000hills-logo.png": (880, 92, True),      # brand mark: WebP copy for <img>
    "Lemigo.png": (900, 88, False),
    "menuhub.png": (760, 86, False),
    "Rose.png": (500, 88, False),
    "cipherfox.jpeg": (900, 80, False),
    "Motel-Nyanza.jpeg": (820, 80, False),
    "1000hills.jpeg": (820, 80, False),
    "Gakire.jpeg": (760, 80, False),
    "Grazia.jpeg": (820, 80, False),
    "Inzozi.jpeg": (820, 80, False),
    "Luxury.jpeg": (820, 80, False),
    "Nsbliss.jpeg": (600, 82, False),
    "Retreat.jpeg": (400, 84, False),
    "Saphir.jpeg": (900, 80, False),
    "Tripsync.jpeg": (820, 80, False),
    "awakart.jpeg": (820, 80, False),
}

DEMO_IMG = {f: (1280, 78) for f in [
    "hotel-hero.jpg", "hotel-room.jpg", "realestate-hero.jpg", "realestate-interior.jpg",
    "restaurant-hero.jpg", "restaurant-interior.jpg", "school-hero.jpg",
    "shop-basket.jpg", "shop-coffee.jpg", "shop-fashion.jpg",
]}


def convert(src, dst, maxw, quality):
    cmd = ["convert", src, "-strip", "-resize", "%dx>" % maxw,
           "-quality", str(quality), "-define", "webp:method=4", dst]
    subprocess.run(cmd, check=True)
    return os.path.getsize(dst)


def size(p):
    return os.path.getsize(p) if os.path.exists(p) else 0


def main():
    os.makedirs(IMG_OUT, exist_ok=True)
    renames = {}          # "cipherfox.jpeg" -> "assets/img/cipherfox.webp"
    saved = 0

    print("--- root images ---")
    for name, (maxw, q, keep) in PLAN.items():
        src = os.path.join(ROOT, name)
        out_name = os.path.splitext(name)[0] + ".webp"
        dst = os.path.join(IMG_OUT, out_name)
        if not os.path.exists(src):
            if not os.path.exists(dst):
                continue
            renames[name] = "assets/img/" + out_name
            continue
        before = size(src)
        after = convert(src, dst, maxw, q)
        saved += before - after
        renames[name] = "assets/img/" + out_name
        print("  %-22s %7.0f KB -> %6.0f KB  (%s)" % (name, before / 1024, after / 1024, out_name))
        if not keep:
            os.remove(src)

    print("--- demos/img ---")
    for name, (maxw, q) in DEMO_IMG.items():
        src = os.path.join(ROOT, "demos", "img", name)
        out_name = os.path.splitext(name)[0] + ".webp"
        dst = os.path.join(ROOT, "demos", "img", out_name)
        if not os.path.exists(src):
            if os.path.exists(dst):
                renames["img/" + name] = "img/" + out_name
            continue
        before, after = size(src), convert(src, dst, maxw, q)
        saved += before - after
        renames["img/" + name] = "img/" + out_name
        print("  %-26s %7.0f KB -> %6.0f KB" % (name, before / 1024, after / 1024))
        os.remove(src)

    # ---- rewrite references ----
    targets = [f for f in os.listdir(ROOT) if f.endswith((".html", ".json", ".js"))]
    targets += ["render.js", "content.json"]
    changed = {}
    for f in sorted(set(targets)):
        path = os.path.join(ROOT, f)
        if not os.path.isfile(path):
            continue
        src = open(path, encoding="utf-8").read()
        new = src
        for old, repl in renames.items():
            if old == "1000hills-logo.png":
                # keep the PNG for og:image + favicon; only <img> tags move to WebP
                new = new.replace('src="%s"' % old, 'src="%s"' % repl)
                continue
            if f.endswith(".json") or f.endswith(".js"):
                new = re.sub(r'(["\'])%s\1' % re.escape(old),
                             lambda m, r=repl: m.group(1) + r + m.group(1), new)
            else:
                new = new.replace('"%s"' % old, '"%s"' % repl)
                new = new.replace("'%s'" % old, "'%s'" % repl)
        # broken reference: client-portal.html pointed at a logo.png that never existed
        new = new.replace('src="logo.png"', 'src="%s"' % renames.get("1000hills-logo.png", "1000hills-logo.png"))
        if new != src:
            open(path, "w", encoding="utf-8").write(new)
            changed[f] = True

    # demo pages live in /demos, so their asset path is one level deeper
    demo_dir = os.path.join(ROOT, "demos")
    for f in sorted(os.listdir(demo_dir)):
        if not f.endswith(".html"):
            continue
        path = os.path.join(demo_dir, f)
        src = open(path, encoding="utf-8").read()
        new = src
        for old, repl in renames.items():
            if old.startswith("img/"):
                new = new.replace('"%s"' % old, '"%s"' % repl).replace("'%s'" % old, "'%s'" % repl)
        if new != src:
            open(path, "w", encoding="utf-8").write(new)
            changed["demos/" + f] = True

    print("\nrewrote references in: %s" % ", ".join(sorted(changed)))
    print("total saved: %.1f MB" % (saved / 1024 / 1024))


if __name__ == "__main__":
    main()
