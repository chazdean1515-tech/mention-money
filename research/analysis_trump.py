# Analysis for KXTRUMPMENTION-26SEP29 (Trump "Golden Age" remarks, Mellon Auditorium, Tue Sep 29 2026)
# Base rates from the research folder: 23 Trump remarks transcripts Jun–Aug 2026 (govinfo DCPD) + 4 Sep 2026 transcripts.
EVENT = "KXTRUMPMENTION-26SEP29"
P = "KXTRUMPMENTION-26SEP29-"
DATA = {
  "title": "Trump remarks at the Mellon Auditorium ('Golden Age' event)",
  "speaker": "Donald Trump",
  "event_time_et": "2026-09-29T10:00:00-04:00",
  "event_time_note": "Morning address; exact start time not published (10:00 ET is a placeholder).",
  "context": ("Daylong 'Golden Age' showcase at the Mellon Auditorium: Trump gives a morning 'address to the nation', "
              "America.gov (an AI-powered federal services portal) launches, afternoon panels on AI, energy, health, space, agriculture; "
              "Musk, Jensen Huang, Vance, Rubio, Energy Sec. Wright, NASA's Isaacman expected. Trump's Sept stump speeches repeat: "
              "'hottest country', '80 all-time stock market records', '$20T+ investment', Most-Favored-Nation drug prices, Iran/oil, tariffs, "
              "'Sleepy Joe Biden'. Key uncertainty: length/format. A long ad-libbed speech (his norm: 7–14k words) makes most staples likely; "
              "a short teleprompter address cuts them. Market prices look like they assume the shorter/scripted version, so my YES leans "
              "below are all correlated bets on 'Trump riffs'. Resolution: exact word or plural/possessive; Trump only."),
  "confidence": "Medium-low. Base rates solid; speech length unknown; all edges correlated.",
  "method": ("Share of 23 Trump remarks transcripts (Jun–Aug 2026, govinfo) containing the word, plus 4 Sep-2026 speeches (RNC Dallas Sep 9, "
             "Rose Garden Sep 2, Gastonia rally Sep 16, healthcare remarks Sep 18), adjusted for a tech/AI-themed, possibly shorter address."),
  "sources": [
    {"title": "CBS News: Trump to headline 'Golden Age' event (Sep 24)", "url": "https://www.cbsnews.com/news/trump-golden-age-event-tech-executives-elon-musk-jensen-huang-ai/"},
    {"title": "Fox News: America.gov AI tool launch at DC event (Sep 25)", "url": "https://www.foxnews.com/politics/trump-usher-golden-age-american-tech-dc-bash-showcasing-powerful-new-tool"},
    {"title": "govinfo: Trump remarks at Mellon Auditorium, Jan 28 2026 (analog)", "url": "https://www.govinfo.gov/content/pkg/DCPD-202600061/html/DCPD-202600061.htm"},
    {"title": "UCSB Presidency Project: RNC Midterm Convention remarks, Sep 9 2026", "url": "http://presidency.ucsb.edu/documents/remarks-night-one-the-2026-republican-midterm-convention-dallas-texas"},
    {"title": "Transcript: Rose Garden dinner, Sep 2 2026", "url": "https://singjupost.com/transcript-president-trump-remarks-at-rose-garden-dinner-sept-2-2026/"},
    {"title": "govinfo Compilation of Presidential Documents (Jun–Aug 2026 remarks corpus)", "url": "https://www.govinfo.gov/app/collection/cpd"},
  ],
  "words": {
    P+"AI":   {"p": 0.94, "reason": "It's an AI showcase (America.gov is AI-powered; AI panels). Said 'AI' in 7/7 tech-themed remarks, 17/23 overall."},
    P+"INVE": {"p": 0.93, "reason": "'$20 trillion invested' is a fixture: 22/23 Jun–Aug transcripts, 4/4 Sept."},
    P+"CHIN": {"p": 0.80, "reason": "AI-race-vs-China framing is standard; 16/23 overall, 5/7 tech events. Fairly priced."},
    P+"OIL":  {"p": 0.85, "reason": "Oil/gas prices + Iran line + energy panel; 20/23 transcripts. Roughly fair."},
    P+"BIDE": {"p": 0.80, "reason": "'Sleepy Joe Biden' in 20/23 Jun–Aug and 4/4 Sept speeches; only risk is a tightly scripted address."},
    P+"HOTT": {"p": 0.74, "reason": "'Hottest country in the world' in every Sept speech checked (4/4), 15/23 earlier. Fair."},
    P+"IRAN": {"p": 0.80, "reason": "The Iran strike and the 'weeks from a nuclear weapon' line are in all 4 Sept speeches; 20/23 earlier."},
    P+"STOC": {"p": 0.70, "reason": "'80 all-time stock market records' is a Sept stump line (3/4); only 2/7 in tech settings. Fair."},
    P+"TARI": {"p": 0.72, "reason": "Tariffs fund his promised 'Trump dividend'; 18/23 Jun–Aug, 4/4 Sept, 5/7 tech events."},
    P+"NUCL": {"p": 0.72, "reason": "Two routes: nuclear power for AI data centers (energy panel) and Iran's nuclear weapon. 17/23 overall, 6/7 tech."},
    P+"HEAL": {"p": 0.48, "reason": "Big Sept theme (MFN drug prices, Sep 18 healthcare speech), but 0/7 in tech-themed remarks. Near fair."},
    P+"INFL": {"p": 0.52, "reason": "14/23 transcripts; usually in economic riffs. Fair."},
    P+"RADI": {"p": 0.50, "reason": "Constant at rallies (4/4 Sept) but only 10/23 in official remarks. Slightly rich at 54–57¢."},
    P+"MIDT": {"p": 0.50, "reason": "Midterms are 5 weeks away, but this isn't a campaign event. 13/23. Fair."},
    P+"MANU": {"p": 0.60, "reason": "Factories/'manufacturing coming back' in 16/23 overall and 5/7 tech events; ties to chips/AI buildout."},
    P+"FAKE": {"p": 0.45, "reason": "4/4 Sept speeches, but only 1/7 tech-themed remarks. Fair."},
    P+"NOTA": {"p": 0.38, "reason": "Stump line (4/4 Sept), 10/23 official remarks, 2/7 tech. Fair."},
    P+"MOST": {"p": 0.28, "reason": "MFN drug pricing is in every Sept stump speech but 0/7 tech events. Fair."},
    P+"IMMI": {"p": 0.30, "reason": "'Immigration/immigrants' in 14/23 remarks (3/7 tech). He often says 'illegal aliens' instead, but 21–23¢ looks low."},
    P+"AFFO": {"p": 0.30, "reason": "'Afford/affordable/affordability' in 11/23 remarks (3/7 tech); he mocks the Democrats' 'affordability' message. 21¢ looks low."},
    P+"TRUM": {"p": 0.15, "reason": "3/23 remarks. Could come up if America.gov links to TrumpRx. Slightly rich."},
    P+"ISRA": {"p": 0.18, "reason": "7/23 remarks, 3/7 tech; can come up through Iran/Middle East riffs. 11¢ looks a bit low."},
    P+"CRYP": {"p": 0.10, "reason": "4/23 overall (0/4 Sept) despite tech crowd. Fair to slightly cheap."},
    P+"NQE":  {"p": 0.02, "reason": "Resolves YES only if the event doesn't qualify (e.g. cancelled). No sign of that."},
  },
}
