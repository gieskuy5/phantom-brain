// SPDX-License-Identifier: MIT
pragma solidity ^0.8.26;

/**
 * @title PayToUnlockCondition
 * @notice Custom CDR read condition: reader must pay a fee to unlock the vault
 * @dev Implements ICDRReadCondition interface for CDR integration
 */
interface ICDRReadCondition {
    function checkReadCondition(
        uint32 uuid,
        bytes calldata accessAuxData,
        bytes calldata conditionData,
        address caller
    ) external view returns (bool);
}

contract PayToUnlockCondition is ICDRReadCondition {
    struct VaultFee {
        address owner;
        uint256 fee; // in wei
        bool active;
    }

    mapping(uint32 => VaultFee) public vaultFees;
    mapping(uint32 => mapping(address => bool)) public hasPaid;

    event FeeSet(uint32 indexed uuid, address indexed owner, uint256 fee);
    event AccessPaid(uint32 indexed uuid, address indexed buyer, uint256 amount);

    /**
     * @notice Set the fee for a vault
     * @param uuid The vault UUID
     * @param fee The fee in wei
     */
    function setFee(uint32 uuid, uint256 fee) external {
        vaultFees[uuid] = VaultFee({
            owner: msg.sender,
            fee: fee,
            active: true
        });
        emit FeeSet(uuid, msg.sender, fee);
    }

    /**
     * @notice Pay for access to a vault
     * @param uuid The vault UUID
     */
    function payForAccess(uint32 uuid) external payable {
        VaultFee storage vf = vaultFees[uuid];
        require(vf.active, "Vault not listed");
        require(msg.value >= vf.fee, "Insufficient payment");

        hasPaid[uuid][msg.sender] = true;
        emit AccessPaid(uuid, msg.sender, msg.value);

        // Transfer payment to vault owner
        (bool success, ) = vf.owner.call{value: msg.value}("");
        require(success, "Transfer failed");
    }

    /**
     * @notice Check if caller can read the vault
     * @dev Called by CDR contract
     */
    function checkReadCondition(
        uint32 uuid,
        bytes calldata, /* accessAuxData */
        bytes calldata, /* conditionData */
        address caller
    ) external view override returns (bool) {
        VaultFee storage vf = vaultFees[uuid];

        // Owner can always read
        if (caller == vf.owner) return true;

        // Must have paid
        return hasPaid[uuid][caller];
    }

    /**
     * @notice Check if a buyer has paid for a vault
     */
    function hasAccess(uint32 uuid, address buyer) external view returns (bool) {
        return hasPaid[uuid][buyer] || buyer == vaultFees[uuid].owner;
    }

    /**
     * @notice Get vault fee info
     */
    function getVaultFee(uint32 uuid) external view returns (address owner, uint256 fee, bool active) {
        VaultFee storage vf = vaultFees[uuid];
        return (vf.owner, vf.fee, vf.active);
    }
}
