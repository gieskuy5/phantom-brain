"""Phantom Brain — Premium Dashboard (Anti-Template)."""
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse

app = FastAPI(title="Phantom Brain", version="2.0.0")
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"])

AGENT = {
    "name": "Phantom Alpha",
    "wallet": "0x69083D13C7767231EF2eAa0676F04F61b6F08a13",
    "totalSignals": 47, "winRate": 68.2, "pnl": 12.4,
    "strategyVault": "a3f2e8d1-7b4c-4e9a-b5d6-1c8f3e2a9b7d",
    "strategy": "Momentum Alpha v1",
    "indicators": ["RSI", "MACD", "Volume Profile", "Funding Rate"],
}
SIGNALS = [
    {"id":1,"token":"ETH","dir":"LONG","entry":3245,"sl":3150,"tp":3480,"conf":82,"tier":"brain","status":"active","time":"2m"},
    {"id":2,"token":"BTC","dir":"SHORT","entry":68500,"sl":69200,"tp":66800,"conf":75,"tier":"signal","status":"active","time":"15m"},
    {"id":3,"token":"SOL","dir":"LONG","entry":178,"sl":172,"tp":195,"conf":88,"tier":"brain","status":"won","time":"1h"},
    {"id":4,"token":"ARB","dir":"LONG","entry":1.12,"sl":1.08,"tp":1.25,"conf":71,"tier":"free","status":"active","time":"2h"},
    {"id":5,"token":"AVAX","dir":"SHORT","entry":42.5,"sl":44.0,"tp":39.0,"conf":69,"tier":"signal","status":"lost","time":"3h"},
]
LISTINGS = [
    {"id":1,"tier":"signal","token":"ETH","dir":"LONG","price":"0.5 IP","buyers":12},
    {"id":2,"tier":"brain","token":"ETH","dir":"LONG","price":"2.0 IP","buyers":3},
    {"id":3,"tier":"signal","token":"BTC","dir":"SHORT","price":"0.8 IP","buyers":8},
]
DEALS = [
    {"id":1,"cp":"0x3C44...93BC","tier":"signal","prop":"1.0 IP","counter":"0.7 IP","status":"settled","msgs":3},
    {"id":2,"cp":"0x7099...79C8","tier":"brain","prop":"3.0 IP","counter":"2.2 IP","status":"negotiating","msgs":2},
]
VAULTS = [
    {"uuid":"a3f2e8d1-...","type":"strategy","tier":"brain","created":"May 24","size":"892 B"},
    {"uuid":"b2a1c3d4-...","type":"signal","tier":"signal","created":"May 25","size":"256 B"},
    {"uuid":"e5f6g7h8-...","type":"signal","tier":"brain","created":"May 25","size":"512 B"},
    {"uuid":"i9j0k1l2-...","type":"proof","tier":"free","created":"May 25","size":"128 B"},
]
REVENUE = {"total":"12.5 IP","signalSales":"7.2 IP","brainSubs":"4.0 IP","a2aDeals":"1.3 IP"}

@app.get("/api/agent")
def ga(): return AGENT

@app.get("/api/signals")
def gs(): return SIGNALS

@app.get("/api/marketplace")
def gm(): return LISTINGS

@app.get("/api/deals")
def gd(): return DEALS

@app.get("/api/vaults")
def gv(): return VAULTS

@app.get("/api/revenue")
def gr(): return REVENUE

@app.get("/", response_class=HTMLResponse)
def index(): return HTML

