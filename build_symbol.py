#!/usr/bin/env python3
"""Build self-contained symbol.html from symbol-template.html + symbol-data.json."""
import json, os

ROOT = '/Users/henry/tree-of-life'
template = open(os.path.join(ROOT, 'symbol-template.html')).read()
data = json.load(open(os.path.join(ROOT, 'symbol-data.json')))
data_js = json.dumps(data, ensure_ascii=False).replace('</', '<\\/')
out = template.replace('/*__SYMBOL_DATA__*/', data_js)
open(os.path.join(ROOT, 'symbol.html'), 'w').write(out)
print(f"built symbol.html ({len(out):,} bytes, {len(data)} symbols)")
