#!/usr/bin/env python3
"""Resolve Wikimedia Commons imagery for batch 2 (new_entries2.E2). Same logic as fetch_new_symbols.py."""
import json, os, time, urllib.request, urllib.parse, urllib.error
from new_entries2 import E2

UA = {"User-Agent": "tree-of-life-site/1.0 (sacred-tree reference; contact: henryandpartners)"}
CBASE = "https://commons.wikimedia.org/w/api.php"
OUT = "new_symbols2_resolved.json"

def api(params):
    url = CBASE + "?" + urllib.parse.urlencode(params)
    for attempt in range(6):
        try:
            req = urllib.request.Request(url, headers=UA)
            with urllib.request.urlopen(req, timeout=25) as r:
                return json.loads(r.read().decode())
        except urllib.error.HTTPError as e:
            if e.code == 429 and attempt < 5:
                wait = 15 * (attempt + 1)
                print(f"  429, backing off {wait}s"); time.sleep(wait); continue
            raise

def search(query, limit=6):
    try:
        p = api({"action":"query","generator":"search",
                 "gsrsearch":f"filetype:bitmap {query}","gsrnamespace":"6",
                 "gsrlimit":str(limit),"prop":"imageinfo",
                 "iiprop":"url|mime|size|extmetadata","iiurlwidth":"960",
                 "iiextmetadatafilter":"LicenseShortName|Artist|Credit",
                 "format":"json"})
        pages = (p.get("query",{}) or {}).get("pages",{}) or {}
        out = []
        for pg in pages.values():
            ii = (pg.get("imageinfo") or [{}])[0]
            if not ii.get("url"): continue
            em = ii.get("extmetadata",{}) or {}
            out.append({
                "file": pg.get("title",""),
                "url": ii.get("url"), "thumb": ii.get("thumburl"),
                "mime": ii.get("mime"), "w": ii.get("width"), "h": ii.get("height"),
                "desc_page": ii.get("descriptionurl"),
                "license": em.get("LicenseShortName",{}).get("value",""),
                "artist": em.get("Artist",{}).get("value",""),
            })
        return out
    except Exception as e:
        print(f"  search err {query}: {e}")
        return []

res = json.load(open(OUT)) if os.path.exists(OUT) else {}
todo = [k for k in E2 if k not in res]
print(f"{len(E2)} entries, {len(res)} cached, {len(todo)} to fetch")
for i, key in enumerate(todo):
    meta = E2[key]
    cands = search(meta["query"])
    time.sleep(3.5)
    ok = None
    for c in cands:
        w, h = c.get("w") or 0, c.get("h") or 0
        if w >= 500 and h and (w/h) < 3 and (h/w) < 3:
            ok = c; break
    if not ok and cands:
        ok = cands[0]
    res[key] = {"ok": bool(ok), "picked": ok, "n_cands": len(cands)}
    status = "OK " if ok else "FAIL"
    print(f"[{i+1}/{len(todo)}] {status} {key} -> {ok['file'] if ok else '-'}")
    json.dump(res, open(OUT,"w"), ensure_ascii=False, indent=1)

print("done. failures:", [k for k,v in res.items() if not v["ok"]] or "none")
