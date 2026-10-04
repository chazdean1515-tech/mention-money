# KXBERNIEMENTION-26OCT04: Bernie Sanders, Fighting Oligarchy, Bakersfield, Sun Oct 4 2026.
# No Bernie transcript corpus on file. Do not invent hit counts.
EVENT = "KXBERNIEMENTION-26OCT04"
P = EVENT + "-"
DATA = {
  "title": "Bernie Sanders Fighting Oligarchy rally in Bakersfield",
  "speaker": "Bernie Sanders",
  "event_time_et": "2026-10-04T21:00:00-04:00",
  "event_time_note": "Friends of Bernie Sanders: doors 4:00 p.m. Pacific, speaking program 6:00 p.m. Pacific (9:00 p.m. ET), Harvey Auditorium, Bakersfield High School, 1241 G St.",
  "context": ("What: 'Fighting Oligarchy: Where We Go From Here,' a Sanders campaign stop, not the Saturday San Francisco 'Ballots Over Billionaires' rally. "
              "Who: Bernie Sanders, with special guest Randy Villegas, the Democrat running in CA-22 against Rep. David Valadao. "
              "Where: Harvey Auditorium at Bakersfield High School. When: Sunday, Oct. 4, 2026, program 6:00 p.m. Pacific / 9:00 p.m. ET. "
              "About: he is in California for Proposition 40, a one-time 5% tax on wealth above $1 billion aimed mostly at healthcare, and to boost Villegas. "
              "Los Angeles is a separate Monday stop. No transcript corpus of Sanders speeches is on file. Saturday's still-open Kalshi prices are not a transcript."),
  "confidence": "Low-medium. No transcript corpus; topic priors from the event listing and the Prop 40 campaign only.",
  "method": "No counted corpus and no hit rates. Judgment from the Bakersfield listing, the billionaire-tax campaign, and the CA-22 race. Slash markets pay on either word. Billionaire needs three says. Trump needs five says. 'Bernie' counts only if he says his own name.",
  "sources": [
    {"title": "Friends of Bernie Sanders: Bakersfield, Oct. 4, doors 4 p.m. PT, program 6 p.m. PT", "url": "https://act.berniesanders.com/signup/rsvp-oligarchy-bakersfield-ca/"},
    {"title": "KBAK: Sanders and Villegas at Bakersfield High, program 6 p.m.", "url": "https://bakersfieldnow.com/news/local/bernie-sanders-to-speak-at-bakersfield-high-school-on-oct-4-with-randy-villegas"},
    {"title": "Fresno Bee: Sunday Bakersfield stop is Prop 40; Saturday was San Francisco", "url": "https://www.fresnobee.com/news/politics-government/article317472599.html"},
    {"title": "KCRA: Sanders on the billionaire tax and why Newsom and Becerra oppose it", "url": "https://www.kcra.com/article/bernie-sanders-california-visit-billionaire-tax-proposal/73962773"},
  ],
  "words": {
    P+"BILL": {"p": 0.93, "reason": "No corpus. The stop is a billionaire-wealth-tax rally, and the contract needs the word three times. That is the speech. Fair at 92–96¢."},
    P+"WORK": {"p": 0.90, "reason": "No corpus. Working class or middle class is his ordinary contrast with billionaires. Fair at 90–91¢."},
    P+"TAXB": {"p": 0.84, "reason": "No corpus. Tax break for the rich is how he frames a wealth tax. Fair-to-slight cheap versus a wide 81–90¢."},
    P+"ELON": {"p": 0.88, "reason": "No corpus. Elon or Musk is his usual oligarch example, including on this California tax fight. Fair at 91–92¢."},
    P+"TRUM": {"p": 0.86, "reason": "No corpus. Five says of Trump is normal at a full Sanders rally and not guaranteed in a shortened program. Wide 73–85¢."},
    P+"OIL": {"p": 0.70, "reason": "No corpus. Oil, gas, or gasoline comes up when he ties energy prices to billionaires, and it is not required for a tax-and-healthcare stop. Fair at 70–74¢."},
    P+"SSEC": {"p": 0.74, "reason": "No corpus. Social Security is a stump staple and can be skipped if he stays on Prop 40 and Villegas. Fair versus 72–79¢."},
    P+"ZOHR": {"p": 0.32, "fragile": True, "reason": "No corpus. Zohran/Mamdani is a national ally, not a Bakersfield guest. The listed program is Villegas and the California tax. One name-check flips it, so the NO is fragile."},
    P+"SOCI": {"p": 0.60, "reason": "No corpus. He has long said democratic socialism, but he does not say socialist/socialism at every stop. Wide market."},
    P+"CORR": {"p": 0.62, "reason": "No corpus. Corrupt/corruption fits an oligarchy speech and is not required. Fair at 56–64¢."},
    P+"ROBO": {"p": 0.45, "reason": "No corpus. Robot/robotics is a newer Sanders riff, not the Prop 40 ask. Wide market."},
    P+"ZILL": {"p": 0.58, "reason": "No corpus. Zillionaire is a word he uses, and there is no count of how often. Wide 55–69¢."},
    P+"ISRA": {"p": 0.40, "reason": "No corpus. Israel or Netanyahu is optional at a domestic tax rally and can crowd out the California ask. Fair-to-slight NO at 47–52¢."},
    P+"CLIM": {"p": 0.48, "reason": "No corpus. Climate is not the same as 'save the planet' or fossil-fuel talk, which would not pay. Fair at 45–55¢."},
    P+"INFL": {"p": 0.46, "reason": "No corpus. Inflation is optional next to the wealth-tax argument. Fair at 47–53¢."},
    P+"FARM": {"p": 0.58, "reason": "No corpus. Bakersfield and CA-22 are farm country, so farm/farmer is plausible and uncounted. Wide 37–57¢."},
    P+"TRIL": {"p": 0.38, "reason": "No corpus. Trillionaire is a rarer flourish than billionaire. Fair-to-slight NO at 41–42¢."},
    P+"BERN": {"p": 0.30, "reason": "No corpus. He usually says 'I,' not his own name. A 36–40¢ YES is a little rich."},
    P+"IMMI": {"p": 0.36, "reason": "No corpus. Immigrant/immigration matters in CA-22, but his listed message is the tax and healthcare, not the border. Slightly cheap at 26–27¢ if he wanders; not a count."},
    P+"CHAT": {"p": 0.20, "reason": "No corpus. ChatGPT or OpenAI is off this stop unless he detours into tech oligarchs by product name. Fair versus 17–27¢."},
    P+"EPST": {"p": 0.06, "reason": "No corpus. Epstein is not this rally. Fair at 2–6¢."},
    P+"NUCL": {"p": 0.08, "reason": "No corpus. Nuclear is not the Bakersfield ask. Fair at 4–8¢."},
    P+"NQE": {"p": 0.03, "reason": "The campaign and local news both list the Sunday program. No transcript count; cancellation looks unlikely."},
  },
}
