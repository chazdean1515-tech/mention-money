# KXEARNINGSMENTIONCCL-26SEP28: Carnival Q3 FY2026 earnings call (Kalshi's ticker says Sep 28, but the call is Tue Sep 29, 10:00 ET).
# Base rates: company speakers only (Weinstein, Bernstein, Roberts, operator) in 5 calls, Q2 2025 to Q2 2026 (research/ec_count.py).
EVENT = "KXEARNINGSMENTIONCCL-26SEP28"
P = EVENT + "-"
DATA = {
  "title": "Carnival (CCL) Q3 FY26 earnings call",
  "speaker": "Carnival Corp. (CEO Josh Weinstein, CFO David Bernstein, IR Beth Roberts, operator)",
  "event_time_et": "2026-09-29T10:00:00-04:00",
  "event_time_note": "Carnival press release sets the call for Tue Sep 29, 10:00 a.m. EDT. Kalshi's ticker says SEP28.",
  "context": ("Q3 FY26 call. Recent themes: Middle East conflict hurt European deployments and yields (Q2 call said 'Middle East' 5 times), "
              "the PROPEL 2029 long-term plan (introduced March 2026), fleet 'modernization programs' including Holland America Evolution, "
              "the RelaxAway Half Moon Cay beach club opening in October, the dividend plus a $2.5B buyback, and fuel-price volatility (they say 'fuel', not 'oil'). "
              "Only Carnival representatives count, not analysts."),
  "confidence": "Medium. 5 comparable transcripts. Word choice varies from call to call.",
  "method": "Count of company-speaker mentions per call, Q2'25, Q3'25, Q4'25, Q1'26, Q2'26 (roic.ai / Earnings Whispers transcripts).",
  "sources": [
    {"title": "Carnival Q2 2026 call transcript (Earnings Whispers)", "url": "https://beta.earningswhispers.com/transcript/CCL/Q22026"},
    {"title": "Carnival transcripts Q2'25 to Q1'26 (roic.ai)", "url": "https://www.roic.ai/quote/CCL/transcripts"},
    {"title": "Carnival Q3 call set for Sep 29, 10am ET (StockTitan/PRN)", "url": "https://www.stocktitan.net/news/CCL/carnival-corporation-ltd-to-hold-conference-call-on-third-quarter-qj29sw7eq97p.html"},
    {"title": "Holland America RelaxAway beach club opens October 2026", "url": "https://cruiseradio.net/half-moon-cay-beach-club-holland-america/"},
  ],
  "words": {
    P+"TAIL": {"p": 0.65, "reason": "Said 'tailwind(s)' in 4 of 5 recent calls (Weinstein uses it every quarter). 45¢ looks cheap."},
    P+"PROP": {"p": 0.75, "reason": "PROPEL is the flagship 2029 plan: 11 mentions when it launched (Q1), still referenced in Q2."},
    P+"PRIN": {"p": 0.55, "reason": "Brand name, in 3/5 calls (0 in the last two, 4 in Q2'26). Princess is also moving calls to Half Moon Cay. Slightly cheap."},
    P+"OIL":  {"p": 0.08, "reason": "0/5 calls. Management says 'fuel', even when fuel spiked in Q2. NO looks good."},
    P+"MODE": {"p": 0.58, "reason": "0,0,0,1,3 over the last 5 calls, trending up with the new modernization programs. Fair."},
    P+"MIDD": {"p": 0.85, "reason": "Conflict still hitting deployments. 5 mentions last call. Slightly cheap at 81¢."},
    P+"IRAN": {"p": 0.04, "reason": "0/5 calls. They say 'Middle East' or 'geopolitical', not the country."},
    P+"INFL": {"p": 0.22, "reason": "1/5 calls. Fair to slightly rich."},
    P+"HOLL": {"p": 0.70, "reason": "2/5 calls, but Q2 had 4 (Holland America Evolution program). Likely yet uncertain; 82–83¢ looks rich. NO lean."},
    P+"HEAD": {"p": 0.62, "reason": "3/5 calls (Q2'26 once). With yields already guided down, 'headwind' is plausible but 70¢ is a bit rich."},
    P+"DRY":  {"p": 0.78, "reason": "4/5 calls (dry-dock timing drives costs) but 0 in Q2'26. Fair."},
    P+"DIVI": {"p": 0.85, "reason": "In 4/5 calls since the dividend was reinstated; capital-return talk is part of every call now."},
    P+"CONS": {"p": 0.45, "reason": "2/5 calls; Q2 cited 'historic low levels of consumer sentiment'. Fair."},
    P+"AI":   {"p": 0.45, "reason": "Company speakers said 'AI' in 3/5 calls (the last 3). Often prompted by an analyst question. 29¢ looks cheap."},
    P+"TARI": {"p": 0.12, "reason": "1/5 calls (Q2'26, looking back at 2025 tariff volatility). Fair."},
  },
}
