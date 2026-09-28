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

function render({mk, an}, q = '', onlyAnalyzed = false) {
  const A = an.events || {};
  const minEdge = an.min_edge ?? 0.05;
  document.getElementById('meta').innerHTML =
    `Last updated <b>${fmtET(mk.fetched_at_et)}</b> (oldest price in view: ${fmtET(mk.oldest_price_et)}) · ${mk.event_count} events / ${mk.market_count} markets with event dates in the next ${mk.horizon_days} days · ${mk.series_scanned}/${mk.series_total} Mentions series scanned` +
    (an.updated_at_et ? ` · analysis written ${fmtET(an.updated_at_et)}` : '');

  const ql = q.trim().toLowerCase();
  const evs = mk.events.filter(e => {
    if (onlyAnalyzed && !A[e.event_ticker]) return false;
    if (!ql) return true;
    return (e.title + ' ' + (e.sub_title||'') + ' ' + e.series_title + ' ' + e.markets.map(m => m.word).join(' ')).toLowerCase().includes(ql);
  });
  // analyzed first, then by time
  evs.sort((a, b) => (!!a.decided - !!b.decided) || (!!A[b.event_ticker] - !!A[a.event_ticker]) || (a.expected_expiration_et || '').localeCompare(b.expected_expiration_et || ''));

  const best = [];
  const cards = evs.map(e => {
    const ea = A[e.event_ticker];
    const words = (ea && ea.words) || {};
    const rows = e.markets.map(m => {
      const w = words[m.ticker] || words[m.word] || null;
      const est = w ? w.p : null;
      const ed = edges(m, est);
      const hl = !e.decided && ed.edge != null && ed.edge >= minEdge;
      if (hl) best.push({e, m, w, ed});
      return {m, w, est, ed, hl};
    }).sort((a, b) => (b.ed.edge ?? -9) - (a.ed.edge ?? -9) || (b.m.last_price ?? 0) - (a.m.last_price ?? 0));

    const tr = rows.map(({m, w, est, ed, hl}) => `
      <tr class="${hl ? 'hl' : ''}">
        <td class="word"><b>${esc(m.word)}</b>${w && w.reason ? `<span class="r-m">${esc(w.reason)}</span>` : ''}</td>
        <td title="yes bid / yes ask">${pct(m.yes_bid)}/${pct(m.yes_ask)}</td>
        <td class="hide-m">${pct(m.last_price)}</td>
        <td class="hide-m">${m.volume != null ? Math.round(m.volume).toLocaleString() : '—'}</td>
        <td>${pctP(est)}</td>
        <td class="${ed.edge == null ? 'mut' : ed.edge > 0 ? 'pos' : 'neg'}">${ed.edge == null ? '—' : `${ed.side} ${ed.edge > 0 ? '+' : ''}${Math.round(ed.edge * 100)}¢`}</td>
        <td class="reason">${w ? esc(w.reason) : ''}</td>
      </tr>`).join('');

    const src = ea && ea.sources ? ea.sources.map(s => `<a href="${esc(s.url)}" target="_blank" rel="noopener">${esc(s.title || s.url)}</a>`).join(' · ') : '';
    const rules = e.markets[0] && e.markets[0].rules_primary ? e.markets[0].rules_primary : '';
    return `<article class="card">
      <div class="hd">
        <h3>${esc(ea?.title || e.title)} ${e.decided ? '<span class="tag">window closed, awaiting settlement</span>' : ea ? '<span class="tag">analyzed</span>' : '<span class="tag pending">analysis pending</span>'}</h3>
        <div class="info">${esc(ea?.speaker || e.series_title)} · event ${ea?.event_time_et ? fmtET(ea.event_time_et) : (e.event_date ? e.event_date + ' (date from ticker)' : '—')} · market closes ${fmtET(e.first_close_et)} · prices as of ${fmtET(e.price_fetched_at_et)} · vol ${Math.round(e.total_volume).toLocaleString()} · <span class="mut">${esc(e.event_ticker)}</span></div>
        ${ea?.event_time_note ? `<div class="info">⏱ ${esc(ea.event_time_note)}</div>` : ''}
        ${ea ? `<details class="ctxd"><summary>Context, method & sources</summary>
          ${ea.context ? `<div class="ctx">${esc(ea.context)}</div>` : ''}
          ${ea.method ? `<div class="info">Method: ${esc(ea.method)}</div>` : ''}
          ${src ? `<div class="src">Sources: ${src}</div>` : ''}</details>` : ''}
        ${ea?.confidence ? `<div class="info">Confidence: ${esc(ea.confidence)}</div>` : ''}
      </div>
      <div class="scroll"><table class="tbl">
        <thead><tr><th class="word">Word</th><th>Bid/Ask</th><th class="hide-m">Last</th><th class="hide-m">Vol</th><th>Est.</th><th>Edge</th><th class="reason">Reason</th></tr></thead>
        <tbody>${tr}</tbody></table></div>
      ${rules ? `<details><summary>rules (first market)</summary><div class="rules">${esc(rules)}\n\n${esc(e.markets[0].rules_secondary || '')}</div></details>` : ''}
    </article>`;
  }).join('');

  best.sort((a, b) => b.ed.edge - a.ed.edge);
  document.getElementById('best').innerHTML = `<h2>Best value (edge ≥ ${Math.round(minEdge*100)}¢ after fee)</h2>` +
    (best.length ? `<div class="bv">${best.slice(0, 10).map(({e, m, w, ed}) => `
      <div class="bvi"><div class="top"><span class="w">${esc(m.word)} <span class="pill ${ed.side.toLowerCase()}">BUY ${ed.side}</span></span>
      <span class="pos">+${Math.round(ed.edge*100)}¢</span></div>
      <div class="ev">${esc(A[e.event_ticker]?.title || e.title)} · ${A[e.event_ticker]?.event_time_et ? fmtET(A[e.event_ticker].event_time_et) : (e.event_date ? e.event_date + ' (date TBC)' : 'date TBC')}</div>
      <div>Pay ${pct(ed.price)} · est. YES ${pctP(w.p)} · yes bid/ask ${pct(m.yes_bid)}/${pct(m.yes_ask)}</div>
      <div class="ev">${esc(w.reason)}</div></div>`).join('')}</div>` : '<div class="mut">No bets clear the threshold right now.</div>');
  document.getElementById('events').innerHTML = cards || '<p class="mut">No events match.</p>';
}

load().then(d => {
  const q = document.getElementById('q'), oa = document.getElementById('onlyAnalyzed');
  const go = () => render(d, q.value, oa.checked);
  q.addEventListener('input', go); oa.addEventListener('change', go); go();
}).catch(err => { document.getElementById('meta').textContent = 'Failed to load data: ' + err; });
