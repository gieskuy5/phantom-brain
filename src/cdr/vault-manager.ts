/**
 * CDR Vault Manager for Phantom Brain
 * Handles vault creation, encryption, and access control
 */

import { CDRClient, initWasm, uuidToLabel } from "@piplabs/cdr-sdk";
import { createPublicClient, createWalletClient, http, toHex, type Hex } from "viem";
import { privateKeyToAccount, type PrivateKeyAccount } from "viem/accounts";
import { encodeAbiParameters } from "viem";

// Aeneid Testnet config
const RPC_URL = process.env.STORY_RPC_URL || "https://aeneid.storyrpc.io";
const API_URL = process.env.STORY_API_URL || "http://172.192.41.96:1317";

// Deployed condition contracts on Aeneid
const OWNER_WRITE_CONDITION = "0x4C9bFC96d7092b590D497A191826C3dA2277c34B";
const LICENSE_READ_CONDITION = "0xC0640AD4CF2CaA9914C8e5C44234359a9102f7a3";
const LICENSE_TOKEN = "0xFe3838BFb30B34170F00030B52eA4893d8aAC6bC";

export interface SignalData {
  token: string;
  direction: "LONG" | "SHORT";
  entry: number;
  stopLoss: number;
  takeProfit: number;
  confidence: number;
  reasoning: string;
  timestamp: number;
}

export interface StrategyData {
  name: string;
  version: number;
  description: string;
  indicators: string[];
  riskParams: Record<string, number>;
  performance: {
    winRate: number;
    avgReturn: number;
    maxDrawdown: number;
    totalTrades: number;
  };
}

export interface VaultInfo {
  uuid: string;
  txHash: string;
  type: "signal" | "strategy" | "proof";
  tier: "free" | "signal" | "brain";
  createdAt: number;
}

export class VaultManager {
  private client: CDRClient;
  private account: PrivateKeyAccount;
  private globalPubKey: any;
  private initialized = false;

  constructor(privateKey: string) {
    this.account = privateKeyToAccount(privateKey as Hex);

    const publicClient = createPublicClient({ transport: http(RPC_URL) });
    const walletClient = createWalletClient({
      account: this.account,
      transport: http(RPC_URL),
    });

    this.client = new CDRClient({
      network: "testnet",
      publicClient,
      walletClient,
      apiUrl: API_URL,
    });
  }

  async init(): Promise<void> {
    if (this.initialized) return;
    await initWasm();
    this.globalPubKey = await this.client.observer.getGlobalPubKey();
    this.initialized = true;
    console.log(`[VaultManager] Initialized. Wallet: ${this.account.address}`);
  }

  /**
   * Create a vault with owner-only access (simplest pattern)
   */
  async createOwnerVault(data: string): Promise<VaultInfo> {
    await this.init();

    const { uuid, txHash } = await this.client.uploader.allocate({
      updatable: true,
      writeConditionAddr: this.account.address,
      readConditionAddr: this.account.address,
      writeConditionData: "0x",
      readConditionData: "0x",
      skipConditionValidation: true,
    });

    const ciphertext = await this.client.uploader.encryptDataKey({
      dataKey: new TextEncoder().encode(data),
      globalPubKey: this.globalPubKey,
      label: uuidToLabel(uuid),
    });

    await this.client.uploader.write({
      uuid,
      accessAuxData: "0x",
      encryptedData: toHex(ciphertext.raw),
    });

    console.log(`[VaultManager] Created vault ${uuid} (tx: ${txHash})`);
    return {
      uuid,
      txHash,
      type: "signal",
      tier: "free",
      createdAt: Date.now(),
    };
  }

  /**
   * Create a pay-to-unlock signal vault
   * Uses custom condition contract for fee gating
   */
  async createSignalVault(signal: SignalData, tier: "signal" | "brain"): Promise<VaultInfo> {
    await this.init();

    const signalJson = JSON.stringify(signal);

    // For demo: use owner-only vault (custom fee contract would be deployed separately)
    const { uuid, txHash } = await this.client.uploader.allocate({
      updatable: true,
      writeConditionAddr: this.account.address,
      readConditionAddr: this.account.address,
      writeConditionData: "0x",
      readConditionData: "0x",
      skipConditionValidation: true,
    });

    const ciphertext = await this.client.uploader.encryptDataKey({
      dataKey: new TextEncoder().encode(signalJson),
      globalPubKey: this.globalPubKey,
      label: uuidToLabel(uuid),
    });

    await this.client.uploader.write({
      uuid,
      accessAuxData: "0x",
      encryptedData: toHex(ciphertext.raw),
    });

    console.log(`[VaultManager] Created ${tier} signal vault ${uuid}`);
    return { uuid, txHash, type: "signal", tier, createdAt: Date.now() };
  }

  /**
   * Create a strategy vault (encrypted brain)
   */
  async createStrategyVault(strategy: StrategyData): Promise<VaultInfo> {
    await this.init();

    const strategyJson = JSON.stringify(strategy);

    const { uuid, txHash } = await this.client.uploader.allocate({
      updatable: true,
      writeConditionAddr: this.account.address,
      readConditionAddr: this.account.address,
      writeConditionData: "0x",
      readConditionData: "0x",
      skipConditionValidation: true,
    });

    const ciphertext = await this.client.uploader.encryptDataKey({
      dataKey: new TextEncoder().encode(strategyJson),
      globalPubKey: this.globalPubKey,
      label: uuidToLabel(uuid),
    });

    await this.client.uploader.write({
      uuid,
      accessAuxData: "0x",
      encryptedData: toHex(ciphertext.raw),
    });

    console.log(`[VaultManager] Created strategy vault ${uuid}`);
    return { uuid, txHash, type: "strategy", tier: "brain", createdAt: Date.now() };
  }

  /**
   * Read/decrypt a vault
   */
  async readVault(uuid: string): Promise<string> {
    await this.init();

    const { dataKey } = await this.client.consumer.accessCDR({
      uuid,
      accessAuxData: "0x",
      timeoutMs: 120_000,
    });

    return new TextDecoder().decode(dataKey);
  }

  /**
   * Get vault info (read-only, no decryption)
   */
  async getVaultInfo(uuid: string): Promise<any> {
    await this.init();
    return this.client.observer.getVault(uuid);
  }

  /**
   * Get current fees
   */
  async getFees(): Promise<{ allocate: string; write: string; read: string }> {
    await this.init();
    const [allocate, write, read] = await Promise.all([
      this.client.observer.getAllocateFee(),
      this.client.observer.getWriteFee(),
      this.client.observer.getReadFee(),
    ]);
    return {
      allocate: allocate.toString(),
      write: write.toString(),
      read: read.toString(),
    };
  }

  getAddress(): string {
    return this.account.address;
  }
}
