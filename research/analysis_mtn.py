# Analysis for KXEARNINGSMENTIONMTN-26SEP28 (Vail Resorts Q4 FY26 / year-end call, Mon Sep 28 2026)
# Base rates: company-speaker mentions in 4 Vail transcripts (FY25 Q4, FY26 Q1–Q3).
EVENT = "KXEARNINGSMENTIONMTN-26SEP28"
P = EVENT + "-"
DATA = {
  "title": "Vail Resorts (MTN) Q4 FY26 / year-end earnings call",
  "speaker": "Vail Resorts (CEO Rob Katz, CFO Angela Korch, IR Connie Wang, operator)",
  "event_time_et": "2026-09-28T17:00:00-04:00",
  "event_time_note": "Vail PR: results after the close Mon Sep 28, call at 5:00 p.m. ET. Kalshi ticker matches the calendar date.",
  "context": ("Year-end call after a weather-challenged FY26 (Rockies snowpack near historic lows in Q2). "
              "Standing themes: Epic Friends (rebranded buddy tickets), pass sales/renewals, conversion of ticket buyers to passes, "
              "ski school and rental digitization in the My Epic app, snowmaking, Northeast resorts, and occasional Canada/Switzerland geography. "
              "Only company representatives count, not analysts. Most Kalshi YES asks sit in the high-70s to 90s — that looks rich versus base rates for several mid-frequency words."),
  "confidence": "Medium. 4 comparable transcripts; CEO name varies (Rob / Robert / Robert A. Katz) across files. Year-end format usually mirrors Q4 FY25.",
  "method": "Company-speaker mention counts (Rob/Robert Katz, Angela Korch, Connie Wang, Operator) in FY25 Q4 and FY26 Q1–Q3 transcripts (roic.ai).",
  "sources": [
    {"title": "Vail Resorts: FY26 Q4/year-end call Sep 28, 5:00pm ET", "url": "https://ca.finance.yahoo.com/news/vail-resorts-announces-fiscal-2026-200500843.html"},
    {"title": "Vail Resorts IR", "url": "https://investors.vailresorts.com"},
    {"title": "Vail transcripts (roic.ai)", "url": "https://www.roic.ai/quote/MTN/transcripts"},
  ],
  "words": {
    P+"EPIC": {"p": 0.94, "reason": "'Epic Friend(s)' in 4/4 calls (3–11 mentions). Flagship product. YES lean vs ~79¢."},
    P+"CONV": {"p": 0.90, "reason": "Pass 'conversion' in 4/4 calls. Core KPI. Slight YES lean at ~79¢."},
    P+"SKIS": {"p": 0.78, "reason": "Ski school in 3/4 (digitization theme). Near fair to slight NO at 89¢."},
    P+"SNOWM": {"p": 0.72, "reason": "Snowmaking in 3/4; weather story invites it. Fair at ~79¢."},
    P+"ACQU": {"p": 0.70, "reason": "Acquire/acquisition in 3/4. Slight NO at 89¢."},
    P+"PERS": {"p": 0.68, "reason": "Personalized/personalization in 3/4 (My Epic). Slight NO at ~79¢."},
    P+"NORT": {"p": 0.65, "reason": "Northeast in 3/4. Slight NO at ~78¢."},
    P+"RENE": {"p": 0.72, "reason": "Renewal in 2/4 but Q4 FY25 had 5 mentions (pass season). Fair at ~78¢."},
    P+"SNOW": {"p": 0.55, "reason": "Snowpack in 2/4 (Q4 FY25 + bad-weather Q2). 90¢ looks rich. NO lean."},
    P+"RENT": {"p": 0.55, "reason": "Rental in 2/4. 89¢ rich. NO lean."},
    P+"DINI": {"p": 0.50, "reason": "Dining in 2/4. 89¢ rich. NO lean."},
    P+"CANA": {"p": 0.40, "reason": "Canada/Canadian in 1/4 (Q4 geography line). 79¢ rich. NO lean."},
    P+"GEN":  {"p": 0.35, "reason": "Gen Z in 1/4 (Q2 Epic Passion campaign). May recur in marketing wrap, but 78¢ is rich."},
    P+"BUDD": {"p": 0.35, "reason": "Buddy in 2/4 when contrasting legacy buddy tickets with Epic Friends; less needed now. 78¢ rich."},
  },
}
