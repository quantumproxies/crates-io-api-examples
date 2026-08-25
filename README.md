# Rust crates (crates.io) API — examples

Rust package search from the crates.io registry — downloads, versions, links.

**Live page, full schema & pricing → [quanticdata.io/collectors/crates-io-api/](https://quanticdata.io/collectors/crates-io-api/)**

Searches crates.io, the Rust package registry, through its keyless JSON API. One row per crate: description, latest stable version, total and recent downloads, created/updated timestamps and the homepage, docs and repository links. Sort by relevance, downloads, recent downloads, recent updates or newest. Completes the npm/PyPI pair for the Rust ecosystem.

## Quick start (curl)

```bash
curl -X POST https://api.quanticdata.io/v1/scraper/collectors/crates_io/run \
  -H "Authorization: Bearer $QD_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"query": "serde", "max_results": 10}'
```

## Python

See [`example.py`](example.py):

```bash
export QD_API_KEY=qd_live_...   # https://quanticdata.io/
python3 example.py
```

## Inputs

- `query` (string, required) — Crate name or keyword.
- `sort` (string) — Result order.
- `max_results` (integer) — How many crates to deliver at most (1–100). You pay only for delivered crates.

## Output — one row per crate

| field | type | description |
|---|---|---|
| `rank` | integer | 1-based position. |
| `name` | string | Crate name. |
| `description` | string | Description. |
| `version` | string | Latest stable version. |
| `downloads` | integer | All-time downloads. |
| `recent_downloads` | integer | Downloads in the last 90 days. |
| `created_at` | string | First publish. |
| `updated_at` | string | Last update. |
| `homepage` | string | Homepage. |
| `documentation` | string | Docs URL. |
| `repository` | string | Repository URL. |
| `exact_match` | boolean | Query matched the name exactly. |
…and 1 more fields — full schema on the [live page](https://quanticdata.io/collectors/crates-io-api/).

## Pricing

**$0.0003 per delivered crate** ($0.3 per 1,000). A run that delivers nothing costs nothing, and failed rows are never billed. The $2/month free allowance covers roughly 6,666 crates — no card required.

## Links

- This collector: https://quanticdata.io/collectors/crates-io-api/
- All collectors: https://quanticdata.io/collectors/
- Docs: https://quanticdata.io/docs/
