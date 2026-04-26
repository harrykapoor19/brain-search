# brain-search

Turn any folder of documents into a local semantic search engine. Three commands. No database. No cloud. Free.

```
books/ articles/ notes/ wiki/ tweets/
         ↓  ingest.py
    structured units (LLM-extracted)
         ↓  embed.py
    vectors (Gemini, free tier)
         ↓  search.py
    http://localhost:7777
```

**Natural language search across 1000 documents in your browser. Results in ~300ms.**

---

## How It Works

1. **Ingest** — an LLM reads your documents and extracts 5–12 structured *units* per file: key arguments, claims, insights, definitions — whatever matters for search. Not raw chunks. Distilled meaning.

2. **Embed** — each unit is converted to 256 numbers (a vector) by Gemini's embedding model. Similar ideas get similar numbers. This is what enables semantic search.

3. **Search** — you type a question, it gets embedded the same way, and the browser computes cosine similarity against all stored vectors in ~5ms. Top 12 results appear instantly.

This is the same pattern used at scale by [The Room](https://github.com/harrykapoor19/feed) (122 AI founders, 1200 claims) — generalized for any corpus.

---

## Quickstart

```bash
git clone https://github.com/harrykapoor19/brain-search
cd brain-search

# Set API keys (one-time)
export ANTHROPIC_API_KEY=sk-ant-...
export GEMINI_API_KEY=AIza...

# Point at your documents
python3 scripts/ingest.py ~/my-books --run --schema books
python3 scripts/embed.py
python3 scripts/search.py
```

Open `http://localhost:7777` and start searching.

---

## Requirements

- Python 3.8+ (no pip installs required for .md/.txt)
- `ANTHROPIC_API_KEY` — for extraction ([get one](https://console.anthropic.com))
- `GEMINI_API_KEY` — for embeddings, **free tier** ([get one](https://aistudio.google.com))
- `pip install pypdf` — only if you have PDF files

**Cost:** ~$0.003/document for extraction (Claude Haiku). Embeddings are free (Gemini).

---

## Document Schemas

Different document types need different extraction logic. Use `--schema`:

| Schema | Best for | Extracts |
|--------|----------|----------|
| `books` | Book chapters, papers | Arguments, theses, evidence, author stance |
| `articles` | Blog posts, essays | Key insights, findings, frameworks, data |
| `wiki` | Knowledge base pages | Definitions, properties, relationships |
| `tweets` | Social content | Claims, predictions, stances, intensity |
| `general` | Anything else | Ideas, claims, insights (default) |

```bash
python3 scripts/ingest.py ~/books --run --schema books
python3 scripts/ingest.py ~/articles --run --schema articles
python3 scripts/ingest.py ~/notes --run  # uses general
```

Custom prompt:
```bash
python3 scripts/ingest.py ~/legal --run --schema custom \
  --prompt "Extract 5-8 key legal arguments, precedents, and rulings."
```

---

## Adding New Documents

The pipeline is incremental. Add files to your folder, then:

```bash
python3 scripts/ingest.py ~/my-docs --run --only-new
python3 scripts/embed.py --only-new
# Restart search server to pick up new embeddings
```

---

## Integration with second-brain

If you use the [Karpathy LLM Wiki pattern](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f), brain-search plugs in naturally. Point it at your `raw/` or `wiki/` folder:

```bash
# Search your wiki pages
python3 scripts/ingest.py ~/second-brain/wiki --run --schema wiki \
  --out ~/second-brain/search_data/wiki
python3 scripts/embed.py \
  --input ~/second-brain/search_data/wiki/units.json \
  --out ~/second-brain/search_data/wiki
python3 scripts/search.py \
  --embeddings ~/second-brain/search_data/wiki/embeddings.json

# Search your ingested books
python3 scripts/ingest.py ~/second-brain/raw/books --run --schema books \
  --out ~/second-brain/search_data/books
```

---

## Claude Code Skill

Install as a Claude Code slash command — then type `/brain-search` in any session:

```bash
cp -r . ~/.claude/commands/brain-search
```

Claude will automatically handle the full pipeline (ingest → embed → search) based on your corpus state.

---

## Project Structure

```
brain-search/
├── scripts/
│   ├── ingest.py      # LLM extraction — docs → units.json
│   ├── embed.py       # Gemini embedding — units.json → embeddings.json
│   ├── search.py      # Local server — serves search UI + embeds queries
│   └── search.html    # Search UI — cosine search in browser
├── SKILL.md           # Claude Code slash command definition
└── README.md
```

Output files (created in `search_data/` by default, gitignored):
```
search_data/
├── units.json         # Extracted units (LLM output)
└── embeddings.json    # Vectors (Gemini output)
```

---

## Architecture

```
OFFLINE (build once):
Documents → ingest.py (LLM) → units.json → embed.py (Gemini) → embeddings.json

RUNTIME (every search):
Query → /embed (Gemini, ~200ms) → query vector
      + embeddings.json loaded in browser (cached)
      → cosine similarity in JS (~5ms)
      → top 12 results rendered
```

Everything runs locally. No database. No vector store. No cloud infra. The entire search index is a single JSON file loaded in the browser.

**Scales to:** ~5000 units before the JSON gets heavy (~15MB). Beyond that, use a proper vector DB (Qdrant, Weaviate) — but for most personal knowledge bases, you'll never hit this.

---

## Search UI Features

- **Type filters** — filter by insight/argument/fact/etc.
- **Similarity score** — % match shown on each result  
- **Tag suggestions** — auto-populated from your corpus
- **Source attribution** — which file each result came from
- **Dark mode** — easy on the eyes for long sessions

---

## FAQ

**Why not just use a vector database?**  
For personal knowledge bases under ~5000 units, a flat JSON file + browser-side cosine search is faster to set up, free, and has zero moving parts. No Docker, no server, no API keys for the search layer.

**Why Gemini for embeddings and not OpenAI?**  
Gemini's embedding API has a free tier (1500 requests/day). OpenAI charges per token. For personal use, Gemini is free indefinitely.

**Why extract units instead of chunking?**  
Chunking preserves raw text verbatim — a chunk of "he argues that..." has no idea what argument it refers to. LLM extraction distills the actual claim. Search quality is significantly better, especially for books and long documents.

**Can I use this with GPT-4 instead of Claude?**  
Edit the `call_llm()` function in `ingest.py` to point at any OpenAI-compatible endpoint.

---

## License

MIT
