# KXEARNINGSMENTIONMU-26SEP30: Micron Q4 FY2026 earnings call (Wed Sep 30, 4:30pm ET).
# Base rates: company speakers (Sanjay Mehrotra, Mark Murphy, operator) in 5 transcripts Q4'25–Q3'26.
EVENT = "KXEARNINGSMENTIONMU-26SEP30"
P = EVENT + "-"
DATA = {
  "title": "Micron (MU) Q4 FY26 earnings call",
  "speaker": "Micron (CEO Sanjay Mehrotra, CFO Mark Murphy, IR, operator)",
  "event_time_et": "2026-09-30T16:30:00-04:00",
  "event_time_note": "Micron IR: results after the close Wed Sep 30; call at 2:30 p.m. Mountain (4:30 p.m. ET).",
  "context": ("Record AI/HBM cycle: Q3 guided Q4 revenue ~$50B ± $1B. Management's every-call vocabulary is "
              "'data center', 'HBM'/'HBM4', 'portfolio', 'Idaho' (HQ/fabs), and 'New York' (Clay fab buildout). "
              "They almost never say 'China', 'tariff', 'Anthropic', or 'research lab' on the prepared + Q&A track. "
              "Kalshi's 'Data Center (3+ times)' and 'Smartphone (3+ times)' are count thresholds — both cleared every "
              "recent call. Liquidity is thin outside Portfolio / Data Center (many 70¢+ spreads, 0 volume)."),
  "confidence": "Medium. 5 comparable transcripts; most markets still too wide/illiquid to trade.",
  "method": "Company-speaker mention counts in MU Q4'25, Q1'26, Q2'26, Q3'26 (roic.ai) + Earnings Whispers Q3'26.",
  "sources": [
    {"title": "Micron IR: Q4 FY26 call Sep 30, 2:30pm MT", "url": "https://investors.micron.com/events-and-presentations/event-details/2026/Microns-Fourth-Quarter-2026-Financial-Call/default.aspx"},
    {"title": "Micron Q3 FY26 results / HBM4 commentary (GlobeNewswire Jun 24)", "url": "https://www.globenewswire.com/news-release/2026/06/24/3317151/0/en/micron-technology-inc-reports-record-results-for-the-third-quarter-of-fiscal-2026.html"},
    {"title": "Micron transcripts (roic.ai)", "url": "https://www.roic.ai/quote/MU/transcripts"},
  ],
  "words": {
    P+"DATA": {"p": 0.96, "reason": "'Data Center' 13–23× every call (5/5). The 3+ threshold is almost automatic. 76–82¢ still a bit cheap."},
    P+"PORT": {"p": 0.92, "reason": "'Portfolio' in 5/5 calls (usually 3–13×). Fair-to-slight cheap; spread is wide."},
    P+"SMAR": {"p": 0.88, "reason": "'Smartphone' 4–8× in 5/5 calls, so 3+ is very likely. Illiquid."},
    P+"NEW":  {"p": 0.85, "reason": "'New York' (Clay / mega-fab) in 5/5 calls. Illiquid."},
    P+"IDAH": {"p": 0.85, "reason": "'Idaho' (Boise HQ / fabs) in 5/5 calls. Illiquid."},
    P+"HBM4": {"p": 0.80, "reason": "Market is HBM4E specifically: 2/5 calls said HBM4E; HBM4 (without E) is 4/5. Uncertain which form they use. Illiquid."},
    P+"INFE": {"p": 0.55, "reason": "'Inference' in 3/5 recent calls as AI workload mix. Fair. Illiquid."},
    P+"TAIW": {"p": 0.50, "reason": "'Taiwan' in 3/5 (supply-chain / TSMC angle). Fair. Illiquid."},
    P+"NVID": {"p": 0.45, "reason": "'Nvidia' in 2/5 calls; often customer-driven. Fair. Illiquid."},
    P+"INVE": {"p": 0.40, "reason": "'Inventory' in 2/5. Fair. Illiquid."},
    P+"AGEN": {"p": 0.35, "reason": "'Agentic' in 2/5 (newer AI buzzword). Fair. Illiquid."},
    P+"HYPE": {"p": 0.25, "reason": "'Hyperscaler' only 1/5. Slight NO lean. Illiquid."},
    P+"TARI": {"p": 0.08, "reason": "0/5 calls. Management talks trade/export without saying 'tariff'. NO lean. Illiquid."},
    P+"CHIN": {"p": 0.06, "reason": "0/5 calls. They avoid naming China on the call. NO lean. Illiquid."},
    P+"RESE": {"p": 0.05, "reason": "0/5 for 'research lab'. NO lean. Illiquid."},
    P+"ANTH": {"p": 0.04, "reason": "0/5 for Anthropic. NO lean. Illiquid."},
  },
}
