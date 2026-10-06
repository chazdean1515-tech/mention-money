# KXTRUMPMENTION-26OCT02: Trump midterm rally, Mobile AL (Mitchell Center), Fri Oct 2 2026.
EVENT = "KXTRUMPMENTION-26OCT02"
P = EVENT + "-"
HISTORY_SOURCE = "Trump-only corpus: 27 comparable transcripts · govinfo CPD + 4 Sep 2026 files · exact listed phrase match."
def H(count):
    return {"count": count, "total": 27 if count is not None else None,
            "source": HISTORY_SOURCE if count is not None else "No event transcript or applicable speech count; settlement condition only."}
DATA = {
  "title": "Trump midterm rally in Mobile, Alabama",
  "speaker": "Donald Trump",
  "event_time_et": "2026-10-02T19:00:00-04:00",
  "event_time_note": "GOP/Trump 47: program begins 6:00 p.m. Central (7:00 p.m. ET) at USA Mitchell Center, Mobile AL.",
  "context": ("What: a Trump 47 Committee midterm rally featuring President Donald J. Trump. Who: Trump is the scheduled speaker, "
              "with the event organizer and local reporting framing it as a GOP turnout stop. Where: the Mitchell Center, 5950 Old Shell Rd, "
              "on the University of South Alabama campus in Mobile, Alabama. When: Friday, Oct. 2, 2026; the official listing says the "
              "program begins at 6:00 p.m. Central, or 7:00 p.m. ET (doors at 2:00 p.m. Central). About: Alabama Public Radio reports "
              "the stop is part of a 32-day midterm campaign push, intended to support Tommy Tuberville's Alabama governor campaign and "
              "nearby Florida Panhandle Republican efforts. Same-week hooks: AP reporting identifies cost of living, the economy, gas prices, "
              "the Iran war and concerns about AI data centers as live campaign issues; the official listing publishes no speech agenda. "
              "Those hooks can shift which optional words appear, while the recent Oklahoma rally is a comparable but separate event. The "
              "University of South Alabama says the RNC rented the venue and that Homecoming/weather and Secret Service road closures affect "
              "the campus schedule, not the rally's published start time."),
  "confidence": "Medium. Same rally base rates as Oklahoma; back-to-back schedule makes a shortened speech a real (small) risk.",
  "method": "Word counts are from Trump's own words in 27 transcripts on file: 23 govinfo CPD remarks (May\u2013August 2026, with the subject index and other speakers removed) plus four September transcripts (Dallas convention Sept. 9, Rose Garden dinner Sept. 2, Gastonia rally Sept. 16, and his own lines in the Sept. 18 healthcare transcript). A form counts only when it matches the contract: the exact listed word, a plural or possessive, or either side of a slash. Other inflections do not count.",
  "sources": [
    {"title": "Trump 47 / GOP: Midterm Rally in Mobile, Alabama (Oct 2, 6pm CT)", "url": "https://events.gop.com/events/midterm-rally-in-mobile-alabama-president-trump"},
    {"title": "WEAR: Trump Mitchell Center Mobile Oct 2", "url": "https://weartv.com/news/local/president-trump-coming-to-mobile-on-oct-2-for-rally-at-usas-mitchell-center"},
    {"title": "Alabama Public Radio / Associated Press: Mobile stop and midterm campaign context (Oct. 1)", "url": "https://www.apr.org/news/2026-10-01/president-trump-heads-to-mobile-to-try-to-shore-up-the-gop-before-the-mid-terms"},
    {"title": "University of South Alabama: presidential visit logistics and venue status (Oct. 1)", "url": "https://www.southalabama.edu/departments/publicrelations/presidential-visit.html"},
    {"title": "govinfo CPD Trump remarks corpus", "url": "https://www.govinfo.gov/app/collection/cpd"},
  ],
  "words": {
    P+"TRAN": {
             "history": H(15),"p": 0.92, "reason": "Trail staple; 15/27 official docs. Fair at 90–91¢."},
    P+"FAKE": {
             "history": H(17),"p": 0.92, "reason": "'Fake News' near-automatic at rallies (17/27 corpus). Fair."},
    P+"OIL":  {
             "history": H(24),"p": 0.92, "reason": "Oil/gas in 24/27. Fair at 90–94¢."},
    P+"SLEE": {
             "history": H(17),"p": 0.90, "reason": "'Sleepy Joe' in 17/27; classic rally closer. Fair at 82–91¢."},
    P+"SAVE": {
             "history": H(16),"p": 0.85, "reason": "'Save America Act' is the midterm bill pitch. Fair at 81–91¢."},
    P+"HEAL": {
             "history": H(12),"p": 0.85, "reason": "Healthcare block is live on the trail. Fair at 88–90¢."},
    P+"CHIN": {
             "history": H(20),"p": 0.88, "reason": "China in 20/27. Fair."},
    P+"AFFO": {
             "history": H(14),"p": 0.85, "reason": "Affordability midterm frame. Fair at 76–83¢."},
    P+"DIVI": {
             "history": H(3),"p": 0.80, "reason": "Dividend/stimulus stump promise. Fair."},
    P+"IRAN": {
             "history": H(19),"p": 0.72, "reason": "Iran (5+ times): 19/27 cleared 5+. Fair at 59–65¢."},
    P+"SUPR": {
             "history": H(13),"p": 0.55, "reason": "Supreme Court in 13/27. Fair at 64–75¢ — slight NO lean."},
    P+"BARA": {
             "history": H(14),"p": 0.58, "reason": "'Barack Hussein Obama' in 14/27. Fair."},
    P+"SPAC": {
             "history": H(6),"p": 0.45, "reason": "'Space Force' in 6/27; Gulf military crowd can pull it in. Fair at 55–62¢ — slight NO."},
    P+"HORM": {
             "history": H(16),"p": 0.42, "reason": "Hormuz in 16/27 when Iran is hot; not every rally. Fair at 45–56¢."},
    P+"AMER": {
             "history": H(8),"p": 0.50, "reason": "'America First' in 8/27. Fair."},
    P+"FRAU": {
             "history": H(9),"p": 0.55, "reason": "Fraud talk rises near midterms. Fair."},
    P+"ICE":  {
             "history": H(8),"p": 0.60, "reason": "ICE / border block. Fair."},
    P+"DEPO": {
             "history": H(6),"p": 0.55, "reason": "Deportation language common on trail. Fair at 31–41¢ — slight cheap."},
    P+"FENT": {
             "history": H(7),"p": 0.55, "reason": "Fentanyl tied to border/China. Fair at 28–38¢ — slight cheap."},
    P+"TRUMA": {
             "history": H(8),"p": 0.45, "reason": "'Trump Account' in 8/27. Fair at 34–40¢."},
    P+"AI":   {
             "history": H(19),"p": 0.50, "reason": "AI less forced at an AL midterm rally than at a tech event. Fair at 38–47¢."},
    P+"RUSS": {
             "history": H(16),"p": 0.42, "reason": "Russia/Ukraine optional here. Fair at 40–45¢."},
    P+"TRUM": {
             "history": H(4),"p": 0.42, "reason": "TrumpRx if healthcare block lands. Fair."},
    P+"CHEA": {
             "history": H(13),"p": 0.48, "reason": "Cheat/cheater in 13/27. Fair."},
    P+"SANC": {
             "history": H(3),"p": 0.40, "reason": "Sanctuary in 3/27 official. Fair-to-slight NO at 46–64¢."},
    P+"MADE": {
             "history": H(9),"p": 0.40, "reason": "Made in America in 9/27. Fair at 27–38¢."},
    P+"ISRA": {
             "history": H(8),"p": 0.28, "reason": "Israel in 8/27; foreign-policy optional. Fair at 17–25¢."},
    P+"DATA": {
             "history": H(5),"p": 0.20, "reason": "Data center is a tech-event word. Fair at 14–25¢."},
    P+"FILI": {
             "history": H(3),"p": 0.22, "reason": "Filibuster in 3/27. Fair at 16–21¢."},
    P+"DRIL": {
             "history": H(0),"p": 0.28, "reason": "The exact phrase was not found in the 27-transcript corpus (0/27); no historical rate is inferred."},
    P+"CEAS": {
             "history": H(1),"p": 0.15, "reason": "Ceasefire uncommon at domestic rallies. Fair at 8–11¢."},
    P+"CRYP": {
             "history": H(3),"p": 0.06, "reason": "Crypto rare on the trail. Fair at 1–2¢."},
    P+"NQE":  {
             "history": H(None),"p": 0.02, "reason": "Publicly scheduled; cancellation unlikely."},
  },
}

