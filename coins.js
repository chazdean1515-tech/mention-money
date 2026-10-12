(function(){
var D=window.MM_COINS,meta=document.getElementById('meta'),stale=document.getElementById('stale');
if(!D){meta.textContent='No snapshot available. Try again later.';return;}
function usd(v){if(v==null)return'—';var a=Math.abs(v);return'$'+(a>=1e9?(v/1e9).toFixed(2)+'B':a>=1e6?(v/1e6).toFixed(2)+'M':a>=1e3?(v/1e3).toFixed(1)+'K':a>=1?v.toFixed(2):v.toPrecision(3));}
function esc(s){return String(s).replace(/[&<>"']/g,function(c){return{'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]});}
meta.textContent='Snapshot as of '+D.generated_et+'. Refreshed daily.';
if(D.generated_ts){var hrs=(Date.now()/1000-D.generated_ts)/3600;if(hrs>26){stale.hidden=false;stale.textContent='The daily refresh did not run. This snapshot is about '+Math.round(hrs)+' hours old, so figures may be far from current.';}}
var tabs=document.getElementById('tabs'),wrap=document.getElementById('tables');
D.chains.forEach(function(c){
  var a=document.createElement('a');a.href='#c-'+c.id;a.textContent=c.name;tabs.appendChild(a);
  var s=document.createElement('section');s.className='chain';s.id='c-'+c.id;s.setAttribute('aria-labelledby','h-'+c.id);
  var h='<h2 id="h-'+c.id+'">'+esc(c.name)+'</h2><p class="swipe" aria-hidden="true">Swipe for more →</p><div class="tw" tabindex="0" role="region" aria-label="'+esc(c.name)+' table"><table><thead><tr><th class="stick">Coin</th><th>#</th><th>Price</th><th>24h</th><th>24h volume</th><th>Liquidity</th><th>X mentions</th><th>Contract</th></tr></thead><tbody>';
  if(!c.coins.length)h+='<tr><td class="stick">—</td><td colspan="7">No coins passed the filters in this snapshot.</td></tr>';
  c.coins.forEach(function(r,j){var ch=r.chg24==null?'—':(r.chg24>0?'+':'')+r.chg24.toFixed(1)+'%';
    h+='<tr><td class="stick"><a href="'+esc(r.url)+'" rel="noopener" target="_blank"><b>$'+esc(r.symbol)+'</b></a><small>'+esc(r.name)+(r.boosted?' <span class="tag boost">Boosted</span>':'')+(r.is_new?' <span class="tag new">New &lt;24h</span>':'')+'</small></td><td>'+(j+1)+'</td><td>'+usd(r.price_usd)+'</td><td class="'+(r.chg24>=0?'up':'dn')+'">'+ch+'</td><td>'+usd(r.vol24)+'</td><td>'+usd(r.liq)+'</td><td class="soon">Coming soon</td><td><code title="'+esc(r.address)+'">'+esc(r.address.slice(0,6)+'…'+r.address.slice(-4))+'</code> <button type="button" class="cp" data-a="'+esc(r.address)+'" aria-label="Copy '+esc(r.symbol)+' contract address">Copy</button></td></tr>';});
  s.innerHTML=h+'</tbody></table></div><p class="tnote">Trading data, not a recommendation. High risk. Verify the contract before trading.</p>';wrap.appendChild(s);
});
function fallback(t){var x=document.createElement('textarea');x.value=t;x.setAttribute('readonly','');x.style.position='fixed';x.style.opacity='0';document.body.appendChild(x);x.select();var ok=false;try{ok=document.execCommand('copy');}catch(e){}document.body.removeChild(x);return ok;}
wrap.addEventListener('click',function(e){var b=e.target.closest('.cp');if(!b)return;var t=b.dataset.a;
  function done(ok){b.textContent=ok?'Copied':'Copy failed';setTimeout(function(){b.textContent='Copy';},2000);}
  if(navigator.clipboard&&window.isSecureContext){navigator.clipboard.writeText(t).then(function(){done(true)},function(){done(fallback(t))});}else done(fallback(t));});
})();
