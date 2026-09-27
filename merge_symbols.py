#!/usr/bin/env python3
"""Merge symbol-data.json (existing 21) + new_entries resolved via new_symbols_resolved.json
into a new symbol-data.json. Drops entries with no resolved image, keeps schema identical."""
import json, re
from new_entries import E
from new_entries2 import E2

res = json.load(open("new_symbols_resolved.json"))
res2 = json.load(open("new_symbols2_resolved.json"))
existing = json.load(open("symbol-data.json"))

def clean_artist(a):
    if not a: return ""
    s = re.sub(r'<[^>]+>', '', a)
    s = re.sub(r'No machine-readable author provided\..*', '', s)
    s = re.sub(r'\(based on copyright claims\)', '', s)
    s = re.sub(r'assumed.*', '', s)
    s = s.replace('Unknown author', '').strip()
    return s.strip(' .')

out = list(existing)
dropped, added = [], 0
for batch_res, batch in ((res, E), (res2, E2)):
    for key, meta in batch.items():
        r = batch_res.get(key) or {}
        p = r.get("picked")
        if not p or not p.get("url"):
            dropped.append(key); continue
        if any(o["name"] == meta["name"] for o in out):
            dropped.append(key + " (dup name)"); continue
        img = p.get("thumb") or p.get("url")
        out.append({
            "id": key,
            "name": meta["name"], "civ": meta["civ"], "era": meta["era"],
            "type": meta["type"], "location": meta["location"],
            "desc": meta["desc"], "credit": meta["credit"],
            "license": p.get("license",""),
            "artist": clean_artist(p.get("artist","")),
            "img": img, "full": p.get("url"),
            "source": p.get("desc_page"),
            "w": p.get("w"), "h": p.get("h"),
        })
        added += 1

json.dump(out, open("symbol-data.json","w"), ensure_ascii=False, indent=1)
civs = sorted({o["civ"] for o in out})
print(f"total {len(out)} ({added} added, {len(dropped)} dropped-no-image)")
print(f"civs({len(civs)}): {civs}")
if dropped: print("dropped:", dropped)
# sanity: any dup ids?
ids = [o["id"] for o in out]
assert len(ids) == len(set(ids)), "dup ids!"
print("no dup ids ✓")
