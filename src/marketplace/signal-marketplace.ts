/**
 * Signal Marketplace
 * Lists signals for sale, handles purchases, manages subscriptions
 */

import { VaultInfo } from "../cdr/vault-manager.js";

export interface Listing {
  id: string;
  agentId: string;
  agentName: string;
  vaultId: string;
  tier: "signal" | "brain";
  token: string;
  direction: "LONG" | "SHORT";
  price: string; // in wei
  createdAt: number;
  buyers: string[];
}

export interface Purchase {
  listingId: string;
  buyerAddress: string;
  vaultId: string;
  price: string;
  timestamp: number;
}

/**
 * In-memory marketplace (for demo)
 * In production, this would be on-chain via smart contracts
 */
export class SignalMarketplace {
  private listings: Map<string, Listing> = new Map();
  private purchases: Purchase[] = [];

  /**
   * List a signal for sale
   */
  listSignal(params: {
    agentId: string;
    agentName: string;
    vaultId: string;
    tier: "signal" | "brain";
    token: string;
    direction: "LONG" | "SHORT";
    price: string;
  }): Listing {
    const listing: Listing = {
      id: crypto.randomUUID(),
      ...params,
      createdAt: Date.now(),
      buyers: [],
    };

    this.listings.set(listing.id, listing);
    console.log(`[Marketplace] Listed: ${params.tier} signal for ${params.token} ${params.direction}`);
    console.log(`  Price: ${params.price} wei | Vault: ${params.vaultId}`);
    return listing;
  }

  /**
   * Purchase a signal
   */
  purchase(listingId: string, buyerAddress: string): Purchase | null {
    const listing = this.listings.get(listingId);
    if (!listing) {
      console.log(`[Marketplace] Listing ${listingId} not found`);
      return null;
    }

    if (listing.buyers.includes(buyerAddress)) {
      console.log(`[Marketplace] Already purchased`);
      return null;
    }

    listing.buyers.push(buyerAddress);
    const purchase: Purchase = {
      listingId,
      buyerAddress,
      vaultId: listing.vaultId,
      price: listing.price,
      timestamp: Date.now(),
    };

    this.purchases.push(purchase);
    console.log(`[Marketplace] Purchase: ${buyerAddress} bought ${listing.tier} signal`);
    return purchase;
  }

  /**
   * Browse available listings
   */
  browse(filter?: { tier?: string; token?: string }): Listing[] {
    let results = Array.from(this.listings.values());
    if (filter?.tier) results = results.filter((l) => l.tier === filter.tier);
    if (filter?.token) results = results.filter((l) => l.token === filter.token);
    return results;
  }

  /**
   * Get marketplace stats
   */
  getStats(): { totalListings: number; totalPurchases: number; totalVolume: string } {
    const totalVolume = this.purchases.reduce((sum, p) => sum + BigInt(p.price), 0n);
    return {
      totalListings: this.listings.size,
      totalPurchases: this.purchases.length,
      totalVolume: totalVolume.toString(),
    };
  }
}
