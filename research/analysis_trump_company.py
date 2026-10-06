# Analysis for KXTRUMPSAYCOMPANY-26OCT01 (companies said in September — window ends Wed night)
EVENT = "KXTRUMPSAYCOMPANY-26OCT01"
P = EVENT + "-"
DATA = {
  "title": "Companies Trump will say in September",
  "speaker": "Donald Trump (any qualifying remarks in September before Oct 1)",
  "event_time_et": "2026-09-30T23:59:00-04:00",
  "event_time_note": "September company market. The window ended Wed Sep 30. Boeing was already about 99¢ in the snapshot used here (treated as said). The calendar inside the window was a Monday Oval announcement and the Tuesday Mellon 'Golden Age' address (Musk, Jensen Huang, AI and energy panels).",
  "context": ("Jun–Aug SEL base rates (23 remarks): Boeing 3, Tesla 4, Meta 3, Micron 3, ChatGPT/OpenAI 2, Uber 2, JPMorgan 2, IBM 2, SpaceX 1, Oracle 1, Deere 1, Caterpillar 1, Hyundai 1; "
              "DoorDash/Airbnb/AMD/TSMC/BlackRock/Paramount/Verizon/Qualcomm/Rigetti/Mastercard/eBay = 0 in SEL (DoorDash 1× elsewhere in 2026 DCPD). "
              "Mellon AI showcase lifts SpaceX / Tesla / ChatGPT-OpenAI / Meta; agriculture panel is a thin Deere/Caterpillar hook. "
              "I do not have a verified September-to-date said/unsaid tape — prices near 90¢+ (DoorDash, Boeing) are treated as nearly resolved YES; mid-priced names may already be said. Confidence is low on those."),
  "confidence": "Low–medium. Solid corpus base rates, but the month-to-date resolution state is inferred from prices for the richest names, and the September window was short.",
  "method": "Jun–Aug 2026 SEL presence rates + full-2026 DCPD checks for rare names; adjusted for Mellon AI guest list and ~2.5 days left in September.",
  "sources": [
    {"title": "govinfo CPD 2026 Trump remarks", "url": "https://www.govinfo.gov/app/collection/cpd"},
    {"title": "CBS: Mellon Golden Age guest list (Musk, Huang)", "url": "https://www.cbsnews.com/news/trump-golden-age-event-tech-executives-elon-musk-jensen-huang-ai/"},
    {"title": "NPR Indicator: Trump trades in DoorDash/Dell/Palantir (Sep 24)", "url": "https://www.npr.org/2026/09/24/nx-s1-5979093/what-doordash-dell-and-palantir-all-have-in-common"},
  ],
  "words": {
    P+"BOEI": {"p": 0.99, "reason": "Market ~99¢; 3/23 SEL. Treat as already said this month."},
    P+"DOOR": {"p": 0.92, "reason": "Market ~91¢ after a year of DoorDash politics + Sep 24 NPR piece; treat as nearly resolved. Fair."},
    P+"CHAT": {"p": 0.55, "reason": "2/23 SEL; Mellon AI crowd. 67¢ a bit rich → slight NO."},
    P+"SPCX": {"p": 0.52, "reason": "1/23 SEL but Musk on the Mellon slate. Fair at ~58¢."},
    P+"TSLA": {"p": 0.48, "reason": "4/23 SEL + Musk. Slight YES vs 37¢ ask."},
    P+"META": {"p": 0.40, "reason": "3/23 SEL; AI panel. Fair at ~43¢."},
    P+"ABNB": {"p": 0.30, "reason": "0/23 SEL. 75¢ looks very rich unless already said — NO lean (low confidence on month-to-date state).",
              "fragile": "Month-to-date state unknown; a 71–75¢ market may mean it was already said."},
    P+"AMD":  {"p": 0.12, "reason": "0/23. Chip talk possible Tue; 22¢ a bit rich."},
    P+"TSM": {"p": 0.10, "reason": "0/23. 29¢ rich. NO lean."},
    P+"MU": {"p": 0.14, "reason": "3/23 SEL (memory/AI). Fair-to-slight YES at thin asks; watch 19¢ ask."},
    P+"ORCL": {"p": 0.14, "reason": "1/23; cloud/AI. Slight YES if ask stays ~9¢."},
    P+"IBM":  {"p": 0.12, "reason": "2/23. Slight YES at ~4¢."},
    P+"DE": {"p": 0.10, "reason": "1/23; agriculture panel hook. 18¢ slight NO."},
    P+"CAT": {"p": 0.08, "reason": "1/23. Fair-to-slight NO at mid-teens if listed."},
    P+"PSKY": {"p": 0.08, "reason": "0/23. 21¢ rich."},
    P+"JPM":  {"p": 0.08, "reason": "2/23. Fair near 10¢."},
    P+"UBER": {"p": 0.08, "reason": "2/23. Fair near 10¢."},
    P+"QCOM": {"p": 0.08, "reason": "0/23. Fair-to-slight NO at 12¢."},
    P+"HYUN": {"p": 0.06, "reason": "1/23. Fair near 5¢."},
    P+"BLAC": {"p": 0.04, "reason": "0/23. Fair near 8¢."},
    P+"VERI": {"p": 0.03, "reason": "0/23. Fair near 8¢."},
    P+"MA": {"p": 0.04, "reason": "0/23. Fair-to-NO at 15¢."},
    P+"RGTI": {"p": 0.02, "reason": "0/23 quantum name. Fair at 4¢."},
    P+"EBAY": {"p": 0.02, "reason": "0/23. Fair at low single digits."},
  },
}
