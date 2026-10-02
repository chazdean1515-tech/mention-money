// Kalshi referral link (single source of truth). Referral links open Kalshi signup and can't deep-link to a
// market, so market links stay as-is and this is shown as a separate "New to Kalshi?" CTA. Lives in the app
// template, not in data/*.json, so the daily rebuild (fetch.py / research/build_analysis.py) never touches it.
const KALSHI_REFERRAL_URL = 'https://kalshi.com/r/7cd20072-8acd-4c35-a907-b6226921c42b';
const REF_DISCLOSURE = 'Referral link: we may earn a bonus if you sign up and trade. Not financial advice.';
const refLink = (cls, html) => `<a class="${cls}" href="${KALSHI_REFERRAL_URL}" target="_blank" rel="sponsored noopener" title="${REF_DISCLOSURE}">${html}</a>`;
// Static referral anchors in index.html carry data-kalshi-ref; fill in the URL and reveal them.
function setupReferral() {
  document.querySelectorAll('a[data-kalshi-ref]').forEach(a => {
    a.href = KALSHI_REFERRAL_URL; a.target = '_blank'; a.rel = 'sponsored noopener'; a.hidden = false;
  });
  document.querySelectorAll('[data-kalshi-ref-disc]').forEach(el => { el.textContent = REF_DISCLOSURE; el.hidden = false; });
}

