"""Phantom Brain — Dashboard."""
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
import json, time, random

app = FastAPI(title="Phantom Brain", version="1.0.0")
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"])

# --- Mock Data ---
AGENT = {
    "name": "Phantom Alpha",
    "wallet": "0x69083D13C7767231EF2eAa0676F04F61b6F08a13",
    "totalSignals": 47,
    "winRate": 68.2,
    "pnl": 12.4,
    "strategyVault": "a3f2e8d1-7b4c-4e9a-b5d6-1c8f3e2a9b7d",
    "strategy": "Momentum Alpha v1",
    "indicators": ["RSI", "MACD", "Volume Profile", "Funding Rate"],
}

SIGNALS = [
    {"id": 1, "token": "ETH", "direction": "LONG", "entry": 3245, "sl": 3150, "tp": 3480, "confidence": 82, "tier": "brain", "status": "active", "time": "2m ago"},
    {"id": 2, "token": "BTC", "direction": "SHORT", "entry": 68500, "sl": 69200, "tp": 66800, "confidence": 75, "tier": "signal", "status": "active", "time": "15m ago"},
    {"id": 3, "token": "SOL", "direction": "LONG", "entry": 178, "sl": 172, "tp": 195, "confidence": 88, "tier": "brain", "status": "won", "time": "1h ago"},
    {"id": 4, "token": "ARB", "direction": "LONG", "entry": 1.12, "sl": 1.08, "tp": 1.25, "confidence": 71, "tier": "free", "status": "active", "time": "2h ago"},
    {"id": 5, "token": "AVAX", "direction": "SHORT", "entry": 42.5, "sl": 44.0, "tp": 39.0, "confidence": 69, "tier": "signal", "status": "lost", "time": "3h ago"},
]

LISTINGS = [
    {"id": 1, "tier": "signal", "token": "ETH", "direction": "LONG", "price": "0.5 IP", "buyers": 12, "vaultId": "b2a1c3d4"},
    {"id": 2, "tier": "brain", "token": "ETH", "direction": "LONG", "price": "2.0 IP", "buyers": 3, "vaultId": "e5f6g7h8"},
    {"id": 3, "tier": "signal", "token": "BTC", "direction": "SHORT", "price": "0.8 IP", "buyers": 8, "vaultId": "i9j0k1l2"},
]

DEALS = [
    {"id": 1, "counterparty": "0x3C44...93BC", "tier": "signal", "proposed": "1.0 IP", "counter": "0.7 IP", "status": "settled", "history": 3},
    {"id": 2, "counterparty": "0x7099...79C8", "tier": "brain", "proposed": "3.0 IP", "counter": "2.2 IP", "status": "negotiating", "history": 2},
]

VAULTS = [
    {"uuid": "a3f2e8d1-...", "type": "strategy", "tier": "brain", "created": "May 24", "size": "892 bytes"},
    {"uuid": "b2a1c3d4-...", "type": "signal", "tier": "signal", "created": "May 25", "size": "256 bytes"},
    {"uuid": "e5f6g7h8-...", "type": "signal", "tier": "brain", "created": "May 25", "size": "512 bytes"},
    {"uuid": "i9j0k1l2-...", "type": "proof", "tier": "free", "created": "May 25", "size": "128 bytes"},
]

REVENUE = {"total": "12.5 IP", "signalSales": "7.2 IP", "brainSubs": "4.0 IP", "a2aDeals": "1.3 IP", "totalBuyers": 23}

@app.get("/api/agent")
def get_agent(): return AGENT

@app.get("/api/signals")
def get_signals(): return SIGNALS

@app.get("/api/marketplace")
def get_marketplace(): return LISTINGS

@app.get("/api/deals")
def get_deals(): return DEALS

@app.get("/api/vaults")
def get_vaults(): return VAULTS

@app.get("/api/revenue")
def get_revenue(): return REVENUE

@app.get("/", response_class=HTMLResponse)
def index():
    return HTML_PAGE

