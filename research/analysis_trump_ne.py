# KXTRUMPMENTION-26OCT05: Trump midterm rally, Grand Island NE (Pinnacle Bank Expo Center, Fonner Park), Mon Oct 5 2026.
# Hit counts below are real Kalshi settlements from the last three midterm rallies (Durant OK Oct 1, Mobile AL Oct 2,
# Vandalia OH Oct 3) plus the 27-speech Jun-Sep 2026 corpus used in analysis_trump_al.py. Nothing else is counted.
EVENT = "KXTRUMPMENTION-26OCT05"
P = EVENT + "-"
DATA = {
  "title": "Trump midterm rally in Grand Island, Nebraska",
  "speaker": "Donald Trump",
  "event_time_et": "2026-10-05T19:00:00-04:00",
  "event_time_note": "GOP/Trump 47 and local press: doors 2:30 p.m. CT, program 4:30 p.m. CT, Trump speaks at 6:00 p.m. CT (7:00 p.m. ET), Pinnacle Bank Expo Center at Fonner Park, Grand Island.",
  "context": ("Fourth midterm rally in five days (Durant OK, Mobile AL, Vandalia OH). He is there mainly for Sen. Pete Ricketts against independent Dan Osborn. "
              "The venue is the Nebraska State Fair grounds in farm country, so farm talk is natural and corn/ethanol is plausible. "
              "The last three rallies used the same stump: Oil/Gas, Fake News, Transgender, Dividend, Healthcare, Fraud, Save America Act, Barack Hussein Obama, Cheat, and Made in America all hit 3 of 3. "
              "TrumpRx, Trump Account, Deport, Fentanyl, Hormuz, Israel, Ceasefire, Filibuster, and Crypto went 0 of 3."),
  "confidence": "Medium. Three same-format rallies this week, all settled, plus a 27-speech summer corpus.",
  "method": "Presence in the last 3 settled midterm rallies (OK, AL, OH), weighted over the 27-speech Jun-Sep corpus; Nebraska adjustments only for farm/corn and data centers.",
  "sources": [
    {"title": "GOP: Midterm Rally in Grand Island, Nebraska (program 4:30 p.m. CT)", "url": "https://events.gop.com/events/midterm-rally-in-grand-island-nebraska-president-donald-j-trump"},
    {"title": "Central Nebraska Today: Trump speaks at 6 p.m. Oct. 5 at Fonner Park", "url": "https://www.centralnebraskatoday.com/2026/09/29/president-trump-will-speak-in-g-i-at-6-p-m-monday-oct-5-at-pinnacle-bank-expo-center-at-fonner-park/"},
    {"title": "NTV: Trump in Grand Island, campaigning for Ricketts vs. Osborn", "url": "https://nebraska.tv/news/local/confirmed-president-trump-is-headed-to-grand-island"},
    {"title": "Kalshi settlements: KXTRUMPMENTION-26OCT01 / 26OCT02 / 26OCT03", "url": "https://kalshi.com/markets/kxtrumpmention"},
  ],
  "words": {
    P+"OIL":  {"p": 0.95, "reason": "3 of 3 this week and 24/27 in the corpus. Fair at the top of the board."},
    P+"FAKE": {"p": 0.95, "reason": "3 of 3 this week. Fair."},
    P+"TRAN": {"p": 0.94, "reason": "3 of 3 this week. Fair."},
    P+"DIVI": {"p": 0.90, "reason": "3 of 3 this week; the dividend/stimulus promise is in the current stump. Fair to slightly rich."},
    P+"HEAL": {"p": 0.92, "reason": "3 of 3 this week. Fair."},
    P+"FRAU": {"p": 0.90, "reason": "3 of 3 this week. Fair to slightly rich."},
    P+"SAVE": {"p": 0.88, "reason": "3 of 3 this week. Fair."},
    P+"FARM": {"p": 0.93, "reason": "Not a market at the last three stops. A rally on the State Fair grounds in farm country almost always gets a farmer riff. Slightly cheap, not enough to clear fees."},
    P+"BARA": {"p": 0.85, "reason": "3 of 3 this week, though only 14/27 over the summer. Fair."},
    P+"CHEA": {"p": 0.85, "reason": "3 of 3 this week. Fair."},
    P+"AFFO": {"p": 0.78, "reason": "2 of 3 this week (missed in Durant). Fair."},
    P+"MADE": {"p": 0.80, "reason": "3 of 3 this week, 9/27 over the summer. Fair."},
    P+"CHIN": {"p": 0.85, "reason": "2 of 3 this week, 20/27 corpus; farm-state crowds get the China-buys-our-crops line. Slightly cheap."},
    P+"SLEE": {"p": 0.70, "reason": "1 of 2 this week (said in Vandalia, not Mobile). Fair."},
    P+"CORN": {"p": 0.72, "reason": "No counted base rate. Nebraska is corn and ethanol country, which makes it plausible, not certain. Fair to slightly cheap."},
    P+"ICE":  {"p": 0.62, "reason": "2 of 3 this week (not Mobile). Fair."},
    P+"DATA": {"p": 0.45, "fragile": True, "reason": "1 of 3 this week (Vandalia only), 5/27 corpus. The 62–63¢ price looks rich on the count. Fragile: Nebraska has real data-center build-outs, so one local riff flips it."},
    P+"IRAN": {"p": 0.60, "reason": "Iran 5+ times hit 2 of 3 this week (missed in Vandalia). Fair."},
    P+"SUPR": {"p": 0.55, "reason": "2 of 3 this week. Fair."},
    P+"AI":   {"p": 0.45, "reason": "1 of 3 this week (Vandalia only). A 55–60¢ YES looks a little rich."},
    P+"AMER": {"p": 0.35, "reason": "1 of 3 this week (Mobile only). Fair."},
    P+"RUSS": {"p": 0.55, "reason": "2 of 3 this week (Mobile, Vandalia). The 37–45¢ price looks a bit low on that count."},
    P+"SANC": {"p": 0.25, "reason": "1 of 3 this week. Fair."},
    P+"ISRA": {"p": 0.15, "reason": "0 of 3 this week. Fair."},
    P+"HORM": {"p": 0.10, "reason": "0 of 3 this week. Fair."},
    P+"DRIL": {"p": 0.15, "reason": "1 of 3 this week (Durant, an oil state). Nebraska is not. Fair."},
    P+"TRUMA": {"p": 0.08, "reason": "0 of 2 where listed this week. Fair."},
    P+"DEPO": {"p": 0.08, "reason": "0 of 3 this week. Fair."},
    P+"TRUM": {"p": 0.06, "reason": "TrumpRx 0 of 3 this week. Fair."},
    P+"FENT": {"p": 0.06, "reason": "0 of 3 this week. Fair."},
    P+"FILI": {"p": 0.04, "reason": "0 of 3 this week. Fair."},
    P+"CEAS": {"p": 0.04, "reason": "0 of 3 this week. Fair."},
    P+"CRYP": {"p": 0.02, "reason": "0 of 3 this week. Fair."},
    P+"NQE":  {"p": 0.01, "reason": "Publicly scheduled with staging already up on Oct 4; cancellation unlikely."},
  },
}
