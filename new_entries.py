#!/usr/bin/env python3
"""Curated expansion entries for the Symbols & Art database.
key -> dict(query=Commons search query, name, civ, era, type, location, desc, credit)
Image URLs/licenses/dimensions are resolved by fetch_new_symbols.py.
"""

E = {

# ─── Mesopotamian ───────────────────────────────────────────────
"Assyrian sacred tree relief": dict(
  query="Ashurnasirpal sacred tree relief Nimrud",
  name="Sacred Tree & Winged Genii (Nimrud)",
  civ="Mesopotamian", era="c. 865–860 BCE", type="Relief",
  location="Northwest Palace, Nimrud (Assyria)",
  desc="The Assyrian sacred tree flanked by winged genii with pollen cones, from Ashurnasirpal II's Northwest Palace — the palm-like world-axis at the heart of Assyrian royal ideology.",
  credit="Alabaster relief, Nimrud; photo public domain / CC"),
"Akkadian sacred tree seal": dict(
  query="cylinder seal sacred tree Mesopotamian",
  name="Cylinder Seal with the Sacred Tree",
  civ="Mesopotamian", era="Akkadian (c. 2250 BCE)", type="Seal",
  location="Mesopotamia",
  desc="A Mesopotamian cylinder seal cut with the sacred tree between gods and beasts — the garden of the gods worn on the wrist, rolled into eternity across clay.",
  credit="Cylinder seal impression; photo public domain / CC"),
"Warka Vase": dict(
  query="Warka Vase",
  name="Warka Vase",
  civ="Mesopotamian", era="c. 3000 BCE", type="Relief",
  location="Uruk (now Iraq Museum, Baghdad)",
  desc="The Warka Vase of Uruk: registers of water, grain, sheep and worshippers rising to the goddess Inanna — the oldest carved narrative of the land's abundance climbing like a tree toward heaven.",
  credit="Uruk ritual vase, Iraq Museum; photo public domain / CC"),
"Etana seal": dict(
  query="Etana seal eagle",
  name="Etana and the Eagle",
  civ="Mesopotamian", era="Old Babylonian (c. 1800 BCE)", type="Seal",
  location="Mesopotamia",
  desc="The shepherd-king Etana carried heavenward on the eagle's back to fetch the plant of birth — the Mesopotamian ascent myth, stamped in miniature on a cylinder seal.",
  credit="Cylinder seal impression; photo public domain / CC"),

# ─── Egyptian ───────────────────────────────────────────────────
"Sennedjem tree goddess": dict(
  query="TT1 Deir el-Medina Sennedjem",
  name="The Tree Goddess (Tomb of Sennedjem)",
  civ="Egyptian", era="19th dynasty (c. 1250 BCE)", type="Painting",
  location="Deir el-Medina, Thebes",
  desc="The goddess Nut pouring water from the sycamore in the tomb of Sennedjem — the tree-goddess who quenches the souls of the dead at the edge of the western desert.",
  credit="Wall painting, Deir el-Medina; photo public domain / CC"),
"Osiris bed": dict(
  query="Osiris bed",
  name="Osiris Bed",
  civ="Egyptian", era="Late period (c. 600 BCE)", type="Sculpture",
  location="Egypt (various museums)",
  desc="The Osiris bed: a wooden frame sown with grain that sprouts in the dark in the shape of the risen god — the Egyptian tree of death-and-return, greenness itself resurrected.",
  credit="Funerary object; photo public domain / CC"),

# ─── Jewish & Kabbalistic ───────────────────────────────────────
"Titus menorah": dict(
  query="Arch of Titus menorah",
  name="Menorah of Titus' Arch",
  civ="Jewish & Kabbalistic", era="c. 81 CE", type="Relief",
  location="Rome, Italy",
  desc="The seven-branched menorah carved on the Arch of Titus, carried from the burning Temple of Jerusalem — the menorah as the Tree of Life in exile, its branches remembered in stone.",
  credit="Marble relief, Rome; photo public domain / CC"),

# ─── Christian ──────────────────────────────────────────────────
"San Clemente apse mosaic": dict(
  query="San Clemente apse mosaic",
  name="Tree of Life — San Clemente Apse",
  civ="Christian (Western)", era="c. 1125–1130", type="Mosaic",
  location="Rome, Italy",
  desc="The apse mosaic of San Clemente in Rome: the crucified Christ rises as a vast acanthus Tree of Life, its coils filling heaven with deer, peacocks, shepherds and saints.",
  credit="Apse mosaic, Basilica San Clemente; photo public domain / CC"),
"Otranto tree mosaic": dict(
  query="Otranto Cathedral nave mosaic",
  name="The Tree of Life — Otranto Floor",
  civ="Christian (Western)", era="1163–1165", type="Mosaic",
  location="Otranto, Italy",
  desc="The vast 12th-century mosaic floor of Otranto Cathedral: the Tree of Life running the whole nave's length, threaded with Alexander, Arthur, Adam and the beasts of every age.",
  credit="Mosaic floor, Otranto Cathedral; photo public domain / CC"),
"Jesse window Saint-Denis": dict(
  query="Tree of Jesse stained glass Saint-Denis",
  name="Tree of Jesse Window (Saint-Denis)",
  civ="Christian (Western)", era="c. 1144", type="Glass",
  location="Basilica of Saint-Denis, France",
  desc="The Tree of Jesse window of Suger's Saint-Denis — the ancestor-tree of Christ bursting into glass and light, the origin of Gothic stained glass itself.",
  credit="Stained glass, Saint-Denis; photo public domain / CC"),
"Green Man carving": dict(
  query="Green Man carving church",
  name="The Green Man",
  civ="Christian (Western)", era="Medieval (12th–15th c.)", type="Sculpture",
  location="Across Europe's churches",
  desc="The Green Man — the foliate face whose mouth pours vines, carved in a thousand churches — the old arboreal spirit folded into the margins of Christian stone.",
  credit="Medieval carving; photo public domain / CC"),

# ─── Islamic ────────────────────────────────────────────────────
"Mshatta facade": dict(
  query="Mshatta facade",
  name="Mshatta Facade",
  civ="Islamic", era="Umayyad (c. 740)", type="Architectural",
  location="Qasr al-Mshatta, Jordan (now Pergamon Museum, Berlin)",
  desc="The Mshatta facade: a mile of carved vines on the desert palace wall — the endless tree of life of Umayyad stonemasons, animals dissolving into its scroll.",
  credit="Carved facade, Pergamon Museum; photo public domain / CC"),
"Isfahan tree of life tile": dict(
  query=" haft rang tilework Isfahan Shah",
  name="Tree of Life Tilework",
  civ="Islamic", era="Safavid (16th–17th c.)", type="Ceramic",
  location="Isfahan, Iran",
  desc="Safavid tilework trees — cypresses bending with birds in lapis and turquoise — the Persian garden of paradise fired onto the walls of Isfahan.",
  credit="Ceramic tile, Iran; photo public domain / CC"),
"Safavid tree of life silk": dict(
  query="Safavid silk textile tree of life",
  name="Tree of Life Silk (Safavid)",
  civ="Islamic", era="16th–17th c.", type="Textile",
  location="Iran (now in museum collections)",
  desc="A Safavid silk woven with the Tree of Life — hunters, simurghs and blossoming branches — paradise textile carried along the silk roads as diplomatic gold.",
  credit="Woven silk, Safavid; photo public domain / CC"),
"Ottoman tree of life textile": dict(
  query="Ottoman textile tree of life",
  name="Ottoman Tree of Life Textile",
  civ="Islamic", era="Ottoman (16th–18th c.)", type="Textile",
  location="Istanbul, Turkey",
  desc="Ottoman court weavers' Tree of Life — carnations, tulips and cypresses rising in silk and metal thread — the imperial garden of eternity.",
  credit="Woven textile, Ottoman; photo public domain / CC"),

# ─── Persian (Sasanian & miniature) ─────────────────────────────
"Senmurv silk": dict(
  query="Sasanian silk senmurv",
  name="Senmurv Silk",
  civ="Persian", era="Sasanian (c. 600–700)", type="Textile",
  location="Sasanian Iran",
  desc="The Sasanian silk with the senmurv — the dog-bird of the tree — circling the pearl-bordered Tree of Life, the royal emblem of a cosmic garden.",
  credit="Woven silk, Sasanian; photo public domain / CC"),
"Pasargadae garden": dict(
  query="Pasargadae",
  name="The Garden of Pasargadae",
  civ="Persian", era="Achaemenid (c. 550 BCE)", type="Garden",
  location="Pasargadae, Iran",
  desc="Cyrus' garden at Pasargadae — the original chahar bagh, four rivers watering a planted paradise — the world's first designed garden as a tree of life in plan.",
  credit="Archaeological site, Iran; photo public domain / CC"),
"Persian garden miniature": dict(
  query="Persian miniature garden painting",
  name="The Enclosed Garden (Persian Miniature)",
  civ="Persian", era="Timurid (15th c.)", type="Painting",
  location="Herat / Tabriz",
  desc="A Timurid miniature of the enclosed garden — blossoming trees, watercourses and lovers — paradise painted as the Persians imagined the soul's destination.",
  credit="Manuscript painting; photo public domain / CC"),

# ─── Hindu / Indian ─────────────────────────────────────────────
"Kalpavriksha painting": dict(
  query="Kalpavriksha painting",
  name="Kalpavriksha — the Wishing Tree",
  civ="Hindu (Indian)", era="Traditional", type="Painting",
  location="India",
  desc="Kalpavriksha, the wish-fulfilling tree of Hindu and Jain cosmology — rooted in the churning of the milk ocean, granting every desire that reaches its shade.",
  credit="Indian painting; photo public domain / CC"),
"Great Banyan": dict(
  query="Great Banyan tree Howrah",
  name="The Great Banyan of Howrah",
  civ="Hindu (Indian)", era="Living (250+ yrs)", type="Living tree",
  location="Botanical Garden, Howrah, India",
  desc="The Great Banyan of the Calcutta garden — a single tree become a forest, dropping aerial roots until it covers a quarter-hectare grove — the banyan as immortal tree-of-life made fact.",
  credit="Ficus benghalensis, Acharya Jagadish Chandra Bose garden; photo CC"),
"Mughal tree of life carpet": dict(
  query="Mughal carpet tree of life",
  name="Mughal Tree of Life Carpet",
  civ="Islamic", era="Mughal (17th c.)", type="Carpet",
  location="Lahore / Agra",
  desc="A Mughal carpet flowering with the Tree of Life — flowering plants naturalized with botanist's eyes, the Persian tree re-planted in the gardens of the Great Mughals.",
  credit="Woven carpet, Mughal; photo public domain / CC"),

# ─── Buddhist / SE Asian ────────────────────────────────────────
"Mahabodhi Temple": dict(
  query="Mahabodhi Temple",
  name="Mahabodhi Temple",
  civ="Buddhist", era="c. 260 BCE / 5th c. CE", type="Architectural",
  location="Bodh Gaya, India",
  desc="The Mahabodhi temple at Bodh Gaya, raised beside the very seat of the Buddha's awakening — the descendants of the original Bodhi tree still shading pilgrims after 2,300 years.",
  credit="Brick temple, Bodh Gaya; photo public domain / CC"),
"Sanchi bodhi worship": dict(
  query="Sanchi torana",
  name="Bodhi Tree Worship (Sanchi)",
  civ="Buddhist", era="c. 100 BCE", type="Relief",
  location="Sanchi, India",
  desc="The aniconic Buddha as the Bodhi tree itself on Sanchi's gateways — worshippers kneeling before an empty throne beneath the leaves, the tree as the Enlightened One.",
  credit="Stone torana relief, Sanchi; photo public domain / CC"),
"Bharhut bodhi": dict(
  query="Bharhut bodhi tree",
  name="Bodhi Tree of Bharhut",
  civ="Buddhist", era="c. 150 BCE", type="Relief",
  location="Bharhut, India (now Indian Museum, Kolkata)",
  desc="The Bharhut railing carved with the Bodhi tree of Bodh Gaya, worshipped by kings and nagas — the earliest surviving sculpture of the tree of awakening.",
  credit="Stone relief, Indian Museum Kolkata; photo public domain / CC"),
"Sri Maha Bodhi": dict(
  query="Jaya Sri Maha Bodhi Anuradhapura",
  name="Jaya Sri Maha Bodhi",
  civ="Buddhist", era="Living (planted 288 BCE)", type="Living tree",
  location="Anuradhapura, Sri Lanka",
  desc="The Jaya Sri Maha Bodhi of Anuradhapura — a sapling of the Buddha's own tree, carried by the nun Sanghamitta — the oldest documented living human-planted tree on Earth.",
  credit="Ficus religiosa, Anuradhapura; photo CC"),
"Borobudur": dict(
  query="Borobudur",
  name="Borobudur",
  civ="Buddhist", era="c. 800–825", type="Architectural",
  location="Central Java, Indonesia",
  desc="Borobudur — the great Javanese stupa as a carved stone mountain, its galleries circling toward emptiness like a walker circling the world-tree to its crown.",
  credit="Borobudur temple; photo public domain / CC"),
"Ta Prohm trees": dict(
  query="Ta Prohm trees",
  name="The Trees of Ta Prohm",
  civ="Buddhist", era="12th c. (ruin)", type="Living tree",
  location="Angkor, Cambodia",
  desc="The strangler figs and silk-cotton trees of Ta Prohm, swallowing the Khmer monastery root by root — the jungle's own tree of life repossessing the temple of the Buddha.",
  credit="Tetrameles nudiflora, Angkor; photo public domain / CC"),

# ─── Chinese ────────────────────────────────────────────────────
"Xiwangmu painting": dict(
  query="Xiwangmu",
  name="Xiwangmu, Queen Mother of the West",
  civ="Chinese", era="Han–Tang tradition", type="Painting",
  location="China",
  desc="Xiwangmu in her western paradise beneath the peach tree of immortality, guarded by the moon-hare and the nine-tailed fox — the Taoist goddess of the immortal orchard.",
  credit="Chinese painting; photo public domain / CC"),

# ─── Japanese ───────────────────────────────────────────────────
"Jomon Sugi": dict(
  query="Jomon Sugi Yakushima",
  name="Jōmon Sugi",
  civ="Japanese", era="Living (2,000–7,000 yrs)", type="Living tree",
  location="Yakushima, Japan",
  desc="Jōmon Sugi, the primeval cedar of Yakushima's moss-forest — a tree old beyond record, sacred to Shintō since before Japan had a name.",
  credit="Cryptomeria japonica, Yakushima; photo CC"),
"Shimenawa sacred tree": dict(
  query="shimenawa sacred tree shrine",
  name="Shinboku — the Rope-Bound Tree",
  civ="Japanese", era="Shintō tradition", type="Living tree",
  location="Japan",
  desc="A shinboku, the sacred tree of a Shintō shrine, bound with the rice-straw rope of the kami — the living tree itself as the body of the god.",
  credit="Sacred tree with shimenawa; photo CC"),

# ─── Greek ──────────────────────────────────────────────────────
"Garden of the Hesperides": dict(
  query="Hesperides hydria",
  name="The Garden of the Hesperides",
  civ="Greek", era="c. 400 BCE", type="Pottery",
  location="Athens / Greek world",
  desc="The Hesperides among their golden apples on the tree Ladon guards at the world's western edge — the Greek tree of immortal life, Herakles' eleventh labor.",
  credit="Greek vase painting; photo public domain / CC"),
"Erechtheion sacred olive": dict(
  query="Erechtheion Athens",
  name="The Sacred Olive of Athena",
  civ="Greek", era="421–406 BCE", type="Architectural",
  location="Acropolis, Athens",
  desc="The Erechtheion, sheltering the mark of Poseidon's trident and Athena's sacred olive — the goddess' gift of the tree that made Athens, replanted after the Persians burned it and sprouting again.",
  credit="Temple, Acropolis; photo public domain / CC"),
"Dodona sacred oak": dict(
  query="Dodona Zeus oracle",
  name="The Sacred Oak of Dodona",
  civ="Greek", era="Sanctuary from c. 2000 BCE", type="Site",
  location="Epirus, Greece",
  desc="The oak of Zeus at Dodona, where the god spoke in the rustling leaves and priestesses read the wind — Greece's oldest oracle, a tree that answered.",
  credit="Sanctuary of Dodona; photo public domain / CC"),

# ─── Mesoamerican ───────────────────────────────────────────────
"Pakal sarcophagus lid": dict(
  query="K'inich Janaab' Pakal sarcophagus",
  name="Pakal's Sarcophagus Lid",
  civ="Maya", era="683 CE", type="Sculpture",
  location="Temple of the Inscriptions, Palenque",
  desc="Pakal the Great falling down the World Tree to Xibalba and rising as the maize god — the Maya axis mundi carved in one vast limestone lid.",
  credit="Sarcophagus lid, Palenque; photo public domain / CC"),
"Izapa Stela 5": dict(
  query="Izapa Stela 5",
  name="Izapa Stela 5",
  civ="Mesoamerican", era="c. 300–50 BCE", type="Sculpture",
  location="Izapa, Chiapas, Mexico",
  desc="Izapa Stela 5, the richest of Izapan carvings — a great branching tree with figures on both sides of its waters — called by some the oldest American Tree of Life.",
  credit="Izapan stone; photo public domain / CC"),
"Codex Borgia world tree": dict(
  query="Codex Borgia",
  name="World Trees of the Codex Borgia",
  civ="Aztec (Mexica)", era="pre-1521", type="Manuscript",
  location="Central Mexico (now Biblioteca Apostolica Vaticana)",
  desc="The folded pages of the Codex Borgia, where four world-trees hold the four directions and the Tlaloques pour the rains — the Mexica cosmos as a grove of colored trees.",
  credit="Pre-Columbian manuscript; photo public domain / CC"),
"Templo Mayor": dict(
  query="Templo Mayor",
  name="Templo Mayor",
  civ="Aztec (Mexica)", era="c. 1325–1521", type="Architectural",
  location="Tenochtitlan (Mexico City)",
  desc="The twin temple of Tenochtitlan — war and rain, the eagle's cactus and the serpent — planted at the center of the Aztec world like a tree between earth and sky.",
  credit="Aztec temple, Mexico City; photo public domain / CC"),
"Aztec sun stone": dict(
  query="Aztec sun stone",
  name="The Sun Stone — Axis of the Fifth Sun",
  civ="Aztec (Mexica)", era="c. 1479", type="Sculpture",
  location="Tenochtitlan (now National Museum of Anthropology, Mexico City)",
  desc="The Aztec Sun Stone — the fifth sun born at Teotihuacan, its rays ending in solar symbols, the face of the axis around which the Mexica world turned.",
  credit="Basalt disk, Mexico City; photo public domain / CC"),

# ─── Amazonian ──────────────────────────────────────────────────
"Ayahuasca vine": dict(
  query="Banisteriopsis caapi vine",
  name="Ayahuasca — the Vine of Souls",
  civ="Amazonian", era="Living tradition", type="Living tree",
  location="Amazon basin",
  desc="Banisteriopsis caapi, the great vine of the Amazon — the 'rope of the dead' that climbs the forest canopy and carries the shaman up the world-tree of vision.",
  credit="Malpighiaceae vine; photo CC"),

# ─── African ────────────────────────────────────────────────────
"Avenue of the Baobabs": dict(
  query="Avenue of the Baobabs Madagascar",
  name="Avenue of the Baobabs",
  civ="African (Malagasy)", era="Living (up to 800 yrs)", type="Living tree",
  location="Menabe, Madagascar",
  desc="The Avenue of the Baobabs — Adansonia grandidieri giants lining a dirt road in Menabe, the upside-down tree of African myth with its roots in the sky.",
  credit="Adansonia grandidieri, Madagascar; photo CC"),
"Iroko tree": dict(
  query="Milicia excelsa iroko",
  name="The Iroko",
  civ="West African", era="Living tradition", type="Living tree",
  location="West Africa (Yoruba, Igbo, Bantu lands)",
  desc="The iroko, the great tree of West African religion — home of spirits, altar of Ogun and the ancestors, never cut without sacrifice — the African world-tree standing between the living and the dead.",
  credit="Milicia excelsa; photo CC"),

# ─── Pacific / Aboriginal ───────────────────────────────────────
"Boab tree": dict(
  query="Adansonia gregorii boab",
  name="The Boab",
  civ="Aboriginal Australian", era="Living (up to 1,500 yrs)", type="Living tree",
  location="Kimberley, Western Australia",
  desc="The boab of the Kimberley, the hollow-bellied prison tree of Dreaming stories — Adansonia gregorii, the ancestral tree of Australia's northwest.",
  credit="Adansonia gregorii; photo CC"),
"Tane Mahuta existing?": None,  # placeholder, dropped below

# ─── Norse / Celtic ─────────────────────────────────────────────
"Celtic tree of life art": dict(
  query="Celtic cross stone carving Ireland",
  name="Crann Bethadh — the Celtic Tree",
  civ="Celtic", era="Early medieval", type="Sculpture",
  location="Ireland & Britain",
  desc="Crann Bethadh, the Tree of Life of the Celts — the oak of the druids connecting sky, sea and land, its memory coiled into high crosses and knotwork branches.",
  credit="Celtic carving; photo public domain / CC"),

# ─── Modern ─────────────────────────────────────────────────────
"Klimt Tree of Life": dict(
  query="Klimt Stoclet Frieze tree of life",
  name="Tree of Life (Stoclet Frieze)",
  civ="Modern", era="1909–1911", type="Painting",
  location="Palais Stoclet, Brussels",
  desc="Gustav Klimt's Tree of Life in the Stoclet dining room — the expectant embrace, the golden spiral branches, the only landscape the master ever painted.",
  credit="Gustav Klimt, Stoclet Frieze; photo public domain / CC"),
}

E.pop("Tane Mahuta existing?")

if __name__ == "__main__":
    print(len(E), "entries")
    from collections import Counter
    print(Counter(v["civ"] for v in E.values()))
