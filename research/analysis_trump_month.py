# Analysis for KXTRUMPSAYMONTH-26OCT01 (selected phrases in September — window ends Wed night)
EVENT = "KXTRUMPSAYMONTH-26OCT01"
P = EVENT + "-"
DATA = {
  "title": "Selected Trump phrases in September",
  "speaker": "Donald Trump (any qualifying remarks in September before Oct 1)",
  "event_time_et": "2026-09-30T23:59:00-04:00",
  "event_time_note": "September phrase market. The window ended Wed Sep 30. The calendar inside it was a Monday Oval announcement, the Tuesday Mellon Golden Age address, and Wednesday Sep 30.",
  "context": ("Corpus (23 Jun–Aug SEL + broader 2026 DCPD): Cognitive 3/23 SEL (5 all-year); Newscum 0/23 SEL but 3 all-year; Peace in the Middle East 1/23 SEL (9 all-year); "
              "UFO/UAP 0; Epstein 0/23 (1 all-year); Peptide 0; Make Iran Great Again 0. "
              "None of these are natural fits for a short AI/diesel Oval hit or a tech showcase, except Cognitive (he uses it to attack opponents' 'cognitive' decline) and Peace in the Middle East on a foreign-policy tangent. "
              "17¢ YES on Cognitive/Newscum looks rich for 2.5 days left unless already said this month."),
  "confidence": "Low. Month-to-date said/unsaid state unknown; phrase markets are jumpy around news spikes (Epstein, Iran).",
  "method": "SEL + full-2026 DCPD presence; adjusted, when the estimate was made, for a short September window and non-rally formats.",
  "sources": [
    {"title": "govinfo CPD 2026", "url": "https://www.govinfo.gov/app/collection/cpd"},
    {"title": "Daily Mail: Sep 28 Oval announcement topic speculation", "url": "https://www.dailymail.com/news/article-16166419/trump-oval-office-announcement-diesel-ai.html"},
  ],
  "words": {
    P+"COGN": {"p": 0.10, "reason": "3/23 SEL. Possible in a political aside, not in AI/diesel core. 17¢ slight NO."},
    P+"NEWS": {"p": 0.06, "reason": "0/23 SEL, 3 all-year ('Newscum'). 17¢ rich. NO lean."},
    P+"PEAC": {"p": 0.08, "reason": "1/23 SEL, 9 all-year. 10¢ roughly fair."},
    P+"UFO":  {"p": 0.03, "reason": "0 corpus. Fair at 4¢."},
    P+"EPST": {"p": 0.04, "reason": "1 all-year; news-driven. Fair at 3¢."},
    P+"PEPT": {"p": 0.02, "reason": "0 hits. Fair at 2¢."},
    P+"MAKE": {"p": 0.02, "reason": "0 hits for 'Make Iran Great Again'. Fair at 2¢."},
  },
}
