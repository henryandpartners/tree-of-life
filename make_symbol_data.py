#!/usr/bin/env python3
"""Assemble symbol-data.json from verified research + curated metadata.

Source: /tmp/symbols_verified.json  ->  { data: {key: {...}}, verify: {key: {...}} }
Each data entry has: file, desc_page, url, thumb, mime, w, h, license, artist.
"""
import json, re

SRC = json.load(open('/tmp/symbols_verified.json'))
DATA = SRC['data']

def clean_artist(a):
    if not a:
        return ""
    s = re.sub(r'<[^>]+>', '', a)          # strip tags
    s = re.sub(r'No machine-readable author provided\..*', '', s)
    s = re.sub(r'\(based on copyright claims\)', '', s)
    s = re.sub(r'assumed.*', '', s)
    s = s.replace('Unknown author', '').strip()
    return s.strip(' .')

# key -> (name, civ, era, type, location, desc, credit)
M = {
"Tree of life bahir Hebrew.svg": (
  "The Tree of Life (Kabbalah)", "Jewish & Kabbalistic", "Medieval (c. 12th c.)",
  "Diagram", "Kabbalistic tradition",
  "Ten luminous sefirot linked by twenty-two paths, traced to the Zohar and the medieval book Bahir \u2014 the canonical diagram of the Kabbalistic Tree of Life.",
  "Diagram after the Bahir / Zohar; public domain"),

"Kircher Tree of Life": (
  "Kircher's Tree of Life", "Christian (Western)", "1653",
  "Diagram", "Rome, Italy",
  "Athanasius Kircher's engraved Tree of Life from Oedipus Aegyptiacus, fusing the ten sefirot with the Tree of Jesse and Egyptian cosmology into a single allegorical system.",
  "Engraving by Athanasius Kircher, S.J.; public domain"),

"Chartres Jesse Tree": (
  "Tree of Jesse (Chartres Rose)", "Christian (Western)", "c. 1145\u20131155",
  "Architectural", "Chartres, France",
  "The Tree of Jesse from the west-rose window of Chartres Cathedral: Christ at the crown, the patriarchs in the branches, and the kings of Judah in the roots \u2014 a stained-glass genealogy of salvation.",
  "Chartres Cathedral glass; public domain (photo C. H. Moore, 1840\u20131930)"),

"Bernwardst\u00fcr": (
  "Bernward Doors \u2014 Christ on the Tree of Life", "Christian (Western)", "c. 1015",
  "Sculpture", "Hildesheim, Germany",
  "The Bernward Doors, bronze gate of Hildesheim Cathedral: Christ on the Tree of Life, flanked by the Fall in Eden and the Redemption in Gethsemane \u2014 an Ottonian statement of the cross as the tree of life.",
  "Bronze by the workshop of Bernward of Hildesheim; photo \u00a9 Bishop's Press Office Hildesheim, CC BY"),

"Book of Kells ChiRho": (
  "Chi-Rho Page, Book of Kells", "Christian (Western)", "c. 800",
  "Manuscript", "Ireland (Trinity College, Dublin)",
  "The Chi-Rho page of the Book of Kells, the IHS monogram of the Word wrapped in interlaced vines, knots and tendrils \u2014 an Insular gospel book where the living tree becomes woven ornament.",
  "Book of Kells, Irish scribes; public domain"),

"Dore Adam and Eve": (
  "Adam and Eve under the Tree of Life (Dor\u00e9)", "Christian (Western)", "1865\u201366",
  "Painting", "Paris, France",
  "Gustave Dor\u00e9's 'Adam and Eve under the Tree of Life': the serpent on the forbidden tree and the Tree of Life beyond, an engraved illustration from his edition of the Bible.",
  "Wood engraving by Gustave Dor\u00e9; public domain"),

"Ishtar Gate lion": (
  "Ishtar Gate & Processional Way", "Mesopotamian", "c. 575 BCE",
  "Relief", "Babylon (Neo-Babylonian)",
  "The glazed-brick lion procession of the Ishtar Gate of Babylon, where sacred trees and lions line the processional way \u2014 the garden of Marduk rendered in blue brick.",
  "Ishtar Gate, Nebuchadnezzar II; photo \u00a9 0x010C, CC BY-SA 4.0"),

"Stele of the Vultures": (
  "Stele of the Vultures", "Mesopotamian", "c. 2450 BCE",
  "Sculpture", "Lagash (Sumer), now Louvre",
  "The Stele of the Vultures: Gudea of Lagash laying out his temple, with a sacred tree and the vultures of the underworld \u2014 Sumerian royal iconography of the sacred tree.",
  "Stele of Gudea, Louvre; photo \u00a9 Kikuyu3, CC BY-SA 4.0"),

"Thutmose III and tree": (
  "Thutmose III and the Tree of Heaven", "Egyptian", "c. 1425 BCE",
  "Painting", "Tomb of Thutmose III, Valley of the Kings",
  "Thutmose III seated beneath the sycamore (the 'tree of heaven') of Hathor, the goddess of the West \u2014 the Egyptian sacred tree of the afterlife in a Theban tomb painting.",
  "Wall painting, Valley of the Kings; public domain"),

"Buddha Bodhi tree Gandhara": (
  "Buddha beneath the Bodhi Tree", "Buddhist", "2nd c. CE",
  "Sculpture", "Jamal Garhi, Gandhara (Pakistan)",
  "The Buddha beneath the Bodhi tree at Jamal Garhi: the wheel of dharma turning, the tree of awakening that frames the first sermon \u2014 Greco-Buddhist schist sculpture of the Enlightenment.",
  "Gandharan schist, 2nd c. CE; photo \u00a9 SpeakingArch, CC BY-SA 4.0"),

"Penglai scene": (
  "Penglai, the Island of the Immortals", "Chinese", "Tang dynasty (8th c.) tradition",
  "Painting", "China",
  "Penglai, the island of the Immortals rising from the sea, with the peach tree of immortality \u2014 a Tang-dynasty tradition of the celestial tree of eternal life in the far-east seas.",
  "After Li Sixun (Li Po-chun); public domain"),

"Bronze Money Tree Sanxingdui": (
  "Bronze Money Tree (Sanxingdui)", "Chinese", "Han dynasty (206 BCE\u2013220 CE)",
  "Sculpture", "Sanxingdui, Sichuan, China",
  "A bronze Money Tree from the Sanxingdui culture: a three-branched trunk crowned with perched birds, a dragon and jade \u2014 a Han-world axis mundi of wealth and the cosmos.",
  "Bronze, Sanxingdui Museum; photo \u00a9 Gary Todd, CC0"),

"Tikal Ceiba Axis Mundi": (
  "The Ceiba of Tikal (Axis Mundi)", "Maya", "Classic Maya period",
  "Living tree", "Tikal, Guatemala",
  "The great ceiba of Tikal, the Maya world-tree whose roots drink from Xibalba and whose canopy holds the gods \u2014 the living ceiba that the Classic Maya cities grew around.",
  "Ceiba pentandra, Tikal National Park; photo CC0 (Flickr)"),

"Ghashghai Tree of Life carpet": (
  "Ghashghai Carpet \u2014 Tree of Life Medallion", "Persian", "19th c.",
  "Carpet", "Shiraz, Iran",
  "A 19th-century Shiraz (Ghashghai) carpet whose central medallion blooms with the Tree of Life, its branches unfurling pomegranates, roses and vine-scroll \u2014 the Persian carpet's garden of paradise.",
  "Shiraz weavers, 19th c.; photo CC0 (Hiart)"),

"Kermanshah Tree of Life": (
  "Kermanshah Carpet \u2014 Tree of Life", "Persian", "19th c. (late)",
  "Carpet", "Kermanshah, Iran",
  "A late-19th-century Kermanshah carpet: a serpentine Tree of Life flanked by the four paradises, its boughs heavy with fruit \u2014 the Persian garden-of-Paradise rendered in wool and silk.",
  "Kermanshah weavers, 19th c.; public domain"),

"Tane Mahuta": (
  "T\u0101ne Mahuta, the Great Kauri", "M\u0101ori / Pacific", "Living (c. 1,500\u20132,000 yrs)",
  "Living tree", "Waipoua Forest, New Zealand",
  "T\u0101ne Mahuta, the great kauri of the Waipoua Forest, the 'Guardian of the Forest' \u2014 one of the largest and oldest living trees on Earth, a M\u0101ori taonga (treasure) of the world-tree.",
  "Kauri (Agathis australis), Waipoua Forest; photo CC BY 2.0 (Flickr)"),

"Ash Yggdrasil Heine": (
  "Yggdrasil (Heine)", "Norse", "1886",
  "Painting", "Oslo, Norway",
  "F. W. Heine's 'Yggdrasil': the great ash of the Norse cosmos, its branches over the nine worlds, with the dragon N\u00eddho\u0141gn gnawing the roots \u2014 a 19th-century romantic revival of the world-tree.",
  "Oil by Friedrich Wilhelm Heine; public domain"),

"Yggdrasil Mundane Tree 1847": (
  "Yggdrasil (Mundane Tree, Bagge)", "Norse", "1847",
  "Painting", "Denmark",
  "Oluf Bagge's 'Mundane Tree' (Yggdrasil): the ash of the Norse world, the eagle on its crown and the serpent in its roots \u2014 a mid-19th-century depiction of the nine-world axis.",
  "Oil by Oluf Bagge; public domain"),

"Bayon Face Tower": (
  "Face-Towers of the Bayon", "Khmer", "12th c.",
  "Architectural", "Angkor, Cambodia",
  "The face-towers of the Bayon at Angkor, whose serene stone faces look out over the world-tree of the Khmer cosmos \u2014 the temple-mountain of Avalokiteshvara as a cosmic tree.",
  "Bayon temple, Angkor; photo \u00a9 Arabsalam, CC BY-SA 3.0"),

"Monreale St Agatha mosaic": (
  "St Agatha & the Tree of Life (Monreale)", "Christian (Western)", "12th\u201313th c.",
  "Mosaic", "Monreale, Sicily",
  "Saint Agatha enthroned beneath a Tree of Life in the apse mosaic of the Cathedral of Monreale, the Norman-Byzantine gold ground of paradise.",
  "Apse mosaic, Monreale Cathedral; photo \u00a9 Jos\u00e9 Luiz, CC BY-SA 4.0"),

"Monreale St Lawrence mosaic": (
  "St Lawrence & the Tree of Life (Monreale)", "Christian (Western)", "12th\u201313th c.",
  "Mosaic", "Monreale, Sicily",
  "Saint Lawrence and the Tree of Life in the Monreale apse mosaic, a golden garden of paradise set in the Norman-Byzantine gold ground.",
  "Apse mosaic, Monreale Cathedral; public domain"),
}

