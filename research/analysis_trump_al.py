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
  "method": "Presence rates in 23 Jun–Aug 2026 SEL + 4 Sep-2026 speeches, adjusted UP for a full midterm rally.",
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
             "history": H(4),"p": 0.42, "reason": "TrumpRX if healthcare block lands. Fair."},
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
