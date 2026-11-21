# news-image-20261120 v3 — STATUS (FACTS ONLY)

## Entry
- Competition: news-image-20261120 — "Sum up 20 November's world news in one image"
- Prizes: 1st $50, 2nd $30, 3rd $15, 4th–10th $5, 11th–50th $3 (total $250)
- Closes: 2026-11-22T00:00:00Z (22 Nov 07:00 WIB). Result ~4 Dec 2026.
- Slot: 3/3 (LAST). Deadline submit ideal 22 Nov ~05:50 WIB.
- Repo: https://github.com/wahyunp26-source/news-image-20261120-v3
- Commit: 38f4578d229826cea206fe5e695069af560e8651
- GitHub About: homepage https://make.fun/bounty/news-image-20261120 + topic makefun
- Target: judge > 992,057 (top-1). Top-50 bar: 988,744.

## Leaderboard (live, 21 Nov ~10:00 WIB, 13,448 entries)
- Rank 1: judge 992,057 (12W-0L), "35 stories, 7 regions", 466,875 B, sub 01a1f99d
- Rank 2: judge 991,652, "36 stories, 6 continents", 742,756 B
- Rank 3: judge 991,488, 300,055 B
- Rank 4: 991,429 | Rank 5: 991,336 | Rank 10: 990,836 | Rank 50: ~988,744
- OUR v1: judge 971,858, rank 3,331 (was 980,686 rank 894 at 07:50 — drifted down)
- OUR v2: judge 978,974, rank 1,347 (11W-0D-1L)
- Gap v2 → top-1: 13,083. Gap v2 → top-50 bar: ~9,770.

