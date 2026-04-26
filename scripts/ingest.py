#!/usr/bin/env python3
"""
brain-search — Ingest
Reads documents from a folder, extracts searchable units via LLM, saves to search_data/units.json.

Supported formats: .md, .txt, .pdf (requires: pip install pypdf)

Usage:
  python3 scripts/ingest.py <docs_folder>          # dry run
  python3 scripts/ingest.py <docs_folder> --run    # extract all
  python3 scripts/ingest.py <docs_folder> --run --only-new  # skip done
  python3 scripts/ingest.py <docs_folder> --run --schema books   # use preset schema
  python3 scripts/ingest.py <docs_folder> --run --schema custom --prompt "Extract..."

Schemas: books | articles | wiki | tweets | general (default)
"""

import json, os, re, argparse, urllib.request, urllib.error, time
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
parser.add_argument('folder', nargs='?', default='.', help='Folder containing documents')
parser.add_argument('--run', action='store_true')
parser.add_argument('--only-new', action='store_true')
parser.add_argument('--schema', default='general', choices=['general','books','articles','wiki','tweets','custom'])
parser.add_argument('--prompt', default=None, help='Custom extraction prompt (used with --schema custom)')
parser.add_argument('--model', default='claude-haiku-4-5-20251001')
parser.add_argument('--out', default='search_data', help='Output folder')
args = parser.parse_args()

DOCS_DIR = Path(args.folder).expanduser().resolve()
OUT_DIR  = Path(args.out)
UNITS_OUT = OUT_DIR / 'units.json'

SCHEMAS = {
    'general': """Extract 5–10 key searchable UNITS from this document.
Each unit = one distinct idea, claim, or insight that someone might search for.
Return a JSON array:
[{"title": "short title", "summary": "2–3 sentences", "tags": ["tag1","tag2"], "type": "insight|fact|argument|example"}]""",

    'books': """Extract 8–12 key ARGUMENTS or CLAIMS from this book chapter/text.
Focus on: central theses, specific claims with evidence, author's position on key debates.
Return a JSON array:
[{"title": "claim title", "summary": "2–3 sentences describing the argument and evidence", "tags": ["topic1","topic2"], "type": "thesis|argument|evidence|counterargument", "author_stance": "bullish|bearish|nuanced"}]""",

    'articles': """Extract 5–8 key INSIGHTS from this article.
Focus on: novel findings, data points, frameworks, surprising claims.
Return a JSON array:
[{"title": "insight title", "summary": "2–3 sentences", "tags": ["tag1","tag2"], "type": "finding|framework|data|opinion"}]""",

    'wiki': """Extract the core KNOWLEDGE from this wiki page for search indexing.
Focus on: main concept definition, key properties, relationships to other concepts.
Return a JSON array with 3–5 units:
[{"title": "aspect title", "summary": "2–3 sentences", "tags": ["tag1","tag2"], "type": "definition|property|relationship|example"}]""",

    'tweets': """Extract 5–10 CLAIMS or POSITIONS from this person's tweets/content.
Focus on: specific beliefs, predictions, stances on debates.
Return a JSON array:
[{"title": "claim", "summary": "2–3 sentences with evidence/context", "tags": ["topic1","topic2"], "type": "prediction|stance|critique|framework", "intensity": 1-10}]""",
}

def read_file(path):
    suffix = path.suffix.lower()
    if suffix in ('.md', '.txt'):
        return path.read_text(errors='ignore')
    elif suffix == '.pdf':
        try:
            from pypdf import PdfReader
            reader = PdfReader(str(path))
            return '\n'.join(page.extract_text() or '' for page in reader.pages)
        except ImportError:
            print(f"  SKIP {path.name} — install pypdf: pip install pypdf")
            return None
    return None

def chunk_text(text, max_chars=6000):
    """Split long text into overlapping chunks."""
    if len(text) <= max_chars:
        return [text]
    chunks, start = [], 0
    while start < len(text):
        end = min(start + max_chars, len(text))
        # Try to break at paragraph boundary
        boundary = text.rfind('\n\n', start, end)
        if boundary > start + 2000:
            end = boundary
        chunks.append(text[start:end])
        start = end - 500  # 500-char overlap
    return chunks

