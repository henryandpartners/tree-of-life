#!/usr/bin/env python3
"""Build the self-contained Tree of Life HTML from data.json."""
import json, html

DATA = json.load(open('/Users/henry/tree-of-life/data.json'))
REGION_LABELS = {
    "ancient-near-east": "Ancient Near East",
    "egypt": "Egypt",
    "persia": "Persia & Zoroastrian",
    "europe": "Europe",
    "africa": "Africa",
    "south-asia": "South Asia",
    "southeast-asia": "Southeast Asia",
    "east-asia": "East Asia",
    "americas": "The Americas",
    "oceania": "Oceania & Pacific",
}
# order: left side bottom->top, then right side bottom->top
ORDER = ["europe", "africa", "egypt", "ancient-near-east", "persia",
         "south-asia", "southeast-asia", "east-asia", "americas", "oceania"]

template = open('/Users/henry/tree-of-life/template.html').read()
data_js = json.dumps(DATA, ensure_ascii=False).replace('</', '<\\/')
out = template.replace('/*__DATA__*/', data_js)
open('/Users/henry/tree-of-life/index.html', 'w').write(out)
print("built", len(out), "bytes")
