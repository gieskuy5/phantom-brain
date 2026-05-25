// SPDX-License-Identifier: MIT
pragma solidity ^0.8.26;

/**
 * @title MarketplaceCondition
 * @notice CDR read condition for a signal marketplace
 * @dev Supports tiered access: free, signal, brain
 */
interface ICDRReadCondition {
    function checkReadCondition(
        uint32 uuid,
        bytes calldata accessAuxData,
        bytes calldata conditionData,
        address caller
    ) external view returns (bool);
}

contract MarketplaceCondition is ICDRReadCondition {
    enum Tier { FREE, SIGNAL, BRAIN }

    struct Listing {
        address agent;
        uint256 signalPrice;  // price for signal tier
        uint256 brainPrice;   // price for brain tier
        Tier minimumTier;
        bool active;
    }

    mapping(uint32 => Listing) public listings;
    mapping(uint32 => mapping(address => Tier)) public buyerTier;

    event Listed(uint32 indexed uuid, address indexed agent, uint256 signalPrice, uint256 brainPrice);
    event Purchased(uint32 indexed uuid, address indexed buyer, Tier tier, uint256 amount);

    /**
     * @notice List a signal vault on the marketplace
     */
    function listVault(
        uint32 uuid,
        uint256 signalPrice,
        uint256 brainPrice
    ) external {
        listings[uuid] = Listing({
            agent: msg.sender,
            signalPrice: signalPrice,
            brainPrice: brainPrice,
            minimumTier: Tier.FREE,
            active: true
        });
        emit Listed(uuid, msg.sender, signalPrice, brainPrice);
    }

    /**
     * @notice Purchase signal-tier access
     */
    function buySignal(uint32 uuid) external payable {
        Listing storage l = listings[uuid];
        require(l.active, "Not listed");
        require(msg.value >= l.signalPrice, "Insufficient payment");

        buyerTier[uuid][msg.sender] = Tier.SIGNAL;
        emit Purchased(uuid, msg.sender, Tier.SIGNAL, msg.value);

        (bool success, ) = l.agent.call{value: msg.value}("");
        require(success, "Transfer failed");
    }

    /**
     * @notice Purchase brain-tier access (includes signal)
     */
    function buyBrain(uint32 uuid) external payable {
        Listing storage l = listings[uuid];
        require(l.active, "Not listed");
        require(msg.value >= l.brainPrice, "Insufficient payment");

        buyerTier[uuid][msg.sender] = Tier.BRAIN;
        emit Purchased(uuid, msg.sender, Tier.BRAIN, msg.value);

        (bool success, ) = l.agent.call{value: msg.value}("");
        require(success, "Transfer failed");
    }

    /**
     * @notice Check read access
     * @dev accessAuxData encodes the required tier: abi.encode(uint8 tier)
     */
    function checkReadCondition(
        uint32 uuid,
        bytes calldata accessAuxData,
        bytes calldata, /* conditionData */
        address caller
    ) external view override returns (bool) {
        Listing storage l = listings[uuid];

        // Agent can always read own vault
        if (caller == l.agent) return true;

        // Decode required tier from accessAuxData
        uint8 requiredTier = abi.decode(accessAuxData, (uint8));

        // Check buyer's tier
        Tier buyerTierVal = buyerTier[uuid][caller];
        return uint8(buyerTierVal) >= requiredTier;
    }
}
