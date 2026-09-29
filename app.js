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
  const done = e => !!e.decided || started(A[e.event_ticker]);
  evs.sort((a, b) => (done(a) - done(b)) || (!!A[b.event_ticker] - !!A[a.event_ticker]) || (a.expected_expiration_et || '').localeCompare(b.expected_expiration_et || ''));

  const best = [];
  const cards = evs.map(e => {
    const ea = A[e.event_ticker];
    const words = (ea && ea.words) || {};
    const rows = e.markets.map(m => {
      const w = words[m.ticker] || words[m.word] || null;
      const est = w ? w.p : null;
      const ed = edges(m, est);
      const hl = !done(e) && ed.edge != null && ed.edge >= minEdge;
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
        <h3>${esc(ea?.title || e.title)} ${e.decided ? '<span class="tag">window closed, awaiting settlement</span>' : started(ea) ? '<span class="tag">event started, picks hidden</span>' : ea ? '<span class="tag">analyzed</span>' : '<span class="tag pending">analysis pending</span>'}</h3>
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

// Play of the Day: chosen at build time (research/build_analysis.py) and stored in analysis.json.
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

// ---------- Spin the Wheel ----------
// 8 slices alternating the 4 play types; picks come from analysis.json `wheel_plays` (built in research/build_analysis.py).
const WHEEL_ORDER = ['BOMB', 'RETIREMENT', 'ROLLS-ROYCE', 'CASH'];
const WHEEL_LABEL = {'BOMB': 'BOMB', 'RETIREMENT': 'RETIREMENT', 'ROLLS-ROYCE': 'ROLLS-ROYCE', 'CASH': 'CASH'};
const reduceMotion = () => window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;
const pickStarted = p => !!(p && p.event_time_et && new Date(p.event_time_et).getTime() <= Date.now());

function wheelSVG(plays) {
  const R = 172, N = 8, seg = 360 / N, rad = d => (d - 90) * Math.PI / 180;
  const pt = (r, d) => `${(r * Math.cos(rad(d))).toFixed(2)} ${(r * Math.sin(rad(d))).toFixed(2)}`;
  let slices = '', labels = '', studs = '';
  for (let i = 0; i < N; i++) {
    const a0 = i * seg - seg / 2, a1 = a0 + seg, t = WHEEL_ORDER[i % 4], pl = plays[t];
    const gold = i % 2 === 0;
    slices += `<path d="M0 0 L${pt(R, a0)} A${R} ${R} 0 0 1 ${pt(R, a1)} Z" fill="url(#${gold ? 'wg-gold' : 'wg-green'})" stroke="#5a4410" stroke-width="1.5"/>`;
    const name = WHEEL_LABEL[t];
    const fs = name.length > 8 ? 12.5 : 16;
    labels += `<g transform="rotate(${i * seg})">
      <text x="0" y="-150" text-anchor="middle" dominant-baseline="middle" font-size="23">${pl ? pl.emoji : ''}</text>
      <text transform="translate(0 -99) rotate(90)" text-anchor="middle" dominant-baseline="middle" font-size="${fs}"${name.length > 8 ? ' textLength="76" lengthAdjust="spacingAndGlyphs"' : ''} class="wl ${gold ? 'on-gold' : 'on-green'}">${name}</text></g>`;
  }
  for (let i = 0; i < 16; i++) {
    const d = i * 22.5 + (i % 2 ? 0 : 0);
    const [x, y] = pt(186, d).split(' ');
    studs += i % 2 === 0
      ? `<circle cx="${x}" cy="${y}" r="5.5" fill="url(#wg-gem)" stroke="#fff6c9" stroke-width="1"/>`
      : `<circle cx="${x}" cy="${y}" r="4.2" fill="url(#wg-ruby)" stroke="#fff6c9" stroke-width=".8"/>`;
  }
  return `<svg viewBox="-200 -200 400 400" class="wheel-svg" aria-hidden="true" focusable="false">
    <defs>
      <linearGradient id="wg-gold" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#8a6a1f"/><stop offset=".3" stop-color="#f7e08a"/><stop offset=".5" stop-color="#d4af37"/><stop offset=".7" stop-color="#fff0a8"/><stop offset="1" stop-color="#9c7a22"/></linearGradient>
      <linearGradient id="wg-green" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#0c3d23"/><stop offset=".5" stop-color="#157a43"/><stop offset="1" stop-color="#0a2e1a"/></linearGradient>
      <linearGradient id="wg-rim" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#fff6c9"/><stop offset=".25" stop-color="#d4af37"/><stop offset=".5" stop-color="#8a6a1f"/><stop offset=".75" stop-color="#f3d36b"/><stop offset="1" stop-color="#9c7a22"/></linearGradient>
      <radialGradient id="wg-gem" cx=".35" cy=".35"><stop offset="0" stop-color="#ffffff"/><stop offset=".4" stop-color="#bfefff"/><stop offset="1" stop-color="#3aa8d8"/></radialGradient>
      <radialGradient id="wg-ruby" cx=".35" cy=".35"><stop offset="0" stop-color="#e8fff1"/><stop offset=".45" stop-color="#3dff9a"/><stop offset="1" stop-color="#0e8a4a"/></radialGradient>
    </defs>
    <circle r="197" fill="url(#wg-rim)"/><circle r="176" fill="#3a2c05"/>
    ${slices}${studs}${labels}
    <circle r="${R}" fill="none" stroke="#fff6c9" stroke-opacity=".55" stroke-width="1.5"/>
  </svg>`;
}

function revealCard(t, play, p) {
  if (!p) return `<article class="potd-card wheel-card"><div class="potd-top"><span class="potd-badge" aria-hidden="true">${play.emoji}</span><span class="potd-label">${esc(t)}</span></div>
    <p class="potd-why">This slot's events have already started. New picks arrive with the next data refresh.</p></article>`;
  const side = p.side === 'NO' ? 'NO' : 'YES', edgeC = Math.round(p.edge * 100);
  return `<article class="potd-card wheel-card">
    <div class="potd-shine" aria-hidden="true"></div>
    <div class="potd-top"><span class="potd-badge" aria-hidden="true">${play.emoji}</span><span class="potd-label">${esc(t)}</span><span class="potd-fire" aria-hidden="true">${play.emoji}</span></div>
    <div class="wheel-blurb">${esc(play.blurb)}</div>
    <div class="potd-event">${esc(p.event_title)}</div>
    <div class="potd-pick"><span class="potd-word">“${esc(p.word)}”</span> <span class="potd-side ${side.toLowerCase()}">BUY ${side}</span></div>
    <div class="potd-stats four">
      <div class="potd-stat"><span class="k">Price (${side})</span><span class="v">${pct(p.price)}</span></div>
      <div class="potd-stat"><span class="k">Our est. (${side})</span><span class="v">${pctP(p.est_side)}</span></div>
      <div class="potd-stat edge"><span class="k">Edge</span><span class="v">${edgeC > 0 ? '+' : ''}${edgeC}¢</span><span class="s">after ~${Math.round(p.fee * 100)}¢ fee</span></div>
      <div class="potd-stat"><span class="k">Payout</span><span class="v">${(1 / p.price).toFixed(1)}×</span><span class="s">if it hits</span></div>
    </div>
    <div class="potd-when">
      ${p.event_time_et ? `<span>🎙 Event <b>${fmtET(p.event_time_et)}</b></span>` : ''}
      <span>⏳ Market closes <b>${fmtET(p.close_time_et)}</b></span>
      ${p.price_fetched_at_et ? `<span class="mut">price as of ${fmtET(p.price_fetched_at_et)}</span>` : ''}
    </div>
    <p class="potd-why">${esc(p.rationale)}</p>
    ${p.fragile ? `<p class="wheel-warn">⚠ ${esc(p.fragile)}</p>` : ''}
    <div class="potd-foot">
      ${p.url ? `<a class="potd-link" href="${esc(p.url)}" target="_blank" rel="noopener">View market on Kalshi →</a>` : ''}
      ${refLink('ref-link sm', 'New to Kalshi? <b>Sign up</b>')}
      <button type="button" class="tip-btn wheel-again">Spin again ↻</button>
    </div>
    <p class="potd-disc ref-disc">${REF_DISCLOSURE}</p>
  </article>`;
}

function burst(el) {
  if (reduceMotion()) return;
  const bits = ['🪙', '💰', '✨', '💵', '💎'];
  let html = '';
  for (let i = 0; i < 30; i++) {
    const a = Math.random() * Math.PI * 2, d = 110 + Math.random() * 170;
    const style = `--dx:${(Math.cos(a) * d).toFixed(0)}px;--dy:${(Math.sin(a) * d - 60).toFixed(0)}px;--r:${Math.round(Math.random() * 720 - 360)}deg;animation-delay:${(Math.random() * 0.15).toFixed(2)}s`;
    html += i % 3 === 0 ? `<i class="cf" style="${style};background:${['#ffd23f', '#fff6c9', '#2ecc71', '#d4af37'][i % 4]}"></i>`
                        : `<span class="cf" style="${style}">${bits[i % bits.length]}</span>`;
  }
  el.innerHTML = html;
  setTimeout(() => { el.innerHTML = ''; }, 1900);
}

function setupWheel(an) {
  const sec = document.getElementById('wheel');
  const raw = (an && an.wheel_plays) || [];
  const plays = {};
  // At page load pick the first pick per play whose event hasn't started (same rule as POTD / Best value).
  raw.forEach(w => { plays[w.type] = {...w, pick: (w.picks || []).find(p => !pickStarted(p)) || null}; });
  if (!WHEEL_ORDER.some(t => plays[t])) { sec.hidden = true; return; }
  WHEEL_ORDER.forEach(t => { if (!plays[t]) plays[t] = {type: t, emoji: {'BOMB':'💣','RETIREMENT':'🏖️','ROLLS-ROYCE':'👑','CASH':'💵'}[t], blurb: '', pick: null}; });
  sec.hidden = false;
  const btn = document.getElementById('wheel-btn'), rot = document.getElementById('wheel-rot');
  const out = document.getElementById('wheel-result'), boom = document.getElementById('wheel-burst');
  rot.innerHTML = wheelSVG(plays);
  let angle = 0, spinning = false;
  const spin = () => {
    if (spinning) return;               // clicks during a spin are ignored
    spinning = true; btn.classList.add('spinning'); btn.setAttribute('aria-disabled', 'true');
    const k = Math.floor(Math.random() * 8);                // random landing slice
    const jitter = (Math.random() - 0.5) * 30;              // stay inside the 45° slice
    const rm = reduceMotion(), dur = rm ? 400 : 4200 + Math.random() * 1600;
    const target = ((-k * 45 + jitter) % 360 + 360) % 360;
    angle += (rm ? 360 : 360 * (5 + Math.floor(Math.random() * 3))) + ((target - angle) % 360 + 360) % 360;
    rot.style.transitionDuration = dur + 'ms';
    rot.style.transform = `rotate(${angle}deg)`;
    setTimeout(() => {
      const t = WHEEL_ORDER[k % 4], play = plays[t];
      burst(boom);
      out.innerHTML = revealCard(WHEEL_LABEL[t], play, play.pick);
      const again = out.querySelector('.wheel-again');
      if (again) again.addEventListener('click', () => { btn.focus(); spin(); });
      spinning = false; btn.classList.remove('spinning'); btn.removeAttribute('aria-disabled');
      btn.dataset.landed = t;
    }, dur + 60);
  };
  btn.addEventListener('click', spin);
  btn.addEventListener('keydown', ev => { if (ev.key === 'Enter' || ev.key === ' ' || ev.key === 'Spacebar') { ev.preventDefault(); spin(); } });
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
  renderPotd(d.an);
  setupWheel(d.an);
  const q = document.getElementById('q'), oa = document.getElementById('onlyAnalyzed');
  const go = () => render(d, q.value, oa.checked);
  q.addEventListener('input', go); oa.addEventListener('change', go); go();
}).catch(err => { document.getElementById('meta').textContent = 'Failed to load data: ' + err; });