def call_llm(prompt, text, model):
    ANTHROPIC_KEY = os.environ.get('ANTHROPIC_API_KEY', '')
    if not ANTHROPIC_KEY:
        raise Exception("No ANTHROPIC_API_KEY")
    payload = json.dumps({
        "model": model,
        "max_tokens": 2000,
        "system": "You are a precise knowledge extractor. Output only valid JSON arrays. No markdown fences.",
        "messages": [{"role": "user", "content": f"{prompt}\n\nDocument:\n---\n{text[:6000]}\n---"}]
    }).encode()
    req = urllib.request.Request(
        "https://api.anthropic.com/v1/messages",
        data=payload,
        headers={
            "x-api-key": ANTHROPIC_KEY,
            "anthropic-version": "2023-06-01",
            "content-type": "application/json",
        },
        method="POST"
    )
    for attempt in range(5):
        try:
            with urllib.request.urlopen(req, timeout=60) as resp:
                data = json.loads(resp.read())
                text_out = data["content"][0]["text"].strip()
                # Strip markdown fences if present
                text_out = re.sub(r'^```[a-z]*\n?', '', text_out)
                text_out = re.sub(r'\n?```$', '', text_out).strip()
                return json.loads(text_out)
        except urllib.error.HTTPError as e:
            body = e.read().decode()
            if e.code in (429, 529) or "overloaded" in body:
                wait = 20 * (attempt + 1)
                print(f"    rate limit, waiting {wait}s…")
                time.sleep(wait); continue
            raise Exception(f"HTTP {e.code}: {body[:200]}")
        except json.JSONDecodeError as e:
            if attempt < 4:
                time.sleep(5); continue
            raise Exception(f"JSON parse failed: {e}")
    raise Exception("Max retries exceeded")

# Discover documents
extensions = {'.md', '.txt', '.pdf'}
docs = sorted([f for f in DOCS_DIR.rglob('*') if f.suffix.lower() in extensions and not f.name.startswith('.')])

extract_prompt = args.prompt if args.schema == 'custom' and args.prompt else SCHEMAS[args.schema]

# Cost estimate: ~$0.003/doc with Haiku
cost_est = len(docs) * 0.003

print(f"\n{'='*55}")
print(f"  brain-search — Ingest")
print(f"{'='*55}")
print(f"  Folder:  {DOCS_DIR}")
print(f"  Docs:    {len(docs)} files ({', '.join(extensions)})")
print(f"  Schema:  {args.schema}")
print(f"  Model:   {args.model}")
print(f"  Cost:    ~${cost_est:.2f} (Claude Haiku)")
print(f"  Output:  {UNITS_OUT}")
print(f"{'='*55}\n")

for d in docs:
    print(f"  {d.name}")

if not args.run:
    print(f"\n  Dry run. Pass --run to extract.\n")
    exit(0)

if not os.environ.get('ANTHROPIC_API_KEY'):
    print("ERROR: No ANTHROPIC_API_KEY"); exit(1)

OUT_DIR.mkdir(parents=True, exist_ok=True)

# Resume
if UNITS_OUT.exists() and args.only_new:
    all_units = json.loads(UNITS_OUT.read_text())
    done_sources = {u['source_file'] for u in all_units}
    print(f"  Resuming — {len(done_sources)} files already processed")
else:
    all_units = []
    done_sources = set()

pending = [d for d in docs if d.name not in done_sources]
print(f"  Processing {len(pending)} file(s)…\n")

for doc in pending:
    print(f"  Extracting: {doc.name}…")
    text = read_file(doc)
    if not text or len(text.strip()) < 100:
        print(f"    skipped — too short or unreadable")
        continue

    chunks = chunk_text(text)
    doc_units = []

    for i, chunk in enumerate(chunks):
        label = f"chunk {i+1}/{len(chunks)}" if len(chunks) > 1 else ""
        try:
            units = call_llm(extract_prompt, chunk, args.model)
            if not isinstance(units, list):
                units = [units]
            for u in units:
                u['source_file'] = doc.name
                u['source_path'] = str(doc.relative_to(DOCS_DIR))
                if 'title' not in u: u['title'] = doc.stem
                if 'summary' not in u: u['summary'] = ''
                if 'tags' not in u: u['tags'] = []
                if 'type' not in u: u['type'] = 'insight'
            doc_units.extend(units)
            if label: print(f"    {label} → {len(units)} units")
        except Exception as e:
            print(f"    ERROR on {label or doc.name}: {e}")
            continue
        time.sleep(0.5)

    all_units.extend(doc_units)
    UNITS_OUT.write_text(json.dumps(all_units, indent=2))
    print(f"    ✓ {len(doc_units)} units extracted (total: {len(all_units)})")

print(f"\n  Done. {len(all_units)} units → {UNITS_OUT}")
