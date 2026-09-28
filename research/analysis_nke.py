# KXEARNINGSMENTIONNKE-26SEP29: Nike Q1 FY27 earnings call (Kalshi ticker says SEP29; Nike IR: Thu Oct 1, 2:00pm PT / 5:00pm ET).
EVENT = "KXEARNINGSMENTIONNKE-26SEP29"
P = EVENT + "-"
DATA = {
  "title": "Nike (NKE) Q1 FY27 earnings call",
  "speaker": "Nike (CEO Elliott Hill, CFO, IR Paul Trussell, operator)",
  "event_time_et": "2026-10-01T17:00:00-04:00",
  "event_time_note": "Nike IR: results after the close Thu Oct 1, call at 2:00pm PT (5:00pm ET). Kalshi's ticker says SEP29.",
  "context": ("Hill's turnaround story: tariffs are a big cost headwind (said 10–16 times per call), 'sustainable, profitable growth', "
              "supply chain, Converse weakness, wholesale 'partners' rather than 'retailers', 'Nike Direct' rather than 'DTC'. "
              "The June call mentioned an upcoming Investor Day 3 times. Alphafly 4 launched Sep 17, inside the quarter. Only Nike representatives count."),
  "confidence": "Medium. Only 3 complete transcripts (Q1, Q2, Q4 FY26); the Q3 text was truncated.",
  "method": "Company-speaker mention counts in Nike calls Sep 2025, Dec 2025, Jun 2026 (roic.ai / Earnings Whispers).",
  "sources": [
    {"title": "Nike IR: Q1 FY27 call Oct 1, 2pm PT", "url": "https://investors.nike.com/investors/news-events-and-reports/investor-news/investor-news-details/2026/NIKE-Inc--Announces-First-Quarter-Fiscal-2027-Earnings-and-Conference-Call/default.aspx"},
    {"title": "Nike Q4 FY26 transcript (Earnings Whispers)", "url": "https://beta.earningswhispers.com/transcript/NKE/Q42026"},
    {"title": "Nike transcripts (roic.ai)", "url": "https://www.roic.ai/quote/NKE/transcripts"},
    {"title": "Nike newsroom: Alphafly 4 launch Sep 17 2026", "url": "https://about.nike.com/en/newsroom/releases/nike-alphafly-4-helps-more-runners-go-the-distance-with-speed-and-confidence"},
  ],
  "words": {
    P+"TARF": {"p": 0.97, "reason": "Said 10–16 times in each of the last 3 calls. Fair at 96–97¢."},
    P+"SUPP": {"p": 0.93, "reason": "3/3 calls (5 in June). Fair."},
    P+"INVD": {"p": 0.88, "reason": "June call flagged an Investor Day 3 times, so a reminder is likely. Fair to slightly rich."},
    P+"SUST": {"p": 0.90, "reason": "'Sustainable, profitable growth' is Hill-era boilerplate: 3/3 calls. Fair."},
    P+"CONV": {"p": 0.92, "reason": "Converse in 3/3 calls (7, 6, 3). Fair."},
    P+"CAIT": {"p": 0.60, "reason": "2/3 calls, but it can come up through any 'Clark'. 70¢ is a bit rich for a mid-season-off quarter."},
    P+"ALPH": {"p": 0.55, "reason": "0/3 past calls, but Alphafly 4 launched Sep 17 inside the quarter and Hill likes to highlight running. Fair-ish."},
    P+"RETA": {"p": 0.38, "reason": "Only 1 mention in 3 calls. Nike says 'wholesale partners'. 57–58¢ looks rich. NO lean."},
    P+"DIVD": {"p": 0.55, "reason": "2/3 calls, usually in the CFO's capital-return line. Fair."},
    P+"SKIM": {"p": 0.40, "reason": "2/3 calls, 0 in June. Fair."},
    P+"SABR": {"p": 0.33, "reason": "2/3 calls, 0 in June. Fair."},
    P+"BEAV": {"p": 0.12, "reason": "0/3 calls. HQ city rarely named on the call. 22–23¢ looks rich."},
    P+"DTC":  {"p": 0.10, "reason": "0/3 calls; Nike says 'Nike Direct'. Slightly rich."},
    P+"MIAM": {"p": 0.06, "reason": "0/3 calls. Slightly rich at 11–12¢."},
  },
}
