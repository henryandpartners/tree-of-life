#!/usr/bin/env python3
"""Merge symbol datasets -> symbols-all.json with region assignment for the 3D tree."""
import json, glob, os

REGIONS = [
    # id, name, hex color, civs (exact match on 'civ' field; unmatched -> fallback by keyword)
    ("mesopotamia", "Mesopotamia & the Levant", "#c9873c", ["Mesopotamian", "Levantine"]),
    ("africa",      "Egypt & Africa",            "#d9b23a", ["Egyptian", "African", "West African", "African (Malagasy)", "African (Aksumite)", "African (Mande)", "Ethiopian", "Coptic"]),
    ("abrahamic",   "Judaism, Christianity & Islam", "#7fae8f", ["Jewish & Kabbalistic", "Islamic", "Byzantine"]),
    ("persia",      "Persia & the Silk Road",    "#b06a4a", ["Persian", "Sogdian", "Turkic & Siberian", "Mongolian & Steppe", "Zoroastrian"]),
    ("europe",      "Europe & the North",        "#8fa8c9", ["Christian (Western)", "Greek", "Roman", "Norse", "Celtic", "Modern", "Slavic", "Baltic & Finnic", "Sami", "Basque", "Armenian & Georgian"]),
    ("southasia",   "South & Southeast Asia",    "#5fa88a", ["Hindu (Indian)", "Buddhist", "Khmer", "Southeast Asian", "Tibetan & Himalayan"]),
    ("eastasia",    "East Asia",                 "#c96a6a", ["Chinese", "Japanese", "Korean"]),
    ("americas",    "The Americas",              "#a86bc9", ["Aztec (Mexica)", "Maya", "Mesoamerican", "Native American", "Mexican (Folk)", "Andean / Mapuche", "Amazonian", "Andean", "Mapuche", "Inuit"]),
    ("oceania",     "Oceania & the Pacific",     "#5ab8c9", ["Aboriginal Australian", "Māori / Pacific", "Pacific / Polynesian", "Māori", "Pacific"]),
]

KEYWORDS = [  # fallback keyword scan (region_id, [keywords])
    ("mesopotamia", ["mesopotam", "assyri", "babylon", "sumer", "levant", "ugarit", "akkad"]),
    ("africa", ["egypt","africa","aksum","ethiop","mande","malagas","coptic","yoruba","kongo","dogon","benin","dahomey","nigerian","mali"]),
    ("abrahamic", ["jewish","kabba","islam","muslim","quran","mosque","byzantine","hebrew","torah","christian","church","cathedral","ottoman","iznik","umayyad"]),
    ("persia", ["persia","iran","sogdi","turkic","siberia","mongol","steppe","zoroast","afghan","uzbek","tajik","kazakh","yakut","altai","buryat"]),
    ("europe", ["europe","greek","roman","norse","celtic","slav","baltic","finn","sami","basque","armenian","georgian","modern","austrian","french","english","german"]),
    ("southasia", ["hindu","india","buddh","khmer","tibet","nepal","bhutan","sri lanka","pakistan","bengal","madhubani","pattachitra","kalamkari","mughal","rajasthani","javanese","indonesia","banjar","balinese"]),
    ("eastasia", ["china","chinese","japan","japanese","korean","dunhuang","tang","song","ming","qing","edo","naxi","yunnan"]),
    ("americas", ["aztec","maya","mesoam","native american","mexic","andean","mapuche","amazon","inuit","north america","south america","andes","tlingit","alaska","chav"]),
    ("oceania", ["australia","aborigin","maori","māori","polynesia","pacific","hawaii","rapa nui","melanesia"]),
]

def region_for(civ, name):
    for rid, _, _, civs in REGIONS:
        if civ in civs:
            return rid
    cl = (civ + " " + name).lower()
    for rid, kws in KEYWORDS:
        if any(k in cl for k in kws):
            return rid
    return "europe"

def main():
    entries = json.load(open("symbol-data.json"))
    seen = {e["id"] for e in entries}
    for f in ["new_symbols4.json"]:
        if os.path.exists(f):
            new = json.load(open(f))
            kept = [e for e in new if e["id"] not in seen and e.get("name")]
            for e in kept:
                seen.add(e["id"])
                e.setdefault("img",""); e.setdefault("full",""); e.setdefault("source","")
                e.setdefault("era",""); e.setdefault("type","Artifact"); e.setdefault("location","")
                e.setdefault("desc",""); e.setdefault("credit",""); e.setdefault("license","")
                e.setdefault("artist",""); e.setdefault("w",0); e.setdefault("h",0)
            entries += kept
            print(f"{f}: +{len(kept)}")
    rmap = {r[0]: {"id": r[0], "name": r[1], "color": r[2]} for r in REGIONS}
    for e in entries:
        rid = region_for(e.get("civ",""), e.get("name",""))
        e["region"] = rid
        # strip tracking params from wikimedia urls
        for k in ("img","full"):
            u = e.get(k) or ""
            if "?" in u and "utm_" in u:
                e[k] = u.split("?")[0]
    out = {"regions": list(rmap.values()), "symbols": entries}
    json.dump(out, open("symbols-all.json","w"), ensure_ascii=False, indent=1)
    from collections import Counter
    c = Counter(e["region"] for e in entries)
    print("total:", len(entries))
    for rid, n in c.most_common():
        print(f"  {n:3d}  {rmap[rid]['name']}")

if __name__ == "__main__":
    main()
