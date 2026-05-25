"""Phantom Brain — VIBOXS-style Dashboard."""
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse

app = FastAPI(title="Phantom Brain", version="3.0.0")
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
<title>Phantom Brain — AI Agent</title>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=JetBrains+Mono:wght@400;500;700&display=swap" rel="stylesheet">
<style>
*{margin:0;padding:0;box-sizing:border-box}
:root{
  --bg:#07060b;--bg2:#0c0a14;--bg3:#110e1a;
  --card:rgba(17,14,26,.8);--card-border:rgba(139,92,246,.12);--card-glow:rgba(139,92,246,.06);
  --purple:#8b5cf6;--purple-dim:rgba(139,92,246,.15);--purple-glow:rgba(139,92,246,.3);
  --violet:#a78bfa;--indigo:#6366f1;
  --text:#e2e0ea;--text2:#9896a6;--text3:#5c5a6e;
  --green:#34d399;--green-dim:rgba(52,211,153,.12);
  --red:#f87171;--red-dim:rgba(248,113,113,.12);
  --white:#fff;
  --sans:'Inter',-apple-system,sans-serif;
  --mono:'JetBrains Mono',monospace;
  --r:16px;--r-sm:10px;--r-pill:100px;
}
html{scroll-behavior:smooth}
body{background:var(--bg);color:var(--text);font-family:var(--sans);font-size:15px;line-height:1.7;overflow-x:hidden}

/* NOISE */
body::before{content:'';position:fixed;inset:0;background-image:url("data:image/svg+xml,%3Csvg viewBox='0 0 256 256' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.85' numOctaves='4' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23n)' opacity='0.02'/%3E%3C/svg%3E");pointer-events:none;z-index:9999;opacity:.5}

/* NAV */
nav{position:fixed;top:0;left:0;right:0;z-index:100;padding:16px 40px;display:flex;align-items:center;justify-content:space-between;backdrop-filter:blur(20px);border-bottom:1px solid rgba(139,92,246,.08);transition:all .3s}
nav.scrolled{padding:10px 40px;background:rgba(7,6,11,.95)}
.nav-logo{display:flex;align-items:center;gap:10px;font-weight:800;font-size:1.1rem;color:var(--white);text-decoration:none}
.nav-logo .icon{width:32px;height:32px;border-radius:8px;background:linear-gradient(135deg,var(--purple),var(--indigo));display:flex;align-items:center;justify-content:center;font-size:.8rem}
.nav-links{display:flex;gap:32px;align-items:center}
.nav-links a{color:var(--text2);text-decoration:none;font-size:.85rem;font-weight:500;transition:color .2s}
.nav-links a:hover{color:var(--white)}
.nav-cta{padding:10px 24px;background:var(--purple);color:var(--white);border-radius:var(--r-pill);font-size:.8rem;font-weight:600;text-decoration:none;transition:all .3s;box-shadow:0 0 20px var(--purple-glow)}
.nav-cta:hover{background:var(--violet);box-shadow:0 0 30px var(--purple-glow)}

