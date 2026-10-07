# KXSPECIALREPORTMENTION-26OCT07: Jeff Bezos interview on Fox News' Special Report with Bret Baier, Wed Oct 7 2026.
# No transcript counts. Topic list is from the Fox News press release. Estimates are judgment calls.
EVENT = "KXSPECIALREPORTMENTION-26OCT07"
P = EVENT + "-"
DATA = {
  "title": "Jeff Bezos on Special Report with Bret Baier",
  "speaker": "Jeff Bezos",
  "event_time_et": "2026-10-07T18:00:00-04:00",
  "event_time_note": "Fox News press release: Special Report at 6 p.m. ET, anchored from Blue Origin's space complex in Cape Canaveral, on Fox News' 30th anniversary.",
  "context": ("Fox says Bezos will discuss space exploration, AI regulation, the midterm elections, the world economy and other news, with a tour of the campus, "
              "mission control and a rocket booster. Only Bezos's own words count, not Baier's. "
              "Space words (Blue Origin, Moon, New Glenn) and AI are natural; Washington Post and Elon/Musk depend on whether Baier pushes and Bezos names them."),
  "fragile_sides": {"NO": "Only Bezos's words count, but an extended interview can stray into any news of the day."},
  "confidence": "Low-medium. Topic list is official; no Bezos transcript counts.",
  "method": "Judgment from the announced topics and setting, anchored to market mid-prices.",
  "sources": [
    {"title": "Fox News press release: Baier interviews Bezos at Blue Origin, Oct 7 on Special Report", "url": "https://press.foxnews.com/2026/10/05/fox-news-channels-bret-baier-to-present-exclusive-interview-with-jeff-bezos-from-blue-origins-space-complex-in-cape-canaveral-florida-on-wednesday-october-7-on-special-report"},
    {"title": "Mediaite: Baier lands Bezos interview", "url": "https://www.mediaite.com/media/tv/fox-news-anchor-bret-baier-lands-exclusive-interview-with-jeff-bezos-timed-to-air-on-networks-30th-anniversary/"},
  ],
  "words": {
    P+"AI":   {"p": 0.93, "reason": "AI regulation is on the announced topic list. Fair."},
    P+"MOON": {"p": 0.88, "reason": "Space exploration is the setting; Bezos talks about the Moon often. Fair."},
    P+"BLUE": {"p": 0.92, "reason": "Interview is at Blue Origin's complex. Fair to slightly cheap; wide spread."},
    P+"NASA": {"p": 0.72, "reason": "Fair; wide spread."},
    P+"DATA": {"p": 0.68, "reason": "Fair; wide spread."},
    P+"NEWG": {"p": 0.72, "reason": "The tour includes a rocket booster. Fair."},
    P+"TRUM": {"p": 0.60, "reason": "Midterms are on the topic list, but he may avoid the name. Fair."},
    P+"CHIN": {"p": 0.48, "reason": "Fair; wide spread."},
    P+"ARTE": {"p": 0.36, "reason": "Fair; wide spread."},
    P+"SPAC": {"p": 0.26, "reason": "Fair; wide spread."},
    P+"NUCL": {"p": 0.16, "reason": "Fair; wide spread."},
    P+"ROBO": {"p": 0.24, "reason": "Fair."},
    P+"ELON": {"p": 0.16, "reason": "Fair."},
    P+"WASH": {"p": 0.10, "reason": "He may say 'the Post' instead. Fair; wide spread."},
    P+"TARI": {"p": 0.10, "reason": "Fair; wide spread."},
    P+"NQE":  {"p": 0.02, "reason": "Announced by Fox News."},
  },
}
