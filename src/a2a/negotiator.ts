/**
 * Agent-to-Agent (A2A) Negotiation Protocol
 * Two agents discover, negotiate, and settle data deals
 */

export interface AgentCard {
  name: string;
  description: string;
  wallet: string;
  skills: string[];
  endpoints: {
    proposeTerms: string;
    counterOffer: string;
    finalizeDeal: string;
  };
  reputation: {
    totalDeals: number;
    winRate: number;
    avgResponseTime: number;
  };
}

export interface DealProposal {
  id: string;
  fromAgent: string;
  toAgent: string;
  vaultId: string;
  tier: "signal" | "brain";
  price: string; // in wei
  token: string;
  message: string;
  timestamp: number;
}

export interface DealCounter {
  proposalId: string;
  fromAgent: string;
  newPrice: string;
  message: string;
  timestamp: number;
}

export interface DealResult {
  id: string;
  proposalId: string;
  buyer: string;
  seller: string;
  finalPrice: string;
  vaultId: string;
  licenseTokenId?: string;
  status: "negotiating" | "agreed" | "settled" | "failed";
  history: (DealProposal | DealCounter)[];
}

/**
 * A2A Negotiation Engine
 * Handles discovery, negotiation, and settlement between agents
 */
export class A2ANegotiator {
  private agentCard: AgentCard;
  private activeDeals: Map<string, DealResult> = new Map();

  constructor(card: AgentCard) {
    this.agentCard = card;
  }

  /**
   * Get this agent's card (for discovery)
   */
  getCard(): AgentCard {
    return this.agentCard;
  }

  /**
   * Propose a deal to another agent
   */
  proposeDeal(params: {
    toAgent: string;
    vaultId: string;
    tier: "signal" | "brain";
    price: string;
    token: string;
    message?: string;
  }): DealProposal {
    const proposal: DealProposal = {
      id: crypto.randomUUID(),
      fromAgent: this.agentCard.wallet,
      toAgent: params.toAgent,
      vaultId: params.vaultId,
      tier: params.tier,
      price: params.price,
      token: params.token,
      message: params.message || `Proposal for ${params.tier} access`,
      timestamp: Date.now(),
    };

    const deal: DealResult = {
      id: crypto.randomUUID(),
      proposalId: proposal.id,
      buyer: params.toAgent,
      seller: this.agentCard.wallet,
      finalPrice: params.price,
      vaultId: params.vaultId,
      status: "negotiating",
      history: [proposal],
    };

    this.activeDeals.set(deal.id, deal);
    console.log(`[A2A] Proposed deal: ${params.tier} access for ${params.price} wei`);
    return proposal;
  }

  /**
   * Counter-offer on a deal
   */
  counterOffer(dealId: string, newPrice: string, message?: string): DealCounter | null {
    const deal = this.activeDeals.get(dealId);
    if (!deal || deal.status !== "negotiating") return null;

    const counter: DealCounter = {
      proposalId: deal.proposalId,
      fromAgent: this.agentCard.wallet,
      newPrice,
      message: message || `Counter: ${newPrice} wei`,
      timestamp: Date.now(),
    };

    deal.finalPrice = newPrice;
    deal.history.push(counter);
    console.log(`[A2A] Counter-offer: ${newPrice} wei`);
    return counter;
  }

  /**
   * Accept a deal (agree on price)
   */
  acceptDeal(dealId: string): boolean {
    const deal = this.activeDeals.get(dealId);
    if (!deal || deal.status !== "negotiating") return false;

    deal.status = "agreed";
    console.log(`[A2A] Deal agreed at ${deal.finalPrice} wei`);
    return true;
  }

  /**
   * Settle a deal (on-chain payment + access grant)
   */
  settleDeal(dealId: string, licenseTokenId?: string): boolean {
    const deal = this.activeDeals.get(dealId);
    if (!deal || deal.status !== "agreed") return false;

    deal.status = "settled";
    deal.licenseTokenId = licenseTokenId;
    console.log(`[A2A] Deal settled! License: ${licenseTokenId || "direct access"}`);
    return true;
  }

  /**
   * Get all active deals
   */
  getActiveDeals(): DealResult[] {
    return Array.from(this.activeDeals.values()).filter(
      (d) => d.status !== "failed"
    );
  }

  /**
   * Get deal by ID
   */
  getDeal(dealId: string): DealResult | undefined {
    return this.activeDeals.get(dealId);
  }
}
