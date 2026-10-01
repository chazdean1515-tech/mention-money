# KXVANCEMENTION-26OCT01: JD Vance midterm rally, Lakeland FL (Sun 'n Fun), Thu Oct 1 2026.
# No Vance transcript corpus on hand — topic priors for a full midterm stump, not word counts.
EVENT = "KXVANCEMENTION-26OCT01"
P = EVENT + "-"
DATA = {
  "title": "JD Vance midterm rally in Lakeland, Florida",
  "speaker": "JD Vance",
  "event_time_et": "2026-10-01T11:30:00-04:00",
  "event_time_note": "GOP/Trump 47: doors 9:30 a.m. ET, program 11:30 a.m. ET at Skylight Hangar A, Sun 'n Fun, Lakeland FL.",
  "context": ("Full midterm rally for Florida turnout — Byron Donalds (gov) is the local headliner Vance is there to boost. "
              "Expect Democrat/Biden contrast, working-class branding, tax-on-tips/overtime, and Florida name-checks (DeSantis). "
              "Length should be a real stump, not a short fireside, so partisan staples clear more easily than at the Sep 29 MAHA summit. "
              "No Vance word-count corpus; these are topic priors only."),
  "fragile_sides": {"YES": "YES leans assume a full midterm stump (≥15 min), not a truncated greeting."},
  "confidence": "Low-medium. Topic priors only; no Vance base-rate corpus.",
  "method": "Topic priors from GOP event page + FL Voice / Newsbreak previews (Donalds, midterm turnout frame).",
  "sources": [
    {"title": "GOP: Midterm Rally in Lakeland FL featuring JD Vance (Oct 1, 11:30am ET)", "url": "https://events.gop.com/events/midterm-rally-in-fl-jd-vance"},
    {"title": "Florida's Voice: Vance to headline Lakeland rally", "url": "https://flvoicenews.com/vance-to-headline-lakeland-rally-as-midterm-elections-approach/"},
  ],
  "words": {
    P+"DEMO": {"p": 0.92, "reason": "Partisan midterm stump; 'Democrat' is near-automatic. Fair at 94–97¢."},
    P+"BIDE": {"p": 0.88, "reason": "Biden contrast is default Vance/Trump midterm framing. Fair at 87–91¢."},
    P+"BYRO": {"p": 0.90, "reason": "He's there to boost Byron Donalds; naming the candidate is the point of the trip. Fair at 87–91¢."},
    P+"TAXO": {"p": 0.85, "reason": "No tax on tips / overtime is a standing Trump–Vance pocketbook line. Fair at 85–88¢."},
    P+"WORK": {"p": 0.80, "reason": "Working class / middle class is Vance's brand. Fair at 57–59¢ — slight cheap."},
    P+"ECON": {"p": 0.75, "reason": "Economy/economic is load-bearing on a midterm stump. Fair-to-slight cheap at 50–53¢."},
    P+"ELEC": {"p": 0.72, "reason": "Election / get-out-the-vote is the event's purpose. Fair at 79–89¢."},
    P+"SOCI": {"p": 0.55, "reason": "Social Security often appears in pocketbook blocks; not guaranteed. Fair-to-slight NO at 77–88¢."},
    P+"DESA": {"p": 0.55, "reason": "DeSantis name-check is natural in Florida but optional. Fair at 58–70¢."},
    P+"FRAU": {"p": 0.50, "reason": "Election/Medicare fraud is a recurring Vance riff. Fair-to-slight NO at 71–76¢."},
    P+"ILLE": {"p": 0.50, "reason": "'Illegal alien' / border language common on trail; length-dependent. Fair-to-slight NO at 72–87¢."},
    P+"AFFO": {"p": 0.55, "reason": "Affordability midterm frame. Fair at 66–76¢."},
    P+"RADI": {"p": 0.45, "reason": "'Radical Left' is optional culture-war spice. Fair at 40–49¢."},
    P+"HEAL": {"p": 0.40, "reason": "Healthcare less forced here than at MAHA; may still appear. Fair at 40–47¢."},
    P+"INFL": {"p": 0.45, "reason": "Inflation often pairs with economy; not automatic. Fair at 46–62¢."},
    P+"CAMP": {"p": 0.40, "reason": "2028/campaign can come up but is off-message for a midterm turnout hit. Fair-to-slight NO at 63–75¢."},
    P+"MANU": {"p": 0.40, "reason": "Manufacturing fits America First; optional at a FL rally. Fair at 45–60¢."},
    P+"AMER": {"p": 0.40, "reason": "'American Dream' is Vance-flavored but not required. Fair at 32–44¢."},
    P+"AMFI": {"p": 0.35, "reason": "'America First' in  the brand but he often paraphrases. Fair-to-slight cheap at 20–21¢."},
    P+"ICE":  {"p": 0.35, "reason": "ICE / border block is optional. Fair-to-slight cheap at 23–25¢."},
    P+"TARI": {"p": 0.30, "reason": "Tariffs more natural at a factory hit than a FL turnout rally. Fair-to-slight cheap at 20–21¢."},
    P+"FAKE": {"p": 0.25, "reason": "'Fake News' is more Trump than Vance. Fair at 19–23¢."},
    P+"OIL":  {"p": 0.22, "reason": "Oil/gas less forced in Lakeland than in OK. Fair at 16–26¢."},
    P+"CHIN": {"p": 0.30, "reason": "China optional unless he goes into trade. Fair at 18–39¢ (wide)."},
    P+"AI":   {"p": 0.22, "reason": "AI not the midterm frame. Fair at 16–17¢."},
    P+"CALI": {"p": 0.20, "reason": "California foil is optional. Wide market."},
    P+"ID":   {"p": 0.20, "reason": "Voter ID sometimes in election-integrity block. Fair at 21–34¢."},
    P+"FOOD": {"p": 0.15, "reason": "Food stamp/SNAP is a niche policy aside. Fair at 16–26¢."},
    P+"MADE": {"p": 0.18, "reason": "'Made in America' more factory than FL rally. Fair-to-slight rich NO at 4–9¢ YES."},
    P+"NQE":  {"p": 0.02, "reason": "Publicly scheduled; cancellation unlikely."},
  },
}
