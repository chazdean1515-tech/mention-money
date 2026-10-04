# KXFTNMENTION-26OCT04: Chris Wright on CBS Face the Nation, Sun Oct 4 2026.
# Counts are Wright's own words in two full transcripts. Partial quotes are not in the denominator.
EVENT = "KXFTNMENTION-26OCT04"
P = EVENT + "-"
HISTORY_SOURCE = "Chris Wright only: 2 full transcripts (CBS Face the Nation May 10, 2026; CNBC Squawk Box Sept 2, 2026). Exact listed word, plural, or possessive."
def H(count):
    return {"count": count, "total": 2, "source": HISTORY_SOURCE}
DATA = {
  "title": "Chris Wright on Face the Nation",
  "speaker": "Chris Wright",
  "event_time_et": "2026-10-04T10:30:00-04:00",
  "event_time_note": "CBS: Face the Nation airs at 10:30 a.m. ET on Oct. 4. The Paramount+ / CBSNews.com stream is 12:30 p.m. ET. Wright is a booked guest, not the whole hour.",
  "context": ("What: CBS Face the Nation with Margaret Brennan. Who: Energy Secretary Chris Wright, listed by CBS on Oct. 2 with Sen. Mark Kelly, Brett McGurk, Iowa nominee Zach Lahn, and CBS correspondents. "
              "Where: the Face the Nation set (Washington). When: Sunday, Oct. 4, 2026, 10:30 a.m. ET. About: Iran was still saying that morning that Hormuz stays closed until its conditions are met. "
              "Wright's recent hits have been that war and the oil flow, not a campaign speech. No Face the Nation transcript exists yet for today."),
  "confidence": "Medium. Two full transcripts of his own words, both during this Hormuz crisis; not a large corpus.",
  "method": "Presence counted only in Wright's answers in two full transcripts: CBS Face the Nation, May 10, 2026, and CNBC Squawk Box from Caracas, Sept. 2, 2026. A slash market hits if either word appears. Trump (3+ times) needs three says of Trump. Quoted lines from other days are not added to the 2-transcript denominator.",
  "sources": [
    {"title": "CBS: Face the Nation guests for Oct. 4, 2026 (airs 10:30 a.m. ET)", "url": "https://www.cbsnews.com/news/face-the-nation-guests-10-04-2026/"},
    {"title": "CBS transcript: Wright on Face the Nation, May 10, 2026", "url": "https://www.cbsnews.com/news/chris-wright-energy-secretary-face-the-nation-transcript-05-10-2026/"},
    {"title": "CNBC transcript: Wright on Squawk Box, Sept. 2, 2026", "url": "https://www.cnbc.com/2026/09/02/cnbc-transcript-us-energy-secretary-chris-wright-speaks-with-cnbcs-brian-sullivan-on-squawk-box-today.html"},
    {"title": "Iran International: Hormuz still closed pending Iran's conditions (Oct. 4)", "url": "https://www.iranintl.com/en/202610040986"},
  ],
  "words": {
    P+"OIL": {"history": H(2), "p": 0.94, "reason": "Oil or gas is in 2/2 full transcripts. Fair at 93–95¢."},
    P+"IRAN": {"history": H(2), "p": 0.90, "reason": "Iran/Iranian is in 2/2. This booking is the same war. Fair at 84–87¢."},
    P+"EURO": {"history": H(0), "p": 0.70, "reason": "Europe/European is 0/2 in the transcripts counted. He does say Europe in other 2026 settings (EU energy rules, pipelines), so it is not a never-word, but 76–85¢ is a little rich if Brennan stays on Hormuz."},
    P+"HORM": {"history": H(2), "p": 0.88, "reason": "Hormuz is in 2/2 full transcripts, and Iran was still conditioning a reopening on Sunday morning. The 68–77¢ YES is short of that."},
    P+"CHIN": {"history": H(0), "p": 0.55, "reason": "China/Russia is 0/2 in Wright's own words in the transcripts counted (the host said both on Sept. 2). A May 15 CNBC excerpt quotes him saying China; that interview is not in the denominator. Spread is too wide to trade off this."},
    P+"NUCL": {"history": H(2), "p": 0.84, "reason": "Nuclear is in 2/2, including the Iranian program. Fair-to-cheap versus a wide 64–75¢."},
    P+"TRUM": {"history": H(1), "p": 0.48, "reason": "Trump three times: 6 says on Sept. 2, but only 1 say in the May 10 Face the Nation interview. A short Sunday hit often misses 3. Wide market."},
    P+"DEMO": {"history": H(0), "p": 0.18, "reason": "Democrat is 0/2. He said 'opposition party' on May 10, which does not count. Wide market."},
    P+"ELEC": {"history": H(0), "p": 0.25, "reason": "Election is 0/2. A midterm question could draw it, but it is not his subject. Fair versus 26–29¢."},
    P+"VENE": {"history": H(1), "p": 0.42, "reason": "Venezuela is 1/2, and that hit was the Sept. 2 interview taped in Caracas. Today's booking is Hormuz, not a Venezuela deal. Wide market."},
    P+"AFFO": {"history": H(0), "p": 0.22, "reason": "Afford/affordable/affordability is 0/2. Wide market."},
    P+"CALI": {"history": H(0), "p": 0.18, "reason": "California is 0/2. No California hook on this guest list beyond other interviewees. Wide market."},
    P+"DATA": {"history": H(0), "p": 0.16, "reason": "Data center is 0/2. Wide market."},
    P+"AI": {"history": H(0), "p": 0.12, "reason": "AI / artificial intelligence is 0/2. Wide market."},
    P+"STOC": {"history": H(0), "p": 0.20, "reason": "Stockpile is 0/2. On Sept. 2 he discussed the Strategic Petroleum Reserve and swaps, not the word stockpile. Fair versus 13–21¢."},
    P+"NQE": {"p": 0.03, "reason": "CBS published the guest list. No transcript count; cancellation looks unlikely."},
  },
}
