(function(){
var D=window.MM_COINS,$=function(id){return document.getElementById(id)};
if(!D){$('meta').textContent='No snapshot available. Try again later.';return;}
function usd(v){if(v==null)return'—';var a=Math.abs(v);return'$'+(a>=1e9?(v/1e9).toFixed(2)+'B':a>=1e6?(v/1e6).toFixed(2)+'M':a>=1e3?(v/1e3).toFixed(1)+'K':a>=1?v.toFixed(2):v.toPrecision(3));}
function num(v){return v>=1e3?(v/1e3).toFixed(1)+'K':String(v)}
function esc(s){return String(s==null?'':s).replace(/[&<>"']/g,function(c){return{'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]});}
function pct(v){return v==null?'—':(v>0?'+':'')+v.toFixed(1)+'%'}
function spark(arr,cls){if(!arr||arr.length<2)return'';var w=80,h=22,mn=Math.min.apply(0,arr),mx=Math.max.apply(0,arr),r=mx-mn||1;
  var pts=arr.map(function(v,i){return(i*w/(arr.length-1)).toFixed(1)+','+(h-1-(v-mn)/r*(h-2)).toFixed(1)}).join(' ');
  return'<svg class="spark '+cls+'" viewBox="0 0 '+w+' '+h+'" width="'+w+'" height="'+h+'" aria-hidden="true"><polyline points="'+pts+'"/></svg>';}
var all={};D.chains.forEach(function(c){c.coins.forEach(function(r){r._c=c;all[r.key]=r;});});
$('meta').textContent='Snapshot as of '+D.generated_et+'. Refreshed daily.';
if(D.generated_ts){var hrs=(Date.now()/1000-D.generated_ts)/3600;if(hrs>26){var st=$('stale');st.hidden=false;st.textContent='The daily refresh did not run. This snapshot is about '+Math.round(hrs)+' hours old, so figures may be far from current.';}}
$('mstatus').textContent=D.mentions_status==='live'?'X mention data: live for this snapshot (post counts by contract address or cashtag, last 24h). '+(D.mentions_note||''):'X mention data is not available for this snapshot, so every score is volume-only.';
// watchlist
var WK='mm_watch_v1',W;try{W=JSON.parse(localStorage.getItem(WK)||'[]')}catch(e){W=[]}
function saveW(){try{localStorage.setItem(WK,JSON.stringify(W))}catch(e){}renderWatch();}
// referrals / trade links
var R=D.referrals||{};
function fill(t,r){var c=r._c;return t.replace(/\{address\}/g,encodeURIComponent(r.address)).replace(/\{pool\}/g,encodeURIComponent(r.pool||'')).replace(/\{gchain\}/g,c.gmgn||'').replace(/\{bullx_chain\}/g,c.bullx||'').replace(/\{dschain\}/g,c.ds||c.id).replace(/\{chain\}/g,c.id);}
function trade(r){var L=(R.terminals||[]).filter(function(t){return t.enabled&&t.chains.indexOf(r.chain_id)>=0});if(!L.length)return'';
  return'<details class="trade"><summary>Trade</summary><div class="tl">'+L.map(function(t){var u=t.code&&t.ref_url?fill(t.ref_url.replace(/\{code\}/g,encodeURIComponent(t.code)),r):fill(t.url,r);
  return'<a href="'+esc(u)+'" target="_blank" rel="'+(t.code?'sponsored ':'')+'noopener">'+esc(t.name)+'</a>'}).join('')+'</div></details>';}
function chips(s){var o=[];if(!s||!s.source)return'<span class="chip unk">No safety data</span>';
  if(s.top10_pct!=null)o.push('<span class="chip '+(s.top10_pct>50?'bad':s.top10_pct>25?'warn':'ok')+'" title="Share held by the 10 largest non-pool holders">Top10 '+s.top10_pct.toFixed(0)+'%</span>');
  if(s.lp_locked_pct!=null&&!s.lp_unknown)o.push('<span class="chip '+(s.lp_locked_pct>=90?'ok':s.lp_locked_pct>=50?'warn':'bad')+'">LP locked '+s.lp_locked_pct.toFixed(0)+'%</span>');
  if(s.lp_burned_pct)o.push('<span class="chip ok">LP burned '+s.lp_burned_pct.toFixed(0)+'%</span>');
  if(s.mint_renounced===true)o.push('<span class="chip ok">Mint renounced</span>');
  return o.join('')+'<span class="src">'+esc(s.source)+'</span>';}
function age(h){return h==null?'—':h<24?Math.round(h)+'h':Math.round(h/24)+'d'}
function coinCell(r){var m=r.mx,b='';
  if(r.safety&&r.safety.flags&&r.safety.flags.length)b+=' <span class="tag flag" title="'+esc(r.safety.flags.join('; '))+'">⚑ Red flag</span>';
  if(r.boosted)b+=' <span class="tag boost">Boosted</span>';if(r.is_new)b+=' <span class="tag new">New &lt;24h</span>';
  (r.tags||[]).forEach(function(t){b+=' <span class="tag div">'+esc(t)+'</span>'});
  var who='';if(m&&m.top_mentioners&&m.top_mentioners.length)who='<small class="who">Top mentioners: '+m.top_mentioners.map(function(u){return'<a href="https://x.com/'+esc(u.u)+'" target="_blank" rel="noopener nofollow">@'+esc(u.u)+'</a> '+num(u.f)}).join(', ')+'</small>';
  if(m&&m.first_caller&&m.first_caller.u)who+='<small class="who">First caller (24h): <a href="'+esc(m.first_caller.url)+'" target="_blank" rel="noopener nofollow">@'+esc(m.first_caller.u)+'</a></small>';
  var on=W.indexOf(r.key)>=0;
  return'<td class="stick"><button type="button" class="star" data-w="'+esc(r.key)+'" aria-pressed="'+on+'" aria-label="'+(on?'Remove':'Add')+' $'+esc(r.symbol)+' '+(on?'from':'to')+' watchlist">'+(on?'★':'☆')+'</button><a href="'+esc(r.url)+'" rel="noopener" target="_blank"><b>$'+esc(r.symbol)+'</b></a><small>'+esc(r.name)+'</small><span class="tags">'+b+'</span>'+who+'</td>';}
// tabs
var tabs=$('tabs');D.chains.forEach(function(c){var a=document.createElement('a');a.href='#c-'+c.id;a.textContent=c.short;tabs.appendChild(a);});
[['heating','Heating Up'],['fresh','Fresh Mints'],['cooling','Cooling Off'],['receipts','Receipts'],['watch','Watchlist']].forEach(function(x){var a=document.createElement('a');a.href='#'+x[0];a.textContent=x[1];a.className='sec';tabs.appendChild(a);});
// featured (sponsored, never scored)
var F=D.featured||{};if(F.enabled&&F.title){var fe=$('featured');fe.hidden=false;fe.innerHTML='<span class="tag spon">'+esc(F.label||'Sponsored')+'</span> <b>'+esc(F.title)+'</b> '+esc(F.blurb||'')+(F.url?' <a href="'+esc(F.url)+'" rel="sponsored noopener" target="_blank">Learn more</a>':'')+'<small>Paid placement. Not ranked, not scored, not a recommendation.</small>';}
// chain tables
var wrap=$('tables');
D.chains.forEach(function(c){
  var s=document.createElement('section');s.className='chain';s.id='c-'+c.id;
  var h='<h2>'+esc(c.name)+'</h2><p class="swipe" aria-hidden="true">Swipe for more →</p><div class="tw" tabindex="0" role="region" aria-label="'+esc(c.name)+' table"><table><thead><tr><th class="stick">Coin</th><th>Score</th><th>Price · 24h</th><th>24h</th><th>Volume</th><th>Liquidity</th><th>X posts 24h</th><th>Safety</th><th>Age</th><th>Contract</th><th>Trade</th></tr></thead><tbody>';
  if(!c.coins.length)h+='<tr><td class="stick">—</td><td colspan="10">No coins passed the filters in this snapshot.</td></tr>';
  c.coins.forEach(function(r){var m=r.mx;
    h+='<tr>'+coinCell(r)+'<td><span class="score'+(r.safety.flags.length?' pen':'')+'">'+r.score+'</span>'+(r.score_kind!=='full'?'<small class="kind">'+(r.score_kind==='volume-only'?'volume-only':'no account sample')+'</small>':'')+'</td>'+
      '<td>'+usd(r.price_usd)+spark(r.spark,r.chg24>=0?'up':'dn')+'</td><td class="'+(r.chg24>=0?'up':'dn')+'">'+pct(r.chg24)+'</td><td>'+usd(r.vol24)+'</td><td>'+usd(r.liq)+'</td>'+
      '<td>'+(m?num(m.m24)+spark(m.hourly,'m')+'<small>last hr '+m.hourly[m.hourly.length-1]+' · ×'+m.accel.toFixed(1)+'</small>':'<span class="soon">No data</span>')+'</td>'+
      '<td class="chips">'+chips(r.safety)+'</td><td>'+age(r.age_h)+'</td>'+
      '<td><code title="'+esc(r.address)+'">'+esc(r.address.slice(0,6)+'…'+r.address.slice(-4))+'</code> <button type="button" class="cp" data-a="'+esc(r.address)+'" aria-label="Copy $'+esc(r.symbol)+' contract address">Copy</button></td><td>'+trade(r)+'</td></tr>';});
  s.innerHTML=h+'</tbody></table></div><p class="tnote">Trading data, not a recommendation. High risk. Verify the contract before trading.</p>';wrap.appendChild(s);
});
function li(r,extra){return'<li><a href="#c-'+r._c.id+'">$'+esc(r.symbol)+'</a> <span class="cn">'+esc(r._c.short)+'</span> '+extra+'</li>'}
function list(id,items,empty){var ol=document.querySelector('#'+id+' ol');ol.innerHTML=items.length?items.join(''):'<li class="empty">'+empty+'</li>';}
var noM='Needs X mention data, which this snapshot does not have.';
list('heating',(D.heating||[]).map(function(k){var r=all[k];return r?li(r,'×'+r.mx.accel.toFixed(1)+' <small>('+r.mx.hourly[r.mx.hourly.length-1]+' posts last hr)</small>'):''}),D.mentions_status==='live'?'No coin is accelerating right now.':noM);
list('fresh',(D.fresh||[]).map(function(k){var r=all[k];return r?li(r,age(r.age_h)+' old · '+num(r.mx.m24)+' posts'):''}),D.mentions_status==='live'?'No new pools with mentions in this snapshot.':noM);
list('cooling',(D.cooling||[]).map(function(c){return'<li>$'+esc(c.symbol)+' <span class="cn">'+esc(c.chain)+'</span> '+num(c.m24)+' → '+num(c.m24_now)+' posts (−'+c.drop_pct+'%)</li>'}),D.cooling_status==='no-history'?'Starts tomorrow: needs yesterday\'s mention snapshot to compare.':D.cooling_status==='no-mentions'?noM:'No former leader is cooling off.');
function renderWatch(){list('watch',W.map(function(k){var r=all[k];return r?li(r,'Score '+r.score+' · '+pct(r.chg24)):'<li>'+esc(k.split(':')[0])+' coin no longer on the board <button type="button" class="star" data-w="'+esc(k)+'" aria-label="Remove from watchlist">✕</button></li>'}),'Tap ☆ on any coin to save it here.');}
renderWatch();
var rb=document.querySelector('#receipts tbody'),rec=D.receipts||[];
rb.innerHTML=rec.length?rec.map(function(p){return'<tr><td class="stick">$'+esc(p.symbol)+' <small>'+esc(p.chain)+'</small></td><td>'+esc(p.date)+'</td><td>'+p.score+(p.score_kind!=='full'?' <small>'+esc(p.score_kind)+'</small>':'')+'</td><td>'+usd(p.price_usd)+'</td><td>'+usd(p.price_now)+'</td><td class="'+(p.chg_since>=0?'up':'dn')+'">'+pct(p.chg_since)+'</td></tr>'}).join(''):
  '<tr><td class="stick">—</td><td colspan="5">Tracking started '+esc(D.date)+'. Today\'s picks: '+(D.picks_today||[]).map(function(p){return'$'+esc(p.symbol)+' ('+esc(p.chain)+', '+usd(p.price_usd)+')'}).join(', ')+'. Results show here from tomorrow.</td></tr>';
// events
function fallback(t){var x=document.createElement('textarea');x.value=t;x.setAttribute('readonly','');x.style.position='fixed';x.style.opacity='0';document.body.appendChild(x);x.select();var ok=false;try{ok=document.execCommand('copy');}catch(e){}document.body.removeChild(x);return ok;}
document.addEventListener('click',function(e){var b=e.target.closest('.cp');
  if(b){var t=b.dataset.a;var done=function(ok){b.textContent=ok?'Copied':'Copy failed';setTimeout(function(){b.textContent='Copy';},2000);};
    if(navigator.clipboard&&window.isSecureContext){navigator.clipboard.writeText(t).then(function(){done(true)},function(){done(fallback(t))});}else done(fallback(t));return;}
  var s=e.target.closest('.star');if(s){var k=s.dataset.w,i=W.indexOf(k);if(i>=0)W.splice(i,1);else W.push(k);
    document.querySelectorAll('.star[data-w="'+k.replace(/"/g,'')+'"]').forEach(function(x){if(x.closest('td.stick')){var on=W.indexOf(k)>=0;x.textContent=on?'★':'☆';x.setAttribute('aria-pressed',on);}});saveW();}});
})();
