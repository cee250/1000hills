#!/usr/bin/env python3
"""Shared loader: pulls the demo catalogue data out of the legacy generators
without running their file-writing tails."""
import os

HERE = os.path.dirname(os.path.abspath(__file__))


def _load(script):
    path = os.path.join(HERE, script)
    src = open(path, encoding="utf-8").read()
    cut = src.index("os.makedirs(ROOT")
    ns = {"__file__": path, "__name__": "legacy_gen"}
    exec(compile(src[:cut], path, "exec"), ns)
    return ns


def catalogue():
    """Return (systems, sites) merged from both legacy generators."""
    d = _load("gen_demos.py")
    m = _load("gen_more.py")

    systems = list(d["SYSTEMS"]) + list(m["SYSTEMS"])
    for s in systems:
        s.setdefault("type", "System Demo")
        s.setdefault("cat", "system")
        s.setdefault("category", "Management System")

    sites = list(m["SITES"]) + list(d["SITES"])
    seen, uniq = set(), []
    for s in sites:
        if s["file"] in seen:
            continue
        seen.add(s["file"])
        uniq.append(s)
    return systems, uniq


if __name__ == "__main__":
    sysm, site = catalogue()
    print("systems:", len(sysm), "sites:", len(site))
    print("system files:", len({s["file"] for s in sysm}))
