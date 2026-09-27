#!/usr/bin/env python3
"""Fetch a real photo per sacred tree from Wikimedia (Wikipedia main image,
Commons search fallback). Writes photo_map.json: {id: {url, source, label}}.
Free/CC images, direct thumbnail URLs (800px wide)."""
import json, re, time, urllib.request, urllib.parse

UA = {"User-Agent": "tree-of-life-site/1.0 (sacred-tree reference; contact: henry)"}
BASE = "https://en.wikipedia.org/w/api.php"
CBASE = "https://commons.wikimedia.org/w/api.php"

def api(base, params):
    url = base + "?" + urllib.parse.urlencode(params)
    req = urllib.request.Request(url, headers=UA)
    with urllib.request.urlopen(req, timeout=25) as r:
        return json.loads(r.read().decode())

def wiki_image(query):
    """Main image (800px thumbnail) of the best-matching Wikipedia article."""
    try:
        s = api(BASE, {"action":"query","list":"search","srsearch":query,"srlimit":"1","format":"json"})
        hits = s.get("query",{}).get("search",[])
        if not hits: return None
        title = hits[0]["title"]
        p = api(BASE, {"action":"query","titles":title,"prop":"pageimages",
                       "piprop":"thumbnail|name|url","pithumbsize":"800","format":"json","redirects":"1"})
        pages = p.get("query",{}).get("pages",{})
        for pg in pages.values():
            pi = pg.get("pageimages",{})
            thumb = pi.get("thumbnail",{})
            if thumb.get("source"):
                return {"url":thumb["source"],"source":"wikipedia","label":title}
    except Exception as e:
        print(f"  wiki err {query}: {e}")
    return None

def commons_image(query):
    """First bitmap matching a Commons search."""
    try:
        p = api(CBASE, {"action":"query","generator":"search",
                        "gsrsearch":f"filetype:bitmap {query}","gsrnamespace":"6",
                        "gsrlimit":"1","prop":"imageinfo","iiprop":"url|mime",
                        "iiurlwidth":"800","format":"json"})
        pages = p.get("query",{}).get("pages",{})
        for pg in pages.values():
            ii = (pg.get("imageinfo") or [{}])[0]
            if ii.get("thumburl"):
                return {"url":ii["thumburl"],"source":"commons","label":pg.get("title","")}
    except Exception as e:
        print(f"  commons err {query}: {e}")
    return None

