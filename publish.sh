#!/usr/bin/env bash
# Republish Mention Money to GitHub Pages: commit updated data/*.json and app files, then push to main.
# Usage: ./publish.sh ["optional commit message"]
set -euo pipefail
cd "$(dirname "$0")"
# Validate JSON the page needs before publishing (avoid pushing a half-written file)
for f in data/markets.json data/analysis.json; do
  python3 -c "import json,sys; json.load(open(sys.argv[1]))" "$f" || { echo "invalid JSON: $f" >&2; exit 1; }
done
git add CNAME data/markets.json data/analysis.json index.html app.js style.css README.md fetch.py screenshot.py screenshot_potd.py screenshot_wheel.py publish.sh .gitignore .nojekyll research/ assets/
git add screenshots/*.png 2>/dev/null || true
if git diff --cached --quiet; then
  echo "Nothing changed; nothing to publish."
  exit 0
fi
msg="${1:-Data refresh $(TZ=America/New_York date '+%Y-%m-%d %H:%M ET')}"
git commit -q -m "$msg"
git push -q origin main
echo "Pushed. Live in ~1 min: https://mentionmoney.com/"
