# KXTRUMPMENTION-26OCT08: Trump at the White House "Science: A New Golden Age" Summit, Thu Oct 8 2026.
# Start time was not published by the morning refresh. No transcript of a comparable event was counted.
EVENT = "KXTRUMPMENTION-26OCT08"
P = EVENT + "-"
DATA = {
  "title": "Trump at the Science: A New Golden Age Summit",
  "speaker": "Donald Trump",
  "event_time_et": "2026-10-08T11:00:00-04:00",
  "event_time_note": "White House event on Thursday; the start time was not public as of 5 a.m. ET. The board uses 11:00 a.m. ET as a conservative cutoff so leans drop off before the event could begin.",
  "context": ("A White House summit on AI-driven science (the Genesis Mission and 'super intelligence'), with more than $1 billion in commitments from AMD, OpenAI, Anthropic and others. "
              "Trump presents the National Medal of Science to Elon Musk, Sergey Brin, Jensen Huang and Lisa Su, and the technology medal to Michael Dell and Satya Nadella. "
              "Energy Secretary Chris Wright and NASA Administrator Jared Isaacman also speak. Introducing the honorees makes Nvidia, Tesla/SpaceX and chips very likely; "
              "everything else depends on how far he ad-libs or whether he takes questions."),
  "fragile_sides": {"NO": "Trump ad-libs at length at White House events; a Q&A can bring up almost anything."},
  "confidence": "Low. No transcript count; start time and format unconfirmed.",
  "method": "Judgment from the announced agenda and honoree list, anchored to the market mid-price.",
  "sources": [
    {"title": "CNBC: Trump awarding medals to Musk, Dell, Nadella at science summit", "url": "https://www.cnbc.com/2026/10/07/trump-awarding-medals-to-musk-dell-nadella-at-science-summit.html"},
    {"title": "Axios: Inside Trump's AI science summit", "url": "https://www.axios.com/2026/10/07/exclusive-inside-trumps-ai-science-summit"},
    {"title": "Reuters via CNA: Trump to appear at White House science event", "url": "https://www.channelnewsasia.com/business/trump-appear-white-house-science-event-thursday-6440771"},
  ],
  "words": {
    P+"GOLD": {"p": 0.94, "reason": "It is the summit's name and one of his stock phrases. Fair."},
    P+"SUPE": {"p": 0.92, "reason": "The summit's stated theme. Fair."},
    P+"NVDA": {"p": 0.88, "reason": "He is handing Jensen Huang a medal and usually names the company. Slight YES lean."},
    P+"TESL": {"p": 0.84, "reason": "Introducing Musk almost always brings up Tesla or SpaceX. YES lean, but check the spread."},
    P+"CHIP": {"p": 0.84, "reason": "Huang and Lisa Su are honorees; chips are a regular Trump riff. Fair; wide spread."},
    P+"GENE": {"p": 0.78, "reason": "The Genesis Mission commitments are the headline announcement, if he reads the script. Fair."},
    P+"DATA": {"p": 0.76, "reason": "He brings up data centers and power plants at most AI events. Fair."},
    P+"BIDE": {"p": 0.62, "reason": "Biden comes up in most Trump remarks, less often at award ceremonies. Small YES lean."},
    P+"TARI": {"p": 0.62, "reason": "Chip tariffs are a natural digression. Fair."},
    P+"NUCL": {"p": 0.64, "reason": "Chris Wright speaks; nuclear power for AI is a common line. Fair; wide spread."},
    P+"IRAN": {"p": 0.62, "reason": "Needs a foreign-policy aside or questions. Fair."},
    P+"MANU": {"p": 0.58, "reason": "Fair."},
    P+"OAI":  {"p": 0.52, "reason": "OpenAI is among the announced commitments, but he may say Sam Altman instead. Fair."},
    P+"ROBO": {"p": 0.52, "reason": "Fair; wide spread."},
    P+"QUAN": {"p": 0.52, "reason": "Fair; wide spread."},
    P+"SPAC": {"p": 0.52, "reason": "A favorite brag, and Isaacman is on the bill. Fair."},
    P+"MOON": {"p": 0.55, "reason": "NASA is on the bill. Fair; wide spread."},
    P+"NOBE": {"p": 0.50, "reason": "Medal talk invites a Nobel comparison or his Peace Prize complaint. Fair."},
    P+"MARS": {"p": 0.44, "reason": "Musk tends to pull Mars in. Fair."},
    P+"CHIN": {"p": 0.44, "reason": "Contract needs 3+ mentions. Fair."},
    P+"NATI": {"p": 0.42, "reason": "Fair."},
    P+"MADE": {"p": 0.40, "reason": "Fair."},
    P+"CANC": {"p": 0.40, "reason": "Curing cancer is a stock AI-science line. Fair."},
    P+"AUTO": {"p": 0.25, "reason": "Fair."},
    P+"SACK": {"p": 0.22, "reason": "Fair."},
    P+"VACC": {"p": 0.12, "reason": "Fair."},
    P+"CRYP": {"p": 0.03, "reason": "Off topic. Fair."},
    P+"NQE":  {"p": 0.02, "reason": "Widely reported with Trump attending."},
  },
}
