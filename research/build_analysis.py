#!/usr/bin/env python3
"""Assemble data/analysis.json from per-event analysis modules in this folder (analysis_*.py)."""
import glob, importlib.util, json, os
from datetime import datetime
from zoneinfo import ZoneInfo
HERE = os.path.dirname(os.path.abspath(__file__))
out = {"updated_at_et": datetime.now(ZoneInfo("America/New_York")).isoformat(timespec="seconds"),
       "min_edge": 0.05,
       "fee_model": "Kalshi taker fee ≈ ceil(0.07·C·p·(1−p)) dollars; edge = est − price − 0.07·p·(1−p) per contract",
       "events": {}}
for f in sorted(glob.glob(os.path.join(HERE, "analysis_*.py"))):
    spec = importlib.util.spec_from_file_location(os.path.basename(f)[:-3], f)
    mod = importlib.util.module_from_spec(spec); spec.loader.exec_module(mod)
    out["events"][mod.EVENT] = mod.DATA
path = os.path.join(HERE, "..", "data", "analysis.json")
json.dump(out, open(path, "w"), indent=1, ensure_ascii=False)
print("wrote", os.path.normpath(path), "events:", list(out["events"]))
