#!/usr/bin/env python3
"""Re-resolve specific batch-3 keys with better queries; merges into new_symbols3_resolved.json."""
import json, time
import fetch_new_symbols3 as F
from new_entries3 import E3

# override queries for problem keys
FIX = {
  "Arbol de la vida": "árbol de la vida Metepec ceramics",
  "Indus pipal seal": "Mohenjo-daro pipal seal",
  "Vouves olive": "Olive tree of Vouves Crete",
  "Mondrian tree": "Mondrian Gray Tree 1911",
  "Morris tree of life": "Dearle Tree of Life tapestry Morris",
  "Ardre stone": "Ardre VIII image stone",
  "Tiffany tree window": "Tiffany stained glass tree window landscape",
}

res = json.load(open(F.OUT))
for key, q in FIX.items():
    print(f"re-fetching {key}: {q}")
    cands = F.search(q, 8)
    time.sleep(3.5)
    for c in cands:
        print("   ", c["file"], c.get("license",""), c.get("w"), c.get("h"))
    ok = None
    for c in cands:
        w, h = c.get("w") or 0, c.get("h") or 0
        if w >= 500 and h and (w/h) < 3 and (h/w) < 3:
            ok = c; break
    if not ok and cands: ok = cands[0]
    res[key] = {"ok": bool(ok), "picked": ok, "n_cands": len(cands)}
    json.dump(res, open(F.OUT,"w"), ensure_ascii=False, indent=1)
print("done")
