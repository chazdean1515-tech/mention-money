# KXBOWMANMENTION-26OCT06: Fed Vice Chair for Supervision Michelle Bowman, morning keynote, 2026 Community Banking Research
# Conference, Federal Reserve Bank of St. Louis, Tue Oct 6 2026. Counts are from her 12 published speech texts most relevant
# to this audience (Oct 2025 - Oct 2026, federalreserve.gov) plus the two settled KXBOWMANMENTION events. Nothing else is counted.
EVENT = "KXBOWMANMENTION-26OCT06"
P = EVENT + "-"
DATA = {
  "title": "Bowman keynote at the Community Banking Research Conference (St. Louis Fed)",
  "speaker": "Michelle Bowman",
  "event_time_et": "2026-10-06T10:45:00-04:00",
  "event_time_note": "St. Louis Fed release and agenda: keynote at 9:45 a.m. CT (10:45 a.m. ET), introduced by St. Louis Fed President Alberto Musalem; break at 10:30 a.m. CT. Livestream at communitybanking.org.",
  "context": ("A community-bank audience, so expect the community bank leverage ratio (cut to 8% this year), streamlined merger and de novo reviews, "
              "and supervisory transparency. Prepared texts: Leverage Ratio 7 of 12, Merger 6 of 12, Transparency 6 of 12, Cyber 4 of 12, President 4 of 12, "
              "AI 3 of 12, Inflation 3 of 12, SVB 3 of 12, Stress Test 2 of 12, Basel III 1 of 12, Crypto 0 of 12. "
              "Her two settled Kalshi events hit far more words than the prepared texts did (AI, Inflation, Basel III, Stress Test all hit Oct 1), because Q&A counts. "
              "The 45-minute slot leaves room for Q&A, so NO leans that depend on a short scripted speech are flagged fragile."),
  "fragile_sides": {"NO": "NO leans assume a scripted community-bank speech with little or no Q&A; an open Q&A can bring up almost any topic."},
  "confidence": "Medium-low. Real text counts, but the Q&A format is unknown.",
  "method": "Word presence in 12 published Bowman speech texts (federalreserve.gov) plus the 2 settled KXBOWMANMENTION events, weighted toward community-bank speeches.",
  "sources": [
    {"title": "St. Louis Fed: 2026 Community Banking Research Conference, Bowman at 9:45 a.m. CT Oct. 6", "url": "https://www.stlouisfed.org/news-releases/2026/09/register-now-for-the-2026-community-banking-research-conference"},
    {"title": "Conference agenda (communitybanking.org)", "url": "https://www.communitybanking.org/conferences/2026"},
    {"title": "Bowman, Welcome Remarks, 2025 Community Banking Research Conference", "url": "https://www.federalreserve.gov/newsevents/speech/bowman20251007a.htm"},
    {"title": "Bowman, Opening Remarks, KC Fed Future of Banking (May 2026)", "url": "https://www.federalreserve.gov/newsevents/speech/bowman20260514a.htm"},
    {"title": "Kalshi settlements: KXBOWMANMENTION-26SEP18 / 26OCT01", "url": "https://kalshi.com/markets/kxbowmanmention"},
  ],
  "words": {
    P+"LEVE": {"p": 0.78, "reason": "7 of 12 texts and 6 of 8 community-bank speeches, plus 2 of 2 settled. The CBLR cut is her signature community-bank win. Fair."},
    P+"TRUM": {"p": 0.85, "reason": "Counts as 'President' too. 4 of 12 texts, and she thanked the host Reserve Bank president in Atlanta and Kansas City; Musalem introduces her today. 1 of 2 settled. Fair."},
    P+"MERG": {"p": 0.68, "reason": "6 of 12 texts, 5 of 8 community-bank speeches; merger review reform is a standing community-bank theme. Fair."},
    P+"AI":   {"p": 0.62, "reason": "Only 3 of 12 texts, but 2 of 2 settled thanks to Q&A. The 78–86¢ price looks rich for a community-bank speech."},
    P+"TRAN": {"p": 0.55, "reason": "6 of 12 texts and 2 of 2 settled. Fair to slightly cheap."},
    P+"CYBE": {"p": 0.40, "reason": "4 of 12 texts (one was a cyber workshop). Fair."},
    P+"INFL": {"p": 0.40, "reason": "3 of 12 texts; hit on Oct 1 through Q&A. A supervision keynote rarely needs it. The 67–68¢ price looks rich unless there is an economy Q&A."},
    P+"BASE": {"p": 0.35, "reason": "1 of 12 texts; 2 of 2 settled at big-bank venues. Less relevant to community banks."},
    P+"STRE": {"p": 0.30, "reason": "2 of 12 texts; 2 of 2 settled. Stress tests are a large-bank topic. Fair to slightly rich."},
    P+"SVB":  {"p": 0.20, "reason": "3 of 12 texts; 1 of 2 settled. Fair."},
    P+"BUDG": {"p": 0.15, "reason": "2 of 12 texts; 0 of 1 settled. Fair."},
    P+"PRIV": {"p": 0.10, "reason": "2 of 12 texts; 1 of 2 settled. Fair."},
    P+"CRYP": {"p": 0.08, "reason": "0 of 12 texts; 0 of 2 settled. Fair to slightly rich."},
    P+"RECE": {"p": 0.05, "reason": "1 of 12 texts; 1 of 2 settled. Fair."},
    P+"NQE":  {"p": 0.02, "reason": "On the published agenda with a livestream."},
  },
}
