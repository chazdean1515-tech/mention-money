# Mention Money

Best value bets on Kalshi mention markets. It is a read-only, mobile-friendly board for Kalshi "Mentions" markets (will a speaker say word X at an event). There is no trading and no login.

## Layout
- `fetch.py`: pulls open Mentions markets from the public Kalshi API into `data/markets.json`. It caches each series in `data/cache/`.
- `data/analysis.json`: my per-word probability estimates, reasons and sources. It is generated from `research/analysis_*.py` by `research/build_analysis.py`.
- `index.html`, `app.js`, `style.css`: a static site. Edge is computed live in the browser from the current prices in `markets.json`.
- `screenshot.py`: headless Chromium screenshots to `screenshots/`.
- `research/`: word counters (`count.py` for Trump transcripts, `ec_count.py` for earnings calls) and the word lists.

## Refresh
```bash
cd /workspace/mentions-app
python3 fetch.py                      # scan up to 15 min (resumable; skips series cached < 60 min ago)
python3 fetch.py --budget 3600        # longer scan -> more of the ~450 series
python3 fetch.py --only KXTRUMPMENTION,KXEARNINGSMENTIONCCL --max-age 0   # quick price refresh of specific series
python3 fetch.py --build-only         # rebuild markets.json from cache, no API calls
python3 research/build_analysis.py    # after editing research/analysis_*.py
python3 -m http.server 8080 --bind 127.0.0.1   # then open http://127.0.0.1:8080/
/workspace/.venv-pw/bin/python screenshot.py
```

## Play of the Day & tips
- `research/build_analysis.py` also writes `play_of_the_day` into `data/analysis.json`: the largest after-fee edge (≥5¢) among open, analyzed markets whose event hasn't started, with a two-sided quote (bid > 0, spread ≤ 10¢) and some volume. Medium-or-better confidence, non-fragile picks are preferred (tier 1), then any non-fragile pick, then fragile ones. Picks within 2¢ of the top edge go to the soonest event. Fragile flags live in the analysis modules (`"fragile"` on a word, `"fragile_sides"` on an event). The daily fetch + build + publish run refreshes it.
- "Tip the House ◎ SOL" opens a panel with the Solana address and a local QR code (`assets/sol-qr.svg`, made with segno).
- **Spin the Wheel**: `build_analysis.py` also writes `wheel_plays`, which has 4 play types, each with a primary pick and up to 3 alternates, all drawn from the same eligible pool as the Play of the Day. Non-fragile picks always rank first. BOMB is the biggest edge at ≤30¢. RETIREMENT is the highest win probability for our side (≥75%). ROLLS-ROYCE is the biggest edge with Medium-or-better confidence, and it skips the Play of the Day pick if it can. CASH is the best edge on events starting within 48h. The four slots prefer distinct picks. When the page loads, it skips any pick whose event has already started. The wheel is free: it's just a reveal, with no wallet or payment.
- `screenshot_wheel.py`: wheel screenshots (before a spin, the result, mobile) and checks that the wheel spins on click or Enter and ignores clicks during a spin.
- `screenshot_potd.py`: screenshots of the hero card and the tip panel, and it checks the copy button.

## Notes
- The unauthenticated Kalshi API was throttling hard from this box (most calls got 429), so a full scan of all ~450 Mentions series takes hours. The scan goes in priority order: Trump/press series first, then this week's earnings, then recently updated series, then by volume.
- Event dates come from the event ticker (e.g. `-26SEP29`). Kalshi's `expected_expiration` is about 2 weeks after the event. Kalshi's ticker date can also differ from the real call date (Carnival: ticker SEP28, call Sep 29; Nike: ticker SEP29, call Oct 1).
- Edge = estimate − price paid − 0.07·p·(1−p) (taker fee per contract). YES is bought at the yes ask, NO at the no ask. Items with edge ≥ 5¢ are highlighted.
- The estimates are judgment calls based on transcript base rates. They are not advice.

## Live site & republishing
Live: https://chazdean1515-tech.github.io/mention-money/ (GitHub Pages, served from `main` branch root; `.nojekyll` disables Jekyll).

After a refresh (`python3 fetch.py`, `python3 research/build_analysis.py`), republish with one command:
```bash
./publish.sh                    # commits data/markets.json, data/analysis.json and any changed app files, then pushes
./publish.sh "custom message"   # optional commit message
```
It validates the JSON first, does nothing if nothing changed, and Pages redeploys within a minute or two. Raw API caches (`data/cache/`, `data/series.json`, `data/event_titles.json`), `__pycache__/`, venvs and logs are git-ignored and never published.