HTML_PAGE = r"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Phantom Brain — Dashboard</title>
<link href="https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@500;700&family=JetBrains+Mono:wght@400;500;700&display=swap" rel="stylesheet">
<style>
:root{--primary:#88B0D0;--primary-glow:rgba(136,176,208,.3);--accent:#D4A574;--bg:#07090f;--bg2:#0d1117;--card:rgba(13,17,23,.6);--glass:rgba(136,176,208,.04);--text:#e8edf5;--muted:#6b7d94;--dim:#3a4a5c;--border:rgba(136,176,208,.08);--border-h:rgba(136,176,208,.2);--green:#4ade80;--red:#f87171;--purple:#a78bfa;--r:20px;--r-sm:12px;--r-pill:100px}
*{margin:0;padding:0;box-sizing:border-box}
body{background:var(--bg);color:var(--text);font-family:'JetBrains Mono',monospace;font-size:.8rem;line-height:1.6;min-height:100vh;overflow-x:hidden}
body::before{content:'';position:fixed;inset:0;background-image:url("data:image/svg+xml,%3Csvg viewBox='0 0 256 256' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.9' numOctaves='4' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23n)' opacity='0.03'/%3E%3C/svg%3E");pointer-events:none;z-index:9999;opacity:.4}
.hero{position:relative;padding:80px 40px 60px;text-center;overflow:hidden}
.hero-grid{position:absolute;inset:0;background-image:linear-gradient(rgba(136,176,208,.03) 1px,transparent 1px),linear-gradient(90deg,rgba(136,176,208,.03) 1px,transparent 1px);background-size:60px 60px;mask-image:radial-gradient(ellipse 60% 50% at 50% 50%,black 20%,transparent 70%)}
.hero-badge{display:inline-flex;align-items:center;gap:8px;padding:8px 20px;background:var(--glass);border:1px solid var(--border);border-radius:var(--r-pill);font-size:.7rem;letter-spacing:.15em;text-transform:uppercase;color:var(--muted);margin-bottom:24px;backdrop-filter:blur(10px)}
.hero-badge::before{content:'';width:6px;height:6px;background:var(--primary);border-radius:50%;box-shadow:0 0 10px var(--primary);animation:blink 2s ease infinite}
h1{font-family:'Space Grotesk',sans-serif;font-size:clamp(2rem,5vw,3.5rem);font-weight:700;background:linear-gradient(135deg,var(--primary),var(--accent));-webkit-background-clip:text;-webkit-text-fill-color:transparent;margin-bottom:12px}
.hero p{color:var(--muted);max-width:600px;margin:0 auto;font-size:.85rem}
.stats-row{display:flex;justify-content:center;gap:40px;margin-top:30px;flex-wrap:wrap}
.stat{text-align:center}
.stat-val{font-family:'Space Grotesk',sans-serif;font-size:1.5rem;font-weight:700;color:var(--primary)}
.stat-label{font-size:.65rem;color:var(--dim);text-transform:uppercase;letter-spacing:.15em;margin-top:4px}
.container{max-width:1200px;margin:0 auto;padding:0 24px 60px}
.section-label{display:inline-block;font-size:.65rem;letter-spacing:.25em;text-transform:uppercase;color:var(--primary);margin-bottom:16px;padding:6px 14px;border:1px solid rgba(136,176,208,.15);border-radius:var(--r-pill)}
.grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(340px,1fr));gap:20px;margin-bottom:40px}
.card{background:var(--card);border:1px solid var(--border);border-radius:var(--r);backdrop-filter:blur(10px);padding:24px;transition:all .4s;position:relative;overflow:hidden}
.card:hover{border-color:var(--border-h);transform:translateY(-2px);box-shadow:0 20px 60px rgba(0,0,0,.3),0 0 40px var(--primary-glow)}
.card::before{content:'';position:absolute;top:0;left:0;right:0;height:1px;background:linear-gradient(90deg,transparent,var(--primary),transparent);opacity:0;transition:opacity .4s}
.card:hover::before{opacity:.5}
.card h3{font-family:'Space Grotesk',sans-serif;font-size:1rem;margin-bottom:16px;display:flex;align-items:center;gap:8px}
.card h3 span{font-size:1.2rem}
table{width:100%;border-collapse:collapse;font-size:.7rem}
th{text-align:left;padding:8px 6px;color:var(--dim);font-weight:500;text-transform:uppercase;letter-spacing:.1em;font-size:.6rem;border-bottom:1px solid var(--border)}
td{padding:8px 6px;border-bottom:1px solid rgba(136,176,208,.04)}
tr:hover td{background:rgba(136,176,208,.02)}
.badge{display:inline-block;padding:2px 8px;border-radius:var(--r-pill);font-size:.6rem;font-weight:500;text-transform:uppercase;letter-spacing:.05em}
.badge-long{background:rgba(74,222,128,.1);color:var(--green);border:1px solid rgba(74,222,128,.2)}
.badge-short{background:rgba(248,113,113,.1);color:var(--red);border:1px solid rgba(248,113,113,.2)}
.badge-free{background:rgba(107,125,148,.1);color:var(--muted);border:1px solid rgba(107,125,148,.2)}
.badge-signal{background:rgba(136,176,208,.1);color:var(--primary);border:1px solid rgba(136,176,208,.2)}
.badge-brain{background:rgba(167,139,250,.1);color:var(--purple);border:1px solid rgba(167,139,250,.2)}
.badge-active{background:rgba(74,222,128,.1);color:var(--green);border:1px solid rgba(74,222,128,.2)}
.badge-won{background:rgba(74,222,128,.15);color:var(--green);border:1px solid rgba(74,222,128,.3)}
.badge-lost{background:rgba(248,113,113,.15);color:var(--red);border:1px solid rgba(248,113,113,.3)}
.badge-settled{background:rgba(74,222,128,.1);color:var(--green);border:1px solid rgba(74,222,128,.2)}
.badge-negotiating{background:rgba(212,165,116,.1);color:var(--accent);border:1px solid rgba(212,165,116,.2)}
.btn{display:inline-flex;align-items:center;gap:6px;padding:6px 14px;background:transparent;border:1px solid var(--border);border-radius:var(--r-pill);color:var(--primary);font-family:'JetBrains Mono',monospace;font-size:.65rem;cursor:pointer;transition:all .3s;text-transform:uppercase;letter-spacing:.1em}
.btn:hover{background:var(--primary);color:var(--bg);border-color:var(--primary);box-shadow:0 0 20px var(--primary-glow)}
.revenue-grid{display:grid;grid-template-columns:repeat(2,1fr);gap:12px}
.rev-item{padding:16px;background:var(--glass);border:1px solid var(--border);border-radius:var(--r-sm);text-align:center}
.rev-val{font-family:'Space Grotesk',sans-serif;font-size:1.3rem;font-weight:700;color:var(--primary)}
.rev-label{font-size:.6rem;color:var(--dim);text-transform:uppercase;letter-spacing:.15em;margin-top:4px}
.vault-row{display:flex;justify-content:space-between;align-items:center;padding:12px 0;border-bottom:1px solid rgba(136,176,208,.04)}
.vault-row:last-child{border-bottom:none}
.vault-uuid{font-size:.7rem;color:var(--muted)}
.vault-meta{display:flex;gap:12px;align-items:center}
.confidence-bar{width:40px;height:4px;background:var(--border);border-radius:2px;overflow:hidden;display:inline-block;vertical-align:middle;margin-left:6px}
.confidence-fill{height:100%;border-radius:2px;background:var(--green)}
footer{text-align:center;padding:40px;color:var(--dim);font-size:.65rem;border-top:1px solid var(--border)}
footer a{color:var(--primary);text-decoration:none}
@keyframes blink{0%,100%{opacity:1}50%{opacity:.3}}
@keyframes fadeUp{from{opacity:0;transform:translateY(20px)}to{opacity:1;transform:translateY(0)}}
.fade{animation:fadeUp .6s ease forwards;opacity:0}
.fade1{animation-delay:.1s}.fade2{animation-delay:.2s}.fade3{animation-delay:.3s}.fade4{animation-delay:.4s}.fade5{animation-delay:.5s}.fade6{animation-delay:.6s}
@media(max-width:768px){.grid{grid-template-columns:1fr}.stats-row{gap:20px}.hero{padding:40px 20px 30px}.container{padding:0 16px 40px}.revenue-grid{grid-template-columns:1fr}}
</style>
</head>
<body>
<div class="hero">
<div class="hero-grid"></div>
<div style="position:relative;z-index:1">
<div class="hero-badge">Powered by Story CDR</div>
<h1>🧠💀 Phantom Brain</h1>
<p>Autonomous AI Agent with Private, Monetizable Intelligence. Signals encrypted in CDR vaults. Strategy never exposed.</p>
<div class="stats-row">
<div class="stat"><div class="stat-val" id="s-signals">—</div><div class="stat-label">Signals</div></div>
<div class="stat"><div class="stat-val" id="s-winrate">—</div><div class="stat-label">Win Rate</div></div>
<div class="stat"><div class="stat-val" id="s-pnl">—</div><div class="stat-label">P&L</div></div>
<div class="stat"><div class="stat-val" id="s-revenue">—</div><div class="stat-label">Revenue</div></div>
</div>
</div>
</div>

