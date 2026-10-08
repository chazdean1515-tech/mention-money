# KXDEBATEMENTION-26OCT08B: Georgia U.S. Senate debate, Jon Ossoff (D) vs. Mike Collins (R), Thu Oct 8 2026, 7:00 p.m. ET.
# No transcript corpus for these two candidates was counted. Estimates are judgment calls, anchored to the market.
EVENT = "KXDEBATEMENTION-26OCT08B"
P = EVENT + "-"
DATA = {
  "title": "Georgia U.S. Senate debate (Ossoff vs. Collins)",
  "speaker": "Jon Ossoff and Mike Collins",
  "event_time_et": "2026-10-08T19:00:00-04:00",
  "event_time_note": "Atlanta News First / Gray Media: 7:00 p.m. ET, one hour, at Assembly Atlanta. First televised meeting of the two.",
  "context": ("Either candidate saying a word counts. Ossoff has run for years on anti-corruption (a congressional stock-trading ban), so 'corrupt' is close to a signature word. "
              "Collins was the lead House sponsor of the Laken Riley Act and will press immigration (border, deportation). "
              "Ossoff will push healthcare cuts (Medicaid/Medicare) and abortion; Georgia's data-center and power-bill fights are a live state issue. "
              "Most markets are thin with wide spreads, so few leans qualify."),
  "confidence": "Low-medium. No transcript count; the candidates' core themes are well known.",
  "method": "Judgment from each candidate's signature issues, anchored to market mid-prices.",
  "sources": [
    {"title": "Atlanta News First: What to watch as Ossoff, Collins debate", "url": "https://www.atlantanewsfirst.com/2026/10/07/control-us-senate-line-what-watch-ossoff-collins-debate-thursday/"},
    {"title": "WTOC: How to watch the Collins-Ossoff debate", "url": "https://www.wtoc.com/2026/10/05/collins-ossoff-debate-how-watch-wtoc/"},
  ],
  "words": {
    P+"MEDI": {"p": 0.90, "reason": "A Democratic incumbent in 2026 will hit healthcare cuts. Fair; wide spread."},
    P+"CORR": {"p": 0.88, "reason": "Anti-corruption and the stock-trading ban are Ossoff's signature theme. YES lean."},
    P+"BORD": {"p": 0.86, "reason": "Collins runs on immigration. Fair; thin."},
    P+"LAKE": {"p": 0.84, "reason": "Collins sponsored the Laken Riley Act and cites it often. YES lean, wide spread."},
    P+"ABOR": {"p": 0.80, "reason": "Georgia's six-week ban makes this likely. Fair; wide spread."},
    P+"DATA": {"p": 0.74, "reason": "Data centers and Georgia Power bills are a live state fight. Fair; wide spread."},
    P+"TARI": {"p": 0.72, "reason": "Fair; wide spread."},
    P+"AI":   {"p": 0.72, "reason": "Fair; wide spread."},
    P+"CHIN": {"p": 0.70, "reason": "Fair; wide spread."},
    P+"SOCI": {"p": 0.70, "reason": "Fair; wide spread."},
    P+"TRUM": {"p": 0.66, "reason": "Contract needs 5+ mentions; Ossoff will tie Collins to Trump. Fair."},
    P+"DEPO": {"p": 0.70, "reason": "Fair; wide spread."},
    P+"SOCIA": {"p": 0.66, "reason": "Republicans use the socialist label often. Fair; wide spread."},
    P+"BILL": {"p": 0.68, "reason": "Fair; wide spread."},
    P+"ISRA": {"p": 0.58, "reason": "Fair; wide spread."},
    P+"FOST": {"p": 0.55, "reason": "Ossoff has made foster care and child welfare an issue. Fair; no trades yet."},
    P+"FILI": {"p": 0.50, "reason": "Fair; wide spread."},
    P+"FENT": {"p": 0.35, "reason": "Fair; wide spread."},
    P+"HARR": {"p": 0.28, "reason": "Fair; wide spread."},
    P+"CRYP": {"p": 0.22, "reason": "Fair; wide spread."},
    P+"NQE":  {"p": 0.03, "reason": "Scheduled and widely promoted."},
  },
}
