#!/usr/bin/env python3
"""
brain-search — Embed
Reads search_data/units.json, embeds each unit via Gemini (free tier), saves embeddings.

Usage:
  python3 scripts/embed.py           # embed all units
  python3 scripts/embed.py --only-new  # skip already-embedded
  python3 scripts/embed.py --dim 256   # embedding dimensions (128|256|512|768|1024)
  python3 scripts/embed.py --input search_data/units.json
"""

import json, os, argparse, urllib.request, urllib.error, time
from pathlib import Path

def load_env():
    env = Path.home() / ".claude" / ".env"
    if env.exists():
        for line in env.read_text().splitlines():
            line = line.strip()
            if line and not line.startswith('#') and '=' in line:
                k, _, v = line.partition('=')
                os.environ.setdefault(k.strip(), v.strip().strip('"\''))
load_env()

parser = argparse.ArgumentParser()
parser.add_argument('--input', default='search_data/units.json')
parser.add_argument('--out', default='search_data')
parser.add_argument('--only-new', action='store_true')
parser.add_argument('--dim', type=int, default=256, choices=[128, 256, 512, 768, 1024])
parser.add_argument('--batch', type=int, default=50)
args = parser.parse_args()

UNITS_PATH = Path(args.input)
OUT_PATH   = Path(args.out) / 'embeddings.json'

if not UNITS_PATH.exists():
    print(f"ERROR: {UNITS_PATH} not found. Run ingest.py first."); exit(1)

units = json.loads(UNITS_PATH.read_text())
n = len(units)

print(f"\n{'='*55}")
print(f"  brain-search — Embed")
print(f"{'='*55}")
print(f"  Units:  {n}")
print(f"  Model:  Gemini gemini-embedding-2 (dim={args.dim})")
print(f"  Cost:   FREE (Gemini free tier — 1500 req/day)")
print(f"  Output: {OUT_PATH}")
print(f"{'='*55}\n")

GEMINI_KEY = os.environ.get('GEMINI_API_KEY', '')
if not GEMINI_KEY:
    print("ERROR: No GEMINI_API_KEY — get one free at aistudio.google.com"); exit(1)

OUT_PATH.parent.mkdir(parents=True, exist_ok=True)

# Resume
if OUT_PATH.exists() and args.only_new:
    existing = json.loads(OUT_PATH.read_text())
    done = {e['idx'] for e in existing}
    print(f"  Resuming — {len(done)} already embedded")
else:
    existing = []
    done = set()

def embed_batch(texts):
    payload = json.dumps({
        "requests": [
            {
                "model": "models/gemini-embedding-2",
                "content": {"parts": [{"text": t[:1000]}]},
                "taskType": "RETRIEVAL_DOCUMENT",
                "outputDimensionality": args.dim,
            }
            for t in texts
        ]
    }).encode()
    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-embedding-2:batchEmbedContents?key={GEMINI_KEY}"
    req = urllib.request.Request(url, data=payload, headers={"Content-Type": "application/json"}, method="POST")
    for attempt in range(5):
        try:
            with urllib.request.urlopen(req, timeout=60) as resp:
                data = json.loads(resp.read())
                return [e['values'] for e in data['embeddings']]
        except urllib.error.HTTPError as e:
            body = e.read().decode()
            if e.code == 429 or "RESOURCE_EXHAUSTED" in body:
                wait = 30 * (attempt + 1)
                print(f"    rate limit, waiting {wait}s…")
                time.sleep(wait); continue
            raise Exception(f"HTTP {e.code}: {body[:200]}")
    raise Exception("Max retries exceeded")

def embed_text(unit):
    return f"{unit.get('title','')}. {unit.get('summary','')}".strip()[:1000]

pending = [(i, u) for i, u in enumerate(units) if i not in done]
print(f"  Embedding {len(pending)} units…\n")

for start in range(0, len(pending), args.batch):
    batch = pending[start:start + args.batch]
    texts = [embed_text(u) for _, u in batch]
    vectors = embed_batch(texts)
    for (i, u), vec in zip(batch, vectors):
        existing.append({
            'idx': i,
            'title': u.get('title', ''),
            'summary': u.get('summary', ''),
            'tags': u.get('tags', []),
            'type': u.get('type', ''),
            'source_file': u.get('source_file', ''),
            'source_path': u.get('source_path', ''),
            'vector': vec,
        })
    OUT_PATH.write_text(json.dumps(existing))
    pct = min(100, round((start + len(batch)) / len(pending) * 100))
    print(f"  ✓ {start + len(batch)}/{len(pending)} ({pct}%)")
    time.sleep(0.5)

sz = OUT_PATH.stat().st_size / 1024
print(f"\n  Done. {len(existing)} embeddings → {OUT_PATH} ({sz:.0f} KB)")
print(f"\n  Next: python3 scripts/search.py")
