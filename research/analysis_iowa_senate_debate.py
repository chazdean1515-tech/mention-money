# KXDEBATEMENTION-26OCT07: Iowa Press Debates: U.S. Senate, Ashley Hinson (R) vs. Josh Turek (D), Iowa PBS, Wed Oct 7 2026.
# No transcript corpus for these two candidates was counted. Estimates are judgment calls, anchored to the market.
EVENT = "KXDEBATEMENTION-26OCT07"
P = EVENT + "-"
DATA = {
  "title": "Iowa U.S. Senate debate (Hinson vs. Turek) on Iowa PBS",
  "speaker": "Ashley Hinson and Josh Turek",
  "event_time_et": "2026-10-07T20:00:00-04:00",
  "event_time_note": "Iowa PBS: 7:00 p.m. CT (8:00 p.m. ET) at the Johnston studios, about an hour, moderated by Kay Henderson with Iowa political reporters. No live audience.",
  "context": ("An hour-long, reporter-led debate for Joni Ernst's open seat. Either candidate saying a word counts. "
              "Farm and trade questions are almost certain in Iowa (tariffs, China soybeans, ethanol/E15, the farm bill), "
              "and a Democrat in 2026 will push healthcare cuts (Medicaid/Medicare) and abortion. "
              "Many markets are thin with wide spreads, so few leans qualify."),
  "confidence": "Low-medium. No transcript counts; format and Iowa issue set are well known.",
  "method": "Judgment from the debate format and Iowa issue set, anchored to market mid-prices.",
  "sources": [
    {"title": "Iowa PBS: Iowa Press Debates: U.S. Senate, Oct 7 at 7 p.m.", "url": "https://www.iowapbs.org/shows/iowapress/special/14524/iowa-press-debates-us-senate"},
    {"title": "CBS2 Iowa: Hinson and Turek debate Oct. 7", "url": "https://cbs2iowa.com/news/local/iowa-pbs-sets-oct-7-us-senate-debate-between-hinson-and-turek"},
  ],
  "words": {
    P+"IRAN": {"p": 0.95, "reason": "Priced as a near-lock; foreign-policy question likely. Fair."},
    P+"TARI": {"p": 0.94, "reason": "Tariffs are the core Iowa farm-economy question. Fair."},
    P+"BILL": {"p": 0.88, "reason": "Fair."},
    P+"BORD": {"p": 0.84, "reason": "Immigration question likely. Fair; thin."},
    P+"SOCI": {"p": 0.84, "reason": "Standard Senate-debate topic. Fair; thin."},
    P+"CANC": {"p": 0.84, "reason": "Iowa's cancer rate is a live state issue. Fair."},
    P+"ETHA": {"p": 0.84, "reason": "Ethanol/E15 is a reliable Iowa debate topic. Fair; wide spread."},
    P+"DATA": {"p": 0.75, "reason": "Fair; wide spread."},
    P+"FARM": {"p": 0.85, "reason": "Exact phrase 'farm bill' is needed; Iowa reporters ask about it. Fair."},
    P+"CORR": {"p": 0.82, "reason": "Fair; wide spread."},
    P+"AI":   {"p": 0.70, "reason": "Fair; wide spread."},
    P+"MEDI": {"p": 0.85, "reason": "Healthcare cuts are the Democrats' main 2026 attack. Fair."},
    P+"TRUM": {"p": 0.75, "reason": "Contract needs 5+ mentions; an hour on a Trump-era midterm should get there. Fair to slightly cheap; wide spread."},
    P+"AGEN": {"p": 0.58, "reason": "Fair; wide spread."},
    P+"ABOR": {"p": 0.62, "reason": "A Democratic Senate nominee in 2026 usually raises it, and reporters often ask. 53¢ looks a bit cheap."},
    P+"MINI": {"p": 0.42, "reason": "Fair."},
    P+"TERM": {"p": 0.45, "reason": "Fair."},
    P+"CRYP": {"p": 0.15, "reason": "Rare in state Senate debates. Fair."},
    P+"CHIN": {"p": 0.86, "reason": "China trade and soybeans are natural in Iowa. Cheap, but the market has not traded."},
    P+"NQE":  {"p": 0.01, "reason": "Scheduled live broadcast."},
  },
}