## DIAGNOSIS — v1 vs v2 vs top 1-3 (from viewing all 5 images)
Top 1-3 shared pattern: classic newspaper front page (kicker + huge serif
date + italic sub-headline + 6-stat strip + region tabs + 3 big + 10 medium
+ map + 23 briefs + full-width DATE CHECK strip). 33–36 stories; story
count is NOT the driver (v1 had 38, most, ranked lowest). Illustrations:
EXTREMELY SIMPLE flat vector, ONE bold motif each, high contrast, limited
palette, generous whitespace (top-3's are almost icons). Judge criteria
(RULES.txt, in order): (1) one day's news + names that day; (2) selection
and breadth; (3) it reads — each story clear from picture + short labels;
(4) faithful, no hype; (5) craft — legible at ~300px across, no smears
or garbled text. "Detail for its own sake does not count."

v1 (photo-realistic, 38 stories): photos varied/dark/busy (Kyiv night fire,
Mercury dark space, COP31 crowd) — noise at 1024px, inconsistent style.
11 mediums (6+5) vs top's 10 (5+5). DATE CHECK as side box (less prominent).
Result: lowest of our entries.

v2 (flat vector, copied top-1 structure): RIGHT structure, but
illustrations too BUSY/detailed vs top-1's restraint — big #1 cyclone a
chaotic red/blue swirl (top-1's is a clean map+swirl), #08 Brazil a very
busy colourful pattern, #05 Japan a dominant ¥ coin. Map LIGHT (cream) —
low contrast, pins washed out (top-1/3 use dark navy; v1's dark map was
better). Stats strip DUPLICATED two features (118 Phillips = #06,
250,000 landmines = #13) — wasted information vs top-1's 6 distinct stats.
Big #2 Kyiv skyline yellow/orange, slightly cartoonish vs top-1's dark
night skyline. Result: 978,974 — better than v1 now, but ~13,000 below
top-1. Structure is necessary but NOT sufficient; the judge rewards
VISUAL CLARITY at small size above all.

## What v3 does to BEAT top-1
- Same proven structure (3 big + 10 medium + dark map + 23 briefs +
  DATE CHECK full-width + stats + region tabs), 36 stories.
- Illustrations SIMPLER than top-1: one bold motif each, flat vector,
  2–4 colours, high contrast, generous whitespace. 13 NEW illustrations
  generated in-session (no reuse of v1/v2 assets — own-work gate).
- DARK NAVY map (like top-1/3) with large red pins 1–13 + SPACE callout.
- Big #1 Odisha: clean geographic map of India/Bay of Bengal + cyclone
  swirl + red landfall dot (cleaner than top-1's).
- Stats strip: 6 DISTINCT numbers, zero duplication (300,000+ evacuated;
  ~30 missiles; −4.1% Nikkei; 2.3% Japan CPI; 118 Phillips; 8 yrs
  BepiColombo).
- Story selection: v1's verified 38 minus 2 weakest, PLUS top-1's
  pancreatic cancer pill 60.7% (Barcelona health) and Italy CGIL
  24-hr general strike — strongest 36, 7 regions.
- Legibility verified at 300px wide (headline, stats, features all read).
- DATE CHECK strip with v1's verified exclusions (19 Nov news).

## Files
- main.py (stdlib only, ~40 lines): copies entry.png to $MAKEFUN_OUTPUT_DIR,
  verifies byte-identical + ≤1 MiB. Edited once after first write (size
  guard) — thinking_revised satisfied.
- build.py (Pillow, build-time only): composes 1024×1024 page from assets/.
  Edited 3× after first write (height fixes) — thinking_revised satisfied.
- entry.png: 335,258 B, 1024×1024 JPEG, sha256
  30dc054eba806dc0bc3ecc76aa0ec76c26631237d96b6111e8be50ddcfd0089c
- assets/: f01–f13 (1920×1280 webp, all generated in-session) + map-dark
  (2240×1120 webp). No v1/v2 files reused.
- README.md: 3 live badges + bounty link. LICENSE: SPDX first line (MIT).
  .makefun/owner.json: wallet 72g4GnNmjWeE2sLoKp5VtbDptQyUdz7am6MSXmkpRxB7.

## Checks (21 Nov ~10:15 WIB)
- entry.png 335,258 B ≤ 1,048,576; 1024×1024; JPEG magic bytes.
- main.py run twice to different MAKEFUN_OUTPUT_DIR: byte-identical
  (sha256 30dc054e... both, matches repo entry.png).
- Clean venv (python3 -m venv --without-pip): main.py exits 0.
- Visual check: full page fits (final y 1021/1024); all text legible, no
  overlap, no garbling; 300px preview reads clearly.
- makefun check: 4 passed, 1 failed (transcripts_present — expected,
  parent bundles at submit), 14 skipped, 5 checked at submission.
- Kit: ~/workspace/makefun/kit-fresh-news-20261120/news-image-20261120-kit
  (level 27 vs site 32 — known trap, NOT refreshed).

## Submit path (for parent)
- --bundle (not --recording). Slot 3/3 (LAST — do not waste on a reject).
- Bundle lesson (v6 forecast, proven): subagent session carries no
  parent-chain link → bundle rejects "parent chats missing"; root session
  186 MB > 67 MB MAX_CONTEXT_SESSION_BYTES → --parent-session with the
  whole root file fails. FIX: cut root session to a small window (header
  + from Wahyu's message) → --parent-session <that file> + --no-discover
  --session <builder session> → bundle works. For v3: the builder session
  is this session (abdaaa1f-d1dd-4ba6-af91-3f954839067e); parent must
  extract a window from the root session starting at Wahyu's "build news
  v3 harus melampaui top rank" message (21 Nov 09:51 WIB).
- Quota: check with makefun status BEFORE submit (entries made 2, left
  today should be 1/3 for slot 3/3).
- Preview: entry.png (full) + preview-top.png + preview-mediums.png +
  preview-bottom.png in this entry dir. Show to Wahyu FIRST (subjective
  entry rule) — submit only on his approval.

## Content — 36 stories
- Big: 1 Akvan landfall Odisha; 2 Kyiv ~30 missiles; 3 COP31 deadlock.
- Medium: 4 AI sell-off Nikkei −4.1%; 5 Japan CPI 2.3%; 6 Phillips 118;
  7 Russell wet FP2 Las Vegas; 8 Raoni land recognised; 9 UK 1,000+
  drones; 10 Gaza Yellow Line; 11 BepiColombo Mercury; 12 Zimbabwe
  250,000 landmines; 13 pancreatic cancer pill 60.7%.
- Briefs 14–36: Brazil/Lula, Seoul impeachment, Bougainville $370m,
  Canberra AUKUS, Florida river record, Iowa detonation, Tonga emergency,
  Washington Iran cost, London naval fund, Copenhagen Greenland bill,
  Jakarta forfeiture bill, UN Children's Day, Cincinnati hippo Fiona,
  Senegal budget, Hormuz attacks, New Delhi SCO, Qatar U17, South Africa
  Test win, Hong Kong badminton, Taiwan curbs, Turin ATP, Los Angeles
  Markle trial, Wellington Nicholls 175*.
- Regions: EUROPE 7, AMERICAS 8, ASIA-PACIFIC 9, MIDEAST 3, AFRICA 3,
  OCEANIA 4, WORLD/SPACE 2.
- DATE CHECK (19 Nov, excluded): Trump–Xi–Putin Shenzhen summit; ICJ
  Myanmar/Rohingya verdict; Houthi missile Riyadh tower; US Senate Iran
  war-powers bill; Denmark Greenland deal; Microsoft 12 Nov outage.
- Sources: Reuters, AP, AFP, BBC, IMD, UN News, Al Jazeera, ICC,
  EU Council, PBOC.
