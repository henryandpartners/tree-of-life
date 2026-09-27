"""Fetch one representative photo per sacred tree via the REST summary API.

data.json has no wiki-title field; the species lives in the `tree` description.
We try a curated list of candidate Wikipedia titles per tree (scientific name
first, then common name, then a generic fallback) and keep the first that
returns an image. 500px thumbnails are preferred (largest reliably-allowed
size), verified with HEAD, falling back to the REST 330px thumbnail.

Writes photo_map.json: {id: {url, source, label, title}}.
"""
import json, time, urllib.request, urllib.parse

UA = {"User-Agent": "tree-of-life-site/1.0 (sacred-tree reference site; contact: henryandpartners)"}
REST = "https://en.wikipedia.org/api/rest_v1/page/summary/"
RASTER = (".jpg", ".jpeg", ".png", ".webp")

# Candidate Wikipedia titles per tree id, in priority order.
CAND = {
 "garden-eden":        ["Ficus carica", "Fig", "Garden of Eden"],
 "gilgamesh-tree":     ["Cedrus", "Cedar"],
 "sumerian-sacred-tree":["Phoenix dactylifera", "Date palm"],
 "egypt-sycamore":     ["Ficus sycomorus", "Sycamore fig"],
 "egypt-ba-tree":      ["Cedrus", "Cedar"],
 "persian-ashoka":     ["Saraca", "Ashoka (plant)", "Sapindus emarginatus"],
 "persian-haoma":      ["Ephedra", "Haoma"],
 "yggdrasil":          ["Fraxinus excelsior", "Fraxinus", "Ash (tree)"],
 "celtic-oak-dagda":   ["Quercus", "Oak"],
 "slavic-world-tree":  ["Quercus", "Oak"],
 "greek-hesperides":   ["Malus domestica", "Apple"],
 "greek-olive-athena": ["Olea europaea", "Olive"],
 "greek-dodona-oak":   ["Quercus", "Oak"],
 "kalpavriksha":       ["Ficus benghalensis", "Banyan"],
 "bodhi-tree":         ["Ficus religiosa", "Bodhi tree", "Peepal"],
 "ashvattha-gita":     ["Ficus religiosa", "Bodhi tree"],
 "ashoka-indian":      ["Saraca", "Sapindus emarginatus", "Ashoka (plant)"],
 "tala-nirvana":       ["Borassus flabellifer", "Bell palm"],
 "pippal-banyan":      ["Ficus benghalensis", "Banyan"],
 "mango-hindu":        ["Mangifera indica", "Mango"],
 "soma-vedic":         ["Ephedra", "Soma (plant)"],
 "xiwangmu-peach":     ["Prunus persica", "Peach"],
 "jing-tree":          ["Cinnamomum camphora", "Camphor tree", "Tree of life"],
 "jade-tree":          ["Pachira aquatica", "Jade plant", "Tree of life"],
 "penglai":            ["Prunus persica", "Peach", "Tree of life"],
 "sun-god-nagi":       ["Machilus", "Nagi tree", "Laurus nobilis"],
 "isonokami-fig":      ["Ficus", "Sacred fig", "Strangler fig"],
 "dado-world-tree":    ["Eucalyptus", "Tree of life", "Tree"],
 "champa-samye":       ["Michelia champaca", "Champa (flower)", "Magnolia"],
 "mongol-ukhai":       ["Populus", "Poplar", "Elm"],
 "ryukyu-kuyaa":       ["Cinnamomum camphora", "Camphor tree", "Ficus"],
 "vietnam-banyan":     ["Ficus microcarpa", "Banyan", "Strangler fig"],
 "philippines-bamboo": ["Bamboo", "Bambusoideae"],
 "thai-phi-tree":      ["Ficus benghalensis", "Banyan", "Mangifera indica"],
 "angkor-banyan":      ["Ficus benghalensis", "Strangler fig", "Banyan"],
 "kaum-kaet":          ["Eucalyptus", "Tree of life", "Tree"],
 "dayak-world-tree":   ["Dipterocarpus", "Shorea", "Rainforest"],
 "javanese-kerasukan": ["Ficus", "Banyan", "Terminalia"],
 "balinese-grove":     ["Areca catechu", "Banyan", "Ficus"],
 "myanmar-nat":        ["Dipterocarpus", "Shorea", "Ficus religiosa"],
 "aztec-ometl":        ["Ceiba pentandra", "Ceiba", "Kapok"],
 "maya-witz":          ["Ceiba pentandra", "Ceiba", "Kapok"],
 "kiche-world-tree":   ["Ceiba pentandra", "Ceiba", "Kapok"],
 "aztec-amate":        ["Ficus cotinifolia", "Amate", "Ficus"],
 "tree-of-peace":      ["Pinus strobus", "Eastern white-pine", "White pine"],
 "lakota-sacred-tree": ["Quercus", "Oak", "Tree of life"],
 "nw-coast-cedar":     ["Thuja plicata", "Western red cedar", "Cedar"],
 "inca-huaca":         ["Polylepis", "Queñua", "Andean mountain"],
 "mapuche-pehuen":     ["Araucaria araucana", "Monkey puzzle"],
 "maori-whakapapa":    ["Metrosideros excelsa", "Metrosideros", "Pohutukawa"],
 "hawaiian-koa":       ["Acacia koa", "Koa"],
 "hawaiian-lehua":     ["Meliosma", "Meliosma rugosa", "Lobelia"],
 "aboriginal-dreaming":["Eucalyptus", "Ironbark", "Acacia"],
 "baobab":             ["Adansonia digitata", "Baobab"],
 "yoruba-iroko":       ["Milicia excelsa", "Iroko", "African teak"],
 "yoruba-egbesu":      ["Adansonia", "Daniellia", "Baobab"],
 "dogon-tree":         ["Acacia", "Savanna", "Tree of life"],
}

