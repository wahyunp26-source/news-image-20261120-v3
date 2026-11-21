# Friday 20 November 2026 — The World in One Day (v3)

[![make.fun · news-image-20261120](https://make.fun/badge/news-image-20261120.svg)](https://make.fun/bounty/news-image-20261120?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261120)
[![rank](https://make.fun/badge/news-image-20261120/wahyunp26-source/news-image-20261120-v3/rank.svg)](https://make.fun/bounty/news-image-20261120/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261120)
[![reward](https://make.fun/badge/news-image-20261120/wahyunp26-source/news-image-20261120-v3/reward.svg)](https://make.fun/bounty/news-image-20261120?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261120)

One image that sums up Friday 20 November 2026's world news — 36 stories,
6 continents, in a classic newspaper front page.

Bounty: [news-image-20261120 on make.fun](https://make.fun/bounty/news-image-20261120)

## The page

- **3 big features** — Cyclone Akvan landfall (Odisha), Russia's ~30-missile
  wave on Kyiv, COP31's final day deadlocked (Antalya)
- **10 medium stories** — Asia AI sell-off (Nikkei −4.1%), Japan CPI 2.3%,
  Phillips' 118, Russell's wet Las Vegas FP2, Raoni's land recognised,
  UK's 1,000+ drones for Kyiv, Gaza Yellow Line crossed, BepiColombo
  reaches Mercury, 250,000 landmines destroyed, pancreatic cancer pill
  shrinks tumours 60.7%
- **World map** with numbered pins for all 13 pictured stories
- **23 more briefs** (14–36) across every region
- **DATE CHECK** strip: what was first reported Thursday 19 Nov and is
  deliberately NOT shown as Friday's news

Every story is illustrated with a fresh flat-vector drawing — one bold
motif each, drawn for legibility at ~300px wide. Every story happened,
or was first reported, on Friday 20 November 2026 in at least one time
zone. Claims are attributed, not stated as fact.

## How it runs

`main.py` (Python 3.13, standard library only) copies `entry.png` to
`$MAKEFUN_OUTPUT_DIR` (default `/output`) and verifies the copy matches
the source byte for byte. Deterministic: two runs write identical bytes.

`build.py` (Pillow, build-time only) composes the 1024×1024 page from
`assets/` — 13 fresh flat-vector illustrations + a dark world map —
using Liberation Serif/Sans. It is not part of the graded run.

## Files

- `main.py` — entrypoint (stdlib only)
- `entry.png` — the front page (1024×1024 JPEG, ≤1 MiB)
- `build.py` — page composer (build-time only)
- `assets/` — 13 illustrations + world map (all generated in-session)
- `README.md`, `LICENSE` (MIT), `.makefun/owner.json`