def img_url(e):
    # prefer a bounded thumb when available & large enough, else the full url
    t = e.get('thumb') or ''
    u = e.get('url') or ''
    return t if t else u

order = list(M.keys())
missing = [k for k in order if k not in DATA]
if missing:
    raise SystemExit(f"keys not in data: {missing}")

out = []
for key in order:
    e = DATA[key]
    name, civ, era, typ, loc, desc, credit = M[key]
    out.append({
        "id": key,
        "name": name,
        "civ": civ,
        "era": era,
        "type": typ,
        "location": loc,
        "desc": desc,
        "credit": credit,
        "license": e["license"],
        "artist": clean_artist(e.get("artist","")),
        "img": img_url(e),
        "full": e.get("url"),
        "source": e.get("desc_page"),
        "w": e.get("w"), "h": e.get("h"),
    })

dst = '/Users/henry/tree-of-life/symbol-data.json'
json.dump(out, open(dst,'w'), ensure_ascii=False, indent=1)
civs = sorted({o['civ'] for o in out})
types = sorted({o['type'] for o in out})
lics = sorted({o['license'] for o in out})
print(f"OK {len(out)} symbols -> {dst}")
print(f"civs({len(civs)}): {civs}")
print(f"types({len(types)}): {types}")
print(f"licenses: {lics}")
print("missing img/desc:", [o['id'] for o in out if not o['img'] or not o['desc']] or "none")