# Readable paragraphs for the Mobile board. Merged at import so a rebuild keeps them.
PROSE = {
  "KXTRUMPMENTION-26OCT02-IRAN": "The contract counts the word \u201cIran,\u201d or a plural or possessive, and only if he says it at least five times. \u201cIranian\u201d does not count. \u201cIran\u201d itself is in 24 of 27 recent remarks, and he reaches five or more in 15 of those 27, including 24 times in the June 4 coal remarks. The Iran war is already part of this week\u2019s stump, so Mobile can get there, unless the speech after Durant is the short one.",
  "KXTRUMPMENTION-26OCT02-OIL": "Oil, gas, or gasoline counts, including a plural or possessive of any of them. One of those words is in 24 of 27 recent remarks, including 20 times in the June 23 Macungie speech. Gas prices are already part of this week’s campaign talk, so a Mobile rally the night after Durant is one of the settings least likely to drop it.",
  "KXTRUMPMENTION-26OCT02-TRAN": "Only the exact word “transgender,” or a plural or possessive, counts. It is in 15 of 27 recent remarks, six times in the Sept. 9 Dallas speech. A Tuberville rally in Mobile, back to back with Durant, is the kind of stump where he usually gets there, unless the second-night speech is cut short.",
  "KXTRUMPMENTION-26OCT02-FAKE": "“Fake news” counts. Other insults do not. It is in 17 of 27 recent remarks, seven times in the May 22 Suffern speech. He uses it more at rallies than at short signings, and Mobile is a rally, but the turnaround from Durant is the reason it is not automatic.",
  "KXTRUMPMENTION-26OCT02-HEAL": "The contract is the single word “healthcare,” plus a plural or possessive. That one-word form is in only 3 of 27 remarks, all in September, including seven times in Dallas. The two-word “health care,” which does not match, is in 9 of 27. Cost of living is a Mobile theme, but if he says it the way he usually does, this contract can still miss.",
  "KXTRUMPMENTION-26OCT02-DIVI": "Either “dividend” or “stimulus” counts, with plurals and possessives. “Stimulus” is in none of the 27. “Dividend” is in 3, including seven times in Dallas on Sept. 9, where he promised a citizen dividend. Alabama adds no local reason to say it, and a shorter speech after Durant makes the riff easy to skip.",
  "KXTRUMPMENTION-26OCT02-SLEE": "The nickname “Sleepy Joe,” or a possessive of it, counts. It is in 17 of 27 recent remarks, five times in Macungie on June 23. Midterm rallies are where he uses it, and Mobile is one, the night after Durant.",
  "KXTRUMPMENTION-26OCT02-SAVE": "The phrase “Save America Act,” or a plural or possessive, counts. It is in 16 of 27, four times in Suffern on May 22. With the midterms close and Tuberville on the Alabama ballot, this is a live pitch, unless the back-to-back schedule shortens the speech.",
  "KXTRUMPMENTION-26OCT02-FRAU": "“Fraud,” or a plural or possessive, counts. “Fraudulent” does not. It is in 9 of 27, five times at the Sept. 2 Rose Garden dinner. Election talk fits a Mobile turnout rally better than a factory stop, but it is not in most of these speeches.",
  "KXTRUMPMENTION-26OCT02-CHEA": "“Cheat,” “cheater,” or “cheating” counts, including a plural or possessive. “Cheated” does not. A listed form is in 13 of 27, seven times in the June 23 Macungie remarks. Tuberville’s race can pull an election riff, and the night after Durant can just as easily skip it.",
  "KXTRUMPMENTION-26OCT02-AFFO": "“Afford,” “affordable,” or “affordability” counts, plus a plural or possessive. “Afforded” does not. One of them is in 14 of 27, six times in the June 4 coal remarks. Cost of living is the issue tied to this week’s stops, so Mobile leans toward the word even if the speech runs short.",
  "KXTRUMPMENTION-26OCT02-MADE": "Either “made in America” or “American made” counts, with a plural or possessive. One of those phrases is in 9 of 27, three times in the July 27 Milford auto remarks. Nothing about Mobile or Tuberville forces the slogan, and it is easy to drop on the second rally in two nights.",
  "KXTRUMPMENTION-26OCT02-SUPR": "“Supreme Court,” or a plural or possessive, counts. It is in 13 of 27, six times at the Aug. 6 semiconductor signing, which was a legal fight rather than a rally. Mobile does not add a court hook, so a back-to-back stump is a weaker setting than the raw rate.",
  "KXTRUMPMENTION-26OCT02-BARA": "The full name “Barack Hussein Obama,” or a possessive, counts. “Obama” alone does not. The full name is in 14 of 27, usually once or twice. He uses it as a rally insult, so Mobile can include it, but Durant the night before may already have spent the bit.",
  "KXTRUMPMENTION-26OCT02-SPAC": "“Space Force,” or a plural or possessive, counts. It is in 6 of 27, five of those mentions in the June 23 Macungie speech. Mobile’s Gulf Coast crowd is a reason he might say it, not a reason he must, especially on the second night after Durant.",
  "KXTRUMPMENTION-26OCT02-CHIN": "“China” or “Chinese” counts, including plurals and possessives. One of them is in 20 of 27, 12 times in the July 29 Dulles remarks. No Alabama hook requires it. It shows up when he riffs, and a shortened Mobile speech is the main way it gets skipped.",
  "KXTRUMPMENTION-26OCT02-AMER": "The phrase “America First,” or a possessive, counts. It is in 7 of 27, and it is not in the four September transcripts. A Tuberville rally might still use the slogan, but these speeches show he often campaigns without saying those two words.",
  "KXTRUMPMENTION-26OCT02-HORM": "“Hormuz,” or a possessive, counts. It is in 13 of 27, five times at the June 22 signing, where Iran was the subject. The Iran war is a live issue this week, so Mobile can include the strait, but it is not in every long speech.",
  "KXTRUMPMENTION-26OCT02-DATA": "“Data center,” or a plural or possessive, counts. It is in 5 of 27, 13 times at the July 23 ratepayer roundtable, and in none of the four September transcripts. Worries about AI data centers are in this week’s campaign coverage, which is the only Mobile-specific reason to expect the phrase.",
  "KXTRUMPMENTION-26OCT02-TRUMA": "“Trump Account,” or a plural or possessive, counts. It is in 8 of 27, and he repeats it when the event is about the program: 23 times on July 6 and 17 times at the Jan. 28 Mellon remarks. Mobile is a Tuberville turnout rally, not an accounts event, so the product name is optional.",
  "KXTRUMPMENTION-26OCT02-RUSS": "“Russia” or “Ukraine” counts, with plurals and possessives. Russia is in 14 of 27 and Ukraine is in 8. Either word settles it, so the rate is at least 14 of 27. A foreign-war aside is optional at an Alabama rally the night after Durant.",
  "KXTRUMPMENTION-26OCT02-AI": "“AI” or “artificial intelligence” counts, including a plural or possessive. The word “AI” is in 17 of 27, nine times at the Aug. 19 meeting with tech leaders. The full phrase is in 6. Data centers are in the news, but a Mobile midterm rally is a weaker room for it than a tech event, and the Durant turnaround can cut the aside.",
  "KXTRUMPMENTION-26OCT02-FENT": "“Fentanyl,” or a possessive, counts. It is in 7 of 27, three times in the Aug. 5 Las Vegas remarks. Border talk can bring it up for a midterm crowd, but most of these speeches skip the word, and Mobile does not force it.",
  "KXTRUMPMENTION-26OCT02-ICE": "The contract is the exact word “ICE,” or a plural or possessive. It is in 7 of 27, six times in the Aug. 5 Las Vegas remarks. He often talks about the border without saying “ICE,” and the second rally in two nights does not require it.",
  "KXTRUMPMENTION-26OCT02-ISRA": "“Israel” or “Israeli” counts, with plurals and possessives. One of them is in 8 of 27, seven times at the June 26 Faith and Freedom speech. Nothing on the Mobile stop requires it, and a domestic rally after Durant is an easy place to leave it out.",
  "KXTRUMPMENTION-26OCT02-DEPO": "“Deport,” “deported,” or “deportation” counts, plus a plural or possessive. “Deporting” does not. A listed form is in 3 of 27: once each at Gastonia on Sept. 16, the Aug. 6 signing, and the Aug. 14 Garden City remarks. He often covers the border without these words. Mobile does not change that.",
  "KXTRUMPMENTION-26OCT02-SANC": "“Sanctuary,” a plural, or a possessive counts. It is in 3 of 27, and when it appears he repeats it: eight times at Gastonia, eight times in Suffern on May 22, and eight times in Garden City on Aug. 14. Alabama is not a sanctuary-state set piece, so the Durant–Mobile double is more likely to skip it.",
  "KXTRUMPMENTION-26OCT02-DRIL": "The contract is the phrase “drill baby drill,” or a plural or possessive of that phrase. The unpunctuated phrase is not in these 27 transcripts. Trump does say “drill, baby, drill” once, in the June 23 Macungie remarks. A similar line at the Aug. 7 mining roundtable is Secretary Burgum, not Trump. Gulf energy gives Mobile a reason to revive it, but the exact chant is rare in this set.",
  "KXTRUMPMENTION-26OCT02-TRUM": "“TrumpRx,” or a possessive, counts, including a spaced “Trump Rx.” It is in 3 of 27: twice in Milford on July 27, and once each in Macungie and Marietta. A Mobile speech that reaches drug prices might say it. A short second-night speech might not.",
  "KXTRUMPMENTION-26OCT02-FILI": "“Filibuster,” or a plural or possessive, counts. It is in 3 of 27, five times in the July 22 Marietta remarks. Senate procedure is not a Mobile applause line, and the night after Durant is a poor time to add it.",
  "KXTRUMPMENTION-26OCT02-CEAS": "“Ceasefire” or “cease-fire,” plus a plural or possessive, counts. In Trump’s own words in these 27 transcripts, it does not appear. The only “ceasefire” in the June 4 coal file is a reporter’s question. A domestic Alabama rally does not fix that.",
  "KXTRUMPMENTION-26OCT02-CRYP": "“Crypto” or “bitcoin” counts, with plurals and possessives. One of them is in 3 of 27, and those hits are long: 25 times at the Aug. 19 tech meeting and 21 times in the July 6 Trump Accounts remarks. A Tuberville rally is not that room. Mobile makes it less likely, not more.",
  "KXTRUMPMENTION-26OCT02-NQE": "This is not a word. It pays only if the Mobile rally is cancelled or fails to qualify. The GOP listing has it at 7:00 p.m. ET at the Mitchell Center. The Durant–Mobile–Ohio run is tight, but a delay that is rescheduled under the rules would not, by itself, make this a yes."
}
for _k,_t in PROSE.items():
    DATA['words'][_k]['prose']=_t
