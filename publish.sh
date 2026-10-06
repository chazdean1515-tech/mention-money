#!/usr/bin/env bash
# Republish Mention Money to GitHub Pages: rebuild the lean board payload, commit, then push to main.
# Pages source stays "Deploy from a branch", main, folder / (root).
# _config.yml (Jekyll) excludes this script, fetch.py, research/, and the README from the domain.
# Do not add a .nojekyll file back, or those files are served on mentionmoney.com again.
# Usage: ./publish.sh ["optional commit message"]
set -euo pipefail
cd "$(dirname "$0")"
python3 build_board.py
# Custom domain is the apex (it has the working certificate; www redirects to it).
# Don't flip this back and forth: every change restarts GitHub's certificate request.
printf 'mentionmoney.com' > CNAME
for f in data/markets.json data/analysis.json; do
  python3 -c "import json,sys; json.load(open(sys.argv[1]))" "$f" || { echo "invalid JSON: $f" >&2; exit 1; }
done
python3 -c 'import json; raw=open("data/board.js").read().strip(); assert raw.startswith("window.MM_BOARD=") and raw.endswith(";"); json.loads(raw[len("window.MM_BOARD="):-1])'
git add CNAME _config.yml robots.txt sitemap.xml favicon.ico apple-touch-icon.png \
  data/markets.json data/analysis.json data/last_potd.json data/board.js \
  index.html about.html contact.html privacy.html terms.html 404.html \
  app.js style.css build_board.py README.md fetch.py screenshot.py screenshot_potd.py publish.sh .gitignore \
  research/ assets/
git add screenshots/*.png 2>/dev/null || true
# Stage intentional removals (retired files, the old collage, .nojekyll).
git add -u screenshot_wheel.py screenshots/live-wheel.png screenshots/wheel-desktop.png screenshots/wheel-mobile-result.png screenshots/wheel-mobile.png screenshots/wheel-result.png assets/collage-bg.jpg assets/og-image.png .nojekyll 2>/dev/null || true
if git diff --cached --quiet; then
  echo "Nothing changed; nothing to publish."
  exit 0
fi
msg="${1:-Data refresh $(TZ=America/New_York date '+%Y-%m-%d %H:%M ET')}"
git commit -q -m "$msg"
git push -q origin main
echo "Pushed. Live in ~1 min: https://mentionmoney.com/"
