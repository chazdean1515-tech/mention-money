# Analysis for KXTRUMPSAYNICKNAME-26OCT01 (nicknames before October — window ends Wed night)
EVENT = "KXTRUMPSAYNICKNAME-26OCT01"
P = EVENT + "-"
DATA = {
  "title": "Trump nicknames before October",
  "speaker": "Donald Trump (any qualifying remarks before Oct 1)",
  "event_time_et": "2026-09-30T23:59:00-04:00",
  "event_time_note": "Kalshi window: say the nickname before October. Remaining calendar: late Mon Sep 28 through Tue Sep 29 (Mellon 'Golden Age') and Wed Sep 30. Not a campaign-rally stretch.",
  "context": ("These nicknames almost never appear in official remarks transcripts. In the full 2026 DCPD dump: Piggy 1×, Whack Job 1×, Numbskull 1×; Trainwreck / Low Energy / Tampon Tim / Comrade Kamala / Crazy Bernie / Biden Crime Family / Fat Slob / Egghead / Rocket Man / Little Communist = 0. "
              "Remaining speaking slots are a short Oval announcement and a tech/'Golden Age' showcase — poor venues for insult nicknames. Prices in the 1–12¢ YES range look roughly right; a few NO asks (Piggy 89¢, Whack Job 91¢) still leave a thin NO edge if you size for correlated long-shot risk."),
  "confidence": "Low. Nicknames are rare in the govinfo corpus; we may miss rally/Truth Social usages that Kalshi still counts. Short remaining window.",
  "method": "Presence counts across Jun–Aug SEL (23) + full 2026 DCPD dump for rare nicknames; adjusted for ~2.5 days left and non-rally formats.",
  "sources": [
    {"title": "govinfo Compilation of Presidential Documents 2026", "url": "https://www.govinfo.gov/app/collection/cpd"},
    {"title": "CBS: Trump 'Golden Age' Mellon Auditorium event Sep 29", "url": "https://www.cbsnews.com/news/trump-golden-age-event-tech-executives-elon-musk-jensen-huang-ai/"},
  ],
  "words": {
    P+"PIGG": {"p": 0.04, "reason": "1 hit in all-2026 DCPD; remaining events are Oval/tech. Thin NO edge vs 12¢ YES / 89¢ NO."},
    P+"WHAC": {"p": 0.03, "reason": "1 all-year hit ('whack/wack job'). Similar NO lean."},
    P+"TRAI": {"p": 0.02, "reason": "0 corpus hits. Fair-to-slight NO at 8¢."},
    P+"LOWE": {"p": 0.03, "reason": "0 in 2026 DCPD dump (classic Jeb-era line). Fair at 6¢."},
    P+"LITT": {"p": 0.02, "reason": "0 hits. Fair at 3¢."},
    P+"COMR": {"p": 0.02, "reason": "0 hits; Kamala less central now. Fair at 3¢."},
    P+"TAMP": {"p": 0.01, "reason": "0 hits; Walz-era insult. Fair at 1¢."},
    P+"ROCK": {"p": 0.02, "reason": "0 in 2026 dump (Kim Jong Un era). Fair at 2¢."},
    P+"NUMB": {"p": 0.02, "reason": "1 all-year hit. Fair at 3¢."},
    P+"FAT": {"p": 0.01, "reason": "0 hits. Fair at 2¢."},
    P+"EGGH": {"p": 0.01, "reason": "0 hits. Fair at 2¢."},
    P+"CRAZ": {"p": 0.02, "reason": "0 hits. Fair at 1¢."},
    P+"BIDE": {"p": 0.03, "reason": "0 exact 'Biden Crime Family' hits in dump; he says Biden often but not this phrase. Fair at 1¢."},
  },
}
