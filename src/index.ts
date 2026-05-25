/**
 * Phantom Brain — Main Entry Point
 * 
 * Autonomous AI Agent with Private, Monetizable Intelligence
 * Built on Story Protocol's Confidential Data Rails (CDR)
 */

export { VaultManager } from "./cdr/vault-manager.js";
export type { SignalData, StrategyData, VaultInfo } from "./cdr/vault-manager.js";

export { PhantomAgent } from "./agent/phantom-agent.js";
export type { AgentConfig, AgentState } from "./agent/phantom-agent.js";

export { SignalMarketplace } from "./marketplace/signal-marketplace.js";
export type { Listing, Purchase } from "./marketplace/signal-marketplace.js";

export { A2ANegotiator } from "./a2a/negotiator.js";
export type { AgentCard, DealProposal, DealCounter, DealResult } from "./a2a/negotiator.js";
