# KXVANCEMENTION-26OCT09: JD Vance midterm rally, Lima OH (Allen County Regional Airport), Fri Oct 9 2026. Vance ~1:40 p.m. ET.
EVENT = "KXVANCEMENTION-26OCT09"
P = EVENT + "-"
DATA = {
  "title": "JD Vance midterm rally in Lima, Ohio",
  "speaker": "JD Vance",
  "event_time_et": "2026-10-09T13:40:00-04:00",
  "event_time_note": "GOP: doors 11:00 a.m. ET, event 12:15 p.m. ET at Allen County Regional Airport, Lima OH; Vance scheduled to speak at 1:40 p.m. ET (Columbus Dispatch).",
  "context": ("Home-state midterm rally for the tight Ohio Senate race (Sen. Jon Husted) and governor candidate Vivek Ramaswamy. "
              "Expect Democrat and Biden contrast, working-class branding, tax on tips and overtime, and Ohio manufacturing and steel lines. "
              "'Fake News' is much more a Trump word than a Vance word."),
  "fragile_sides": {"YES": "YES leans assume a full stump speech, not a short warm-up."},
  "confidence": "Low-medium. Topic priors from earlier Vance rallies; no word-count corpus.",
  "method": "Topic priors from the Lakeland and earlier Vance boards plus Ohio previews.",
  "sources": [
    {"title": "GOP: Midterm Rally in Lima, Ohio featuring JD Vance", "url": "https://events.gop.com/events/midterm-rally-in-lima-oh-vance-vp"},
    {"title": "LimaOhio.com: Vance coming to Lima on Friday (speaks 1:40 p.m.)", "url": "https://www.limaohio.com/top-stories/2026/10/06/vance-coming-to-lima-on-friday/"},
  ],
  "words": {
    P+"DEMO": {"p": 0.96, "reason": "Partisan midterm stump. Fair."},
    P+"VIVE": {"p": 0.92, "reason": "Boosting Ramaswamy is part of the trip. Fair."},
    P+"ELEC": {"p": 0.86, "reason": "Get-out-the-vote is the point. Fair."},
    P+"BIDE": {"p": 0.90, "reason": "Biden contrast is default framing. Fair."},
    P+"BORD": {"p": 0.86, "reason": "Border is a standard block. Fair."},
    P+"ILLE": {"p": 0.78, "reason": "'Illegal alien' is common Vance phrasing. Fair."},
    P+"SOCI": {"p": 0.76, "reason": "Social Security is a pocketbook line for an older Ohio crowd. Fair."},
    P+"CAMP": {"p": 0.72, "reason": "'Campaign' is easy to say at a campaign rally. Fair."},
    P+"TAXO": {"p": 0.82, "reason": "No tax on tips or overtime is a standing line. Fair."},
    P+"STEE": {"p": 0.70, "reason": "Steel fits Ohio, but it's not guaranteed. Fair."},
    P+"FRAU": {"p": 0.70, "reason": "Fraud is a recurring Vance riff. Fair."},
    P+"ECON": {"p": 0.70, "reason": "Economy is load-bearing on a midterm stump. Fair."},
    P+"AFFO": {"p": 0.65, "reason": "Affordability midterm frame. Fair."},
    P+"WORK": {"p": 0.65, "reason": "Working class is Vance's brand. Fair."},
    P+"RADI": {"p": 0.58, "reason": "'Radical Left' is optional. Fair."},
    P+"MANU": {"p": 0.65, "reason": "Manufacturing fits Ohio. Fair."},
    P+"INFL": {"p": 0.55, "reason": "Inflation often pairs with economy. Fair."},
    P+"HEAL": {"p": 0.55, "reason": "Healthcare may come up. Fair."},
    P+"FAKE": {"p": 0.25, "reason": "'Fake News' is a Trump catchphrase; Vance usually says media or press instead. The market prices it well above his habit. NO lean."},
    P+"CHIN": {"p": 0.30, "reason": "China only if he goes into trade. Fair."},
    P+"OIL":  {"p": 0.25, "reason": "Oil and gas less forced in Ohio. Fair."},
    P+"AMER": {"p": 0.28, "reason": "'American Dream' is optional. Fair."},
    P+"SMAL": {"p": 0.26, "reason": "Small business is optional. Fair."},
    P+"AMFI": {"p": 0.22, "reason": "He often paraphrases America First. Fair."},
    P+"TARI": {"p": 0.17, "reason": "Tariffs are off the midterm script lately. Fair."},
    P+"AI":   {"p": 0.14, "reason": "AI is not the midterm frame. Fair."},
    P+"MADE": {"p": 0.06, "reason": "The exact phrase is rare for Vance. Fair."},
    P+"NQE":  {"p": 0.01, "reason": "Publicly scheduled; cancellation unlikely."},
  },
}
