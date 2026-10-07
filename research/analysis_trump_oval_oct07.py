# KXTRUMPMENTIONB-26OCT07: Trump Oval Office announcement, Wed Oct 7 2026, 1:00 p.m. ET (White House schedule).
# The subject was not announced. Reference: the settled Peterbilt remarks (KXTRUMPMENTIONB-26OCT01). Nothing else is counted.
EVENT = "KXTRUMPMENTIONB-26OCT07"
P = EVENT + "-"
DATA = {
  "title": "Trump Oval Office announcement",
  "speaker": "Donald Trump",
  "event_time_et": "2026-10-07T13:00:00-04:00",
  "event_time_note": "White House daily guidance: 1:00 p.m. ET, THE PRESIDENT makes an Announcement, Oval Office, pool coverage. He leaves for San Antonio afterward.",
  "context": ("The topic is unannounced, so every word depends on what he announces and whether he takes questions. "
              "Oval announcements usually run long with a press Q&A, which pulls in Iran, China, Russia, Biden and oil. "
              "Markets are thin with wide spreads; estimates stay close to the market."),
  "fragile_sides": {"YES": "The topic is unknown; a short scripted signing could skip most words.",
                    "NO": "The topic is unknown; a long Q&A can bring up almost anything."},
  "confidence": "Low. The subject is unannounced.",
  "method": "Market-anchored, adjusted lightly using the settled Peterbilt remarks on Oct 1 (Investment, Manufacturing, Stock Market, Iran, Nuclear, China, Inflation, Biden, Tariff, Oil all hit).",
  "sources": [
    {"title": "White House schedule for Oct 7 (via TradingView/MNI)", "url": "https://www.tradingview.com/news/macenews:2741288df094b:0-wednesday-white-house-schedule-president-trump-makes-an-announcement-at-1p-et-then-travels-to-san-antonio/"},
    {"title": "Kalshi settlements: KXTRUMPMENTIONB-26OCT01", "url": "https://kalshi.com/markets/kxtrumpmentionb"},
  ],
  "words": {
    P+"OIL":  {"p": 0.74, "reason": "Hit at Peterbilt; oil and diesel prices are a live White House theme. Fair."},
    P+"DEAL": {"p": 0.72, "reason": "Topic unknown. Fair."},
    P+"NUCL": {"p": 0.70, "reason": "Hit at Peterbilt. Fair."},
    P+"CHIN": {"p": 0.74, "reason": "Hit at Peterbilt; a Q&A almost always gets there. Fair."},
    P+"BIDE": {"p": 0.72, "reason": "Hit at Peterbilt. Fair."},
    P+"RUSS": {"p": 0.66, "reason": "Topic unknown. Fair."},
    P+"INFL": {"p": 0.66, "reason": "Hit at Peterbilt. Fair; wide spread."},
    P+"IRAN": {"p": 0.60, "reason": "Contract needs 3+ mentions. Fair."},
    P+"INVE": {"p": 0.64, "reason": "Hit at Peterbilt. Fair."},
    P+"TARI": {"p": 0.68, "reason": "Hit at Peterbilt. Fair; wide spread."},
    P+"ISRA": {"p": 0.50, "reason": "Topic unknown. Fair."},
    P+"MIDT": {"p": 0.36, "reason": "Topic unknown. Fair; wide spread."},
    P+"BLOC": {"p": 0.33, "reason": "Topic unknown. Fair; wide spread."},
    P+"HOTT": {"p": 0.45, "reason": "Missed at Peterbilt, hit in Mobile. Fair."},
    P+"STEE": {"p": 0.35, "reason": "Topic unknown. Fair; wide spread."},
    P+"MANU": {"p": 0.38, "reason": "Hit at Peterbilt (a factory). Fair; wide spread."},
    P+"NEGO": {"p": 0.33, "reason": "Topic unknown. Fair; wide spread."},
    P+"SUPE": {"p": 0.35, "reason": "Only likely if the announcement is about AI. Fair."},
    P+"HEAL": {"p": 0.32, "reason": "Topic unknown. Fair; wide spread."},
    P+"AI":   {"p": 0.37, "reason": "Missed at Peterbilt. Fair; wide spread."},
    P+"SUPR": {"p": 0.28, "reason": "Topic unknown. Fair."},
    P+"STOC": {"p": 0.30, "reason": "Hit at Peterbilt. Fair."},
    P+"JAPA": {"p": 0.33, "reason": "Topic unknown. Fair; wide spread."},
    P+"AFFO": {"p": 0.21, "reason": "Topic unknown. Fair."},
    P+"TAIW": {"p": 0.16, "reason": "Topic unknown. Fair."},
    P+"FENT": {"p": 0.12, "reason": "Topic unknown. Fair."},
    P+"CRYP": {"p": 0.04, "reason": "Missed at Peterbilt. Fair."},
    P+"NQE":  {"p": 0.03, "reason": "On the official schedule with pool coverage."},
  },
}
