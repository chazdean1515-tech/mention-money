// Kalshi referral URL lives on <body data-kalshi-ref> so the daily data rebuild never edits it.
const KALSHI_REFERRAL_URL = document.body.dataset.kalshiRef || "";
const REF_DISCLOSURE = (document.getElementById("ref-header-disc")?.textContent || "").replace(/\s+/g, " ").trim();
const STALE_MS = 3 * 60 * 60 * 1000;
const MAX_SPREAD = 0.10;

const FEE = (p) => 0.07 * p * (1 - p);
const pct = (x) => (x == null || isNaN(x)) ? "—" : Math.round(x * 100) + "¢";
const pctP = (x) => (x == null || isNaN(x)) ? "—" : Math.round(x * 100) + "%";
const esc = (s) => String(s ?? "").replace(/[&<>"']/g, (c) => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c]));
const fmtET = (iso) => {
  if (!iso) return "—";
  const d = new Date(iso);
  return d.toLocaleString("en-US", { timeZone: "America/New_York", weekday: "short", month: "short", day: "numeric", hour: "numeric", minute: "2-digit" }) + " ET";
};
const etDate = (value) => value ? new Intl.DateTimeFormat("en-CA", { timeZone: "America/New_York", year: "numeric", month: "2-digit", day: "2-digit" }).format(new Date(value)) : "";
const todayET = etDate(Date.now());

function displayWord(word) {
  return /^trump\s*rx$/i.test(String(word ?? "").trim()) ? "TrumpRx" : String(word ?? "");
}

// Gap for buying YES at the ask, or NO at the no ask, after the taker-fee estimate.
function edges(m, est) {
  const out = { side: null, edge: null, price: null };
  if (est == null) return out;
  let best = null;
  if (m.yes_ask && m.yes_ask > 0 && m.yes_ask < 1) {
    const e = est - m.yes_ask - FEE(m.yes_ask);
    best = { side: "YES", edge: e, price: m.yes_ask };
  }
  if (m.no_ask && m.no_ask > 0 && m.no_ask < 1) {
    const e = (1 - est) - m.no_ask - FEE(m.no_ask);
    if (!best || e > best.edge) best = { side: "NO", edge: e, price: m.no_ask };
  }
  return best || out;
}

function quoteOk(m, side) {
  const ask = side === "YES" ? m.yes_ask : m.no_ask;
  const bid = side === "YES" ? m.yes_bid : m.no_bid;
  if (ask == null || bid == null) return false;
  if (!(ask > 0 && ask < 1) || bid <= 0) return false;
  return ask - bid <= MAX_SPREAD + 1e-9;
}

function yesQuote(m) {
  const bid = m.yes_bid, ask = m.yes_ask;
  if (bid != null && ask != null) {
    const b = Math.round(bid * 100), a = Math.round(ask * 100);
    return b === a ? a + "¢" : b + "–" + a + "¢";
  }
  if (m.last_price != null) return Math.round(m.last_price * 100) + "¢";
  return "—";
}

const analyzed = (ea) => !!(ea && ea.words && Object.keys(ea.words).length);
const windowStarted = (ea) => !!(ea && ea.event_time_et && new Date(ea.event_time_et).getTime() <= Date.now());
function windowOver(ea, e) {
  if (e && e.decided) return true;
  if (windowStarted(ea)) return true;
  if (e && e.first_close_et && new Date(e.first_close_et).getTime() <= Date.now()) return true;
  return false;
}
function marketClosed(m) {
  if (m.status && m.status !== "active" && m.status !== "open") return true;
  if (m.close_time_et && new Date(m.close_time_et).getTime() <= Date.now()) return true;
  return false;
}
function isToday(e, ea) {
  if (ea && ea.event_time_et) return etDate(ea.event_time_et) === todayET;
  return e.event_date === todayET;
}
function isStale(iso) {
  if (!iso) return true;
  return Date.now() - new Date(iso).getTime() > STALE_MS;
}

function refLink(cls, html, describedBy) {
  return `<a class="${cls}" href="${esc(KALSHI_REFERRAL_URL)}" target="_blank" rel="sponsored noopener" aria-describedby="${describedBy}">${html}</a>`;
}

function setupReferral() {
  document.querySelectorAll("a[data-kalshi-ref]").forEach((a) => {
    if (!a.getAttribute("href") && KALSHI_REFERRAL_URL) a.href = KALSHI_REFERRAL_URL;
    a.target = "_blank";
    a.rel = "sponsored noopener";
  });
  const foot = document.getElementById("ref-foot-disc");
  if (foot && REF_DISCLOSURE) foot.textContent = REF_DISCLOSURE;
}

function renderStatus(mk, an) {
  const seriesN = new Set((mk.events || []).map((e) => e.series_ticker)).size;
  const when = fmtET(mk.fetched_at_et);
  const nEvents = (mk.events || []).length;
  document.getElementById("meta").innerHTML =
    `Prices as of <b>${esc(when)}</b>` +
    (an.updated_at_et ? ` · analysis written ${esc(fmtET(an.updated_at_et))}` : "") +
    ` · ${nEvents} events across ${seriesN} series in this snapshot`;
  const banner = document.getElementById("stale");
  if (!banner) return;
  if (isStale(mk.fetched_at_et)) {
    const hours = Math.max(1, Math.floor((Date.now() - new Date(mk.fetched_at_et).getTime()) / 3600000));
    banner.hidden = false;
    banner.textContent = `These prices are not live. The snapshot was taken ${when}, about ${hours} hours ago. Do not read the tape as a live quote.`;
  } else {
    banner.hidden = true;
    banner.textContent = "";
  }
}

function wordStats(m, w, ea, e, minEdge) {
  if (!w || w.p == null) {
    return `<div class="word-stats"><span>No estimate in this snapshot</span><span>YES price <b>${esc(yesQuote(m))}</b></span></div>`;
  }
  const over = windowOver(ea, e) || marketClosed(m);
  const gap = edges(m, w.p);
  const bits = [`<span>Our estimate <b>${pctP(w.p)} YES</b></span>`, `<span>YES price <b>${esc(yesQuote(m))}</b></span>`];
  if (!over && gap && gap.edge != null && gap.side) {
    const c = Math.round(gap.edge * 100);
    bits.push(`<span>Gap after fee <b>${c > 0 ? "+" : ""}${c}¢</b> on ${esc(gap.side)}</span>`);
    if (gap.edge >= minEdge && quoteOk(m, gap.side)) bits.push(`<span class="lean ${gap.side.toLowerCase()}">Our lean: ${esc(gap.side)}</span>`);
    else if (gap.edge >= minEdge) bits.push(`<span class="lean snap">No lean: the quote is wide or one-sided</span>`);
    else bits.push(`<span class="lean snap">No lean: gap is under ${Math.round(minEdge * 100)}¢ after the fee</span>`);
  } else if (over) {
    bits.push(`<span class="lean snap">Window started — snapshot only, not a current lean</span>`);
  }
  if (w.fragile) bits.push(`<span class="lean snap">Flagged fragile</span>`);
  return `<div class="word-stats">${bits.join("")}</div>`;
}

function render(d, q = "", onlyAnalyzed = false) {
  const mk = d.mk, an = d.an || {};
  const A = an.events || {};
  const minEdge = an.min_edge ?? 0.05;
  const ql = q.trim().toLowerCase();
  const evs = (mk.events || []).filter((e) => {
    const ea = A[e.event_ticker];
    if (!isToday(e, ea)) return false;
    if (onlyAnalyzed && !analyzed(ea)) return false;
    if (!ql) return true;
    const words = (e.markets || []).map((m) => displayWord(m.word)).join(" ");
    return (e.title + " " + (e.sub_title || "") + " " + (e.series_title || "") + " " + words).toLowerCase().includes(ql);
  });
  evs.sort((a, b) => {
    const ao = windowOver(A[a.event_ticker], a) ? 1 : 0;
    const bo = windowOver(A[b.event_ticker], b) ? 1 : 0;
    if (ao !== bo) return ao - bo;
    const aa = analyzed(A[a.event_ticker]) ? 1 : 0;
    const bb = analyzed(A[b.event_ticker]) ? 1 : 0;
    if (aa !== bb) return bb - aa;
    const at = (A[a.event_ticker] && A[a.event_ticker].event_time_et) || a.event_date || "";
    const bt = (A[b.event_ticker] && A[b.event_ticker].event_time_et) || b.event_date || "";
    return String(at).localeCompare(String(bt));
  });

  const cards = evs.map((e) => {
    const ea = A[e.event_ticker];
    const words = (ea && ea.words) || {};
    const rows = (e.markets || []).map((m) => ({ m, w: words[m.ticker] || words[m.word] || null }))
      .sort((a, b) => displayWord(a.m.word).localeCompare(displayWord(b.m.word)));
    const tr = rows.map(({ m, w }) => {
      const note = (w && (w.prose || w.note || w.reason)) || "No transcript read for this word yet.";
      return `<div class="word-row"><h3>${esc(displayWord(m.word))}</h3>${wordStats(m, w, ea, e, minEdge)}<p>${esc(note)}</p></div>`;
    }).join("");
    const src = ea && ea.sources ? ea.sources.map((s) => `<a href="${esc(s.url)}" target="_blank" rel="noopener">${esc(s.title || s.url)}</a>`).join(" · ") : "";
    const rules = e.rules_primary || (e.markets && e.markets[0] && e.markets[0].rules_primary) || "";
    const rules2 = e.rules_secondary || (e.markets && e.markets[0] && e.markets[0].rules_secondary) || "";
    const tag = e.decided ? "window closed, awaiting settlement"
      : windowStarted(ea) ? "event started — snapshot only"
      : analyzed(ea) ? "analyzed"
      : "analysis pending";
    const tagCls = analyzed(ea) || e.decided || windowStarted(ea) ? "tag" : "tag pending";
    return `<article class="card">
      <div class="hd">
        <h2>${esc((ea && ea.title) || e.title)} <span class="${tagCls}">${tag}</span></h2>
        <div class="info">${esc((ea && ea.speaker) || e.series_title || "")} · event ${ea && ea.event_time_et ? fmtET(ea.event_time_et) : (e.event_date ? esc(e.event_date) + " (date from ticker)" : "—")} · market closes ${fmtET(e.first_close_et)} · prices as of ${fmtET(e.price_fetched_at_et || mk.fetched_at_et)} · vol ${Math.round(e.total_volume || 0).toLocaleString()} · <span class="mut">${esc(e.event_ticker)}</span></div>
        ${ea && ea.event_time_note ? `<div class="info">⏱ ${esc(ea.event_time_note)}</div>` : ""}
        ${ea ? `<div class="event-context"><b>Event context</b>
          ${ea.context ? `<div class="ctx">${esc(ea.context)}</div>` : ""}
          ${ea.method ? `<div class="info">Method: ${esc(ea.method)}</div>` : ""}
          ${src ? `<div class="src">Sources: ${src}</div>` : ""}</div>` : `<div class="info">No write-up for this event in the snapshot.</div>`}
        ${ea && ea.confidence ? `<div class="info">Confidence: ${esc(ea.confidence)}</div>` : ""}
      </div>
      <div class="word-list">${tr}</div>
      ${rules ? `<details><summary>Rules (first market)</summary><div class="rules">${esc(rules)}\n\n${esc(rules2)}</div></details>` : ""}
    </article>`;
  }).join("");

  const todayCount = (mk.events || []).filter((e) => isToday(e, A[e.event_ticker])).length;
  const empty = todayCount === 0
    ? "No Mentions events dated today are in this snapshot."
    : "No events match.";
  document.getElementById("events").innerHTML = cards || `<p class="mut">${empty}</p>`;
}

function tickerPrice(m) {
  if (m.last_price != null) return Math.round(m.last_price * 100);
  if (m.yes_bid != null && m.yes_ask != null) return Math.round(((m.yes_bid + m.yes_ask) / 2) * 100);
  return null;
}

function renderTicker(mk, an) {
  const A = (an && an.events) || {};
  const stale = isStale(mk.fetched_at_et);
  const events = (mk.events || []).filter((e) => {
    const ea = A[e.event_ticker];
    return ea && ea.event_time_et && etDate(ea.event_time_et) === todayET && !windowOver(ea, e);
  }).sort((a, b) => new Date(A[a.event_ticker].event_time_et) - new Date(A[b.event_ticker].event_time_et));
  const el = document.getElementById("today-ticker");
  if (!el) return;
  const clock = (iso) => new Date(iso).toLocaleTimeString("en-US", { timeZone: "America/New_York", hour: "numeric", minute: "2-digit" });
  const bits = [];
  events.forEach((e) => {
    const ea = A[e.event_ticker];
    const markets = (e.markets || []).filter((m) => !marketClosed(m));
    if (!markets.length) return;
    bits.push(`<span class="tick mark"><b>${esc(clock(ea.event_time_et))} ET</b> ${esc(ea.title || e.title || "Event")}</span>`);
    markets.slice().sort((a, b) => displayWord(a.word).localeCompare(displayWord(b.word))).forEach((m) => {
      const px = tickerPrice(m);
      const cls = px == null ? "mark" : (px >= 50 ? "up" : "down");
      const label = displayWord(m.word);
      const shown = label === "TrumpRx" ? "TrumpRx" : label.toUpperCase();
      bits.push(`<span class="tick ${cls}"><b>${esc(shown)}</b>${px == null ? "" : `<span class="px">${px}¢</span>`}</span>`);
    });
  });
  if (!bits.length) { el.hidden = true; el.innerHTML = ""; return; }
  const seq = bits.join('<span class="tick mark sep">●</span>');
  const seconds = Math.max(22, bits.length * 2.4);
  el.classList.toggle("is-stale", stale);
  el.setAttribute("aria-label", stale
    ? `Snapshot prices as of ${fmtET(mk.fetched_at_et)}. Not a live quote.`
    : `Today's Mentions prices as of ${fmtET(mk.fetched_at_et)}.`);
  el.innerHTML = `<span class="ticker-label">${stale ? "NOT LIVE" : "MM"}</span><div class="ticker-window"><div class="ticker-track" style="animation-duration:${seconds}s"><span class="ticker-seq">${seq}</span><span class="ticker-seq" aria-hidden="true">${seq}</span></div></div>`;
  el.hidden = false;
}

function renderPotd(an) {
  const el = document.getElementById("potd");
  const p = an && an.play_of_the_day;
  if (!el) return;
  if (!p || (p.event_time_et && new Date(p.event_time_et).getTime() <= Date.now())) {
    el.hidden = true;
    el.innerHTML = "";
    return;
  }
  const side = p.side === "NO" ? "NO" : "YES";
  const edgeC = Math.round(p.edge * 100);
  const feeC = Math.round((p.fee || 0) * 100);
  el.innerHTML = `<article class="potd-card">
    <div class="potd-shine" aria-hidden="true"></div>
    <div class="potd-top">
      <span class="potd-badge" aria-hidden="true">🏆</span>
      <h2 class="potd-label">Play of the Day</h2>
    </div>
    <div class="potd-event">${esc(p.event_title)}</div>
    <div class="potd-pick"><span class="potd-word">“${esc(displayWord(p.word))}”</span> <span class="potd-side ${side.toLowerCase()}">Our lean: ${side}</span></div>
    <div class="potd-stats">
      <div class="potd-stat"><span class="k">Snapshot price (${side})</span><span class="v">${pct(p.price)}</span></div>
      <div class="potd-stat"><span class="k">Our estimate (${side})</span><span class="v">${pctP(p.est_side)}</span>${side === "NO" ? `<span class="s">YES ${pctP(p.est_yes)}</span>` : ""}</div>
      <div class="potd-stat edge"><span class="k">Gap after fee</span><span class="v">${edgeC > 0 ? "+" : ""}${edgeC}¢</span><span class="s">fee about ${feeC}¢ · opinion</span></div>
    </div>
    <div class="potd-when">
      ${p.event_time_et ? `<span>🎙 Event <b>${fmtET(p.event_time_et)}</b></span>` : ""}
      <span>⏳ Market closes <b>${fmtET(p.close_time_et)}</b></span>
      ${p.price_fetched_at_et ? `<span class="mut">price as of ${fmtET(p.price_fetched_at_et)}</span>` : ""}
    </div>
    <p class="potd-why">${esc(p.rationale)}</p>
    <div class="potd-foot">
      ${p.url ? `<a class="potd-link" href="${esc(p.url)}" target="_blank" rel="noopener">View market on Kalshi →</a>` : ""}
      ${KALSHI_REFERRAL_URL ? refLink("ref-link", "New to Kalshi? <b>Sign up with our link</b>", "potd-disc") : ""}
    </div>
    <p id="potd-disc" class="potd-disc ref-disc">${esc(REF_DISCLOSURE)}</p>
  </article>`;
  el.hidden = false;
}

function setupTip() {
  const dlg = document.getElementById("tip");
  if (!dlg) return;
  const status = document.getElementById("tip-status");
  const open = () => { status.textContent = ""; if (dlg.showModal) dlg.showModal(); else dlg.setAttribute("open", ""); };
  const close = () => { if (dlg.close) dlg.close(); else dlg.removeAttribute("open"); };
  document.querySelectorAll("[data-tip-open]").forEach((b) => b.addEventListener("click", open));
  dlg.querySelector("[data-tip-close]").addEventListener("click", close);
  dlg.addEventListener("click", (ev) => { if (ev.target === dlg) close(); });
  document.getElementById("tip-copy").addEventListener("click", async () => {
    const addr = document.getElementById("sol-addr").textContent.trim();
    let ok = false;
    try { await navigator.clipboard.writeText(addr); ok = true; } catch (_) {
      const ta = document.createElement("textarea");
      ta.value = addr;
      ta.setAttribute("readonly", "");
      ta.style.position = "fixed";
      ta.style.opacity = "0";
      dlg.appendChild(ta);
      ta.select();
      try { ok = document.execCommand("copy"); } catch (_) {}
      ta.remove();
    }
    status.textContent = ok ? "Copied!" : "Copy failed. Select the address above.";
    status.classList.toggle("ok", ok);
    clearTimeout(setupTip.t);
    setupTip.t = setTimeout(() => { status.textContent = ""; }, 2500);
  });
}

function boot() {
  const d = window.MM_BOARD;
  if (!d || !d.mk) {
    document.getElementById("meta").textContent = "Failed to load the snapshot.";
    return;
  }
  renderStatus(d.mk, d.an || {});
  renderTicker(d.mk, d.an || {});
  renderPotd(d.an || {});
  const q = document.getElementById("q");
  const oa = document.getElementById("onlyAnalyzed");
  const go = () => render(d, q.value, oa.checked);
  q.addEventListener("input", go);
  oa.addEventListener("change", go);
  go();
}

setupTip();
setupReferral();
boot();