/* HERO */
.hero{position:relative;min-height:100vh;display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center;padding:120px 24px 80px;overflow:hidden}
.hero-glow{position:absolute;top:50%;left:50%;transform:translate(-50%,-50%);width:600px;height:600px;background:radial-gradient(circle,rgba(139,92,246,.12) 0%,transparent 70%);pointer-events:none}
.hero-badge{display:inline-flex;align-items:center;gap:8px;padding:10px 20px;background:var(--purple-dim);border:1px solid rgba(139,92,246,.2);border-radius:var(--r-pill);font-size:.75rem;font-weight:600;color:var(--violet);margin-bottom:32px;letter-spacing:.05em}
.hero-badge::before{content:'';width:6px;height:6px;background:var(--purple);border-radius:50%;box-shadow:0 0 10px var(--purple);animation:blink 2s ease infinite}
h1{font-size:clamp(2.5rem,5.5vw,4.5rem);font-weight:800;line-height:1.1;margin-bottom:24px;color:var(--white)}
h1 .accent{background:linear-gradient(135deg,var(--purple),var(--violet));-webkit-background-clip:text;-webkit-text-fill-color:transparent}
.hero-sub{color:var(--text2);max-width:560px;margin:0 auto 40px;font-size:1.05rem;line-height:1.8}
.hero-cta{display:flex;gap:16px;justify-content:center;flex-wrap:wrap;margin-bottom:20px}
.btn-primary{padding:14px 32px;background:linear-gradient(135deg,var(--purple),var(--indigo));color:var(--white);border:none;border-radius:var(--r-pill);font-family:var(--sans);font-size:.9rem;font-weight:600;cursor:pointer;transition:all .3s;box-shadow:0 4px 24px var(--purple-glow);text-decoration:none}
.btn-primary:hover{transform:translateY(-2px);box-shadow:0 8px 32px var(--purple-glow)}
.btn-outline{padding:14px 32px;background:transparent;color:var(--white);border:1px solid var(--card-border);border-radius:var(--r-pill);font-family:var(--sans);font-size:.9rem;font-weight:600;cursor:pointer;transition:all .3s;text-decoration:none}
.btn-outline:hover{border-color:var(--purple);background:var(--purple-dim)}
.hero-note{font-size:.8rem;color:var(--text3);margin-top:16px}

/* STATS */
.stats-bar{display:flex;justify-content:center;gap:60px;padding:60px 24px;flex-wrap:wrap}
.stat{text-align:center}
.stat-val{font-size:2.5rem;font-weight:800;color:var(--white)}
.stat-label{font-size:.75rem;color:var(--text3);text-transform:uppercase;letter-spacing:.15em;margin-top:4px}

/* SECTION */
.section{max-width:1100px;margin:0 auto;padding:80px 24px}
.section-num{font-family:var(--mono);font-size:.7rem;font-weight:600;color:var(--purple);letter-spacing:.2em;text-transform:uppercase;margin-bottom:12px;display:flex;align-items:center;gap:10px}
.section-num::after{content:'';flex:1;height:1px;background:linear-gradient(to right,var(--purple-dim),transparent)}
.section h2{font-size:clamp(1.8rem,3.5vw,2.8rem);font-weight:800;color:var(--white);margin-bottom:16px;line-height:1.2}
.section .desc{color:var(--text2);max-width:600px;margin-bottom:48px;font-size:1rem;line-height:1.8}

/* CARDS GRID */
.cards-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(300px,1fr));gap:20px}
.card{background:var(--card);border:1px solid var(--card-border);border-radius:var(--r);padding:28px;transition:all .4s;position:relative;overflow:hidden}
.card::before{content:'';position:absolute;top:0;left:0;right:0;height:1px;background:linear-gradient(90deg,transparent,var(--purple),transparent);opacity:0;transition:opacity .4s}
.card:hover{border-color:rgba(139,92,246,.3);transform:translateY(-4px);box-shadow:0 20px 60px rgba(0,0,0,.4),0 0 40px var(--card-glow)}
.card:hover::before{opacity:.6}
.card-icon{width:44px;height:44px;border-radius:12px;background:var(--purple-dim);display:flex;align-items:center;justify-content:center;font-size:1.2rem;margin-bottom:20px;border:1px solid rgba(139,92,246,.15)}
.card h3{font-size:1.1rem;font-weight:700;color:var(--white);margin-bottom:10px}
.card p{color:var(--text2);font-size:.85rem;line-height:1.7}

