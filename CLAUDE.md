# CLAUDE.md

Guidance for Claude Code when working in this repository.

## What this repo is

**brain-search** turns a folder of documents into a local semantic search engine. Three stages, no database, no cloud:

```
ingest.py  →  LLM extracts 5–12 structured units per document  →  search_data/units.json
embed.py   →  Gemini embeds each unit as a 256-dim vector      →  search_data/embeddings.json
search.py  →  serves a browser UI at http://localhost:7777     →  cosine similarity in ~5ms
```

`research/` holds market-research deliverables produced in this repo; it is unrelated to the pipeline code.

## Commands

```bash
# Required keys (standard sk-ant-... keys and Claude Max OAuth sk-ant-oat... both work)
export ANTHROPIC_API_KEY=sk-ant-...
export GEMINI_API_KEY=AIza...

python3 scripts/ingest.py <folder-or-file> --run --schema <books|articles|wiki|tweets|general>
python3 scripts/embed.py
python3 scripts/search.py            # opens http://localhost:7777

# Incremental update after adding files
python3 scripts/ingest.py <folder> --run --only-new
python3 scripts/embed.py --only-new
```

- Omit `--run` for a dry run. `--schema general` is the default.
- Custom extraction: `--schema custom --prompt "..."`.
- `pip install pypdf` is only needed for PDF input. Nothing else requires pip.
- Extraction costs roughly $0.003/document (Claude Haiku); embeddings are free on Gemini's tier.

## Conventions for the code

- Python 3.8+, standard library only for `.md`/`.txt` paths — do not add dependencies for the core pipeline.
- Ingest detects document structure with one cheap LLM call that returns a regex for the natural unit boundary, then applies it to the whole document, falling back to paragraph-aware chunking. Preserve that two-step shape when editing `ingest.py`.
- Sections over 12,000 characters are split further by paragraph.
- All generated state belongs in `search_data/` and is gitignored.

## Conventions for research deliverables (`research/`)

These rules were set while producing `research/automated-ads-market-2026.md`. Follow them for any further market or competitive research in this repo.

**Sourcing and honesty**

- Label every modelled figure `est.` with its source (Latka, Tracxn, Growjo, PitchBook). Leave unmarked only figures from company announcements, SEC filings, or credible press.
- Write `n/a` when something is not found. Never fill a gap with a plausible number.
- When sources conflict, show both and say which is verifiable. Record the conflict in the caveats section rather than silently picking one.
- State valuations as last-round post-money with the round date, since they age.
- Distinguish what a company confirmed from what reporters inferred. (Icon's shutdown was inferred from a password-walled site and staff leaving LinkedIn; the company never announced it.)

**Never infer a URL from a name pattern.** This is the rule most easily broken. `linkedin.com/in/<firstnamelastname>` is wrong often enough to matter — five of the guesses in the first draft here were wrong, including Mark Douglas, who is `/in/teachmehow2douglas`. Resolve profiles against a people database (the Crustdata MCP tools; `crustdata_people_search_db_v2` returns vanity URLs where the v1 tool returns URN-format fallbacks) or a source that shows the URL verbatim. If neither resolves it, leave it unlinked and say so.

**Credits.** Crustdata calls cost credits and the balance is small. Run `crustdata_credit_costs` (free) before spending, prefer `crustdata_people_search_db_v2` at 3 credits per 100 results over per-profile enrichment, batch many people into one OR-filtered query, and always report spend and remaining balance to the user. Keep filters tight — a loose name-only query burns credits on irrelevant matches.

**Formatting**

- Hyperlink every company name to its official website on first appearance and in table cells.
- Give each company its ad-library links, constructed as:
  - Meta: `https://www.facebook.com/ads/library/?active_status=active&ad_type=all&country=ALL&q=<name>&search_type=keyword_unordered`
  - Google: `https://adstransparency.google.com/?region=anywhere&domain=<domain>` (exact, advertiser-domain lookup)
  - LinkedIn: `https://www.linkedin.com/ad-library/search?keyword=<name>`
  - Note that Meta and LinkedIn are keyword searches and will return unrelated advertisers; Google is exact.
- Keep per-company research notes with every source URL in `research/segments/`, and keep the synthesized report separate from them.

**Publishing.** Reports are published as Artifacts. Load the `artifact-design` skill before writing the page, and `dataviz` before any chart. Run the palette validator rather than eyeballing contrast. Prefer a dot plot to bars on a log scale — bar length implies a proportionality a log axis breaks.

## Git

- Develop on the branch named in the task; create it from the default branch if absent.
- Push with `git push -u origin <branch>`; retry network failures with backoff.
- Do not open a pull request unless explicitly asked.
