const { expect } = require("chai");
const { ethers } = require("hardhat");

describe("Bond Factory", function () {
  it("Deployment should assign the signer as the bond sponsor", async function () {
    const [owner] = await ethers.getSigners();

    const BondFactory = await ethers.getContractFactory("BondFactory");

    const hardhatBF = await BondFactory.deploy();

    //const ownerBalance = await hardhatBF.IssueNewBond(owner.address);
    //expect(await hardhatToken.totalSupply()).to.equal(ownerBalance);
  });
});