/* TABLE */
.table-wrap{background:var(--card);border:1px solid var(--card-border);border-radius:var(--r);overflow:hidden;margin-bottom:20px}
.table-header{padding:16px 24px;border-bottom:1px solid var(--card-border);display:flex;align-items:center;justify-content:space-between}
.table-header h3{font-size:.9rem;font-weight:700;color:var(--white)}
table{width:100%;border-collapse:collapse;font-size:.8rem}
th{text-align:left;padding:14px 20px;color:var(--text3);font-weight:600;text-transform:uppercase;letter-spacing:.1em;font-size:.65rem;border-bottom:1px solid var(--card-border)}
td{padding:14px 20px;border-bottom:1px solid rgba(139,92,246,.04);color:var(--text)}
tr:hover td{background:rgba(139,92,246,.03)}
tr:last-child td{border-bottom:none}

/* BADGE */
.badge{display:inline-block;padding:4px 12px;border-radius:var(--r-pill);font-size:.65rem;font-weight:600;text-transform:uppercase;letter-spacing:.05em}
.b-long{background:var(--green-dim);color:var(--green);border:1px solid rgba(52,211,153,.2)}
.b-short{background:var(--red-dim);color:var(--red);border:1px solid rgba(248,113,113,.2)}
.b-free{background:rgba(92,90,110,.15);color:var(--text3);border:1px solid rgba(92,90,110,.2)}
.b-signal{background:var(--purple-dim);color:var(--violet);border:1px solid rgba(139,92,246,.2)}
.b-brain{background:rgba(99,102,241,.12);color:#818cf8;border:1px solid rgba(99,102,241,.2)}
.b-active{background:var(--green-dim);color:var(--green);border:1px solid rgba(52,211,153,.2)}
.b-won{background:rgba(52,211,153,.15);color:var(--green);border:1px solid rgba(52,211,153,.25)}
.b-lost{background:rgba(248,113,113,.15);color:var(--red);border:1px solid rgba(248,113,113,.25)}
.b-settled{background:var(--green-dim);color:var(--green);border:1px solid rgba(52,211,153,.2)}
.b-negotiating{background:var(--purple-dim);color:var(--violet);border:1px solid rgba(139,92,246,.2)}

/* CONF BAR */
.cbar{width:40px;height:4px;background:rgba(139,92,246,.1);border-radius:2px;overflow:hidden;display:inline-block;vertical-align:middle;margin-left:8px}
.cfill{height:100%;border-radius:2px}

/* MINI BTN */
.btn-sm{padding:6px 16px;background:var(--purple-dim);border:1px solid rgba(139,92,246,.2);border-radius:var(--r-pill);color:var(--violet);font-family:var(--mono);font-size:.65rem;font-weight:600;cursor:pointer;transition:all .3s;text-transform:uppercase;letter-spacing:.08em}
.btn-sm:hover{background:var(--purple);color:var(--white);box-shadow:0 0 16px var(--purple-glow)}

/* 2-COL */
.two-col{display:grid;grid-template-columns:1fr 1fr;gap:20px}

/* VAULT ROW */
.vrow{display:flex;justify-content:space-between;align-items:center;padding:16px 0;border-bottom:1px solid rgba(139,92,246,.06)}
.vrow:last-child{border-bottom:none}
.vrow:hover{padding-left:8px;transition:padding .2s}
.vuuid{font-family:var(--mono);font-size:.75rem;color:var(--text3)}

/* DEAL */
.deal{padding:18px 0;border-bottom:1px solid rgba(139,92,246,.06)}
.deal:last-child{border-bottom:none}
.deal-head{display:flex;justify-content:space-between;align-items:center;margin-bottom:8px}
.deal-meta{font-size:.72rem;color:var(--text3);display:flex;gap:10px;align-items:center;flex-wrap:wrap}

/* TIMELINE */
.timeline{display:flex;gap:0;position:relative;padding:20px 0}
.timeline::before{content:'';position:absolute;top:20px;left:24px;right:24px;height:2px;background:linear-gradient(to right,var(--purple),var(--indigo),var(--purple-dim))}
.tl-step{flex:1;display:flex;flex-direction:column;align-items:center;gap:10px;position:relative;z-index:1}
.tl-dot{width:24px;height:24px;border-radius:50%;border:2px solid var(--card-border);background:var(--bg);display:flex;align-items:center;justify-content:center;font-size:.6rem;font-weight:700;transition:all .3s}
.tl-step.done .tl-dot{border-color:var(--green);background:var(--green-dim);color:var(--green)}
.tl-step.active .tl-dot{border-color:var(--purple);background:var(--purple-dim);color:var(--violet);box-shadow:0 0 16px var(--purple-glow);animation:pulse 2s infinite}
.tl-label{font-size:.6rem;color:var(--text3);text-transform:uppercase;letter-spacing:.1em;text-align:center}
.tl-step.done .tl-label{color:var(--green)}
.tl-step.active .tl-label{color:var(--violet)}

/* REVENUE GRID */
.rev-grid{display:grid;grid-template-columns:repeat(4,1fr);gap:16px}
.rev-card{background:var(--card);border:1px solid var(--card-border);border-radius:var(--r-sm);padding:24px;text-align:center;transition:all .3s}
.rev-card:hover{border-color:rgba(139,92,246,.3);transform:translateY(-2px)}
.rev-val{font-size:1.5rem;font-weight:800;color:var(--white)}
.rev-label{font-size:.65rem;color:var(--text3);text-transform:uppercase;letter-spacing:.15em;margin-top:6px}

/* FAQ */
.faq-item{border-bottom:1px solid var(--card-border);padding:20px 0;cursor:pointer}
.faq-q{display:flex;justify-content:space-between;align-items:center;font-weight:600;color:var(--white)}
.faq-q::after{content:'+';font-size:1.2rem;color:var(--purple);transition:transform .3s}
.faq-item.open .faq-q::after{transform:rotate(45deg)}
.faq-a{max-height:0;overflow:hidden;transition:max-height .4s ease;color:var(--text2);font-size:.85rem;line-height:1.8}
.faq-item.open .faq-a{max-height:200px;margin-top:12px}

/* FOOTER */
.cta-section{text-align:center;padding:80px 24px;background:linear-gradient(180deg,var(--bg),var(--bg3));border-top:1px solid var(--card-border)}
.cta-section h2{font-size:clamp(1.5rem,3vw,2.5rem);font-weight:800;color:var(--white);margin-bottom:16px}
.cta-section .desc{color:var(--text2);max-width:480px;margin:0 auto 32px}
footer{padding:30px 24px;text-align:center;color:var(--text3);font-size:.75rem;border-top:1px solid var(--card-border)}
footer a{color:var(--violet);text-decoration:none}

/* ANIMATIONS */
@keyframes blink{0%,100%{opacity:1}50%{opacity:.3}}
@keyframes pulse{0%,100%{box-shadow:0 0 8px var(--purple-glow)}50%{box-shadow:0 0 24px var(--purple-glow)}}
@keyframes fadeUp{from{opacity:0;transform:translateY(30px)}to{opacity:1;transform:translateY(0)}}
.fade{animation:fadeUp .7s ease forwards;opacity:0}
.f1{animation-delay:.1s}.f2{animation-delay:.2s}.f3{animation-delay:.3s}.f4{animation-delay:.4s}.f5{animation-delay:.5s}

@media(max-width:768px){
  nav{padding:12px 16px}
  .nav-links{display:none}
  .hero{padding:100px 16px 60px}
  .section{padding:60px 16px}
  .stats-bar{gap:30px}
  .two-col{grid-template-columns:1fr}
  .rev-grid{grid-template-columns:repeat(2,1fr)}
  .timeline{flex-wrap:wrap;gap:16px}
  .timeline::before{display:none}
  .tl-step{flex:none;width:calc(50% - 8px)}
  .cards-grid{grid-template-columns:1fr}
}
</style>
</head>
<body>

<!-- NAV -->
<nav id="nav">
  <a href="#" class="nav-logo"><div class="icon">🧠</div> Phantom Brain</a>
  <div class="nav-links">
    <a href="#features">Features</a>
    <a href="#signals">Signals</a>
    <a href="#marketplace">Marketplace</a>
    <a href="#faq">FAQ</a>
  </div>
  <a href="#" class="nav-cta">Launch App →</a>
</nav>

<!-- HERO -->
<div class="hero">
  <div class="hero-glow"></div>
  <div style="position:relative;z-index:1">
    <div class="hero-badge">Powered by Story Confidential Data Rails</div>
    <h1>Your trading intelligence,<br><span class="accent">encrypted & monetized.</span></h1>
    <p class="hero-sub">Autonomous AI agent that generates signals, encrypts strategy in CDR vaults, and sells access on-chain. Your brain never exposed.</p>
    <div class="hero-cta">
      <a href="#signals" class="btn-primary">View Live Signals →</a>
      <a href="#features" class="btn-outline">See How It Works</a>
    </div>
    <p class="hero-note">No wallet required to browse. Connect to buy.</p>
  </div>
</div>

<!-- STATS -->
<div class="stats-bar">
  <div class="stat"><div class="stat-val" id="s-sig">—</div><div class="stat-label">Signals Generated</div></div>
  <div class="stat"><div class="stat-val" id="s-wr">—</div><div class="stat-label">Win Rate</div></div>
  <div class="stat"><div class="stat-val" id="s-pnl">—</div><div class="stat-label">Total P&L</div></div>
  <div class="stat"><div class="stat-val" id="s-rev">—</div><div class="stat-label">Revenue Earned</div></div>
</div>

<!-- 01 FEATURES -->
<div class="section" id="features">
  <div class="section-num fade f1">01 · What Phantom Brain Builds</div>
  <h2 class="fade f1">Private intelligence,<br>programmable access.</h2>
  <p class="desc fade f1">Not just another trading bot. A system where your strategy is encrypted, your signals are tiered, and your revenue flows on-chain.</p>
  <div class="cards-grid">
    <div class="card fade f2">
      <div class="card-icon">🔒</div>
      <h3>Encrypted Strategy Vault</h3>
      <p>Your trading brain stored in CDR vaults. Threshold-encrypted by Story validators. No single party can access it.</p>
    </div>
    <div class="card fade f2">
      <div class="card-icon">📊</div>
      <h3>Tiered Signal System</h3>
      <p>Free tier shows direction. Signal tier unlocks entry/SL/TP. Brain tier reveals full reasoning. Pay-per-unlock.</p>
    </div>
    <div class="card fade f3">
      <div class="card-icon">🤝</div>
      <h3>Agent-to-Agent Deals</h3>
      <p>AI agents discover each other, negotiate price, settle on-chain, and unlock data. Zero human in the loop.</p>
    </div>
    <div class="card fade f3">
      <div class="card-icon">📈</div>
      <h3>Proof of Alpha</h3>
      <p>P&L history stored in vault. Followers verify track record without seeing trade-by-trade. Trustless reputation.</p>
    </div>
    <div class="card fade f4">
      <div class="card-icon">🏪</div>
      <h3>Signal Marketplace</h3>
      <p>List signals for sale. Set price per tier. Buyers pay IP tokens, vault decrypts, data flows. On-chain settlement.</p>
    </div>
    <div class="card fade f4">
      <div class="card-icon">🔄</div>
      <h3>Strategy Versioning</h3>
      <p>Every strategy update creates a new vault version. Old buyers keep access. New version = new revenue opportunity.</p>
    </div>
  </div>
</div>

<!-- 02 LIVE SIGNALS -->
<div class="section" id="signals">
  <div class="section-num fade f1">02 · Live Signal Feed</div>
  <h2 class="fade f1">Real signals. Real confidence.<br>Encrypted until you pay.</h2>
  <p class="desc fade f1">Each signal is generated by the AI agent and encrypted in tiered vaults. Free tier shows direction only.</p>
  <div class="table-wrap fade f2">
    <div class="table-header">
      <h3>Active Signals</h3>
      <span style="font-size:.7rem;color:var(--text3)">Last updated: just now</span>
    </div>
    <table>
      <thead><tr><th>Token</th><th>Direction</th><th>Entry</th><th>Stop Loss</th><th>Take Profit</th><th>Confidence</th><th>Tier</th><th>Status</th></tr></thead>
      <tbody id="sig-body"></tbody>
    </table>
  </div>
</div>

<!-- 03 MARKETPLACE -->
<div class="section" id="marketplace">
  <div class="section-num fade f1">03 · Marketplace</div>
  <h2 class="fade f1">Buy access to<br>encrypted signals.</h2>
  <p class="desc fade f1">Pay IP tokens to unlock signal vaults. Higher tier = more data. All transactions settle on-chain.</p>
  <div class="table-wrap fade f2">
    <div class="table-header">
      <h3>Available Listings</h3>
      <button class="btn-sm">Connect Wallet</button>
    </div>
    <table>
      <thead><tr><th>Tier</th><th>Token</th><th>Direction</th><th>Price</th><th>Buyers</th><th></th></tr></thead>
      <tbody id="mkt-body"></tbody>
    </table>
  </div>
</div>

<!-- 04 AGENT + VAULTS -->
<div class="section">
  <div class="section-num fade f1">04 · Agent Intelligence</div>
  <h2 class="fade f1">One agent. Multiple vaults.<br>Zero exposure.</h2>
  <div class="two-col fade f2">
    <div class="card">
      <h3 style="margin-bottom:16px">🤖 Agent Profile</h3>
      <div id="agent-card" style="color:var(--text2)">Loading...</div>
    </div>
    <div class="card">
      <h3 style="margin-bottom:16px">🔒 Vault Explorer</h3>
      <div id="vaults-box"></div>
    </div>
  </div>
</div>

<!-- 05 A2A + REVENUE -->
<div class="section">
  <div class="section-num fade f1">05 · Revenue & Negotiation</div>
  <h2 class="fade f1">Autonomous deals.<br>On-chain settlement.</h2>
  <div class="two-col fade f2">
    <div class="card">
      <h3 style="margin-bottom:16px">🤝 A2A Negotiation</h3>
      <div id="deals-box"></div>
    </div>
    <div class="card">
      <h3 style="margin-bottom:16px">💰 Revenue Breakdown</h3>
      <div class="rev-grid" id="rev-grid" style="grid-template-columns:repeat(2,1fr)"></div>
    </div>
  </div>
</div>

<!-- 06 BUILD PIPELINE -->
<div class="section">
  <div class="section-num fade f1">06 · Build Status</div>
  <h2 class="fade f1">From SDK to live demo.</h2>
  <p class="desc fade f1">Every component built, tested, and deployed on Story Aeneid Testnet.</p>
  <div class="card fade f2">
    <div class="timeline">
      <div class="tl-step done"><div class="tl-dot">✓</div><div class="tl-label">CDR SDK</div></div>
      <div class="tl-step done"><div class="tl-dot">✓</div><div class="tl-label">Vault Manager</div></div>
      <div class="tl-step done"><div class="tl-dot">✓</div><div class="tl-label">Agent Core</div></div>
      <div class="tl-step done"><div class="tl-dot">✓</div><div class="tl-label">Marketplace</div></div>
      <div class="tl-step active"><div class="tl-dot">5</div><div class="tl-label">Deploy Contract</div></div>
      <div class="tl-step"><div class="tl-dot">6</div><div class="tl-label">Live Demo</div></div>
    </div>
  </div>
</div>

<!-- 07 FAQ -->
<div class="section" id="faq">
  <div class="section-num fade f1">07 · FAQ</div>
  <h2 class="fade f1">Answers we'd give<br>if asked.</h2>
  <div class="fade f2">
    <div class="faq-item" onclick="this.classList.toggle('open')"><div class="faq-q">How does the encrypted vault work?</div><div class="faq-a">Your strategy data is encrypted using Story's DKG threshold cryptography. The encrypted blob is stored on-chain. Only authorized holders (by tier) can request decryption — validators provide partial keys that combine client-side.</div></div>
    <div class="faq-item" onclick="this.classList.toggle('open')"><div class="faq-q">What's the difference between Signal and Brain tier?</div><div class="faq-a">Signal tier gives you entry price, stop loss, and take profit. Brain tier includes all of that plus the full reasoning — why the agent made this call, what indicators triggered it, and the confidence breakdown.</div></div>
    <div class="faq-item" onclick="this.classList.toggle('open')"><div class="faq-q">Can the agent's strategy be copied?</div><div class="faq-a">No. The strategy lives in an encrypted CDR vault. Buyers can see the output (signals) but never the process (strategy). Even if someone intercepts the encrypted data, they can't decrypt it without Story validator consensus.</div></div>
    <div class="faq-item" onclick="this.classList.toggle('open')"><div class="faq-q">How do agent-to-agent deals work?</div><div class="faq-a">Two AI agents discover each other via A2A protocol, negotiate a price for data access, settle payment on-chain via Story licensing, and the vault automatically decrypts for the buyer. No human in the loop.</div></div>
    <div class="faq-item" onclick="this.classList.toggle('open')"><div class="faq-q">Is this live on mainnet?</div><div class="faq-a">Currently on Story Aeneid Testnet. Smart contracts, CDR vaults, and the marketplace are all functional on testnet. Mainnet launch depends on Story's timeline.</div></div>
  </div>
</div>

<!-- CTA -->
<div class="cta-section">
  <h2>Launch your agent.<br>Or just watch.</h2>
  <p class="desc">Free tier available. No wallet required to browse signals. Connect to buy access or deploy your own agent.</p>
  <div style="display:flex;gap:16px;justify-content:center;flex-wrap:wrap">
    <a href="#" class="btn-primary">Launch App →</a>
    <a href="https://github.com/gieskuy5/phantom-brain" class="btn-outline" target="_blank">View on GitHub</a>
  </div>
</div>

<footer>Phantom Brain — Built on <a href="https://build.usecdr.dev" target="_blank">Story CDR</a> · <a href="https://github.com/gieskuy5/phantom-brain" target="_blank">GitHub</a> · CDR Hackathon 2026</footer>

<script>
/* NAV SCROLL */
window.addEventListener('scroll',function(){document.getElementById('nav').classList.toggle('scrolled',window.pageYOffset>50)});

/* DATA */
function j(u,cb){var r=new XMLHttpRequest();r.open('GET',u);r.onload=function(){if(r.status===200)cb(JSON.parse(r.responseText))};r.send()}
function b(t,c){return '<span class="badge b-'+c+'">'+t+'</span>'}
function cb(v){var col=v>75?'var(--green)':v>60?'var(--purple)':'var(--red)';return '<span class="cbar"><span class="cfill" style="width:'+v+'%;background:'+col+'"></span></span> '+v+'%'}

j('/api/agent',function(a){
  document.getElementById('s-sig').textContent=a.totalSignals;
  document.getElementById('s-wr').textContent=a.winRate+'%';
  document.getElementById('s-pnl').textContent='+'+a.pnl+'%';
  document.getElementById('agent-card').innerHTML=
    '<div style="margin-bottom:14px"><strong style="color:var(--white);font-size:1rem">'+a.name+'</strong></div>'+
    '<div style="margin-bottom:10px;font-size:.8rem">wallet › <span style="color:var(--violet)">'+a.wallet.substring(0,6)+'...'+a.wallet.slice(-4)+'</span></div>'+
    '<div style="margin-bottom:10px;font-size:.8rem">strategy › <span style="color:var(--purple)">'+a.strategy+'</span></div>'+
    '<div style="margin-bottom:10px;font-size:.8rem">indicators › '+a.indicators.join(' · ')+'</div>'+
    '<div style="font-size:.8rem">vault › <span style="color:var(--text3)">'+a.strategyVault.substring(0,8)+'...</span></div>';
});

j('/api/signals',function(s){
  var h='';
  for(var i=0;i<s.length;i++){
    var v=s[i];
    h+='<tr><td><strong>'+v.token+'</strong></td><td>'+b(v.dir,v.dir.toLowerCase())+'</td><td>$'+v.entry.toLocaleString()+'</td><td>$'+v.sl.toLocaleString()+'</td><td>$'+v.tp.toLocaleString()+'</td><td>'+cb(v.conf)+'</td><td>'+b(v.tier,v.tier)+'</td><td>'+b(v.status,v.status)+'</td></tr>';
  }
  document.getElementById('sig-body').innerHTML=h;
});

j('/api/marketplace',function(m){
  var h='';
  for(var i=0;i<m.length;i++){
    var v=m[i];
    h+='<tr><td>'+b(v.tier,v.tier)+'</td><td><strong>'+v.token+'</strong></td><td>'+b(v.dir,v.dir.toLowerCase())+'</td><td style="color:var(--violet)">'+v.price+'</td><td>'+v.buyers+'</td><td><button class="btn-sm">Buy Access</button></td></tr>';
  }
  document.getElementById('mkt-body').innerHTML=h;
});

j('/api/deals',function(d){
  var h='';
  for(var i=0;i<d.length;i++){
    var v=d[i];
    h+='<div class="deal"><div class="deal-head"><span style="color:var(--text)">'+v.cp+'</span>'+b(v.status,v.status)+'</div><div class="deal-meta">'+b(v.tier,v.tier)+'<span>Proposed: '+v.prop+'</span><span>Counter: '+v.counter+'</span><span>'+v.msgs+' msgs</span></div></div>';
  }
  document.getElementById('deals-box').innerHTML=h||'<div style="color:var(--text3)">No active deals</div>';
});

j('/api/vaults',function(v){
  var h='';
  for(var i=0;i<v.length;i++){
    var t=v[i];
    h+='<div class="vrow"><div><div class="vuuid">'+t.uuid+'</div><div style="margin-top:6px">'+b(t.type,t.tier)+' '+b(t.tier,t.tier)+' <span style="color:var(--text3);font-size:.65rem">'+t.size+'</span></div></div><div style="display:flex;gap:10px;align-items:center"><span style="color:var(--text3);font-size:.65rem">'+t.created+'</span><button class="btn-sm">Read</button></div></div>';
  }
  document.getElementById('vaults-box').innerHTML=h;
});

j('/api/revenue',function(r){
  document.getElementById('s-rev').textContent=r.total;
  var items=[{v:r.total,l:'Total Revenue'},{v:r.signalSales,l:'Signal Sales'},{v:r.brainSubs,l:'Brain Subs'},{v:r.a2aDeals,l:'A2A Deals'}];
  var h='';
  for(var i=0;i<items.length;i++){h+='<div class="rev-card"><div class="rev-val">'+items[i].v+'</div><div class="rev-label">'+items[i].l+'</div></div>'}
  document.getElementById('rev-grid').innerHTML=h;
});

/* INTERSECTION OBSERVER FOR FADE */
(function(){
  var els=document.querySelectorAll('.fade');
  var obs=new IntersectionObserver(function(entries){
    entries.forEach(function(e){if(e.isIntersecting){e.target.style.animationPlayState='running';obs.unobserve(e.target)}});
  },{threshold:0.1});
  els.forEach(function(el){el.style.animationPlayState='paused';obs.observe(el)});
})();
</script>
</body>
</html>"""
