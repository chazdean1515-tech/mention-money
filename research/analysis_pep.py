# KXEARNINGSMENTIONPEP-26OCT08: PepsiCo Q3 2026 results, Thu Oct 8 2026. Live analyst Q&A at 8:15 a.m. ET.
# PepsiCo posts prepared remarks in writing at ~6:00 a.m. and the live call is Q&A only, so scripted words may never be spoken.
EVENT = "KXEARNINGSMENTIONPEP-26OCT08"
P = EVENT + "-"
DATA = {
  "title": "PepsiCo Q3 2026 earnings call",
  "speaker": "PepsiCo management (Ramon Laguarta, Steve Schmitt)",
  "event_time_et": "2026-10-08T08:15:00-04:00",
  "event_time_note": "PepsiCo: release, 10-Q and prepared remarks posted around 6:00 a.m. EDT; live Q&A with the CEO and CFO at 8:15 a.m. EDT.",
  "context": ("The test this quarter is whether February's price cuts of up to 15% on Lay's and Doritos bought volume in North American snacks. "
              "Volume and affordability are near-certain Q&A topics. Protein, fiber and prebiotic sodas (Poppi) are the product story; Celsius is the energy partner. "
              "Because the spoken call is Q&A only, product words depend on what analysts ask."),
  "fragile_sides": {"YES": "The live call is analyst Q&A only; anything that lives in the written remarks may not be said aloud."},
  "confidence": "Low-medium. No transcript count this run; estimates sit near the market.",
  "method": "Judgment from the call format and the Q3 preview themes, anchored to market mid-prices.",
  "sources": [
    {"title": "PepsiCo: timing of Q3 2026 results", "url": "https://www.pepsico.com/newsroom/press-releases/2026/pepsico-announces-timing-and-availability-of-third-quarter-2026-financial-results"},
    {"title": "Pip Theory: PepsiCo Q3 2026 earnings preview", "url": "https://piptheory.com/research/pepsico-q3-2026-earnings-preview-frito-lay-pricing"},
  ],
  "words": {
    P+"VOLU": {"p": 0.97, "reason": "Volume after the price cuts is the main question of the quarter. Fair."},
    P+"AFFO": {"p": 0.92, "reason": "Affordability is how management frames the price cuts. Fair."},
    P+"AWAY": {"p": 0.88, "reason": "A standard PepsiCo channel term, but it needs an analyst or answer to go there. Fair."},
    P+"PROT": {"p": 0.70, "reason": "Protein launches are a growth talking point. Fair."},
    P+"TARI": {"p": 0.62, "reason": "Cost questions now lean on oil and packaging more than tariffs. Fair."},
    P+"CELS": {"p": 0.62, "reason": "Energy drinks come up most quarters. Fair."},
    P+"CHIN": {"p": 0.50, "reason": "Fair."},
    P+"WORL": {"p": 0.40, "reason": "The quarter covered the World Cup, but Q&A may not revisit it. Fair."},
    P+"FIBE": {"p": 0.36, "reason": "Fair."},
    P+"ACQU": {"p": 0.34, "reason": "Fair."},
    P+"GLP":  {"p": 0.30, "reason": "Fair."},
    P+"ARTI": {"p": 0.25, "reason": "Fair."},
    P+"PREB": {"p": 0.18, "reason": "Fair."},
    P+"AUTO": {"p": 0.08, "reason": "Fair."},
    P+"BUBL": {"p": 0.04, "reason": "Fair."},
    P+"FOOD": {"p": 0.03, "reason": "Fair."},
  },
}