<div class="container">
<div class="grid">
<div class="card fade fade1">
<h3><span>🤖</span> Agent Status</h3>
<div id="agent-info" style="font-size:.7rem;color:var(--muted)">Loading...</div>
</div>
<div class="card fade fade2">
<h3><span>💰</span> Revenue</h3>
<div class="revenue-grid" id="revenue-grid"></div>
</div>
</div>

<span class="section-label">01 — Live Signals</span>
<div class="card fade fade3" style="margin-bottom:40px;overflow-x:auto">
<table>
<thead><tr><th>Token</th><th>Dir</th><th>Entry</th><th>SL</th><th>TP</th><th>Conf</th><th>Tier</th><th>Status</th><th>Time</th></tr></thead>
<tbody id="signals-body"></tbody>
</table>
</div>

<span class="section-label">02 — Marketplace</span>
<div class="card fade fade4" style="margin-bottom:40px;overflow-x:auto">
<table>
<thead><tr><th>Tier</th><th>Token</th><th>Direction</th><th>Price</th><th>Buyers</th><th>Action</th></tr></thead>
<tbody id="market-body"></tbody>
</table>
</div>

<div class="grid">
<div class="card fade fade5">
<h3><span>🤝</span> A2A Deals</h3>
<div id="deals-container"></div>
</div>
<div class="card fade fade6">
<h3><span>🔒</span> Vault Explorer</h3>
<div id="vaults-container"></div>
</div>
</div>
</div>

