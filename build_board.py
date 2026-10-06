#!/usr/bin/env python3
"""Write the lean snapshot the page actually loads (data/board.js).

Keeps data/markets.json and data/analysis.json as the research files.
The page does not fetch those. Rules text is stored once per event, and
word notes are the readable prose only.
"""
import json, os

HERE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(HERE, "data")

POTD_KEYS = (
    "event_title", "word", "side", "price", "est_yes", "est_side", "edge", "fee",
    "event_time_et", "close_time_et", "price_fetched_at_et", "rationale", "url", "confidence",
)


def slim_market(m):
    keep = ("ticker", "word", "yes_bid", "yes_ask", "no_bid", "no_ask", "last_price", "volume", "status", "close_time_et")
    return {k: m.get(k) for k in keep}


def slim_event(e):
    markets = e.get("markets") or []
    first = markets[0] if markets else {}
    return {
        "event_ticker": e.get("event_ticker"),
        "series_ticker": e.get("series_ticker"),
        "series_title": e.get("series_title"),
        "title": e.get("title"),
        "sub_title": e.get("sub_title"),
        "event_date": e.get("event_date"),
        "first_close_et": e.get("first_close_et"),
        "price_fetched_at_et": e.get("price_fetched_at_et"),
        "decided": e.get("decided"),
        "total_volume": e.get("total_volume"),
        "rules_primary": first.get("rules_primary") or "",
        "rules_secondary": first.get("rules_secondary") or "",
        "markets": [slim_market(m) for m in markets],
    }


def slim_analysis(an):
    events = {}
    for ticker, ev in (an.get("events") or {}).items():
        words = {}
        for wt, w in (ev.get("words") or {}).items():
            if not isinstance(w, dict):
                continue
            note = w.get("prose") or w.get("reason") or ""
            item = {"p": w.get("p"), "prose": note}
            if w.get("fragile"):
                item["fragile"] = True
            words[wt] = item
        events[ticker] = {
            "title": ev.get("title"),
            "speaker": ev.get("speaker"),
            "event_time_et": ev.get("event_time_et"),
            "event_time_note": ev.get("event_time_note"),
            "context": ev.get("context"),
            "confidence": ev.get("confidence"),
            "method": ev.get("method"),
            "sources": ev.get("sources") or [],
            "words": words,
        }
    potd = an.get("play_of_the_day") or None
    if potd:
        potd = {k: potd.get(k) for k in POTD_KEYS}
    return {
        "updated_at_et": an.get("updated_at_et"),
        "min_edge": an.get("min_edge", 0.05),
        "play_of_the_day": potd,
        "events": events,
    }


def main():
    mk = json.load(open(os.path.join(DATA, "markets.json")))
    an = json.load(open(os.path.join(DATA, "analysis.json")))
    board = {"mk": {"fetched_at_et": mk.get("fetched_at_et"), "events": [slim_event(e) for e in mk.get("events") or []]},
             "an": slim_analysis(an)}
    raw = json.dumps(board, ensure_ascii=False, separators=(",", ":"))
    # Keep the file a script even if a note contains a literal line separator.
    raw = raw.replace("\u2028", "\\u2028").replace("\u2029", "\\u2029")
    path = os.path.join(DATA, "board.js")
    with open(path, "w") as fh:
        fh.write("window.MM_BOARD=" + raw + ";\n")
    print(f"wrote {path} ({os.path.getsize(path)} bytes)")


if __name__ == "__main__":
    main()
