#!/usr/bin/env python3
"""HEAD-check every img URL in symbol-data.json; report failures."""
import json, urllib.request
d = json.load(open("symbol-data.json"))
UA = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) tree-of-life-site/1.0"}
bad = []
for i, o in enumerate(d):
    url = o["img"]
    try:
        req = urllib.request.Request(url, method="HEAD", headers=UA)
        with urllib.request.urlopen(req, timeout=20) as r:
            if r.status != 200:
                bad.append((o["id"], f"HTTP {r.status}"))
    except Exception as e:
        bad.append((o["id"], str(e)[:80]))
print(f"{len(d)} entries, {len(bad)} bad image urls")
for b in bad: print(" BAD", b)
