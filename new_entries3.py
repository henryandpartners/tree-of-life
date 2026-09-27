#!/usr/bin/env python3
"""Batch 3 of curated Tree of Life entries — focus: painting, sculpture, artifact & more.
key -> dict(query, name, civ, era, type, location, desc, credit)"""

E3 = {

# ─── Roman ──────────────────────────────────────────────────────
"Villa of Livia fresco": dict(
  query="Villa of Livia garden fresco Prima Porta",
  name="The Garden Room — Villa of Livia",
  civ="Roman", era="c. 30–20 BCE", type="Painting",
  location="Prima Porta, Rome (now Palazzo Massimo)",
  desc="The painted garden of Livia's villa — walls dissolved into a birdsong paradise of laurels, pomegranates and cypresses, an eternal spring grown indoors for an empress.",
  credit="Roman fresco, Palazzo Massimo alle Terme; photo public domain / CC"),

# ─── Mesopotamian (painting) ────────────────────────────────────
"Investiture of Zimri-Lim": dict(
  query="Investiture of Zimri-Lim mural Mari",
  name="The Investiture of Zimri-Lim",
  civ="Mesopotamian", era="c. 1780 BCE", type="Painting",
  location="Royal Palace of Mari, Syria (now Louvre)",
  desc="The wall-painting of King Zimri-Lim and Ishtar beneath date palms and flowing vases — the Mesopotamian sacred tree granting legitimacy to the throne of Mari.",
  credit="Old Babylonian mural, Louvre; photo public domain / CC"),

# ─── Modern painting ────────────────────────────────────────────
"Van Gogh mulberry": dict(
  query="Van Gogh mulberry tree painting",
  name="The Mulberry Tree (Van Gogh)",
  civ="Modern", era="1889", type="Painting",
  location="Saint-Rémy-de-Provence (now Norton Simon Museum)",
  desc="Van Gogh's mulberry in the asylum garden at Saint-Rémy — a single tree burning gold against the blue, roots gripping the rock of a world the painter could not keep.",
  credit="Vincent van Gogh, 1889; public domain"),
"Mondrian tree": dict(
  query="Piet Mondrian tree painting",
  name="The Gray Tree (Mondrian)",
  civ="Modern", era="1911", type="Painting",
  location="Netherlands",
  desc="Mondrian's early tree — branches dissolving into cubist lattice, the world-tree abstracting toward the vertical and horizontal, a theosophist's Tree of Life losing its leaves to geometry.",
  credit="Piet Mondrian; public domain"),

# ─── East Asian painting ────────────────────────────────────────
"Korin plum screens": dict(
  query="Ogata Korin red white plum screens",
  name="Red and White Plum Trees (Kōrin)",
  civ="Japanese", era="c. 1710–16", type="Painting",
  location="Edo Japan (now MOA Museum)",
  desc="Ogata Kōrin's paired plum trees — one austere white, one blooming crimson — across a golden river: the Rinpa master's flat, luminous world-tree in gold leaf and tarashikomi.",
  credit="Ogata Kōrin, folding screen; public domain"),
"Guo Xi old trees": dict(
  query="Guo Xi Old Trees Level Distance",
  name="Old Trees, Level Distance (Guo Xi)",
  civ="Chinese", era="Song dynasty (11th c.)", type="Painting",
  location="China (now Metropolitan Museum of Art)",
  desc="Guo Xi's ink scroll of ancient trees receding into mist — the literati cosmology in which gnarled pines are elders, mist is breath, and distance itself is a spiritual exercise.",
  credit="Guo Xi, handscroll, Metropolitan Museum of Art; public domain"),

# ─── Arts & Crafts / Modern textile & glass ─────────────────────
"Morris tree of life": dict(
  query="Tree of Life tapestry Morris",
  name="Tree of Life Tapestry (Morris & Co.)",
  civ="Modern", era="c. 1885–1915", type="Textile",
  location="England (Merton Abbey)",
  desc="The Arts and Crafts Tree of Life — William Morris's medievalist vine, coiling acanthus and fruiting boughs woven at Merton Abbey, sacred nature redeemed by the hand of the craftsman.",
  credit="Morris & Co. design; photo public domain / CC"),
"Tiffany tree window": dict(
  query="Tiffany tree of life window stained glass",
  name="Tree of Life Window (Tiffany Studios)",
  civ="Modern", era="c. 1900", type="Glass",
  location="New York",
  desc="The Tiffany Studios Tree of Life — a symmetrical vine in opalescent glass, roots and crown mirroring in leaded light, the American Gothic window become a luminous world-axis.",
  credit="Tiffany Studios, leaded glass; photo public domain / CC"),

# ─── Indian textile ─────────────────────────────────────────────
"Palampore": dict(
  query="Palampore tree of life cotton",
  name="Palampore — the Coromandel Tree of Life",
  civ="Hindu (Indian)", era="18th c.", type="Textile",
  location="Coromandel Coast, India (for export)",
  desc="The palampore — a chintz tree of life drawn and dyed on the Coromandel Coast for the world's beds and altars: one flowering stem rooted in a mound, branching into peacocks, moths and lotus.",
  credit="Indian chintz, mordant-dyed cotton; photo public domain / CC"),

# ─── Mexican folk ───────────────────────────────────────────────
"Arbol de la vida": dict(
  query="arbol de la vida pottery Metepec",
  name="Árbol de la Vida — Tree of Life Candelabra",
  civ="Mexican (Folk)", era="Living tradition", type="Ceramic",
  location="Metepec & Izúcar de Matamoros, Mexico",
  desc="The Metepec tree of life — a clay candelabra flowering with Adam and Eve, mermaids, cactus and doves, the Tree of Eden retold in Talavera color by generations of Mexican family workshops.",
  credit="Mexican folk pottery; photo public domain / CC"),

# ─── Indus Valley ───────────────────────────────────────────────
"Indus pipal seal": dict(
  query="Indus Valley seal pipal tree",
  name="Pipal Tree Seal of the Indus",
  civ="Indus (Harappan)", era="c. 2600–1900 BCE", type="Artifact",
  location="Mohenjo-daro / Harappa",
  desc="The unicorn and pipal seals of Harappa — a leaf-veined ficus religiosa standing on a platform above worshippers, the oldest script-less testament to a sacred tree, four thousand years old.",
  credit="Indus Valley steatite seal; photo public domain / CC"),

# ─── Egyptian artifact ──────────────────────────────────────────
"Djed pillar": dict(
  query="djed pillar amulet Osiris",
  name="The Djed Pillar — Backbone of Osiris",
  civ="Egyptian", era="Old Kingdom onward", type="Artifact",
  location="Egypt",
  desc="The djed pillar — four crossbars like a lopped trunk, the backbone of Osiris and the tree-stump of the buried god, raised at the Sed festival to steady the axis of the world.",
  credit="Egyptian amulet / relief; photo public domain / CC"),

# ─── Norse relief ───────────────────────────────────────────────
"Ardre stone": dict(
  query="Ardre image stone Gotland",
  name="The Ardre Image Stone",
  civ="Norse", era="8th–10th c.", type="Relief",
  location="Ardre, Gotland, Sweden",
  desc="The carved slabs of Gotland — Odin, Thor fishing the serpent, and a rider beneath the arch of the world-tree: Viking cosmology chiseled into limestone flagstones that raised the dead.",
  credit="Viking picture stone, Gotland; photo public domain / CC"),

# ─── Levantine living trees ─────────────────────────────────────
"Cedars of God": dict(
  query="Cedars of God Bsharri",
  name="The Cedars of God — Horsh Arz el-Rab",
  civ="Levantine", era="Living (groves 3,000+ yrs)", type="Living tree",
  location="Bsharri, Mount Lebanon",
  desc="The Cedars of God — the last ancient grove of the Lebanon cedar, timber of Solomon's temple and Gilgamesh's forbidden forest, a thousand survivors standing in their own sanctuary.",
  credit="Cedrus libani; photo public domain / CC"),
"Olives of Gethsemane": dict(
  query="Gethsemane ancient olive trees",
  name="The Olives of Gethsemane",
  civ="Christian (Western)", era="Living (root systems ~2,000 yrs)", type="Living tree",
  location="Mount of Olives, Jerusalem",
  desc="The eight gnarled olives of Gethsemane — scientifically dated to the era of Christ, their roots older than their trunks, witnesses at the foot of the Mount of Olives.",
  credit="Olea europaea, Jerusalem; photo public domain / CC"),
"Vouves olive": dict(
  query="Vouves ancient olive tree Crete",
  name="The Olive Tree of Vouves",
  civ="Greek", era="Living (2,000–4,000 yrs)", type="Living tree",
  location="Ano Vouves, Crete, Greece",
  desc="The Monumental Olive of Vouves — a Minoan-era tree still bearing fruit, its hollow trunk a cathedral of grain, the great mother of the Mediterranean's oil-giving tree of life.",
  credit="Olea europaea, Crete; photo public domain / CC"),

# ─── Mughal garden ──────────────────────────────────────────────
"Shalimar Bagh": dict(
  query="Shalimar Bagh Srinagar garden",
  name="Shalimar Bagh — the Mughal Paradise",
  civ="Islamic", era="Mughal (1619)", type="Garden",
  location="Srinagar, Kashmir",
  desc="Jahangir's Shalimar Bagh — terraces of chinar and water falling through marble pavilions along Dal Lake, the Persian chahār bāgh rebuilt in Kashmir as a Quranic garden for an empress.",
  credit="Mughal garden, Srinagar; photo public domain / CC"),

# ─── Native American sculpture ──────────────────────────────────
"Totem pole": dict(
  query="totem pole Pacific Northwest",
  name="The Totem Pole — Cedar Column",
  civ="Native American", era="18th c.–living tradition", type="Sculpture",
  location="Pacific Northwest coast",
  desc="The totem pole — a western red cedar carved with raven, bear and thunderbird rising crest above crest, the coast peoples' genealogy raised as a living column between earth and sky.",
  credit="Pacific Northwest carved cedar; photo public domain / CC"),
}

if __name__ == "__main__":
    print(len(E3), "entries batch 3")