<footer>Phantom Brain &mdash; Built on <a href="https://build.usecdr.dev" target="_blank">Story CDR</a> &middot; <a href="https://github.com/gieskuy5/phantom-brain" target="_blank">GitHub</a> &middot; CDR Hackathon 2026</footer>

<script>
function fetchJSON(url, cb) {
    var xhr = new XMLHttpRequest();
    xhr.open("GET", url);
    xhr.onload = function() { if (xhr.status === 200) cb(JSON.parse(xhr.responseText)); };
    xhr.send();
}

function badge(text, cls) { return '<span class="badge badge-' + cls + '">' + text + '</span>'; }

function confidenceBar(val) {
    return '<span class="confidence-bar"><span class="confidence-fill" style="width:' + val + '%;background:' + (val > 75 ? 'var(--green)' : val > 60 ? 'var(--accent)' : 'var(--red)') + '"></span></span> ' + val + '%';
}

fetchJSON("/api/agent", function(a) {
    document.getElementById("s-signals").textContent = a.totalSignals;
    document.getElementById("s-winrate").textContent = a.winRate + "%";
    document.getElementById("s-pnl").textContent = "+" + a.pnl + "%";
    document.getElementById("agent-info").innerHTML =
        '<div style="margin-bottom:12px"><strong style="color:var(--text)">' + a.name + '</strong></div>' +
        '<div style="margin-bottom:8px">Wallet: <span style="color:var(--primary)">' + a.wallet.substring(0,6) + "..." + a.wallet.substring(a.wallet.length-4) + '</span></div>' +
        '<div style="margin-bottom:8px">Strategy: <span style="color:var(--accent)">' + a.strategy + '</span></div>' +
        '<div style="margin-bottom:8px">Indicators: ' + a.indicators.join(", ") + '</div>' +
        '<div>Vault: <span style="color:var(--dim)">' + a.strategyVault.substring(0,8) + '...</span></div>';
});

