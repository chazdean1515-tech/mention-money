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