# id -> (wiki_species_query, commons_descriptive_query)
Q = {
 "garden-eden":        ("Ficus carica","fig tree"),
 "gilgamesh-tree":     ("Cedrus","cedar tree"),
 "sumerian-sacred-tree":("Phoenix dactylifera","date palm tree"),
 "egypt-sycamore":     ("Ficus sycomorus","sycamore fig tree"),
 "egypt-ba-tree":      ("Phoenix dactylifera","ba tree egypt"),
 "persian-ashoka":     ("Saraca asoca","ashoka tree saraca"),
 "persian-haoma":      ("Ephedra","ephedra shrub"),
 "yggdrasil":          ("Fraxinus excelsior","ash tree europe"),
 "celtic-oak-dagda":   ("Quercus petraea","oak tree"),
 "slavic-world-tree":  ("Quercus robur","oak tree slavic"),
 "greek-hesperides":   ("Malus domestica","apple tree"),
 "greek-olive-athena": ("Olea europaea","olive tree"),
 "greek-dodona-oak":   ("Quercus pubescens","oak tree greece"),
 "kalpavriksha":       ("Ficus benghalensis","banyan tree india"),
 "bodhi-tree":         ("Ficus religiosa","bodhi tree ficus religiosa"),
 "ashvattha-gita":     ("Ficus religiosa","sacred fig ashvattha"),
 "ashoka-indian":      ("Saraca asoca","ashoka tree buddhist"),
 "tala-nirvana":       ("Borassus flabellifer","tala palm tree"),
 "pippal-banyan":      ("Ficus benghalensis","banyan tree root"),
 "mango-hindu":        ("Mangifera indica","mango tree fruit"),
 "soma-vedic":         ("Ephedra","ephedra plant"),
 "xiwangmu-peach":     ("Prunus persica","peach tree blossom"),
 "jing-tree":          (None,"sacred tree heaven"),
 "jade-tree":          (None,"sacred jade tree"),
 "penglai":            ("Prunus persica","longevity peach garden"),
 "sun-god-nagi":       ("Machilus","nagi laurel tree"),
 "isonokami-fig":      ("Ficus","sacred fig shrine japan"),
 "dado-world-tree":    (None,"great world tree"),
 "champa-samye":       ("Michelia champaca","cempaka champa flower"),
 "mongol-ukhai":       ("Quercus","sacred tree steppe mongolia"),
 "ryukyu-kuyaa":       (None,"sacred tree okinawa"),
 "vietnam-banyan":     ("Ficus benghalensis","banyan tree vietnam village"),
 "philippines-bamboo": ("Bamboo","bamboo stalk forest"),
 "thai-phi-tree":      (None,"sacred tree thailand village"),
 "angkor-banyan":      ("Ficus","banyan tree angkor wat root"),
 "kaum-kaet":          (None,"sacred tree sky"),
 "dayak-world-tree":   (None,"sacred tree borneo"),
 "javanese-kerasukan": (None,"sacred tree java indonesia"),
 "balinese-grove":     (None,"sacred grove bali banyan"),
 "myanmar-nat":        (None,"sacred tree myanmar nat"),
 "aztec-ometl":        ("Ceiba pentandra","ceiba tree"),
 "maya-witz":          ("Ceiba pentandra","ceiba tree maya"),
 "kiche-world-tree":   ("Ceiba pentandra","ceiba tree"),
 "aztec-amate":        ("Ficus cotinifolia","amate fig tree bark"),
 "tree-of-peace":      ("Pinus strobus","white pine tree"),
 "lakota-sacred-tree": (None,"sacred tree native american"),
 "nw-coast-cedar":     ("Thuja plicata","red cedar tree"),
 "inca-huaca":         (None,"sacred tree andes inca"),
 "mapuche-pehuen":     ("Araucaria araucana","araucaria monkey puzzle tree"),
 "maori-whakapapa":    (None,"sacred tree maori new zealand"),
 "hawaiian-koa":       ("Acacia koa","koa tree hawaii"),
 "hawaiian-lehua":     ("Meliosma","lehua flower hawaii"),
 "aboriginal-dreaming":("Eucalyptus","ironbark eucalyptus tree australia"),
 "baobab":             ("Adansonia digitata","baobab tree africa"),
 "yoruba-iroko":       ("Milicia excelsa","iroko tree africa"),
 "yoruba-egbesu":      (None,"sacred tree nigeria yoruba"),
 "dogon-tree":         (None,"sacred tree dogon mali"),
}

data = json.load(open("/Users/henry/tree-of-life/data.json"))
out, miss = {}, []
for t in data:
    tid = t["id"]
    wq, cq = Q.get(tid, (None, "sacred tree"))
    r = None
    if wq:
        r = wiki_image(wq)
        if r and r.get("url"):
            out[tid] = r
        else:
            print(f"{tid}: wiki miss ({wq}), trying commons")
    if not r or not r.get("url"):
        r = commons_image(cq)
        if r and r.get("url"):
            out[tid] = r
        else:
            print(f"{tid}: COMMONS MISS ({cq})")
            miss.append(tid)
    time.sleep(0.15)

json.dump(out, open("/Users/henry/tree-of-life/photo_map.json","w"), indent=1, ensure_ascii=False)
print(f"\nOK: {len(out)}/{len(data)} photos  |  misses: {miss if miss else 'none'}")
