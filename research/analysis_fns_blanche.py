# KXFNSMENTION-26OCT04: Todd Blanche on Fox News Sunday, Sun Oct 4 2026.
# No Blanche transcript corpus on file. Do not invent hit counts.
EVENT = "KXFNSMENTION-26OCT04"
P = EVENT + "-"
DATA = {
  "title": "Todd Blanche on Fox News Sunday",
  "speaker": "Todd Blanche",
  "event_time_et": "2026-10-04T09:00:00-04:00",
  "event_time_note": "Fox News Sunday airs live at 9:00 a.m. ET on the FOX broadcast network (Wikipedia; FOX 5 DC lists 9:00 a.m.). Some local stations delay it. Fox News Channel re-airs it at 2:00 p.m. ET.",
  "context": ("What: FOX News Sunday with Shannon Bream. Who: Attorney General Todd Blanche, booked with Justice Samuel Alito on the Supreme Court's new term (Fox promo and Politico's Sunday listings). "
              "Where: the Fox News Sunday set. When: Sunday, Oct. 4, 2026, live at 9:00 a.m. ET. About: the promo is the Court's term, not a rally. "
              "Separate from that booking, Blanche told CBS on Sept. 14 that mail voting has a greater 'potential for fraud' than 'in-person voting with ID,' "
              "and on Sept. 30 he announced Minnesota voter-fraud indictments and said 'voter fraud' at that press conference. "
              "No transcript corpus, so none of those appearances is a hit rate."),
  "confidence": "Low-medium. No transcript corpus; judgment from the booking plus two sourced appearances.",
  "method": "No counted corpus. Probabilities are topic judgment. Quoted words below are from reported remarks, not a transcript tally. Slash markets pay on either word. 'Illegal Alien' is that phrase, not 'illegally' or 'illegal immigrant.' Trump (3+ times) needs three says.",
  "fragile_sides": {"YES": "Several YES cases need an exact phrase he has not been quoted using."},
  "sources": [
    {"title": "Fox: Coming Up on Fox News Sunday, Oct. 4, 2026 (Blanche and Alito)", "url": "https://www.foxnews.com/video/6406176458112"},
    {"title": "Wikipedia: Fox News Sunday airs live at 9:00 a.m. ET", "url": "https://en.wikipedia.org/wiki/Fox_News_Sunday"},
    {"title": "CBS: Blanche on mail ballots, fraud, and ID (Sept. 14, 2026)", "url": "https://www.cbsnews.com/news/blanche-defends-mail-ballot-changes-election-practices-probed/"},
    {"title": "Fox: Blanche announces Minnesota voter-fraud charges (Sept. 30, 2026)", "url": "https://www.foxnews.com/politics/blanche-announces-charges-against-10-permanent-residents-accused-minnesota-voter-fraud"},
  ],
  "words": {
    P+"SUPR": {"p": 0.86, "reason": "No corpus. The Fox promo says he is there with Justice Alito on the Court's new term, and the Court just left his mail-ballot rule blocked. Fair at 85–91¢."},
    P+"MIDT": {"p": 0.70, "reason": "No corpus. Midterm or election fits a voting-rule interview, but the promo is the Court, not a campaign hit. Wide 70–81¢."},
    P+"MINN": {"p": 0.72, "reason": "No corpus. He announced Minnesota voter-fraud charges on Sept. 30, so the state is live, but this segment may stay on the Court. Roughly fair at 74–78¢."},
    P+"TRUM": {"p": 0.50, "reason": "No corpus. He works for Trump, but three says in one Sunday answer is not automatic. Wide and thin volume."},
    P+"FRAU": {"p": 0.72, "reason": "No hit count. He used 'fraud' with CBS on Sept. 14 and 'voter fraud' at the Sept. 30 press conference. A Court-term interview may not go there. Still short of 72% at 62–64¢."},
    P+"DEMO": {"p": 0.45, "reason": "No corpus. Democrat is optional in a legal interview. Fair-to-slight NO at 50–57¢."},
    P+"FBI": {"p": 0.40, "reason": "No corpus and no recent Blanche quote using FBI in the sources read. Wide market."},
    P+"ILLE": {"p": 0.28, "fragile": True, "reason": "No corpus. The contract is the phrase 'illegal alien.' Quoted remarks say 'here illegally'; the Fox writeup says 'illegal immigrants,' which does not by itself pay. Wide market."},
    P+"ID": {"p": 0.32, "reason": "No corpus. On Sept. 14 he contrasted mail voting with 'in-person voting with ID,' so the word has a real hook and is not a count. Fair versus 21–27¢."},
    P+"AI": {"p": 0.10, "reason": "No corpus. AI is off the Court-and-voting booking. Fair-to-slight NO versus 14–23¢."},
    P+"ICE": {"p": 0.30, "reason": "No corpus. ICE is in the Minnesota judicial fight he complained about, but he may not name the agency. Fair versus 17–27¢."},
    P+"CHIN": {"p": 0.10, "reason": "No corpus. China is not this booking. Wide market."},
    P+"WEAP": {"p": 0.22, "reason": "No corpus. Weaponize/weaponization is a DOJ talking point he has not been quoted on in the sources read. Wide market."},
    P+"TERR": {"p": 0.12, "reason": "No corpus. Terrorist/terrorism is not the Sunday promo. Fair versus 10–18¢."},
    P+"FENT": {"p": 0.08, "reason": "No corpus. Fentanyl is not this booking. Wide market."},
    P+"EPST": {"p": 0.06, "reason": "No corpus. Epstein is a tail word here. Fair versus 1–8¢."},
    P+"NQE": {"p": 0.03, "reason": "Fox posted the Oct. 4 promo with Blanche. No transcript count; cancellation looks unlikely."},
  },
}