def head_ok(url):
    req = urllib.request.Request(url, headers=UA, method="HEAD")
    try:
        return urllib.request.urlopen(req, timeout=25).status == 200
    except Exception:
        return False

def build_thumb(orig, w=500):
    base = orig.split("?")[0]
    if not base.lower().endswith(RASTER):
        return None
    i = base.index("commons/")
    pre, rest = base[:i] + "commons/thumb/", base[i + 8:]
    return pre + rest + f"/{w}px-" + rest.split("/")[-1]

def summary(title):
    t = urllib.parse.quote(title, safe="")
    for _ in range(3):
        try:
            return json.loads(urllib.request.urlopen(urllib.request.Request(REST + t, headers=UA), timeout=30).read().decode())
        except Exception:
            time.sleep(2)
    return None

def fetch_id(tid):
    for title in CAND.get(tid, ["Tree"]):
        d = summary(title)
        if not d:
            continue
        orig = (d.get("originalimage") or {}).get("source")
        thumb = (d.get("thumbnail") or {}).get("source")
        if not orig and not thumb:
            continue
        label = d.get("title", title)
        if orig:
            t500 = build_thumb(orig)
            if t500 and head_ok(t500):
                return {"url": t500, "source": "wikipedia", "label": label, "title": title}
        if thumb:
            return {"url": thumb.split("?")[0], "source": "wikipedia", "label": label, "title": title}
        if orig:
            return {"url": orig.split("?")[0], "source": "wikipedia", "label": label, "title": title}
    return None

def main():
    data = json.load(open("/Users/henry/tree-of-life/data.json"))
    ids = [t["id"] for t in data]
    out, miss = {}, []
    for tid in ids:
        im = fetch_id(tid)
        if im:
            out[tid] = im
            print(f"  ok  {tid:24} <- {im['title']}")
        else:
            miss.append(tid)
            print(f"  --  {tid:24} NO IMAGE")
        time.sleep(0.5)
    json.dump(out, open("/Users/henry/tree-of-life/photo_map.json", "w"), indent=1, ensure_ascii=False)
    print(f"\nOK: {len(out)}/{len(ids)}  |  missing: {miss if miss else 'none'}")

if __name__ == "__main__":
    main()
