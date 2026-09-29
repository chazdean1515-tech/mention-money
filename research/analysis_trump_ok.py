# KXTRUMPMENTION-26OCT01: Trump midterm rally, Durant OK (Choctaw Event Center), Thu Oct 1 2026.
EVENT = "KXTRUMPMENTION-26OCT01"
P = EVENT + "-"
DATA = {
  "title": "Trump midterm rally in Durant, Oklahoma",
  "speaker": "Donald Trump",
  "event_time_et": "2026-10-01T19:00:00-04:00",
  "event_time_note": "GOP/Trump 47: program begins 6:00 p.m. Central (7:00 p.m. ET) at Choctaw Event Center, Durant OK.",
  "context": ("Full midterm rally — long, ad-libbed, stump-heavy. Base rates from 23 Jun–Aug 2026 govinfo remarks + 4 Sep speeches "
              "understate rally density of Fake News / Transgender / Sleepy Joe / Affordability. Midterms are ~5 weeks out, so "
              "'Save America Act', voter-fraud, and deportation riffs are live. Oklahoma oil country lifts Oil/Gas and Drill Baby Drill. "
              "Paxton/Talarico is a Texas primary fight — less natural in Durant unless he name-checks the race. "
              "Most YES staples are correlated bets on 'he riffs for an hour'."),
  "confidence": "Medium. Rally format is the high-base-rate setting; individual long-shots still noisy.",
  "method": "Presence rates in 23 Jun–Aug 2026 SEL + 4 Sep-2026 speeches, adjusted UP for a full midterm rally vs. scripted Oval/tech hits.",
  "sources": [
    {"title": "Trump 47 / GOP: Midterm Rally in Oklahoma (Oct 1, 6pm CT)", "url": "https://events.gop.com/events/midterm-rally-in-ok-president-trump"},
    {"title": "News From The States: Trump Durant OK rally", "url": "https://www.newsfromthestates.com/article/trump-set-rally-gop-voters-hold-midterm-election-event-oklahoma"},
    {"title": "govinfo CPD Trump remarks corpus", "url": "https://www.govinfo.gov/app/collection/cpd"},
  ],
  "words": {
    P+"FAKE": {"p": 0.92, "reason": "'Fake News' in 17/27 corpus docs; near-automatic at midterm rallies. Fair at 89–92¢."},
    P+"OIL":  {"p": 0.93, "reason": "Oil/gas in 24/27; Oklahoma venue pushes it higher. Fair at 90–94¢."},
    P+"TRAN": {"p": 0.90, "reason": "'Transgender' in 15/27 official docs, much stickier on the trail. Fair at 86–88¢."},
    P+"CHIN": {"p": 0.88, "reason": "China in 20/27; tariffs/fentanyl China riff is standard. Fair."},
    P+"AFFO": {"p": 0.85, "reason": "Affordability message is his midterm frame; 14/27 official, higher on trail. Fair at 74–83¢."},
    P+"HEAL": {"p": 0.82, "reason": "Healthcare / TrumpRx / MFN is a live Sep–Oct stump block. Fair."},
    P+"SAVE": {"p": 0.80, "reason": "'Save America Act' in 16/27 and built for midterm rallies. Fair at 75–87¢."},
    P+"DIVI": {"p": 0.78, "reason": "Dividend/stimulus ('Trump dividend') is a current stump promise. Fair."},
    P+"IRAN": {"p": 0.70, "reason": "Market is Iran (5+ times): 19/27 hit 5+. Rallies often clear it. Fair-to-slight cheap."},
    P+"FENT": {"p": 0.65, "reason": "Fentanyl in 7/27 official docs but a rally staple tied to border/China. Fair at 54–69¢."},
    P+"ICE":  {"p": 0.65, "reason": "ICE in 8/27; border rallies push it up. Fair at 60–69¢."},
    P+"DEPO": {"p": 0.60, "reason": "Deportation language in 6/27 official; common on the trail. Fair."},
    P+"AI":   {"p": 0.55, "reason": "AI in 19/27 but less forced at a heartland midterm rally than at Mellon. Fair at 45–54¢."},
    P+"BARA": {"p": 0.55, "reason": "'Barack Hussein Obama' in 14/27. Fair."},
    P+"FRAU": {"p": 0.55, "reason": "Fraud (voter/Medicare) in 9/27; midterm context helps. Fair."},
    P+"AMER": {"p": 0.50, "reason": "'America First' in 8/27. Fair."},
    P+"SANC": {"p": 0.48, "reason": "'Sanctuary' in 3/27 official; trail-only. Fair at 61–70¢ — slight NO lean."},
    P+"TRUM": {"p": 0.45, "reason": "TrumpRX in 4/27; healthcare block may pull it in. Fair."},
    P+"HORM": {"p": 0.40, "reason": "Hormuz in 16/27 when Iran/oil is hot; not guaranteed every rally. Fair-to-rich."},
    P+"CHEA": {"p": 0.45, "reason": "Cheat/cheater in 13/27. Fair."},
    P+"SUPR": {"p": 0.40, "reason": "Supreme Court in 13/27. Fair."},
    P+"RUSS": {"p": 0.40, "reason": "Russia/Ukraine in 16/27; optional at domestic midterm rally. Fair."},
    P+"PAXT": {"p": 0.35, "reason": "Paxton/Talarico is a Texas race; Durant OK is adjacent but not automatic. Fair at 42–50¢."},
    P+"DRIL": {"p": 0.35, "reason": "'Drill baby drill' only 2/27 in corpus; oil-state crowd helps. Fair-to-slight cheap vs wide ask."},
    P+"DATA": {"p": 0.22, "reason": "Data center in 5/27; more tech-event than OK rally. Fair-to-slight rich."},
    P+"MADE": {"p": 0.35, "reason": "Made in America in 9/27. Fair."},
    P+"FILI": {"p": 0.18, "reason": "Filibuster in 3/27. Fair at 8–19¢."},
    P+"ALUM": {"p": 0.18, "reason": "Aluminum in 5/27. Illiquid."},
    P+"CEAS": {"p": 0.15, "reason": "Ceasefire in 3/27; foreign-policy optional. Fair at 6–11¢."},
    P+"CRYP": {"p": 0.06, "reason": "Crypto/Bitcoin in 3/27; rare on the trail. Fair at 1–2¢."},
    P+"NQE":  {"p": 0.02, "reason": "Rally is publicly scheduled; cancellation unlikely."},
  },
}
