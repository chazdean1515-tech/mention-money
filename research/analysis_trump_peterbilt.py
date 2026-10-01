# KXTRUMPMENTIONB-26OCT01: Trump remarks at Peterbilt Motors, Denton TX, Thu Oct 1 2026.
# Factory / manufacturing hit (not a full midterm rally). Topic priors from White House preview + plant theme.
EVENT = "KXTRUMPMENTIONB-26OCT01"
P = EVENT + "-"
DATA = {
  "title": "Trump remarks at Peterbilt Motors (Denton, TX)",
  "speaker": "Donald Trump",
  "event_time_et": "2026-10-01T16:00:00-04:00",
  "event_time_note": "Polymarket/event cards list remarks ~4:00 p.m. ET at Peterbilt Motors, Denton TX; then Durant OK rally same evening.",
  "context": ("Scripted factory visit to tout tariffs on heavy trucks, reshoring, and manufacturing jobs at PACCAR/Peterbilt. "
              "White House preview leans hard on tariff / Made in America / investment / jobs language. Shorter and more on-message "
              "than a midterm rally, so culture-war and election-integrity riffs (Cheat, Save America Act) are optional add-ons. "
              "No plant-speech transcript corpus; estimates are venue/topic priors adjusted down vs. full-rally base rates."),
  "fragile_sides": {"YES": "YES leans assume he gives a full factory stump (≥10 min), not a 3-minute photo-op greeting."},
  "confidence": "Low-medium. Factory format + White House theme sheet; no matching transcript corpus.",
  "method": "Topic priors from White House / Fox Business / KERA / NT Daily previews of the Denton Peterbilt stop.",
  "sources": [
    {"title": "Fox Business: Trump Peterbilt Denton manufacturing stop", "url": "https://www.foxbusiness.com/politics/trump-make-surprise-stop-texas-truck-factory-tout-manufacturing"},
    {"title": "NT Daily: Trump to visit Denton Peterbilt Oct 1", "url": "https://www.ntdaily.com/news/president-donald-trump-set-to-visit-denton/article_2714bc9a-410b-45f6-a2e2-0336c266316c.html"},
    {"title": "KERA: Trump prepares to tour Peterbilt plant", "url": "https://www.keranews.org/news/2026-09-29/president-trump-prepares-to-tour-peterbilt-plant-in-denton-on-thursday"},
  ],
  "words": {
    P+"INVE": {"p": 0.90, "reason": "Investment/jobs is the White House theme for this stop. Fair at 92–94¢."},
    P+"BILL": {"p": 0.88, "reason": "Billion/trillion investment boasts are standard on factory hits. Fair at 88–89¢."},
    P+"TARI": {"p": 0.88, "reason": "25% heavy-truck tariffs are the explicit talking point. Fair at 83–87¢."},
    P+"MANU": {"p": 0.90, "reason": "Manufacturing renaissance is the event's purpose. Fair at 83–86¢."},
    P+"OIL":  {"p": 0.75, "reason": "Oil/gas often tags along on energy/economy blocks; less forced than at an OK rally. Fair at 81–86¢ — slight NO."},
    P+"CHIN": {"p": 0.70, "reason": "China / trade foil is natural with tariffs. Fair at 76–80¢ — slight NO."},
    P+"MADE": {"p": 0.72, "reason": "'Made in America' fits the plant floor. Fair-to-slight cheap at 54–56¢."},
    P+"HOTT": {"p": 0.55, "reason": "'Hottest' (economy/stock) is a recurring boast; optional. Fair at 68–71¢ — slight NO."},
    P+"NOTA": {"p": 0.55, "reason": "No tax on overtime is a pocketbook line he may drop for workers. Fair at 70–75¢ — slight NO."},
    P+"IRAN": {"p": 0.45, "reason": "Iran optional on a domestic factory hit. Fair-to-slight NO at 70–71¢."},
    P+"BIDE": {"p": 0.55, "reason": "Biden contrast is easy but not required for a manufacturing speech. Fair at 71–75¢ — slight NO."},
    P+"INFL": {"p": 0.55, "reason": "Inflation/prices often pair with tariffs. Fair at 49–50¢."},
    P+"STOC": {"p": 0.50, "reason": "Stock market boast is common; length-dependent. Fair at 62–65¢ — slight NO."},
    P+"DIES": {"p": 0.55, "reason": "Diesel is on-theme at a truck plant; may or may not be named. Fair at 57–61¢."},
    P+"ELEC": {"p": 0.50, "reason": "EV / electric vehicle contrast fits truck manufacturing. Fair at 48–51¢."},
    P+"CANA": {"p": 0.45, "reason": "Canada/USMCA sometimes in trade blocks. Fair at 53–55¢ — slight NO."},
    P+"SAVE": {"p": 0.35, "reason": "Save America Act is more midterm-rally than factory. Fair-to-slight NO at 27–32¢ YES — slight YES lean vs ask."},
    P+"ID":   {"p": 0.30, "reason": "Voter ID is election-integrity, off-theme here. Fair at 34–40¢."},
    P+"MEXI": {"p": 0.40, "reason": "Mexico / nearshoring can come up with truck tariffs. Fair at 31–40¢."},
    P+"ELON": {"p": 0.25, "reason": "Elon/Musk optional; EV contrast might pull it in. Fair at 20–24¢."},
    P+"AI":   {"p": 0.22, "reason": "AI less forced at a truck plant. Fair at 18–21¢."},
    P+"CHEA": {"p": 0.25, "reason": "Cheat/cheater is rally language. Fair at 26–32¢."},
    P+"CALI": {"p": 0.30, "reason": "California foil optional. Fair at 35–39¢."},
    P+"EPA":  {"p": 0.35, "reason": "EPA / deregulation fits manufacturing; not guaranteed. Fair-to-slight cheap at 18–19¢."},
    P+"HOAX": {"p": 0.18, "reason": "Hoax is culture-war optional. Fair at 15–16¢."},
    P+"CAFE": {"p": 0.20, "reason": "CAFE standards are niche auto-reg; possible on a truck stop. Fair at 6–13¢."},
    P+"NUCL": {"p": 0.22, "reason": "Nuclear is off-theme unless he pivots to energy. Fair at 47–58¢ — NO lean (wide)."},
    P+"CRYP": {"p": 0.04, "reason": "Crypto rare on factory hits. Fair at 1–2¢."},
    P+"NQE":  {"p": 0.03, "reason": "Publicly scheduled en route to OK rally; cancellation unlikely."},
  },
}