HTML = r"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Phantom Brain</title>
<link href="https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;500;700&family=Space+Grotesk:wght@500;700&display=swap" rel="stylesheet">
<style>
*{margin:0;padding:0;box-sizing:border-box}
:root{--bg:#050508;--surface:rgba(255,255,255,.02);--glass:rgba(136,176,208,.04);--glass-h:rgba(136,176,208,.08);--border:rgba(136,176,208,.1);--border-a:rgba(136,176,208,.3);--text:#c8d6e0;--dim:#4a5c6a;--bright:#e8f0f4;--accent:#88B0D0;--glow:rgba(136,176,208,.12);--hot:#a8d0f0;--green:#4ade80;--red:#f87171;--purple:#a78bfa;--mono:'JetBrains Mono','Fira Code',monospace;--sans:'Space Grotesk',sans-serif}
html{scroll-behavior:smooth}
body{background:var(--bg);color:var(--text);font-family:var(--mono);font-size:.75rem;line-height:1.6;overflow-x:hidden;cursor:crosshair}

/* NOISE */
body::before{content:'';position:fixed;inset:0;background-image:url("data:image/svg+xml,%3Csvg viewBox='0 0 256 256' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.9' numOctaves='4' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23n)' opacity='0.03'/%3E%3C/svg%3E");pointer-events:none;z-index:9999;opacity:.4}

/* SCANLINES */
body::after{content:'';position:fixed;inset:0;background:repeating-linear-gradient(0deg,transparent,transparent 2px,rgba(136,176,208,.008) 2px,rgba(136,176,208,.008) 4px);pointer-events:none;z-index:9998}

/* PARTICLES CANVAS */
#particles{position:fixed;inset:0;z-index:0;pointer-events:none}

/* CURSOR */
.cursor-dot{position:fixed;width:4px;height:4px;background:var(--accent);border-radius:50%;pointer-events:none;z-index:9997;opacity:0;transition:opacity .3s;box-shadow:0 0 8px var(--accent)}
body:hover .cursor-dot{opacity:1}

/* HERO */
.hero{position:relative;z-index:1;padding:100px 40px 80px;text-center;min-height:60vh;display:flex;flex-direction:column;align-items:center;justify-content:center}
.hero-grid{position:absolute;inset:0;background-image:linear-gradient(rgba(136,176,208,.03) 1px,transparent 1px),linear-gradient(90deg,rgba(136,176,208,.03) 1px,transparent 1px);background-size:60px 60px;mask-image:radial-gradient(ellipse 60% 50% at 50% 50%,black 20%,transparent 70%)}

/* GLITCH TITLE */
.glitch{position:relative;font-family:var(--sans);font-size:clamp(2.5rem,6vw,4.5rem);font-weight:700;color:var(--bright);letter-spacing:-0.02em;margin-bottom:16px}
.glitch::before,.glitch::after{content:attr(data-text);position:absolute;top:0;left:0;width:100%;height:100%;opacity:0}
.glitch::before{color:#ff006e;animation:g1 5s infinite;clip-path:inset(0 0 80% 0)}
.glitch::after{color:#00f5d4;animation:g2 5s infinite;clip-path:inset(80% 0 0 0)}
@keyframes g1{0%,92%,100%{opacity:0;transform:none}93%{opacity:.8;transform:translate(-2px,-1px)}94%{opacity:0}95%{opacity:.6;transform:translate(2px,1px)}96%{opacity:0}}
@keyframes g2{0%,94%,100%{opacity:0;transform:none}95%{opacity:.7;transform:translate(2px,2px)}96%{opacity:0}97%{opacity:.5;transform:translate(-1px,-2px)}98%{opacity:0}}

.hero-sub{color:var(--dim);max-width:640px;margin:0 auto 40px;font-size:.8rem;line-height:1.8}
.hero-badge{display:inline-flex;align-items:center;gap:8px;padding:10px 24px;background:var(--glass);border:1px solid var(--border);border-radius:100px;font-size:.65rem;letter-spacing:.2em;text-transform:uppercase;color:var(--dim);margin-bottom:32px;backdrop-filter:blur(10px)}
.hero-badge::before{content:'';width:6px;height:6px;background:var(--accent);border-radius:50%;box-shadow:0 0 12px var(--accent);animation:blink 2s ease infinite}

/* STATS */
.stats-row{display:flex;justify-content:center;gap:60px;flex-wrap:wrap}
.stat{text-align:center}
.stat-val{font-family:var(--sans);font-size:2rem;font-weight:700;color:var(--bright)}
.stat-label{font-size:.6rem;color:var(--dim);text-transform:uppercase;letter-spacing:.2em;margin-top:6px}

/* SCROLL */
.scroll-hint{position:absolute;bottom:30px;left:50%;transform:translateX(-50%);display:flex;flex-direction:column;align-items:center;gap:8px;color:var(--dim);font-size:.6rem;letter-spacing:.2em;text-transform:uppercase;animation:float 3s ease-in-out infinite}
.scroll-hint::after{content:'';width:1px;height:30px;background:linear-gradient(to bottom,var(--dim),transparent)}

/* CONTAINER */
.container{max-width:1200px;margin:0 auto;padding:0 24px 80px;position:relative;z-index:1}

/* SECTION LABEL */
.section-label{font-family:var(--mono);font-size:.6rem;font-weight:500;letter-spacing:.2em;text-transform:uppercase;color:var(--dim);margin-bottom:20px;padding-left:2px;display:block}
.section-label::before{content:'›';margin-right:8px;color:var(--accent)}

/* GRID */
.grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(340px,1fr));gap:16px;margin-bottom:40px}

/* CARD — CORNER ACCENTS */
.card{background:var(--glass);border:1px solid var(--border);border-radius:16px;padding:24px;position:relative;transition:all .4s;backdrop-filter:blur(10px);overflow:hidden}
.card::before,.card::after{content:'';position:absolute;width:20px;height:20px;border-color:var(--accent);opacity:0;transition:opacity .4s}
.card::before{top:-1px;left:-1px;border-top:1px solid;border-left:1px solid;border-radius:16px 0 0 0}
.card::after{bottom:-1px;right:-1px;border-bottom:1px solid;border-right:1px solid;border-radius:0 0 16px 0}
.card:hover{border-color:var(--border-a);transform:translateY(-2px);box-shadow:0 20px 60px rgba(0,0,0,.4),0 0 40px var(--glow)}
.card:hover::before,.card:hover::after{opacity:.5}
.card h3{font-family:var(--sans);font-size:.95rem;margin-bottom:20px;display:flex;align-items:center;gap:10px;color:var(--bright)}
.card h3 .icon{font-size:1.1rem}

/* TABLE */
table{width:100%;border-collapse:collapse;font-size:.68rem}
th{text-align:left;padding:10px 8px;color:var(--dim);font-weight:500;text-transform:uppercase;letter-spacing:.12em;font-size:.58rem;border-bottom:1px solid var(--border)}
td{padding:10px 8px;border-bottom:1px solid rgba(136,176,208,.03)}
tr{transition:all .2s}
tr:hover td{background:rgba(136,176,208,.02);transform:translateX(2px)}

/* BADGE */
.badge{display:inline-block;padding:3px 10px;border-radius:100px;font-size:.55rem;font-weight:600;text-transform:uppercase;letter-spacing:.08em}
.b-long{background:rgba(74,222,128,.08);color:var(--green);border:1px solid rgba(74,222,128,.15)}
.b-short{background:rgba(248,113,113,.08);color:var(--red);border:1px solid rgba(248,113,113,.15)}
.b-free{background:rgba(74,96,108,.1);color:var(--dim);border:1px solid rgba(74,96,108,.2)}
.b-signal{background:rgba(136,176,208,.08);color:var(--accent);border:1px solid rgba(136,176,208,.15)}
.b-brain{background:rgba(167,139,250,.08);color:var(--purple);border:1px solid rgba(167,139,250,.15)}
.b-active{background:rgba(74,222,128,.08);color:var(--green);border:1px solid rgba(74,222,128,.15)}
.b-won{background:rgba(74,222,128,.12);color:var(--green);border:1px solid rgba(74,222,128,.2)}
.b-lost{background:rgba(248,113,113,.12);color:var(--red);border:1px solid rgba(248,113,113,.2)}
.b-settled{background:rgba(74,222,128,.08);color:var(--green);border:1px solid rgba(74,222,128,.15)}
.b-negotiating{background:rgba(136,176,208,.08);color:var(--accent);border:1px solid rgba(136,176,208,.15)}

/* CONFIDENCE BAR */
.cbar{width:36px;height:3px;background:var(--border);border-radius:2px;overflow:hidden;display:inline-block;vertical-align:middle;margin-left:6px}
.cfill{height:100%;border-radius:2px}

/* BUTTON — BORDER TO FILL */
.btn{position:relative;padding:8px 18px;background:transparent;border:1px solid var(--accent);border-radius:8px;color:var(--accent);font-family:var(--mono);font-size:.6rem;font-weight:600;letter-spacing:.1em;text-transform:uppercase;cursor:pointer;transition:all .3s;overflow:hidden}
.btn::before{content:'';position:absolute;inset:0;background:linear-gradient(135deg,var(--accent),var(--hot));opacity:0;transition:opacity .3s;z-index:-1}
.btn:hover{color:var(--bg);border-color:transparent;box-shadow:0 0 24px var(--glow);transform:translateY(-1px)}
.btn:hover::before{opacity:1}

/* REVENUE */
.rev-grid{display:grid;grid-template-columns:repeat(2,1fr);gap:10px}
.rev-item{padding:16px;background:var(--surface);border:1px solid var(--border);border-radius:12px;text-align:center;transition:all .3s}
.rev-item:hover{border-color:var(--border-a);background:var(--glass)}
.rev-val{font-family:var(--sans);font-size:1.2rem;font-weight:700;color:var(--bright)}
.rev-label{font-size:.55rem;color:var(--dim);text-transform:uppercase;letter-spacing:.15em;margin-top:4px}

/* VAULT ROW */
.vrow{display:flex;justify-content:space-between;align-items:center;padding:14px 0;border-bottom:1px solid rgba(136,176,208,.03);transition:all .2s}
.vrow:hover{transform:translateX(4px)}
.vrow:last-child{border-bottom:none}
.vuuid{font-size:.65rem;color:var(--dim)}

/* DEAL ITEM */
.deal{padding:16px 0;border-bottom:1px solid rgba(136,176,208,.03)}
.deal:last-child{border-bottom:none}
.deal-header{display:flex;justify-content:space-between;align-items:center;margin-bottom:8px}
.deal-meta{font-size:.6rem;color:var(--dim);display:flex;gap:8px;align-items:center;flex-wrap:wrap}

/* PROGRESS STEPS */
.steps{display:flex;gap:0;margin:30px 0;position:relative}
.steps::before{content:'';position:absolute;top:10px;left:10px;right:10px;height:1px;background:var(--border)}
.step{flex:1;display:flex;flex-direction:column;align-items:center;gap:8px;position:relative;z-index:1}
.step-dot{width:20px;height:20px;border-radius:50%;border:1px solid var(--border);display:flex;align-items:center;justify-content:center;font-size:.5rem;background:var(--bg);transition:all .3s}
.step.active .step-dot{border-color:var(--accent);box-shadow:0 0 12px var(--glow);animation:pulse 1.5s infinite}
.step.done .step-dot{border-color:var(--green);background:rgba(74,222,128,.1);color:var(--green)}
.step-label{font-size:.5rem;color:var(--dim);text-transform:uppercase;letter-spacing:.1em;text-align:center}
.step.active .step-label{color:var(--accent)}
.step.done .step-label{color:var(--green)}

/* FOOTER */
footer{text-align:center;padding:40px;color:var(--dim);font-size:.6rem;border-top:1px solid var(--border);position:relative;z-index:1}
footer a{color:var(--accent);text-decoration:none;transition:color .2s}
footer a:hover{color:var(--hot)}

@keyframes blink{0%,100%{opacity:1}50%{opacity:.3}}
@keyframes pulse{0%,100%{box-shadow:0 0 8px var(--glow)}50%{box-shadow:0 0 20px var(--glow)}}
@keyframes float{0%,100%{transform:translateX(-50%) translateY(0)}50%{transform:translateX(-50%) translateY(-8px)}}
@keyframes fadeUp{from{opacity:0;transform:translateY(20px)}to{opacity:1;transform:translateY(0)}}
.fade{animation:fadeUp .6s ease forwards;opacity:0}
.f1{animation-delay:.1s}.f2{animation-delay:.2s}.f3{animation-delay:.3s}.f4{animation-delay:.4s}.f5{animation-delay:.5s}.f6{animation-delay:.6s}

@media(max-width:768px){
  .grid{grid-template-columns:1fr}
  .stats-row{gap:24px}
  .hero{padding:60px 20px 40px;min-height:auto}
  .container{padding:0 16px 60px}
  .rev-grid{grid-template-columns:1fr}
  .steps{flex-direction:column;gap:12px;align-items:flex-start}
  .steps::before{display:none}
  .step{flex-direction:row;gap:12px}
}
</style>
</head>
<body>
<canvas id="particles"></canvas>
<div class="cursor-dot" id="cursorDot"></div>

<div class="hero">
<div class="hero-grid"></div>
<div style="position:relative;z-index:1">
<div class="hero-badge">Powered by Story Confidential Data Rails</div>
<div class="glitch" data-text="Phantom Brain">Phantom Brain</div>
<p class="hero-sub">Autonomous AI agent with private, monetizable intelligence.<br>Strategy encrypted. Signals tiered. Never exposed.</p>
<div class="stats-row">
<div class="stat"><div class="stat-val" id="s-sig">—</div><div class="stat-label">Signals</div></div>
<div class="stat"><div class="stat-val" id="s-wr">—</div><div class="stat-label">Win Rate</div></div>
<div class="stat"><div class="stat-val" id="s-pnl">—</div><div class="stat-label">P&L</div></div>
<div class="stat"><div class="stat-val" id="s-rev">—</div><div class="stat-label">Revenue</div></div>
</div>
</div>
<div class="scroll-hint"><span>Scroll</span></div>
</div>

<div class="container">

<!-- AGENT + REVENUE -->
<div class="grid fade f1">
<div class="card">
<h3><span class="icon">🤖</span> Agent Status</h3>
<div id="agent-card" style="color:var(--dim)">Loading...</div>
</div>
<div class="card">
<h3><span class="icon">💰</span> Revenue</h3>
<div class="rev-grid" id="rev-grid"></div>
</div>
</div>

<!-- LIVE SIGNALS -->
<span class="section-label">01 — Live Signals</span>
<div class="card fade f2" style="margin-bottom:40px;overflow-x:auto">
<table>
<thead><tr><th>Token</th><th>Dir</th><th>Entry</th><th>SL</th><th>TP</th><th>Conf</th><th>Tier</th><th>Status</th><th>Time</th></tr></thead>
<tbody id="sig-body"></tbody>
</table>
</div>

<!-- MARKETPLACE -->
<span class="section-label">02 — Marketplace</span>
<div class="card fade f3" style="margin-bottom:40px;overflow-x:auto">
<table>
<thead><tr><th>Tier</th><th>Token</th><th>Direction</th><th>Price</th><th>Buyers</th><th></th></tr></thead>
<tbody id="mkt-body"></tbody>
</table>
</div>

<!-- DEALS + VAULTS -->
<div class="grid fade f4">
<div class="card">
<h3><span class="icon">🤝</span> A2A Negotiation</h3>
<div id="deals-box"></div>
</div>
<div class="card">
<h3><span class="icon">🔒</span> Vault Explorer</h3>
<div id="vaults-box"></div>
</div>
</div>

<!-- PROGRESS -->
<span class="section-label">03 — Build Pipeline</span>
<div class="card fade f5" style="margin-bottom:40px">
<div class="steps">
<div class="step done"><div class="step-dot">✓</div><div class="step-label">CDR SDK</div></div>
<div class="step done"><div class="step-dot">✓</div><div class="step-label">Vault Manager</div></div>
<div class="step done"><div class="step-dot">✓</div><div class="step-label">Agent Core</div></div>
<div class="step done"><div class="step-dot">✓</div><div class="step-label">Marketplace</div></div>
<div class="step active"><div class="step-dot">5</div><div class="step-label">Deploy Contract</div></div>
<div class="step"><div class="step-dot">6</div><div class="step-label">Live Demo</div></div>
</div>
</div>

</div>

<footer>Phantom Brain &mdash; <a href="https://build.usecdr.dev" target="_blank">Story CDR Hackathon</a> &middot; <a href="https://github.com/gieskuy5/phantom-brain" target="_blank">GitHub</a> &middot; May 2026</footer>

<script>
/* PARTICLES */
(function(){
  var c=document.getElementById('particles'),x=c.getContext('2d'),pts=[],mx=-1e3,my=-1e3;
  function rs(){c.width=window.innerWidth;c.height=window.innerHeight}rs();
  window.addEventListener('resize',rs);
  function P(){this.x=Math.random()*c.width;this.y=Math.random()*c.height;this.vx=(Math.random()-.5)*.3;this.vy=(Math.random()-.5)*.3;this.r=Math.random()*1.5+.5;this.o=Math.random()*.4+.1}
  for(var i=0;i<50;i++)pts.push(new P());
  function draw(){
    x.clearRect(0,0,c.width,c.height);
    for(var i=0;i<pts.length;i++){
      var p=pts[i];p.x+=p.vx;p.y+=p.vy;
      if(p.x<0)p.x=c.width;if(p.x>c.width)p.x=0;if(p.y<0)p.y=c.height;if(p.y>c.height)p.y=0;
      var dx=p.x-mx,dy=p.y-my,d=Math.sqrt(dx*dx+dy*dy);
      if(d<120){p.x+=dx*.01;p.y+=dy*.01}
      x.beginPath();x.arc(p.x,p.y,p.r,0,Math.PI*2);
      x.fillStyle='rgba(136,176,208,'+p.o+')';x.fill();
      for(var j=i+1;j<pts.length;j++){
        var p2=pts[j],dd=Math.sqrt(Math.pow(p.x-p2.x,2)+Math.pow(p.y-p2.y,2));
        if(dd<150){x.beginPath();x.moveTo(p.x,p.y);x.lineTo(p2.x,p2.y);x.strokeStyle='rgba(136,176,208,'+(0.06*(1-dd/150))+')';x.lineWidth=.5;x.stroke()}
      }
    }
    requestAnimationFrame(draw);
  }
  draw();
  document.addEventListener('mousemove',function(e){mx=e.clientX;my=e.clientY});
})();

/* CURSOR TRAIL */
(function(){
  var dot=document.getElementById('cursorDot'),mx=0,my=0,dx=0,dy=0;
  document.addEventListener('mousemove',function(e){mx=e.clientX;my=e.clientY});
  function anim(){dx+=(mx-dx)*.15;dy+=(my-dy)*.15;dot.style.left=dx-2+'px';dot.style.top=dy-2+'px';requestAnimationFrame(anim)}anim();
})();

/* DATA */
function j(u,cb){var r=new XMLHttpRequest();r.open('GET',u);r.onload=function(){if(r.status===200)cb(JSON.parse(r.responseText))};r.send()}
function b(t,c){return '<span class="badge b-'+c+'">'+t+'</span>'}
function cb(v){var col=v>75?'var(--green)':v>60?'var(--accent)':'var(--red)';return '<span class="cbar"><span class="cfill" style="width:'+v+'%;background:'+col+'"></span></span> '+v+'%'}

j('/api/agent',function(a){
  document.getElementById('s-sig').textContent=a.totalSignals;
  document.getElementById('s-wr').textContent=a.winRate+'%';
  document.getElementById('s-pnl').textContent='+'+a.pnl+'%';
  document.getElementById('agent-card').innerHTML=
    '<div style="margin-bottom:14px"><strong style="color:var(--bright);font-size:.85rem">'+a.name+'</strong></div>'+
    '<div style="margin-bottom:10px">wallet › <span style="color:var(--accent)">'+a.wallet.substring(0,6)+'...'+a.wallet.slice(-4)+'</span></div>'+
    '<div style="margin-bottom:10px">strategy › <span style="color:var(--hot)">'+a.strategy+'</span></div>'+
    '<div style="margin-bottom:10px">indicators › '+a.indicators.join(' · ')+'</div>'+
    '<div>vault › <span style="color:var(--dim)">'+a.strategyVault.substring(0,8)+'...</span></div>';
});

j('/api/signals',function(s){
  var h='';
  for(var i=0;i<s.length;i++){
    var v=s[i];
    h+='<tr><td><strong>'+v.token+'</strong></td><td>'+b(v.dir,v.dir.toLowerCase())+'</td><td>$'+v.entry.toLocaleString()+'</td><td>$'+v.sl.toLocaleString()+'</td><td>$'+v.tp.toLocaleString()+'</td><td>'+cb(v.conf)+'</td><td>'+b(v.tier,v.tier)+'</td><td>'+b(v.status,v.status)+'</td><td style="color:var(--dim)">'+v.time+'</td></tr>';
  }
  document.getElementById('sig-body').innerHTML=h;
});

j('/api/marketplace',function(m){
  var h='';
  for(var i=0;i<m.length;i++){
    var v=m[i];
    h+='<tr><td>'+b(v.tier,v.tier)+'</td><td><strong>'+v.token+'</strong></td><td>'+b(v.dir,v.dir.toLowerCase())+'</td><td style="color:var(--accent)">'+v.price+'</td><td>'+v.buyers+'</td><td><button class="btn" onclick="alert(\'Connect wallet\')">Buy</button></td></tr>';
  }
  document.getElementById('mkt-body').innerHTML=h;
});

j('/api/deals',function(d){
  var h='';
  for(var i=0;i<d.length;i++){
    var v=d[i];
    h+='<div class="deal"><div class="deal-header"><span style="color:var(--text)">'+v.cp+'</span>'+b(v.status,v.status)+'</div><div class="deal-meta">'+b(v.tier,v.tier)+'<span>Proposed: '+v.prop+'</span><span>Counter: '+v.counter+'</span><span>'+v.msgs+' msgs</span></div></div>';
  }
  document.getElementById('deals-box').innerHTML=h||'<div style="color:var(--dim)">No active deals</div>';
});

j('/api/vaults',function(v){
  var h='';
  for(var i=0;i<v.length;i++){
    var t=v[i];
    h+='<div class="vrow"><div><div class="vuuid">'+t.uuid+'</div><div style="margin-top:6px">'+b(t.type,t.tier)+' '+b(t.tier,t.tier)+' <span style="color:var(--dim);font-size:.55rem">'+t.size+'</span></div></div><div style="display:flex;gap:10px;align-items:center"><span style="color:var(--dim);font-size:.55rem">'+t.created+'</span><button class="btn">Read</button></div></div>';
  }
  document.getElementById('vaults-box').innerHTML=h;
});

j('/api/revenue',function(r){
  document.getElementById('s-rev').textContent=r.total;
  var items=[{v:r.total,l:'Total Revenue'},{v:r.signalSales,l:'Signal Sales'},{v:r.brainSubs,l:'Brain Subs'},{v:r.a2aDeals,l:'A2A Deals'}];
  var h='';
  for(var i=0;i<items.length;i++){h+='<div class="rev-item"><div class="rev-val">'+items[i].v+'</div><div class="rev-label">'+items[i].l+'</div></div>'}
  document.getElementById('rev-grid').innerHTML=h;
});
</script>
</body>
</html>"""
