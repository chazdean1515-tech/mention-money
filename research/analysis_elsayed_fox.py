# KXFOXNEWSMENTION-26OCT05: Abdul El-Sayed on Fox News' The Story with Martha MacCallum, Mon Oct 5 2026.
# No El-Sayed transcript corpus on file and no settled El-Sayed Kalshi event found. Do not invent hit counts.
EVENT = "KXFOXNEWSMENTION-26OCT05"
P = EVENT + "-"
DATA = {
  "title": "Abdul El-Sayed on The Story with Martha MacCallum",
  "speaker": "Abdul El-Sayed",
  "event_time_et": "2026-10-05T15:00:00-04:00",
  "event_time_note": "The Story airs weekdays 3:00–4:00 p.m. ET; the interview's slot inside the hour was not published. Board uses the show start.",
  "context": ("El-Sayed is the Democratic Senate nominee in Michigan against Mike Rogers, a physician running on health costs. Fox hosts spent last week attacking his health platform as a MAHA copycat. "
              "A cable interview runs a few minutes, so optional words need the host to raise them. No transcript count."),
  "confidence": "Low. No corpus; short interview; estimates sit close to the market.",
  "method": "Judgment only: his campaign themes and last week's Fox coverage. No hit rates.",
  "sources": [
    {"title": "Fox News: The Five on El-Sayed's health platform (Oct 2)", "url": "https://www.foxnews.com/video/6406140158112"},
    {"title": "Fox News: Mike Rogers on El-Sayed (Hannity, Oct 3)", "url": "https://www.foxnews.com/video/6406147186112"},
  ],
  "words": {
    P+"TRUM": {"p": 0.85, "reason": "No corpus. A Democrat on Fox almost always names Trump. Fair."},
    P+"HEAL": {"p": 0.82, "reason": "No corpus. His platform is health costs and the Fox attacks were about it. Fair."},
    P+"AFFO": {"p": 0.78, "reason": "No corpus. Affordability is the Democratic midterm frame. Fair."},
    P+"BILL": {"p": 0.58, "reason": "No corpus. Sanders-wing populist, so billionaires are likely but not required in a short hit. Fair."},
    P+"IRAN": {"p": 0.58, "reason": "No corpus. Depends on the host raising this week's Iran news. Fair."},
    P+"ISRA": {"p": 0.52, "reason": "No corpus. Gaza and Israel come up for him, host-dependent. Wide market."},
    P+"TARI": {"p": 0.55, "reason": "No corpus. Michigan autos make tariffs natural. Fair."},
    P+"AIPA": {"p": 0.30, "reason": "No corpus. Only if asked about primary spending. Fair."},
    P+"DATA": {"p": 0.22, "reason": "No corpus. Michigan data-center fights exist but are not his lead. Wide market."},
    P+"AI":   {"p": 0.28, "reason": "No corpus. Fair."},
    P+"CORR": {"p": 0.28, "reason": "No corpus. Fair."},
    P+"ELON": {"p": 0.15, "reason": "No corpus. Fair."},
    P+"IMMI": {"p": 0.25, "reason": "No corpus. Fair."},
    P+"FILI": {"p": 0.06, "reason": "No corpus. Fair."},
    P+"NQE":  {"p": 0.04, "reason": "Booked cable hits get bumped sometimes; no sign of that."},
  },
}
