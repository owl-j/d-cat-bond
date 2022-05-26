// SPDX-License-Identifier: MIT
pragma solidity >=0.4.22 <0.9.0;

import "./CatastropheBond.sol";

contract BondFactory {
    // Public list of cat bonds created by this factory
    CatastropheBond[] public CatastropheBondArray;

    function IssueNewBond(
        address _sponsor,
        address _oracle,
        uint64[] calldata _tiles,
        uint _insuredSum,
        uint _premium,
        uint _expiryDate,
        uint8 _threshold
    ) public {
        CatastropheBond catBond = new CatastropheBond(_sponsor,_oracle,_tiles,_insuredSum,_premium,_expiryDate,_threshold);
        CatastropheBondArray.push(catBond);
    }


}