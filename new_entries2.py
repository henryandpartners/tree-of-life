#!/usr/bin/env python3
"""Batch 2 of curated Tree of Life entries. key -> dict(query, name, civ, era, type, location, desc, credit)"""

E2 = {

# ─── Mesopotamian ───────────────────────────────────────────────
"Balawat Gates": dict(
  query="Balawat Gates bronze band",
  name="The Bronze Gates of Balawat",
  civ="Mesopotamian", era="c. 850 BCE", type="Relief",
  location="Balawat, Assyria (now British Museum)",
  desc="The bronze bands of Shalmaneser III's gates, repoussé with the sacred tree between campaigns — the Assyrian world-tree marching with the army.",
  credit="Bronze repoussé, British Museum; photo public domain / CC"),
"Ur puabi headdress": dict(
  query="Puabi headdress Ur",
  name="Treasures of Ur — the Great Death Pit",
  civ="Mesopotamian", era="c. 2600 BCE", type="Artifact",
  location="Royal Cemetery of Ur (now British Museum / Penn Museum)",
  desc="The gold, lapis and carnelian of Ur's royal cemetery — trees and rosettes of the Sumerian garden of the dead, dug from the soil between the rivers.",
  credit="Sumerian goldwork; photo public domain / CC"),

# ─── Egyptian ───────────────────────────────────────────────────
"Egyptian sycamore amulet": dict(
  query="Egyptian tree goddess amulet",
  name="Tree-Goddess Amulet",
  civ="Egyptian", era="Late period (c. 664–332 BCE)", type="Artifact",
  location="Egypt",
  desc="A small amulet of the sycamore goddess with her offering vessel — Hathor-Nut of the West, the tree that feeds the dead, carried on the living.",
  credit="Egyptian amulet; photo public domain / CC"),
"Nut swallowing sun": dict(
  query="Nut sky goddess tomb painting",
  name="Nut, the Sky-Tree Mother",
  civ="Egyptian", era="New Kingdom", type="Painting",
  location="Theban tombs / papyri",
  desc="The sky-goddess Nut arched over the earth, her hands at the western and eastern horizons — mother of the sun who dies in her mouth and is born from her womb as the morning sycamore.",
  credit="Tomb painting / papyrus; photo public domain / CC"),

# ─── Jewish & Kabbalistic ───────────────────────────────────────
"Yggdrasil? no": None,

# ─── Christian (Eastern) ────────────────────────────────────────
"Hagia Sophia mosaic tree": dict(
  query="Hagia Sophia mosaic",
  name="Hagia Sophia — the Golden Vine",
  civ="Byzantine", era="6th c.", type="Mosaic",
  location="Istanbul, Turkey",
  desc="The golden vines and verdant marble of Justinian's Hagia Sophia — the Byzantine church as a garden, its columns grown like a forest beneath the dome of heaven.",
  credit="Byzantine mosaic and marble, Hagia Sophia; photo public domain / CC"),
"Sinai transfiguration apse": dict(
  query="Sinai monastery Transfiguration mosaic apse",
  name="The Transfiguration Apse (Sinai)",
  civ="Byzantine", era="c. 565", type="Mosaic",
  location="Saint Catherine's, Mount Sinai",
  desc="The apse mosaic of Saint Catherine's monastery at Sinai — Christ in a mandorla of light, the bush that burned and was not consumed, rays falling like branches over the prophets.",
  credit="Byzantine mosaic, Sinai; photo public domain / CC"),

# ─── Islamic ────────────────────────────────────────────────────
"Alhambra": dict(
  query="Alhambra Court of the Lions",
  name="The Alhambra — the Walled Garden of Paradise",
  civ="Islamic", era="Nasrid (14th c.)", type="Architectural",
  location="Granada, Spain",
  desc="The Alhambra's Court of the Lions, water running from the fountain through four rivers of marble — the Nasrid palace as the Quran's garden beneath which rivers flow, carved in stucco groves.",
  credit="Nasrid architecture, Granada; photo public domain / CC"),
"Qur'an garden verse illumination": dict(
  query="Quran illumination borders",
  name="Qur'anic Garden Illumination",
  civ="Islamic", era="Ottoman / Mamluk (14th–16th c.)", type="Manuscript",
  location="Istanbul / Cairo",
  desc="The illuminated borders of the Mamluk and Ottoman Qur'an — gold vines and palm-blossoms growing around the promise of the garden beneath which rivers flow.",
  credit="Manuscript illumination; photo public domain / CC"),

# ─── Persian ────────────────────────────────────────────────────
"Chahar Bagh Isfahan": dict(
  query="Chaharbagh Boulevard Isfahan",
  name="Chahār Bāgh — the Persian Paradise Avenue",
  civ="Persian", era="Safavid (17th c.)", type="Garden",
  location="Isfahan, Iran",
  desc="The Chahār Bāgh avenue of Safavid Isfahan, a garden-city's spine of plane trees and water — the Achaemenid paradise evolved into a city's tree of life.",
  credit="Safavid urban garden, Isfahan; photo CC"),

# ─── Hindu / Indian ─────────────────────────────────────────────
"Bodh Gaya throne": dict(
  query="Vajrasana Bodh Gaya",
  name="The Vajrāsana — Diamond Throne",
  civ="Buddhist", era="Ashokan (c. 250 BCE)", type="Sculpture",
  location="Bodh Gaya, India",
  desc="The Vajrāsana, the sandstone throne Ashoka placed at the foot of the Bodhi tree — the diamond seat where the earth herself witnessed the Buddha's awakening.",
  credit="Mauryan sculpture, Bodh Gaya; photo public domain / CC"),
# ─── Chinese / East Asian ───────────────────────────────────────
"Chinese scholar pine": dict(
  query="Pinus bungeana",
  name="The Pine of Longevity",
  civ="Chinese", era="Living tradition", type="Living tree",
  location="China (temple courtyards, Beijing)",
  desc="The bungeana pines of Chinese temples — bark flaked like clouds, bent by centuries into dragons — the pine of longevity planted beside every hall of the immortals.",
  credit="Pinus bungeana; photo CC"),
"Ginkgo tree china": dict(
  query="Ginkgo biloba ancient tree",
  name="The Ginkgo — the Living Fossil Tree",
  civ="Chinese", era="Living (individuals 1,000+ yrs)", type="Living tree",
  location="China / Japan (temple grounds)",
  desc="The ginkgo, sole survivor of a genus 200 million years old, planted at Chinese and Japanese temples as the tree of endurance — leaves like golden fans falling at equinox.",
  credit="Ginkgo biloba; photo CC"),

# ─── Mesoamerican ───────────────────────────────────────────────
# ─── Andean ─────────────────────────────────────────────────────
"Chilean araucaria": dict(
  query="Araucaria araucana monkey puzzle forest",
  name="Araucaria — the Sacred Monkey-Puzzle",
  civ="Andean / Mapuche", era="Living (groves 1,000 yrs)", type="Living tree",
  location="Chile / Argentina (Araucanía)",
  desc="The araucaria groves of the Mapuche — pehuen trees of the Andean slopes, sacred to the people who take their name from them, their seeds the bread of the mountain gods.",
  credit="Araucaria araucana; photo CC"),

# ─── North American / Native ────────────────────────────────────
"Sequoia": dict(
  query="giant sequoia General Sherman",
  name="The Giant Sequoia",
  civ="Native American", era="Living (2,000–3,000 yrs)", type="Living tree",
  location="Sierra Nevada, California",
  desc="The giant sequoias of the Sierra — the largest living things on Earth, elders of 3,000 years held sacred by the Sierra tribes, each a standing biography of the continent.",
  credit="Sequoiadendron giganteum; photo CC"),
"Cedar tree totem": dict(
  query="western red cedar totem",
  name="The Western Red Cedar",
  civ="Native American", era="Living tradition", type="Living tree",
  location="Pacific Northwest",
  desc="The western red cedar, the tree-of-life of the Pacific Northwest coast — the Longhouse Lifegiver from whose body the peoples cut houses, canoes, boxes and totems.",
  credit="Thuja plicata; photo CC"),

# ─── Pacific / Oceanic ──────────────────────────────────────────
"Breadfruit tree": dict(
  query="breadfruit tree Artocarpus",
  name="The Breadfruit — Tree of Navigators",
  civ="Pacific / Polynesian", era="Living tradition", type="Living tree",
  location="Polynesia",
  desc="The breadfruit carried across the Pacific in canoes — the tree of Bounty mutiny and of island life itself, planted as a blessing for unborn generations.",
  credit="Artocarpus altilis; photo CC"),
# ─── African ────────────────────────────────────────────────────
"Baobab tree africa": dict(
  query="Adansonia digitata baobab tree",
  name="The Baobab — the Upside-Down Tree",
  civ="African", era="Living (2,000+ yrs)", type="Living tree",
  location="Sub-Saharan Africa",
  desc="The African baobab — the upside-down tree of a thousand folk tales, the tree the gods planted in anger and threw back roots-to-sky — water-hoarding giant of the savanna, home of spirits.",
  credit="Adansonia digitata; photo CC"),
"Aksum obelisk": dict(
  query="Obelisk of Axum",
  name="The Stelae of Aksum",
  civ="African (Aksumite)", era="c. 4th c. CE", type="Architectural",
  location="Aksum, Ethiopia",
  desc="The granite stelae of Aksum, carved like multi-story towers with false doors and beam-ends — stone trees raised over the kings of Ethiopia, roots of a Christian-African world-axis.",
  credit="Aksumite stelae; photo public domain / CC"),
"Dogon kanaga": dict(
  query="Kanaga mask Dogon",
  name="Kanaga Mask of the Dogon",
  civ="African (Mande)", era="20th c. (living tradition)", type="Mask",
  location="Bandiagara Escarpment, Mali",
  desc="The Dogon kanaga mask — the cruciform of Amma's creative hand and the falling nommo, danced at dama funerals to complete the tree of the world's order.",
  credit="Dogon wood mask; photo public domain / CC"),

# ─── Aboriginal Australian ──────────────────────────────────────
"Aboriginal coolabah": dict(
  query="Eucalyptus coolabah tree",
  name="Coolabah of the Watercourses",
  civ="Aboriginal Australian", era="Living tradition", type="Living tree",
  location="Central Australia",
  desc="The coolabah, shade-tree of the inland waterholes in Waltzing Matilda country — in Aboriginal tradition the tree of the waters, where the rainbow serpent sleeps beneath its roots.",
  credit="Eucalyptus coolabah; photo CC"),

# ─── Modern ─────────────────────────────────────────────────────
"Klimt modern tree?": None,
}
E2 = {k: v for k, v in E2.items() if v}
if __name__ == "__main__":
    print(len(E2), "entries batch 2")
