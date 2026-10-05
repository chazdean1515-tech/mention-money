# KXEARNINGSMENTIONSTZ-26OCT05: Constellation Brands Q2 FY27 earnings call.
EVENT = "KXEARNINGSMENTIONSTZ-26OCT05"
P = EVENT + "-"
DATA = {
  "title": "Constellation Brands (STZ) Q2 FY27 earnings call",
  "speaker": "Constellation Brands (CEO Nick Fink, CFO Garth Hankinson, IR, operator)",
  "event_time_et": "2026-10-07T08:00:00-04:00",
  "event_time_note": "Constellation Brands IR (Sep 10, 2026): results Tue Oct 6 after the close, conference call Wed Oct 7 at 8:00 a.m. ET. Kalshi's Oct 5 ticker date is not the call date.",
  "context": ("Beer-driven story (Modelo Especial, Pacifico, Corona). 'Depletions' is their core beer KPI and comes up every call. "
              "Wine divestiture talk has faded (0 wine mentions in the July call). Aluminum/tariff costs came up during tariff quarters. "
              "Spreads are wide (5–7¢), so edges must clear the spread too."),
  "confidence": "Low-medium. The available transcripts look partial (~3–4k company words), which biases hit rates DOWN.",
  "method": "Company-speaker counts in 4 calls (Oct 2025, Jan 2026, Apr 2026, Jul 2026) from roic.ai / Earnings Whispers.",
  "sources": [
    {"title": "Constellation Brands IR: Q2 FY27 results Oct 6, call Oct 7 at 8:00 a.m. ET", "url": "https://ir.cbrands.com/news-events/press-releases/detail/345/constellation-brands-to-report-second-quarter-fiscal-2027-financial-results-on-october-6-2026-after-market-close-and-host-conference-call-on-october-7-2026-at-8-00-am-et"},
    {"title": "STZ Q1 FY27 transcript (Earnings Whispers)", "url": "https://beta.earningswhispers.com/transcript/STZ/Q12027"},
    {"title": "STZ transcripts (roic.ai)", "url": "https://www.roic.ai/quote/STZ/transcripts"},
    {"title": "Earnings calendar week of Sep 28 2026", "url": "https://fffinstill.com/earnings-calendar/week/2026-09-28"},
  ],
  "words": {
    P+"DEPL": {"p": 0.95, "reason": "'Depletions' is STZ's headline beer metric: 4/4 calls even in partial transcripts."},
    P+"PACI": {"p": 0.85, "reason": "Pacifico in 4/4 calls (a growth brand)."},
    P+"ESPE": {"p": 0.70, "reason": "'Modelo Especial' is the #1 brand: 3/4 calls even in partial text. 51¢ ask looks cheap."},
    P+"INVE": {"p": 0.65, "reason": "3/4 calls (distributor inventory levels). Fair."},
    P+"WINE": {"p": 0.50, "reason": "2/4 calls, 0 in July after the divestiture. Fair to rich."},
    P+"TARI": {"p": 0.50, "reason": "3/4 calls, 0 in July. Fair."},
    P+"VICT": {"p": 0.45, "reason": "Brand (Victoria), 2/4 calls. Fair."},
    P+"OIL":  {"p": 0.50, "reason": "2/4 calls; 4 mentions in July (fuel/energy costs). Fair."},
    P+"INFL": {"p": 0.45, "reason": "2/4 calls. Fair to slightly rich."},
    P+"MI":   {"p": 0.30, "reason": "0/4 in Earnings Whispers text (1 in one roic copy); tequila is a minor brand. 47–50¢ looks rich (low confidence)."},
    P+"ALUM": {"p": 0.35, "reason": "2/4 calls (aluminum tariffs). Fair."},
    P+"DIVI": {"p": 0.25, "reason": "1/4 calls. Slightly rich."},
    P+"ICE":  {"p": 0.03, "reason": "0/4. Fair."},
  },
}
