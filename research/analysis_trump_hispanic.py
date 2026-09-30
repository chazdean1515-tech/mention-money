# KXTRUMPMENTION-26SEP30: Trump Hispanic Heritage Month Celebration, East Room, Wed Sep 30 2026 1:00 PM ET.
# Separate from any Commerce announcement later the same afternoon (~3:30 PM ET).
EVENT = "KXTRUMPMENTION-26SEP30"
P = EVENT + "-"
DATA = {
  "title": "Trump Hispanic Heritage Month Celebration (East Room)",
  "speaker": "Donald Trump",
  "event_time_et": "2026-09-30T13:00:00-04:00",
  "event_time_note": "White House Hispanic Heritage Month celebration, East Room, 1:00 p.m. ET. Commerce announcement later (~3:30 PM ET) is a separate event and is NOT in this market.",
  "context": ("East Room reception for Hispanic Heritage Month with hundreds of Hispanic Americans and business owners. "
              "Press previews (Washington Examiner, Voz, WH background) say Trump will spotlight Cuba sanctions / the Cuban "
              "communist regime, Venezuela / Maduro / Operation Absolute Resolve and the Venezuela oil deal, plus economic "
              "wins for Hispanics (record-low Hispanic poverty, record Hispanic homeownership, Working Families Tax Cuts: "
              "no tax on tips / Social Security). Sec. of State Marco Rubio (Cuban American) and Sean Duffy / Rachel "
              "Campos-Duffy are expected to attend — Rubio is a natural name-check. Format is a celebration/reception, "
              "not a midterm stump rally, so ICE / Tariff / Crypto / AI are softer than at Durant or Alabama. "
              "Resolution: exact word or plural/possessive; Trump only."),
  "confidence": "Medium. Strong press preview on the Cuba/Venezuela/Rubio/American Dream block; reception length still uncertain.",
  "method": ("Press-preview themes for this specific reception (Cuba sanctions, Venezuela/Maduro/oil, Communist Cuba, Rubio attending, "
             "American Dream / Hispanic homeownership / poverty, no-tax-on-tips / Social Security) blended with Trump Jun–Aug 2026 "
             "govinfo remarks + Sep stump base rates, adjusted DOWN for ICE/Tariff/Crypto/AI because this is an East Room celebration "
             "rather than a midterm rally."),
  "sources": [
    {"title": "Washington Examiner: Trump Hispanic Heritage Month White House celebration (Sep 29)", "url": "https://www.washingtonexaminer.com/news/white-house/4747848/trump-hispanic-heritage-month-white-house-celebration/"},
    {"title": "Voz: Hispanic Heritage reception — Cuba, Venezuela oil, Rubio (Sep 29)", "url": "https://voz.us/en/politics/260930/39515/trump-to-host-hispanic-heritage-month-reception-highlighting-economic-and-foreign-policy-gains.html"},
    {"title": "Political.org: Cuba sanctions + Venezuela oil deal preview", "url": "https://political.org/2026/09/29/trump-to-host-white-house-hispanic-heritage-month-celebration-wednesday-spotlighting-cuba-sanctions-and-venezuela-oil-deal/"},
    {"title": "govinfo Compilation of Presidential Documents (Jun–Aug 2026 remarks corpus)", "url": "https://www.govinfo.gov/app/collection/cpd"},
  ],
  "words": {
    P+"CUBA": {"p": 0.95, "reason": "Press preview: Cuba sanctions are a headline theme; Rubio is Cuban American and attending. Near-automatic YES."},
    P+"VENE": {"p": 0.92, "reason": "Operation Absolute Resolve / Maduro capture + Venezuela oil deal are explicitly previewed talking points."},
    P+"COMM": {"p": 0.90, "reason": "'Communist / Communism' rides with Cuba sanctions language ('Cuban communist regime' in WH background). Strong YES."},
    P+"OIL":  {"p": 0.88, "reason": "Venezuela oil deal is a featured win; Oil/Gas/Gasoline should clear. Slightly below Cuba/Venezuela pure names."},
    P+"RUBI": {"p": 0.90, "reason": "SecState Marco Rubio is attending and issued the preview statement; natural name-check at a Cuban/Hispanic event."},
    P+"NOTA": {"p": 0.82, "reason": "'No Tax on Tips' is listed in the Working Families Tax Cuts block WH previewed for this reception. Strong lean YES."},
    P+"SOCI": {"p": 0.80, "reason": "'No tax on Social Security' sits in the same tax-cut talking-point block WH previewed with tips. Strong lean YES."},
    P+"AMER": {"p": 0.75, "reason": "'American Dream' + Hispanic homeownership / poverty-rate records are core celebration messaging. Market looks cheap vs prior."},
    P+"SMAL": {"p": 0.55, "reason": "Business owners and Hispanic entrepreneurs are being recognized; 'Small Business' is natural but not guaranteed phrasing."},
    P+"BORD": {"p": 0.55, "reason": "Border can appear via hemispheric security / cartels, but this is a celebration not a deportation rally. Near fair."},
    P+"IMMI": {"p": 0.50, "reason": "Immigration is politically live for Latino outreach, yet WH preview emphasized economy + Cuba/Venezuela over deportation riffs."},
    P+"BIDE": {"p": 0.55, "reason": "'Biden' is a stump reflex (high corpus rate) but less forced in a scripted East Room celebration. Near fair."},
    P+"HOTT": {"p": 0.45, "reason": "'Hottest country' is a Sep stump line; optional at a heritage reception. Slightly rich if priced mid-50s."},
    P+"TRUM": {"p": 0.40, "reason": "'Trump Account' is not explicit in the WH preview (tips/SS/overtime are), but market has bid it up; soft prior."},
    P+"INFL": {"p": 0.35, "reason": "Inflation can appear in economic wins, but poverty/homeownership/tax cuts are the previewed metrics. Near fair."},
    P+"CHIN": {"p": 0.28, "reason": "China is a general stump staple but off-theme for a Western Hemisphere / Hispanic celebration. Soft venue."},
    P+"MIDT": {"p": 0.28, "reason": "Midterms are ~5 weeks out and Latino outreach is the subtext, but WH framing is celebration + policy wins, not 'midterm'."},
    P+"TARI": {"p": 0.18, "reason": "Tariff is a softer venue here vs rallies; not in the Cuba/Venezuela/tax-cut preview. Lean NO."},
    P+"ICE":  {"p": 0.15, "reason": "ICE / mass deportation is the awkward contrast press notes; unlikely Trump leads with it at this celebration. Soft venue, lean NO."},
    P+"AI":   {"p": 0.12, "reason": "AI is off-theme for Hispanic Heritage; softer than Mellon/tech events. Lean NO."},
    P+"LAND": {"p": 0.12, "reason": "'Landslide' is campaign brag language; optional here. Lean NO unless he riffs 2024."},
    P+"CRYP": {"p": 0.03, "reason": "Crypto/Bitcoin almost never appears in this setting. Strong NO."},
    P+"NQE":  {"p": 0.02, "reason": "Event is publicly scheduled today; cancellation / non-qualify is unlikely."},
  },
}