fetchJSON("/api/signals", function(signals) {
    var html = "";
    for (var i = 0; i < signals.length; i++) {
        var s = signals[i];
        html += "<tr>";
        html += "<td><strong>" + s.token + "</strong></td>";
        html += "<td>" + badge(s.direction, s.direction.toLowerCase()) + "</td>";
        html += "<td>$" + s.entry.toLocaleString() + "</td>";
        html += "<td>$" + s.sl.toLocaleString() + "</td>";
        html += "<td>$" + s.tp.toLocaleString() + "</td>";
        html += "<td>" + confidenceBar(s.confidence) + "</td>";
        html += "<td>" + badge(s.tier, s.tier) + "</td>";
        html += "<td>" + badge(s.status, s.status) + "</td>";
        html += '<td style="color:var(--dim)">' + s.time + "</td>";
        html += "</tr>";
    }
    document.getElementById("signals-body").innerHTML = html;
});

fetchJSON("/api/marketplace", function(listings) {
    var html = "";
    for (var i = 0; i < listings.length; i++) {
        var l = listings[i];
        html += "<tr>";
        html += "<td>" + badge(l.tier, l.tier) + "</td>";
        html += "<td><strong>" + l.token + "</strong></td>";
        html += "<td>" + badge(l.direction, l.direction.toLowerCase()) + "</td>";
        html += '<td style="color:var(--accent)">' + l.price + "</td>";
        html += "<td>" + l.buyers + "</td>";
        html += '<td><button class="btn" onclick="alert(\'Connect wallet to buy\')">Buy Access</button></td>';
        html += "</tr>";
    }
    document.getElementById("market-body").innerHTML = html;
});

fetchJSON("/api/deals", function(deals) {
    var html = "";
    for (var i = 0; i < deals.length; i++) {
        var d = deals[i];
        html += '<div style="padding:12px 0;border-bottom:1px solid var(--border)">';
        html += '<div style="display:flex;justify-content:space-between;margin-bottom:8px">';
        html += '<span style="color:var(--text)">' + d.counterparty + '</span>';
        html += badge(d.status, d.status) + '</div>';
        html += '<div style="font-size:.65rem;color:var(--muted)">';
        html += badge(d.tier, d.tier) + ' &middot; Proposed: ' + d.proposed + ' &middot; Counter: ' + d.counter + ' &middot; ' + d.history + ' messages';
        html += '</div></div>';
    }
    document.getElementById("deals-container").innerHTML = html || '<div style="color:var(--dim)">No active deals</div>';
});

fetchJSON("/api/vaults", function(vaults) {
    var html = "";
    for (var i = 0; i < vaults.length; i++) {
        var v = vaults[i];
        html += '<div class="vault-row">';
        html += '<div><div class="vault-uuid">' + v.uuid + '</div>';
        html += '<div style="margin-top:4px">' + badge(v.type, v.tier) + ' ' + badge(v.tier, v.tier) + ' <span style="color:var(--dim);font-size:.6rem">' + v.size + '</span></div></div>';
        html += '<div class="vault-meta"><span style="color:var(--dim);font-size:.6rem">' + v.created + '</span>';
        html += '<button class="btn" onclick="alert(\'Decrypting vault...\')">Read</button></div>';
        html += '</div>';
    }
    document.getElementById("vaults-container").innerHTML = html;
});

fetchJSON("/api/revenue", function(r) {
    document.getElementById("s-revenue").textContent = r.total;
    var items = [
        {val: r.total, label: "Total Revenue"},
        {val: r.signalSales, label: "Signal Sales"},
        {val: r.brainSubs, label: "Brain Subs"},
        {val: r.a2aDeals, label: "A2A Deals"}
    ];
    var html = "";
    for (var i = 0; i < items.length; i++) {
        html += '<div class="rev-item"><div class="rev-val">' + items[i].val + '</div><div class="rev-label">' + items[i].label + '</div></div>';
    }
    document.getElementById("revenue-grid").innerHTML = html;
});
</script>
</body>
</html>"""
