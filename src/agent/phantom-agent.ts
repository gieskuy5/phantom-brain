/**
 * Phantom Brain — AI Agent Core
 * Generates trading signals with encrypted reasoning
 */

import { VaultManager, SignalData, StrategyData, VaultInfo } from "../cdr/vault-manager.js";

export interface AgentConfig {
  name: string;
  strategy: StrategyData;
  privateKey: string;
}

export interface AgentState {
  id: string;
  name: string;
  walletAddress: string;
  strategyVault: VaultInfo | null;
  signalVaults: VaultInfo[];
  totalSignals: number;
  winRate: number;
  pnl: number;
}

/**
 * The Phantom Brain Agent
 * Generates signals, encrypts them in CDR vaults, manages subscriptions
 */
export class PhantomAgent {
  private vault: VaultManager;
  private config: AgentConfig;
  private state: AgentState;

  constructor(config: AgentConfig) {
    this.config = config;
    this.vault = new VaultManager(config.privateKey);
    this.state = {
      id: crypto.randomUUID(),
      name: config.name,
      walletAddress: "",
      strategyVault: null,
      signalVaults: [],
      totalSignals: 0,
      winRate: 0,
      pnl: 0,
    };
  }

  async init(): Promise<void> {
    await this.vault.init();
    this.state.walletAddress = this.vault.getAddress();
    console.log(`[PhantomAgent] "${this.config.name}" initialized`);
    console.log(`[PhantomAgent] Wallet: ${this.state.walletAddress}`);
  }

  /**
   * Deploy the agent's strategy to a CDR vault (encrypted brain)
   */
  async deployStrategy(): Promise<VaultInfo> {
    console.log(`[PhantomAgent] Deploying strategy vault...`);
    const vault = await this.vault.createStrategyVault(this.config.strategy);
    this.state.strategyVault = vault;
    console.log(`[PhantomAgent] Strategy vault: ${vault.uuid}`);
    return vault;
  }

  /**
   * Generate a trading signal and encrypt it in tiered vaults
   * - Free tier: basic signal (token + direction only)
   * - Signal tier: full signal with entry/SL/TP
   * - Brain tier: full signal + reasoning
   */
  async generateSignal(params: {
    token: string;
    direction: "LONG" | "SHORT";
    entry: number;
    stopLoss: number;
    takeProfit: number;
    confidence: number;
    reasoning: string;
  }): Promise<{
    freeVault: VaultInfo;
    signalVault: VaultInfo;
    brainVault: VaultInfo;
    signalId: string;
  }> {
    const signalId = crypto.randomUUID();
    const timestamp = Date.now();

    const fullSignal: SignalData = {
      ...params,
      timestamp,
    };

    console.log(`[PhantomAgent] Generating signal #${this.state.totalSignals + 1}...`);
    console.log(`[PhantomAgent] ${params.direction} ${params.token} @ ${params.entry}`);

    // Tier 1: Free — basic info only
    const freeData = JSON.stringify({
      id: signalId,
      token: params.token,
      direction: params.direction,
      confidence: params.confidence,
      timestamp,
    });
    const freeVault = await this.vault.createOwnerVault(freeData);
    freeVault.tier = "free";

    // Tier 2: Signal — full entry/SL/TP
    const signalData: SignalData = {
      token: params.token,
      direction: params.direction,
      entry: params.entry,
      stopLoss: params.stopLoss,
      takeProfit: params.takeProfit,
      confidence: params.confidence,
      reasoning: "", // no reasoning in signal tier
      timestamp,
    };
    const signalVault = await this.vault.createSignalVault(signalData, "signal");

    // Tier 3: Brain — full signal + reasoning
    const brainVault = await this.vault.createSignalVault(fullSignal, "brain");

    this.state.signalVaults.push(freeVault, signalVault, brainVault);
    this.state.totalSignals++;

    console.log(`[PhantomAgent] Signal vaults created:`);
    console.log(`  Free:   ${freeVault.uuid}`);
    console.log(`  Signal: ${signalVault.uuid}`);
    console.log(`  Brain:  ${brainVault.uuid}`);

    return { freeVault, signalVault, brainVault, signalId };
  }

  /**
   * Record a trade result for proof-of-alpha
   */
  recordTrade(result: { win: boolean; pnl: number }): void {
    const total = this.state.totalSignals;
    const currentWins = this.state.winRate * (total - 1);
    const newWins = currentWins + (result.win ? 1 : 0);
    this.state.winRate = newWins / total;
    this.state.pnl += result.pnl;

    console.log(
      `[PhantomAgent] Trade recorded: ${result.win ? "WIN" : "LOSS"} | ` +
        `PnL: ${result.pnl > 0 ? "+" : ""}${result.pnl.toFixed(2)}% | ` +
        `Win Rate: ${(this.state.winRate * 100).toFixed(1)}%`
    );
  }

  /**
   * Get agent's public profile (proof-of-alpha)
   */
  getPublicProfile(): {
    name: string;
    wallet: string;
    totalSignals: number;
    winRate: number;
    pnl: number;
    strategyVaultId: string | null;
  } {
    return {
      name: this.state.name,
      wallet: this.state.walletAddress,
      totalSignals: this.state.totalSignals,
      winRate: this.state.winRate,
      pnl: this.state.pnl,
      strategyVaultId: this.state.strategyVault?.uuid || null,
    };
  }

  /**
   * Read back own vault data
   */
  async readVault(uuid: string): Promise<string> {
    return this.vault.readVault(uuid);
  }

  getState(): AgentState {
    return { ...this.state };
  }
}
