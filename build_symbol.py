#!/usr/bin/env python3
"""Build self-contained symbol.html from symbol-template.html + symbol-data.json.
Writes to both <repo>/symbol.html and <repo>/dist/symbol.html (Vercel serves dist/).
"""
import json, os, shutil

ROOT = os.path.dirname(os.path.abspath(__file__))
template = open(os.path.join(ROOT, 'symbol-template.html')).read()
data = json.load(open(os.path.join(ROOT, 'symbol-data.json')))
data_js = json.dumps(data, ensure_ascii=False).replace('</', '<\\/')
out = template.replace('/*__SYMBOL_DATA__*/', data_js)
out_path = os.path.join(ROOT, 'symbol.html')
open(out_path, 'w').write(out)
# also emit to dist/ (the directory Vercel deploys)
dist = os.path.join(ROOT, 'dist', 'symbol.html')
os.makedirs(os.path.join(ROOT, 'dist'), exist_ok=True)
shutil.copyfile(out_path, dist)
print(f"built symbol.html ({len(out):,} bytes, {len(data)} symbols) -> symbol.html + dist/symbol.html")
