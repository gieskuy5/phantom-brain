# 🧠💀 Phantom Brain

**Autonomous AI Agent with Private, Monetizable Intelligence**

> Built on Story Protocol's Confidential Data Rails (CDR)

## What is Phantom Brain?

An AI trading agent whose brain (strategy, reasoning, data sources) is **encrypted in CDR vaults**. The agent can:

1. **Autonomously analyze** markets and generate signals
2. **Sell signals** — followers pay to unlock tiered signal data
3. **Negotiate with other agents** — A2A price discovery
4. **Evolve** — strategy updates are versioned in the vault

## Architecture

```
┌─────────────────────────────────────────┐
│            PHANTOM BRAIN                │
│                                         │
│  ┌──────────┐    ┌──────────────────┐   │
│  │ AI Agent │───▶│  CDR Vault       │   │
│  │ (Brain)  │    │  ┌────────────┐  │   │
│  │          │    │  │ Strategy   │  │   │
│  │ - Analyze│    │  │ (encrypted)│  │   │
│  │ - Trade  │    │  ├────────────┤  │   │
│  │ - Learn  │    │  │ Signals    │  │   │
│  │ - Sell   │    │  │ (tiered)   │  │   │
│  └──────────┘    │  ├────────────┤  │   │
│       │          │  │ History    │  │   │
│       │          │  │ (proof)    │  │   │
│       │          │  └────────────┘  │   │
│       │          └──────────────────┘   │
│       │               │                 │
│       ▼               ▼                 │
│  ┌──────────┐    ┌──────────────┐       │
│  │ On-Chain │    │ Access Gate  │       │
│  │ Actions  │    │ (Who/When/   │       │
│  │ (trade,  │    │  How much)   │       │
│  │  swap)   │    └──────────────┘       │
│  └──────────┘                           │
└─────────────────────────────────────────┘
         │           │           │
    👤 Human    🤖 Agent    🤖 Agent
    Follower    Buyer A     Buyer B
```

## Revenue Model

| Layer | What's Sold | Price | Access |
|-------|------------|-------|--------|
| **Free** | Agent existence + performance proof | Free | Public on-chain |
| **Signal** | Entry/exit alerts, token picks | Per-unlock | CDR vault → pay to reveal |
| **Brain** | Full strategy + reasoning | Subscription | CDR vault → recurring access |

## Tech Stack

- **Story Testnet (Aeneid)** — CDR vaults, access control, on-chain settlement
- **@piplabs/cdr-sdk** — vault create, read/write conditions, dynamic permissions
- **@story-protocol/core-sdk** — IP asset registration, licensing
- **viem** — Ethereum client
- **AI Layer** — LLM-based analysis agent

## Quick Start

```bash
npm install
cp .env.example .env  # fill in your private key
npx tsx demo/run-agent.ts
```

## Network

- Chain ID: 1315 (Aeneid Testnet)
- RPC: https://aeneid.storyrpc.io
- Explorer: https://aeneid.storyscan.io
- CDR API: http://172.192.41.96:1317

## License

MIT
