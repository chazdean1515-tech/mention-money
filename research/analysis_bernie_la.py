# KXBERNIEMENTION-26OCT05: Bernie Sanders, Ballots Over Billionaires rally, The Novo, Los Angeles, Mon Oct 5 2026.
# Counts are real Kalshi settlements from his two California stops this weekend: San Francisco (KXBERNIEMENTION-26OCT03,
# settled) and Bakersfield (KXBERNIEMENTION-26OCT04, closed at 99¢/1¢; four markets still awaiting settlement at 1¢).
EVENT = "KXBERNIEMENTION-26OCT05"
P = EVENT + "-"
DATA = {
  "title": "Bernie Sanders Ballots Over Billionaires rally in Los Angeles",
  "speaker": "Bernie Sanders",
  "event_time_et": "2026-10-05T22:00:00-04:00",
  "event_time_note": "Friends of Bernie Sanders: doors 5:00 p.m. PT, speaking program 7:00 p.m. PT (10:00 p.m. ET), The Novo, 800 W Olympic Blvd. Guests Ro Khanna and Jane Kim.",
  "context": ("Third California stop in three days for Proposition 40, the one-time 5% tax on billionaire wealth. Saturday San Francisco used the same 'Ballots Over Billionaires' name. "
              "Across SF and Bakersfield: Tax Break, Elon/Musk, Billionaire (3+), Trump (5+), Oil/Gas, and Working/Middle Class hit 2 of 2. Bernie, Social Security, Trillionaire, Nuclear, ChatGPT, and Epstein went 0 of 2. "
              "Note today's 'Working Class' market does not accept 'middle class', and 'Billionaire' now needs 5 says, not 3."),
  "confidence": "Low-medium. Two same-tour speeches settled this weekend; no full transcript count.",
  "method": "Presence in the SF (Oct 3) and Bakersfield (Oct 4) Kalshi settlements, with summer Sanders events as a tiebreak.",
  "sources": [
    {"title": "Friends of Bernie Sanders: Los Angeles, Oct. 5, program 7 p.m. PT at The Novo", "url": "https://act.berniesanders.com/signup/rsvp-ballots-over-billionaires-la/"},
    {"title": "POLITICO: Sanders' late push for the California billionaire tax", "url": "https://www.politico.com/news/2026/10/03/bernie-sanders-billionaire-tax-san-francisco-rally-01105995"},
    {"title": "Kalshi settlements: KXBERNIEMENTION-26OCT03 / 26OCT04", "url": "https://kalshi.com/markets/kxberniemention"},
  ],
  "words": {
    P+"TAXB": {"p": 0.92, "reason": "2 of 2 this weekend. Fair."},
    P+"ELON": {"p": 0.94, "reason": "2 of 2 this weekend. Fair."},
    P+"BILL": {"p": 0.95, "reason": "The rally is named for billionaires and 3+ hit 2 of 2; 5+ is a higher bar but normal for this speech. Fair."},
    P+"TRUM": {"p": 0.88, "reason": "5+ hit 2 of 2 this weekend. Fair."},
    P+"AI":   {"p": 0.85, "reason": "Hit in San Francisco (not listed in Bakersfield). Fair."},
    P+"WORK": {"p": 0.86, "reason": "'Working class' alone; middle class does not count here. Working/Middle hit 2 of 2, and 'working class' alone hit at his Aug 29 rally. Fair."},
    P+"OIL":  {"p": 0.80, "reason": "2 of 2 this weekend. Fair to slightly rich."},
    P+"CORR": {"p": 0.60, "reason": "1 of 2 this weekend (Bakersfield yes, SF no). Fair to slightly rich."},
    P+"CLIM": {"p": 0.25, "reason": "0 of 2 this weekend (Bakersfield sitting at 1¢). Spread too wide to call."},
    P+"SOCI": {"p": 0.45, "reason": "1 of 2 this weekend (SF yes, Bakersfield no). Wide market."},
    P+"ISRA": {"p": 0.45, "reason": "1 of 2 this weekend (Bakersfield yes). Wide market."},
    P+"ROBO": {"p": 0.45, "reason": "1 of 2 this weekend (Bakersfield yes). Fair."},
    P+"ZILL": {"p": 0.52, "reason": "1 of 2 this weekend (SF yes), also hit Aug 29. Fair to slightly cheap; low confidence."},
    P+"DATA": {"p": 0.12, "reason": "0 of 1 this weekend. Wide market."},
    P+"IMMI": {"p": 0.45, "reason": "1 of 2 this weekend (Bakersfield yes); Los Angeles makes immigration enforcement more likely. Wide market."},
    P+"BERN": {"p": 0.10, "reason": "He has to say his own name. 0 of 2 this weekend and 0 of 3 at earlier settled events listed here. A 22–23¢ YES looks rich."},
    P+"SSEC": {"p": 0.18, "reason": "0 of 2 this weekend. Fair."},
    P+"TRIL": {"p": 0.06, "reason": "0 of 2 this weekend. Fair."},
    P+"NUCL": {"p": 0.04, "reason": "0 of 2 this weekend. Fair."},
    P+"CHAT": {"p": 0.04, "reason": "0 of 2 this weekend. Fair."},
    P+"EPST": {"p": 0.04, "reason": "0 of 2 this weekend. Fair."},
    P+"NQE":  {"p": 0.02, "reason": "Publicly listed by the campaign; cancellation unlikely."},
  },
}
