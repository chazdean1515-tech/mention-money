# KXVANCEMENTION-26SEP29: JD Vance at MAHA Summit, Waldorf Astoria DC, Tue Sep 29 2026.
EVENT = "KXVANCEMENTION-26SEP29"
P = EVENT + "-"
DATA = {
  "title": "JD Vance at the MAHA Summit (Waldorf Astoria, DC)",
  "speaker": "JD Vance",
  "event_time_et": "2026-09-29T16:00:00-04:00",
  "event_time_note": "Summit livestream from 9:00 a.m. ET; Vance + RFK Jr. close the day (afternoon fireside). 4:00 p.m. ET is a placeholder for Vance's speaking window.",
  "context": ("Make America Healthy Again summit: chronic disease, pharma/'food as medicine', obesity, Medicare/Medicaid, "
              "GLP-1s, autism (RFK Jr. theme), TrumpRx. Vance co-headlines the closing fireside with RFK Jr., so 'Trump' "
              "(3+ times), 'healthcare', and MAHA staples are the load-bearing words. Length unknown — a short scripted "
              "hit cuts the long-shot political riffs (Biden/Democrat/Obama). No Vance transcript corpus on hand; "
              "estimates are topic priors, not word counts."),
  "fragile_sides": {"YES": "YES leans assume Vance speaks more than a short greeting in the closing fireside; a truncated hit flips them."},
  "confidence": "Low-medium. Topic priors only; speaking length/format unknown; no Vance base-rate corpus.",
  "method": "Topic priors from MAHA Summit agenda / Politico preview, adjusted for a closing Vance–RFK fireside (not a full stump speech).",
  "sources": [
    {"title": "MAHA Summit 2026 agenda", "url": "https://www.mahasummit.com/agenda"},
    {"title": "MAHA Summit livestream (from 9am ET)", "url": "https://www.mahasummit.com/register"},
    {"title": "Politico: Vance, RFK Jr. headline MAHA Summit (Sep 28)", "url": "https://www.politico.com/news/2026/09/28/vance-rfk-tyson-hines-maha-summit-01095218"},
  ],
  "words": {
    P+"HEAL": {"p": 0.75, "reason": "It's a health summit; 'healthcare' is almost automatic if he speaks more than a greeting."},
    P+"CHRO": {"p": 0.55, "reason": "'Chronic disease' is core MAHA language, but length unknown. 34–35¢ looks a bit cheap."},
    P+"MEDI": {"p": 0.70, "reason": "Medicare/Medicaid reform is a standing Vance/RFK talking point. Roughly fair at 75–76¢."},
    P+"PHAR": {"p": 0.55, "reason": "Pharma/pharmaceutical is baked into MAHA (drug prices, TrumpRx). Slight cheap vs 26–35¢ if he speaks at length."},
    P+"OBES": {"p": 0.55, "reason": "Obesity is a headline MAHA metric. Fair-to-slight cheap at 51–62¢."},
    P+"TRUM": {"p": 0.60, "reason": "Market is Trump (3+ times). Closing with RFK on a Trump admin agenda makes 3+ likely. Fair at 50–60¢."},
    P+"GLP":  {"p": 0.45, "reason": "GLP-1s are the live drug-policy fight; may or may not be named explicitly. Fair at 36–39¢."},
    P+"TRUMR": {"p": 0.40, "reason": "TrumpRX fits the drug-price lane; not guaranteed in a short hit. Fair at 35–38¢."},
    P+"AFFO": {"p": 0.45, "reason": "'Affordability' of food/drugs is MAHA framing. Spread is wide."},
    P+"FRAU": {"p": 0.40, "reason": "Medicare fraud is a recurring Vance riff; less forced here than on the trail. Fair at 68–76¢."},
    P+"CANC": {"p": 0.35, "reason": "Cancer often appears in chronic-disease lists. Fair."},
    P+"AUTI": {"p": 0.30, "reason": "Autism is more RFK Jr. than Vance; possible in a joint chat. Fair-to-slight cheap at 10–21¢."},
    P+"AI":   {"p": 0.28, "reason": "AI is not the summit theme; only comes up if he pivots to tech/regulation. 25–39¢ roughly fair."},
    P+"BIDE": {"p": 0.28, "reason": "Optional political riff in a health-policy fireside. Fair at 21–32¢."},
    P+"DEMO": {"p": 0.32, "reason": "Same — partisan aside, not required. Fair."},
    P+"OBAM": {"p": 0.28, "reason": "Obama/Obamacare only if he goes into ACA history. Fair-to-slight rich."},
    P+"CAMP": {"p": 0.08, "reason": "2028/campaign is off-theme for a MAHA policy close. Fair at 4–10¢."},
    P+"NQE":  {"p": 0.03, "reason": "Summit is live today; cancellation looks unlikely."},
  },
}
