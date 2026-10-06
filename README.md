# Mention Money

Daily research on Kalshi Mentions markets. It is a read-only, mobile-friendly board for Kalshi Mentions markets (will a speaker say a word at an event). The board shows only events whose researched real start is today in America/New_York. There is no trading and no login.

The page shows each word's note, our probability estimate, the snapshot YES price, and the gap after the taker-fee estimate. "Our lean" is an opinion, not an instruction to trade.

## Layout
- `fetch.py`: pulls open Mentions markets from the public Kalshi API into `data/markets.json`. It caches each series in `data/cache/`.
- `data/analysis.json`: per-word probability estimates, reasons, and sources. It is generated from `research/analysis_*.py` by `research/build_analysis.py`. Short reasons are expanded into grammatical notes by `research/notes.py` at build time. Hand-written paragraphs (the `prose` field) are kept.
- `build_board.py`: writes `data/board.js`, the lean snapshot the page loads. The browser does not fetch `markets.json` or `analysis.json`.
- `index.html`, `app.js`, `style.css`: the static site. About, Contact, Privacy, and Terms are separate pages. `404.html` is the GitHub Pages missing-page file.
- `screenshot.py`: headless Chromium screenshots to `screenshots/`.
- `research/`: word counters (`count.py` for Trump transcripts, `ec_count.py` for earnings calls) and the word lists.

## Refresh
```bash
python3 fetch.py                      # scan up to 15 min (resumable; skips series cached < 60 min ago)
python3 fetch.py --budget 3600        # longer scan -> more of the ~450 series
python3 fetch.py --only KXTRUMPMENTION,KXEARNINGSMENTIONCCL --max-age 0   # quick price refresh of specific series
python3 fetch.py --build-only         # rebuild markets.json from cache, no API calls
python3 research/build_analysis.py    # after editing research/analysis_*.py
python3 build_board.py                # refresh data/board.js (publish.sh does this)
python3 -m http.server 8080 --bind 127.0.0.1   # then open http://127.0.0.1:8080/
python3 screenshot.py
```

## Play of the Day and support
- `research/build_analysis.py` also writes `play_of_the_day` into `data/analysis.json`: the largest after-fee gap (≥5¢) among open, analyzed markets happening today whose event hasn't started, with a two-sided quote (bid > 0, spread ≤ 10¢) and some volume. Medium-or-better confidence, non-fragile picks are preferred (tier 1), then any non-fragile pick, then fragile ones. Picks within 2¢ of the top gap go to the soonest event. Fragile flags live in the analysis modules (`"fragile"` on a word, `"fragile_sides"` on an event). The daily fetch + build + publish run refreshes it. The card says "Our lean", not a buy instruction.
- **Kalshi referral**: the signup URL is `data-kalshi-ref` on `<body>` in `index.html` (not in `data/`, so the daily fetch/build never touches it). It shows as a green "New to Kalshi? Sign up" link on the Play of the Day, in the header (hidden under 480px wide), and in the footer. Each visible link has the same disclosure next to it, including the desktop header: "18+ only. Availability depends on Kalshi's eligibility rules. You can lose money. Not financial advice. Mention Money earns a bonus if you sign up and trade with this link." Links use `rel="sponsored noopener"`.
- "Support Mention Money" opens a panel with the Solana address and a local QR code (`assets/sol-qr.svg`, made with segno).
- **Today-only research board**: `research/build_analysis.py` restricts Play of the Day candidates to events whose researched `event_time_et` date is today in America/New_York. The page applies the same filter. The "Analyzed only" checkbox hides today's events that have no write-up; leaving it unchecked shows them. The tape omits windows that have already started, labels prices in cents, and shows "NOT LIVE" when the snapshot is more than three hours old.
- `screenshot_potd.py`: screenshots of the hero card and the support panel, and it checks the copy button.

## Notes
- The unauthenticated Kalshi API was throttling hard (most calls got 429), so a full scan of all ~450 Mentions series takes hours. The scan goes in priority order: Trump/press series first, then this week's earnings, then recently updated series, then by volume.
- Event dates come from the event ticker (e.g. `-26SEP29`). Kalshi's `expected_expiration` is about 2 weeks after the event. Kalshi's ticker date can also differ from the real call date (Carnival: ticker SEP28, call Sep 29; Nike: ticker SEP29, call Oct 1).
- Gap = estimate − price paid − 0.07·p·(1−p) (taker fee per contract). YES is priced at the yes ask, NO at the no ask. A lean is shown when that gap is at least 5¢, the quote is two-sided with a spread of 10¢ or less, and the speaking window has not started.
- The estimates are judgment calls based on transcript base rates. They are not advice.
- `fetch.py` no longer publishes `series_scanned` / `series_total`. That pair printed as "103/16" when the builder counted every cache file against a short series list. The page says how many events and series are in the snapshot.

## Live site and republishing
Live: https://mentionmoney.com/ (GitHub Pages, custom domain).

**Pages source stays "Deploy from a branch", branch `main`, folder `/` (root).** No setting change is required for this layout. There is no `.nojekyll` file. `_config.yml` tells Jekyll to exclude `README.md`, `fetch.py`, `publish.sh`, the screenshot scripts, `build_board.py`, `.gitignore`, `research/`, and `screenshots/` so those are not served on the domain. Do not add `.nojekyll` back, or GitHub Pages will publish them again. `CNAME` is included on purpose.

The old address, https://chazdean1515-tech.github.io/mention-money/, redirects to the domain. DNS is at Porkbun: four apex A records to 185.199.108.153–111.153, plus `www` CNAME → `chazdean1515-tech.github.io`.

**www certificate:** https://www.mentionmoney.com can show a name-mismatch warning because the certificate covers the apex only. That is a GitHub Pages setting, not something this repo can change. In the repo Settings → Pages, remove and re-save the custom domain so GitHub reissues a certificate that includes `www`, then confirm Enforce HTTPS.

After a refresh (`python3 fetch.py`, `python3 research/build_analysis.py`), republish with one command:
```bash
./publish.sh                    # rebuilds data/board.js, commits data and app files, then pushes
./publish.sh "custom message"   # optional commit message
```
It validates the JSON first, does nothing if nothing changed, and Pages redeploys within a minute or two. Raw API caches (`data/cache/`, `data/series.json`, `data/event_titles.json`), `__pycache__/`, venvs and logs are git-ignored and never published.

Contact is https://x.com/MentionMoneyHQ until the domain has an email address. Do not invent one.
