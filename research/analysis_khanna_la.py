# KXKHANNAMENTION-26OCT05: Ro Khanna at the Ballots Over Billionaires rally, Los Angeles, Mon Oct 5 2026.
# Counts are real Kalshi settlements: SF rally Oct 3 (KXKHANNAMENTION-26OCT03) and Meet the Press Sep 27 (26SEP27).
EVENT = "KXKHANNAMENTION-26OCT05"
P = EVENT + "-"
DATA = {
  "title": "Ro Khanna at the Ballots Over Billionaires rally in Los Angeles",
  "speaker": "Ro Khanna",
  "event_time_et": "2026-10-05T22:00:00-04:00",
  "event_time_note": "Same Sanders rally: doors 5:00 p.m. PT, program 7:00 p.m. PT (10:00 p.m. ET) at The Novo. Khanna is a listed guest and likely speaks before Sanders.",
  "context": ("Khanna opened for Sanders in San Francisco on Saturday. There he hit Working/Middle Class, Bernie/Sanders, Trump, Healthcare, and Billionaire, "
              "and missed Affordability, Corruption, Oil/Gas, Wealth Tax, Iran, AI, Data Center, China, and Epstein. A warm-up speech is short, so optional words rarely land."),
  "confidence": "Low-medium. One same-format speech settled, plus one TV interview.",
  "method": "Presence in the SF rally settlement, with Meet the Press (Sep 27) as a weak tiebreak for issue words.",
  "sources": [
    {"title": "Friends of Bernie Sanders: LA rally with special guests Ro Khanna and Jane Kim", "url": "https://act.berniesanders.com/signup/rsvp-ballots-over-billionaires-la/"},
    {"title": "Kalshi settlements: KXKHANNAMENTION-26OCT03 / 26SEP27", "url": "https://kalshi.com/markets/kxkhannamention"},
  ],
  "words": {
    P+"BILL": {"p": 0.95, "reason": "Hit at SF and on Meet the Press. Fair."},
    P+"BERN": {"p": 0.93, "reason": "Hit at SF; he is warming up Sanders' crowd. Fair."},
    P+"TRUM": {"p": 0.90, "reason": "Hit at SF and Meet the Press. Fair."},
    P+"HEAL": {"p": 0.85, "reason": "Hit at SF (missed on Meet the Press). Prop 40 money goes mostly to healthcare. Fair to slightly rich."},
    P+"WORK": {"p": 0.85, "reason": "Hit at SF. Fair."},
    P+"AFFO": {"p": 0.35, "reason": "Missed at SF and on Meet the Press. The 57–68¢ quote looks rich, but the spread is too wide to call."},
    P+"OIL":  {"p": 0.30, "reason": "Missed at SF (hit on Meet the Press). Spread too wide."},
    P+"MIDT": {"p": 0.20, "reason": "Not counted at SF. Fair."},
    P+"WEAL": {"p": 0.20, "reason": "Missed at SF; he calls it the billionaire tax. Fair."},
    P+"CORR": {"p": 0.18, "reason": "Missed at SF and on Meet the Press. Fair."},
    P+"EPST": {"p": 0.12, "reason": "Missed at SF and on Meet the Press. Fair."},
    P+"IRAN": {"p": 0.12, "reason": "Missed at SF. Fair."},
    P+"AI":   {"p": 0.22, "reason": "Missed at SF (hit on Meet the Press). Fair."},
    P+"DATA": {"p": 0.10, "reason": "Missed at SF and on Meet the Press. Fair."},
    P+"CHIN": {"p": 0.10, "reason": "Missed at SF. Fair."},
    P+"NQE":  {"p": 0.03, "reason": "He is a listed guest; a no-show is the main risk."},
  },
}
