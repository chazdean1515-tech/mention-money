# Analysis for KXTRUMPMENTION-26SEP28 (Oval Office announcement, Mon Sep 28 2026 ~2pm ET)
# Base rates from 23 Jun–Aug 2026 govinfo remarks + topic priors (AI vs diesel-export speculation).
EVENT = "KXTRUMPMENTION-26SEP28"
P = EVENT + "-"
DATA = {
  "title": "Trump Oval Office announcement (topic undisclosed)",
  "speaker": "Donald Trump",
  "event_time_et": "2026-09-28T14:00:00-04:00",
  "event_time_note": "White House schedule: announcement open to press pool at 2:00 p.m. ET. Topic not officially disclosed as of morning ET.",
  "context": ("Short Oval Office announcement (usually tighter than a rally). Press guesswork centers on (a) AI policy after a Sunday dinner with Anthropic CEO Dario Amodei "
              "and a Tuesday AI meeting with tech CEOs, and/or (b) a diesel/fuel export restriction after Trump said Sunday he was looking 'very seriously' at a ban. "
              "Those two paths load different word sets (AI/China/tariff/nuclear vs oil/gas/Iran). Staples like Biden/fake news are less automatic in a scripted Oval hit. "
              "'Super Intelligence' has ~0 hits in the Jun–Aug corpus — an 81¢ ask is only sane if the speech is explicitly about AGI."),
  "confidence": "Low–medium. Topic unconfirmed; format short; base rates from longer remarks overstate stump staples.",
  "method": ("Share of 23 Jun–Aug 2026 govinfo Trump remarks containing the word, adjusted down for a short scripted Oval announcement and for the AI-vs-energy topic fork."),
  "sources": [
    {"title": "Daily Mail: mystery Oval announcement 2pm; diesel ban / AI speculation (Sep 28)", "url": "https://www.dailymail.com/news/article-16166419/trump-oval-office-announcement-diesel-ai.html"},
    {"title": "Newsweek: mystery announcement; Anthropic dinner context", "url": "https://www.newsweek.com/donald-trump-to-make-mystery-announcement-today-what-we-know-12495760"},
    {"title": "govinfo CPD Trump remarks corpus (Jun–Aug 2026)", "url": "https://www.govinfo.gov/app/collection/cpd"},
  ],
  "words": {
    P+"AI":   {"p": 0.72, "reason": "17/23 overall; AI is one of the two live topic guesses after the Anthropic dinner. Fair-to-slight NO at 78¢."},
    P+"OIL":  {"p": 0.70, "reason": "20/23 base rate; diesel/export-ban path is the other live guess. Slight NO at 88¢."},
    P+"CHIN": {"p": 0.62, "reason": "16/23; AI-race framing if it's an AI speech. 88¢ looks rich for a short hit."},
    P+"TARI": {"p": 0.55, "reason": "18/23 in long remarks; semiconductor-tariff angle only if AI/chips. 84¢ rich."},
    P+"INVE": {"p": 0.55, "reason": "22/23 stump staple ('trillions invested') but less forced in a short Oval policy hit. 63¢ roughly fair."},
    P+"IRAN": {"p": 0.45, "reason": "Market is 'Iran (2+ times)'. 20/23 say Iran once in long speeches; twice in a short Oval is harder. 75¢ rich."},
    P+"BIDE": {"p": 0.40, "reason": "20/23 in long remarks; Oval policy announcements often skip the Biden riff. 83¢ rich. NO lean."},
    P+"NUCL": {"p": 0.40, "reason": "17/23; nuclear power for AI data centers OR Iran. Uncertain. 68¢ a bit rich."},
    P+"SUPE": {"p": 0.22, "reason": "0/23 Jun–Aug hits for 'super intelligence'. Only pays if the AI speech uses that buzzword. 81¢ very rich. NO lean."},
    P+"FAKE": {"p": 0.25, "reason": "13/23 in long remarks; uncommon in scripted Oval policy hits. 75¢ rich."},
    P+"STOC": {"p": 0.30, "reason": "14/23 stump line; not core to AI or diesel. 71¢ rich."},
    P+"HOTT": {"p": 0.25, "reason": "'Hottest country' is stump, not Oval policy. 68¢ rich."},
    P+"DEMO": {"p": 0.35, "reason": "18/23 say Democrat(s); still optional here. 74¢ rich."},
    P+"INFL": {"p": 0.40, "reason": "14/23; diesel prices could pull it in. Fair-to-slight NO at 58¢."},
    P+"UKRA": {"p": 0.25, "reason": "6/23; not on the AI/diesel shortlist. 52¢ rich."},
    P+"RUSS": {"p": 0.28, "reason": "12/23; same. 50¢ rich."},
    P+"FAVO": {"p": 0.18, "reason": "Most-favored-nation / favored nation 4/23; healthcare track. 48¢ rich."},
    P+"HEAL": {"p": 0.20, "reason": "8/23; not the speculated topic. 44¢ rich."},
    P+"IMMI": {"p": 0.18, "reason": "14/23 in long remarks; unlikely today. 38¢ rich."},
    P+"NATO": {"p": 0.12, "reason": "7/23. 31¢ rich."},
    P+"TRUM": {"p": 0.10, "reason": "TrumpRx 3/23. 32¢ rich."},
    P+"AFFO": {"p": 0.18, "reason": "11/23; fuel prices could trigger 'affordability'. Fair at 22¢."},
    P+"FENT": {"p": 0.08, "reason": "5/23. Slightly rich at 19¢."},
    P+"GREE": {"p": 0.04, "reason": "0/23 in corpus. 16¢ rich."},
    P+"CRYP": {"p": 0.06, "reason": "4/23. Fair at 8¢."},
    P+"NQE":  {"p": 0.03, "reason": "Cancels only if the event doesn't qualify. Schedule looks firm."},
  },
}
