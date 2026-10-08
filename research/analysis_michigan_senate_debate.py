# KXDEBATEMENTION-26OCT08: Michigan U.S. Senate debate, Abdul El-Sayed (D) vs. Mike Rogers (R), WOOD TV8, Thu Oct 8 2026, 7:00 p.m. ET.
# No transcript corpus for these two candidates was counted. Estimates are judgment calls, anchored to the market.
EVENT = "KXDEBATEMENTION-26OCT08"
P = EVENT + "-"
DATA = {
  "title": "Michigan U.S. Senate debate (El-Sayed vs. Rogers)",
  "speaker": "Abdul El-Sayed and Mike Rogers",
  "event_time_et": "2026-10-08T19:00:00-04:00",
  "event_time_note": "WOOD TV8, Grand Rapids: 7:00 p.m. ET, one hour, moderated by Rick Albin with viewer questions from Amber Krycka. A second debate is Oct 21 in Detroit.",
  "context": ("Either candidate saying a word counts. El-Sayed, a Sanders-backed physician, runs on health costs (Medicare for All), billionaires and unions; "
              "Rogers, a former House Intelligence chair, will call him a socialist and push foreign policy, energy and China. "
              "Michigan autos make tariffs and unions near-certain; Israel and AIPAC were big in the Democratic primary. "
              "Most markets are thin with wide spreads, so few leans qualify."),
  "confidence": "Low-medium. No transcript count; the candidates' core themes are well known.",
  "method": "Judgment from each candidate's signature issues, anchored to market mid-prices.",
  "sources": [
    {"title": "WOOD TV8: El-Sayed and Rogers to debate Oct. 8", "url": "https://www.woodtv.com/news/elections/u-s-senate-candidates-el-sayed-rogers-to-debate-at-wood-tv8/"},
    {"title": "MLive: Debate week for Michigan governor and Senate candidates", "url": "https://www.mlive.com/politics/2026/10/its-debate-week-for-michigan-governor-us-senate-candidates-heres-how-to-watch.html"},
  ],
  "words": {
    P+"MEDI": {"p": 0.93, "reason": "Health costs are El-Sayed's core platform. Fair; wide spread."},
    P+"TARI": {"p": 0.90, "reason": "Autos and tariffs are the Michigan economy question. Fair; wide spread."},
    P+"SOCI": {"p": 0.88, "reason": "Rogers's main line on El-Sayed. Fair; wide spread."},
    P+"BILL": {"p": 0.88, "reason": "A staple of El-Sayed's stump speech. Fair; wide spread."},
    P+"DATA": {"p": 0.84, "reason": "Michigan data-center fights are a live issue. Fair; wide spread."},
    P+"UNIO": {"p": 0.82, "reason": "UAW state; both candidates court labor. Fair; no trades yet."},
    P+"ISRA": {"p": 0.80, "reason": "A big issue in the Democratic primary. Fair; wide spread."},
    P+"AI":   {"p": 0.80, "reason": "Fair; wide spread."},
    P+"AIPA": {"p": 0.76, "reason": "El-Sayed attacks AIPAC spending. Fair; wide spread."},
    P+"TRUM": {"p": 0.78, "reason": "Contract needs 5+ mentions. Fair; wide spread."},
    P+"OIL":  {"p": 0.78, "reason": "Gas prices and energy are Rogers themes. Fair; wide spread."},
    P+"IRAN": {"p": 0.70, "reason": "Contract needs 3+ mentions; Rogers leans on foreign policy. Fair; wide spread."},
    P+"ICE":  {"p": 0.66, "reason": "Fair; wide spread."},
    P+"ENDO": {"p": 0.58, "reason": "Fair; wide spread."},
    P+"CORR": {"p": 0.60, "reason": "Fair; wide spread."},
    P+"FRAU": {"p": 0.60, "reason": "Fair; no trades yet."},
    P+"ZOHR": {"p": 0.42, "reason": "Rogers may tie El-Sayed to Mamdani. Fair; wide spread."},
    P+"OBAM": {"p": 0.40, "reason": "Fair; wide spread."},
    P+"CLIM": {"p": 0.34, "reason": "Fair; wide spread."},
    P+"BALL": {"p": 0.28, "reason": "Fair; wide spread."},
    P+"ELON": {"p": 0.20, "reason": "Fair; wide spread."},
    P+"FILI": {"p": 0.18, "reason": "Fair; wide spread."},
    P+"NQE":  {"p": 0.03, "reason": "Scheduled and widely promoted."},
  },
}