const FEE = p => 0.07 * p * (1 - p);
const pct = x => (x == null || isNaN(x)) ? '—' : Math.round(x * 100) + '¢';
const pctP = x => (x == null || isNaN(x)) ? '—' : Math.round(x * 100) + '%';
const esc = s => String(s ?? '').replace(/[&<>"']/g, c => ({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
const fmtET = iso => { if (!iso) return '—'; const d = new Date(iso);
  return d.toLocaleString('en-US', {timeZone:'America/New_York', weekday:'short', month:'short', day:'numeric', hour:'numeric', minute:'2-digit'}) + ' ET'; };

// Edge for buying YES at ask, or NO at no_ask, net of taker fee.
function edges(m, est) {
  const out = {side:null, edge:null, price:null};
  if (est == null) return out;
  let best = null;
  if (m.yes_ask && m.yes_ask > 0 && m.yes_ask < 1) {
    const e = est - m.yes_ask - FEE(m.yes_ask);
    best = {side:'YES', edge:e, price:m.yes_ask};
  }
  if (m.no_ask && m.no_ask > 0 && m.no_ask < 1) {
    const e = (1 - est) - m.no_ask - FEE(m.no_ask);
    if (!best || e > best.edge) best = {side:'NO', edge:e, price:m.no_ask};
  }
  return best || out;
}

async function load() {
  const bust = '?t=' + Date.now();
  const [mk, an] = await Promise.all([
    fetch('data/markets.json' + bust).then(r => r.json()),
    fetch('data/analysis.json' + bust).then(r => r.ok ? r.json() : {events:{}}).catch(() => ({events:{}}))
  ]);
  return {mk, an};
}

// Same rule as the Play of the Day in research/build_analysis.py: once an event's speaking window has started
// (analysis event_time_et in the past), its prices are stale for betting, so its picks are not listed.
const started = ea => !!(ea && ea.event_time_et && new Date(ea.event_time_et).getTime() <= Date.now());
const etDate = value => value ? new Intl.DateTimeFormat('en-CA', {timeZone:'America/New_York', year:'numeric', month:'2-digit', day:'2-digit'}).format(new Date(value)) : '';
const todayET = etDate(Date.now());
function render({mk, an}, q = '', onlyAnalyzed = false) {
  const A = an.events || {};
  const minEdge = an.min_edge ?? 0.05;
  document.getElementById('meta').innerHTML =
    `Today only · prices updated <b>${fmtET(mk.fetched_at_et)}</b> · ${mk.series_scanned}/${mk.series_total} Mentions series scanned` +
    (an.updated_at_et ? ` · analysis written ${fmtET(an.updated_at_et)}` : '');

  const ql = q.trim().toLowerCase();
  // The board is deliberately a same-day board. Use the research event time, not the ticker date.
  const evs = mk.events.filter(e => {
    const ea = A[e.event_ticker];
    if (!ea || !ea.event_time_et || etDate(ea.event_time_et) !== todayET) return false;
    if (onlyAnalyzed && !ea) return false;
    if (!ql) return true;
    return (e.title + ' ' + (e.sub_title||'') + ' ' + e.series_title + ' ' + e.markets.map(m => m.word).join(' ')).toLowerCase().includes(ql);
  });
  // analyzed first, then by time
  const done = e => !!e.decided || started(A[e.event_ticker]);
  evs.sort((a, b) => (done(a) - done(b)) || (!!A[b.event_ticker] - !!A[a.event_ticker]) || (a.expected_expiration_et || '').localeCompare(b.expected_expiration_et || ''));

  const cards = evs.map(e => {
    const ea = A[e.event_ticker];
    const words = (ea && ea.words) || {};
    const rows = e.markets.map(m => {
      const w = words[m.ticker] || words[m.word] || null;
      return {m, w};
    }).sort((a, b) => a.m.word.localeCompare(b.m.word));

    const tr = rows.map(({m, w}) => `
      <div class="word-row">
        <h4>${esc(m.word)}</h4>
        <p>${esc((w && (w.prose || w.reason)) || 'No transcript read for this word yet.')}</p>
      </div>`).join('');

    const src = ea && ea.sources ? ea.sources.map(s => `<a href="${esc(s.url)}" target="_blank" rel="noopener">${esc(s.title || s.url)}</a>`).join(' · ') : '';
    const rules = e.markets[0] && e.markets[0].rules_primary ? e.markets[0].rules_primary : '';
    return `<article class="card">
      <div class="hd">
        <h3>${esc(ea?.title || e.title)} ${e.decided ? '<span class="tag">window closed, awaiting settlement</span>' : started(ea) ? '<span class="tag">event started, picks hidden</span>' : ea ? '<span class="tag">analyzed</span>' : '<span class="tag pending">analysis pending</span>'}</h3>
        <div class="info">${esc(ea?.speaker || e.series_title)} · event ${ea?.event_time_et ? fmtET(ea.event_time_et) : (e.event_date ? e.event_date + ' (date from ticker)' : '—')} · market closes ${fmtET(e.first_close_et)} · prices as of ${fmtET(e.price_fetched_at_et)} · vol ${Math.round(e.total_volume).toLocaleString()} · <span class="mut">${esc(e.event_ticker)}</span></div>
        ${ea?.event_time_note ? `<div class="info">⏱ ${esc(ea.event_time_note)}</div>` : ''}
        ${ea ? `<div class="event-context"><b>Event context</b>
          ${ea.context ? `<div class="ctx">${esc(ea.context)}</div>` : ''}
          ${ea.method ? `<div class="info">Method: ${esc(ea.method)}</div>` : ''}
          ${src ? `<div class="src">Sources: ${src}</div>` : ''}</div>` : ''}
        ${ea?.confidence ? `<div class="info">Confidence: ${esc(ea.confidence)}</div>` : ''}
      </div>
      <div class="word-list">${tr}</div>
      ${rules ? `<details><summary>rules (first market)</summary><div class="rules">${esc(rules)}\n\n${esc(e.markets[0].rules_secondary || '')}</div></details>` : ''}
    </article>`;
  }).join('');

  document.getElementById('events').innerHTML = cards || '<p class="mut">No events match.</p>';
}

// Play of the Day: chosen at build time (research/build_analysis.py) and stored in analysis.json.
function renderTicker(mk, an) {
  const A = (an && an.events) || {};
  const events = (mk.events || []).filter(e => {
    const ea = A[e.event_ticker];
    return ea && ea.event_time_et && etDate(ea.event_time_et) === todayET;
  }).sort((a, b) => new Date(A[a.event_ticker].event_time_et) - new Date(A[b.event_ticker].event_time_et));
  const el = document.getElementById('today-ticker');
  if (!el || !events.length) { if (el) el.hidden = true; return; }
  const clock = iso => new Date(iso).toLocaleTimeString('en-US', {timeZone:'America/New_York', hour:'numeric', minute:'2-digit'});
  const bits = [];
  events.forEach(e => {
    const ea = A[e.event_ticker];
    bits.push(`<span class="tick mark"><b>${esc(clock(ea.event_time_et))} ET</b> ${esc(ea.title || e.title || 'Event')}</span>`);
    e.markets.slice().sort((a, b) => a.word.localeCompare(b.word)).forEach(m => {
      const px = m.last_price != null ? Math.round(m.last_price * 100) : (m.yes_bid != null && m.yes_ask != null ? Math.round(((m.yes_bid + m.yes_ask) / 2) * 100) : null);
      const cls = px == null ? 'mark' : (px >= 50 ? 'up' : 'down');
      bits.push(`<span class="tick ${cls}"><b>${esc(m.word).toUpperCase()}</b>${px == null ? '' : `<span class="px">${px}</span>`}</span>`);
    });
  });
  const seq = bits.join('<span class="tick mark sep">●</span>');
  const seconds = Math.max(22, bits.length * 2.4);
  el.innerHTML = `<span class="ticker-label">MM</span><div class="ticker-window"><div class="ticker-track" style="animation-duration:${seconds}s"><span class="ticker-seq">${seq}</span><span class="ticker-seq" aria-hidden="true">${seq}</span></div></div>`;
  el.hidden = false;
}

function renderPotd(an) {
  const el = document.getElementById('potd');
  const p = an && an.play_of_the_day;
  if (!p || (p.event_time_et && new Date(p.event_time_et).getTime() <= Date.now())) { el.hidden = true; el.innerHTML = ''; return; }
  const side = p.side === 'NO' ? 'NO' : 'YES';
  const edgeC = Math.round(p.edge * 100);
  el.innerHTML = `<article class="potd-card">
    <div class="potd-shine" aria-hidden="true"></div>
    <div class="potd-top">
      <span class="potd-badge" aria-hidden="true">🏆</span>
      <span class="potd-label">Play of the Day</span>
      <span class="potd-fire" aria-hidden="true">🔥</span>
    </div>
    <div class="potd-event">${esc(p.event_title)}</div>
    <div class="potd-pick"><span class="potd-word">“${esc(p.word)}”</span> <span class="potd-side ${side.toLowerCase()}">BUY ${side}</span></div>
    <div class="potd-stats">
      <div class="potd-stat"><span class="k">Price (${side})</span><span class="v">${pct(p.price)}</span></div>
      <div class="potd-stat"><span class="k">Our est. (${side})</span><span class="v">${pctP(p.est_side)}</span>${side === 'NO' ? `<span class="s">YES ${pctP(p.est_yes)}</span>` : ''}</div>
      <div class="potd-stat edge"><span class="k">Edge</span><span class="v">${edgeC > 0 ? '+' : ''}${edgeC}¢</span><span class="s">after ~${Math.round(p.fee * 100)}¢ fee</span></div>
    </div>
    <div class="potd-when">
      ${p.event_time_et ? `<span>🎙 Event <b>${fmtET(p.event_time_et)}</b></span>` : ''}
      <span>⏳ Market closes <b>${fmtET(p.close_time_et)}</b></span>
      ${p.price_fetched_at_et ? `<span class="mut">price as of ${fmtET(p.price_fetched_at_et)}</span>` : ''}
    </div>
    <p class="potd-why">${esc(p.rationale)}</p>
    <div class="potd-foot">
      ${p.url ? `<a class="potd-link" href="${esc(p.url)}" target="_blank" rel="noopener">View market on Kalshi →</a>` : ''}
      ${refLink('ref-link', 'New to Kalshi? <b>Sign up with our link</b>')}
    </div>
    <p class="potd-disc ref-disc">${REF_DISCLOSURE}</p>
  </article>`;
  el.hidden = false;
}

// Tip panel (SOL address is static in index.html; copy reads it from the DOM).
function setupTip() {
  const dlg = document.getElementById('tip');
  if (!dlg) return;
  const status = document.getElementById('tip-status');
  const open = () => { status.textContent = ''; if (dlg.showModal) dlg.showModal(); else dlg.setAttribute('open', ''); };
  const close = () => { if (dlg.close) dlg.close(); else dlg.removeAttribute('open'); };
  document.querySelectorAll('[data-tip-open]').forEach(b => b.addEventListener('click', open));
  dlg.querySelector('[data-tip-close]').addEventListener('click', close);
  dlg.addEventListener('click', ev => { if (ev.target === dlg) close(); });  // backdrop click
  document.getElementById('tip-copy').addEventListener('click', async () => {
    const addr = document.getElementById('sol-addr').textContent.trim();
    let ok = false;
    try { await navigator.clipboard.writeText(addr); ok = true; } catch (_) {
      const ta = document.createElement('textarea'); ta.value = addr; ta.setAttribute('readonly', '');
      ta.style.position = 'fixed'; ta.style.opacity = '0'; dlg.appendChild(ta); ta.select();
      try { ok = document.execCommand('copy'); } catch (_) {} ta.remove();
    }
    status.textContent = ok ? 'Copied!' : 'Copy failed. Select the address above.';
    status.classList.toggle('ok', ok);
    clearTimeout(setupTip.t); setupTip.t = setTimeout(() => { status.textContent = ''; }, 2500);
  });
}
setupTip();
setupReferral();

load().then(d => {
  renderTicker(d.mk, d.an);
  renderPotd(d.an);
  const q = document.getElementById('q'), oa = document.getElementById('onlyAnalyzed');
  const go = () => render(d, q.value, oa.checked);
  q.addEventListener('input', go); oa.addEventListener('change', go); go();
}).catch(err => { document.getElementById('meta').textContent = 'Failed to load data: ' + err; });
