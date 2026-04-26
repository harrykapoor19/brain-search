---
name: brain-search
description: Turn any folder of documents into a semantic search engine. Ingest books, articles, wikis, tweets — extract structured units via LLM, embed with Gemini (free), search with natural language in browser. Use when user says "search my docs", "build a knowledge base", "semantic search over my files", "ingest these books", "brain-search", or wants to search across a large document corpus.
---

# brain-search

Turn any folder of documents into a local semantic search engine. Three steps: ingest → embed → search.

**Requires:** `ANTHROPIC_API_KEY` + `GEMINI_API_KEY` (both in `~/.claude/.env` or env)

## What You Do

When the user invokes this skill, figure out what stage they're at and run the right command(s):

### Stage 1 — Ingest (extract structured units from documents)

```bash
# From the repo root or any folder with search_data/
python3 /path/to/brain-search/scripts/ingest.py <docs_folder> --run --schema <schema>
```

**Schemas:**
- `books` — chapter arguments, author theses, evidence
- `articles` — key insights, findings, frameworks
- `wiki` — concept definitions, properties, relationships
- `tweets` — claims, stances, predictions
- `general` (default) — works for anything

**How long documents are split:**
The ingest script automatically detects chapter/section headings (e.g. "Chapter 1", "Part II", "## Heading") and splits there first — each chapter goes to the LLM as one unit. If no chapter structure is found, or a chapter is >12,000 chars, it falls back to paragraph-aware character chunking. The terminal output tells you which path was taken:
```
detected 13 chapters → 13 sections      ← chapter-aware
no chapters detected → 47 paragraph chunks  ← fallback
```

**Examples:**
```bash
python3 scripts/ingest.py ~/second-brain/raw/books --run --schema books
python3 scripts/ingest.py ~/articles --run --schema articles
python3 scripts/ingest.py ~/notes --run
```

Output: `search_data/units.json`

---

### Stage 2 — Embed (convert units to vectors)

```bash
python3 /path/to/brain-search/scripts/embed.py
```

Reads `search_data/units.json`, embeds with Gemini (free tier), saves `search_data/embeddings.json`.

For incremental updates (new files added):
```bash
python3 scripts/ingest.py <folder> --run --only-new
python3 scripts/embed.py --only-new
```

---

### Stage 3 — Search

```bash
python3 /path/to/brain-search/scripts/search.py
```

Opens `http://localhost:7777` — natural language search, results by cosine similarity.

---

## Full Pipeline (first time)

```bash
git clone https://github.com/harrykapoor19/brain-search
cd brain-search

# 1. Ingest your docs
python3 scripts/ingest.py ~/my-docs --run --schema books

# 2. Embed
python3 scripts/embed.py

# 3. Search
python3 scripts/search.py
```

---

## Integration with second-brain

If the user has a `~/second-brain` setup, books and documents live in `raw/books/`. Run:

```bash
python3 ~/Projects/brain-search/scripts/ingest.py ~/second-brain/raw/books --run --schema books --out ~/second-brain/search_data/books
python3 ~/Projects/brain-search/scripts/embed.py --input ~/second-brain/search_data/books/units.json --out ~/second-brain/search_data/books
python3 ~/Projects/brain-search/scripts/search.py --embeddings ~/second-brain/search_data/books/embeddings.json
```

---

## Re-embed after adding new pages/docs

```bash
python3 scripts/ingest.py <folder> --run --only-new
python3 scripts/embed.py --only-new
# Server auto-reloads on next search
```

---

## Troubleshooting

| Error | Fix |
|---|---|
| `No ANTHROPIC_API_KEY` | `source ~/.claude/.env` or set env var |
| `No GEMINI_API_KEY` | Get free key at aistudio.google.com |
| `No embeddings` | Run ingest.py then embed.py first |
| PDF not reading | `pip install pypdf` |
| Rate limit | Script auto-retries with backoff |

---

## When user asks to search their docs

1. Check if `search_data/embeddings.json` exists. If yes → go straight to `search.py`.
2. If not → run ingest + embed first, then search.
3. If user adds new documents → run with `--only-new` flags.
