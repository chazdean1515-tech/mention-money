# KXTRUMPMENTION-26OCT06: Trump remarks at Anduril Industries, Tradepoint Atlantic (Sparrows Point, Baltimore County MD), Tue Oct 6 2026.
# Hit counts are real Kalshi settlements: the last 12 KXTRUMPMENTION events (Sep 17 - Oct 5) plus the Peterbilt factory
# stop (KXTRUMPMENTIONB-26OCT01), the closest same-format event. Nothing else is counted.
EVENT = "KXTRUMPMENTION-26OCT06"
P = EVENT + "-"
DATA = {
  "title": "Trump remarks at Anduril Industries (Sparrows Point, MD)",
  "speaker": "Donald Trump",
  "event_time_et": "2026-10-06T16:00:00-04:00",
  "event_time_note": "White House schedule and pool guidance: remarks at 4:00 p.m. ET at Tradepoint Atlantic, 1660 Shipyard Road, Sparrows Point MD. Anduril CEO Brian Schimpf and others speak earlier; only Trump's words count.",
  "context": ("Anduril is announcing 'the next chapter' of its defense manufacturing push, widely reported as a drone-boat (autonomous surface vessel) "
              "factory at the old Bethlehem Steel shipyard. It comes days after Hegseth stood up an Autonomous Warfare Command. "
              "This is a company/factory event like Peterbilt in Denton (Oct 1), where Manufacturing, Made in America, Tariff, China, Biden, Stock Market, Nuclear and Iran all hit "
              "and AI, Elon and Crypto did not. Made in America is 5 for 5 where it was listed this month (four rallies plus Peterbilt)."),
  "confidence": "Medium. One same-format factory event plus 12 recent settled Trump events; the defense-specific words have no counted history.",
  "method": "Presence across the 12 most recent settled KXTRUMPMENTION events and the Peterbilt factory stop, adjusted for the Anduril/shipyard/defense theme.",
  "sources": [
    {"title": "White House pool guidance: remarks at Anduril, 4:00 PM EDT, Tradepoint Atlantic", "url": "https://pool.pp.tools/reports/9421"},
    {"title": "CBS Baltimore: Trump scheduled to visit Tradepoint Atlantic Tuesday", "url": "https://www.cbsnews.com/baltimore/news/trump-scheduled-visit-baltimore-countys-tradepoint-atlantic/"},
    {"title": "WSJ: Anduril weighs Baltimore shipyard investment to build drone boats", "url": "https://www.wsj.com/business/logistics/anduril-weighs-baltimore-shipyard-investment-to-build-drone-boats-d7ae923d"},
    {"title": "Kalshi settlements: KXTRUMPMENTION (Sep 17 - Oct 5) and KXTRUMPMENTIONB-26OCT01", "url": "https://kalshi.com/markets/kxtrumpmention"},
  ],
  "words": {
    P+"MANU": {"p": 0.95, "reason": "Defense manufacturing is the whole event; hit at Peterbilt. Fair at the top of the board."},
    P+"IRAN": {"p": 0.90, "reason": "2 of 3 where listed in the series plus a hit at Peterbilt, with the Iran war still live. Fair."},
    P+"CHIN": {"p": 0.88, "reason": "8 of 11 recent Trump events plus Peterbilt (9 of 12). China is the natural foil for a defense build-out. Fair."},
    P+"PALM": {"p": 0.85, "reason": "No counted history. Trump name-checks hosts, and Luckey is Anduril's founder and public face. Fair, but it needs him to be there or be thanked."},
    P+"NUCL": {"p": 0.82, "reason": "3 of 5 in the series plus Peterbilt (4 of 6). Fair."},
    P+"NAVY": {"p": 0.82, "reason": "No counted history. The product is drone boats for the Navy at a shipyard. Fair."},
    P+"MADE": {"p": 0.82, "reason": "5 of 5 where listed this month (Durant, Mobile, Vandalia, Grand Island, and the Peterbilt factory). An American-made weapons announcement fits it. The 64–67¢ price looks low on that count."},
    P+"BIDE": {"p": 0.78, "reason": "4 of 8 in the series plus Peterbilt (5 of 9), and he blames Biden for the depleted arsenal often. Fair."},
    P+"SHIP": {"p": 0.75, "reason": "No counted history. The venue is a historic shipyard and shipbuilding is a frequent Trump riff. Slightly cheap, not enough to clear fees."},
    P+"TARI": {"p": 0.74, "reason": "4 of 8 in the series plus Peterbilt (5 of 9). Less central at a defense event than at a truck plant. Fair to slightly rich."},
    P+"AI":   {"p": 0.70, "reason": "4 of 11 in the series and a miss at Peterbilt, but Anduril is an AI/autonomy company. Fair."},
    P+"SPAC": {"p": 0.70, "reason": "1 of 1 where listed (Mobile). He likes to say he created the Space Force. Fair."},
    P+"RUSS": {"p": 0.65, "reason": "1 of 3 in the series; Russia / Ukraine hit in Grand Island. Fair."},
    P+"SUBM": {"p": 0.62, "reason": "No counted history. Submarines come up in his military riffs. Fair."},
    P+"AUTO": {"p": 0.55, "reason": "No counted history. Others will say autonomous; Trump more often says drones. Fair to slightly rich."},
    P+"GOLD": {"p": 0.55, "reason": "No counted history. A defense speech is a natural place for Golden Dome. Fair."},
    P+"NSEC": {"p": 0.55, "reason": "0 of 1 where listed. Fair."},
    P+"ELON": {"p": 0.50, "reason": "Missed at Peterbilt, the only count. Fair."},
    P+"STOC": {"p": 0.50, "reason": "1 of 7 in the series plus Peterbilt (2 of 8). The 64–67¢ price looks rich on that count."},
    P+"UKRA": {"p": 0.40, "reason": "Russia / Ukraine hit in Grand Island; Ukraine alone has no count. Fair."},
    P+"TAIW": {"p": 0.07, "reason": "0 of 1 where listed. Fair."},
    P+"CRYP": {"p": 0.03, "reason": "Crypto missed at Peterbilt and all four rallies. Fair."},
    P+"NQE":  {"p": 0.01, "reason": "On the White House schedule with pool guidance issued; cancellation unlikely."},
  },
}
