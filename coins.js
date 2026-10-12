(function(){
var D=window.MM_COINS; if(!D){document.getElementById('meta').textContent='No snapshot yet.';return;}
function usd(v){if(v==null)return'—';var a=Math.abs(v);return'$'+(a>=1e9?(v/1e9).toFixed(2)+'B':a>=1e6?(v/1e6).toFixed(2)+'M':a>=1e3?(v/1e3).toFixed(1)+'K':a>=1?v.toFixed(2):v.toPrecision(3));}
function esc(s){return String(s).replace(/[&<>"]/g,function(c){return{'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]});}
document.getElementById('meta').textContent='Snapshot as of '+D.generated_et+'. Refreshed daily.';
var tabs=document.getElementById('tabs'),wrap=document.getElementById('tables');
D.chains.forEach(function(c,i){
  var b=document.createElement('button');b.type='button';b.textContent=c.name;b.setAttribute('role','tab');b.dataset.i=i;tabs.appendChild(b);
  var s=document.createElement('section');s.className='chain';s.id='c-'+c.id;
  var h='<h2>'+esc(c.name)+'</h2><div class="tw"><table><thead><tr><th>#</th><th>Coin</th><th>Price</th><th>24h</th><th>24h volume</th><th>Liquidity</th><th>X mentions 24h</th><th>Contract</th></tr></thead><tbody>';
  c.coins.forEach(function(r,j){var ch=r.chg24==null?'—':(r.chg24>0?'+':'')+r.chg24.toFixed(1)+'%';
    h+='<tr><td>'+(j+1)+'</td><td><a href="'+esc(r.url)+'" rel="noopener" target="_blank"><b>$'+esc(r.symbol)+'</b></a><small>'+esc(r.name)+(r.boosted?' <span class="boost">Boosted</span>':'')+'</small></td><td>'+usd(r.price_usd)+'</td><td class="'+(r.chg24>=0?'up':'dn')+'">'+ch+'</td><td>'+usd(r.vol24)+'</td><td>'+usd(r.liq)+'</td><td>'+(r.mentions==null?'—':r.mentions.toLocaleString())+'</td><td><code title="'+esc(r.address)+'">'+esc(r.address.slice(0,6)+'…'+r.address.slice(-4))+'</code> <button class="cp" data-a="'+esc(r.address)+'">Copy</button></td></tr>';});
  s.innerHTML=h+'</tbody></table></div>';wrap.appendChild(s);
});
tabs.addEventListener('click',function(e){var i=e.target.dataset.i;if(i==null)return;document.getElementById('c-'+D.chains[i].id).scrollIntoView({behavior:'smooth'});});
wrap.addEventListener('click',function(e){var a=e.target.dataset.a;if(a&&navigator.clipboard){navigator.clipboard.writeText(a);e.target.textContent='Copied';}});
})();
