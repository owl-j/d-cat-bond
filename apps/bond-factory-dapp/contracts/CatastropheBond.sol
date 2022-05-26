
pragma solidity >=0.7.0 <0.9.0;


// Uses H3 encoding as

contract CatastropheBond{
    address payable public sponsor; // The sponsor of the contract (needs the insurance)
    address payable public investor; // The investor of the contract (forking out the Principal)

    uint64[] public tiles; // The list of tiles this contract insures.
    address public oracle; // Address of the oracle to resolve the sensor
    uint8 public threshold; // The threshold value
    uint8 public index; // the value of the index

    uint public insuredSum; // Principal assigned to each tile
    uint public premium; // premium payment assigned to each tile

    uint public deployDate; // Datetime the bond was deployed
    uint public expiryDate; // Datetime the bond expires
    uint public waitTime = 604800; // 604800 = Wait a week before withdrawing the offer.

    mapping (uint => uint) indexHistory; // Store the history of the index

    enum Status{
        OFFER, // Contract is seeking an investor
        LIVE, // Contract is live
        EVENTOCCURED, // Contract expired after the event was observed
        BONDEXPIRED // Contract expired and coupon paid
    }
    Status public status;






    constructor (
        address _sponsor, // Address
        address _oracle,
        uint64[] memory _tiles,
        uint _insuredSum,
        uint _premium,
        uint _expiryDate,
        uint8 _threshold
        ) payable {
            require(msg.value == _premium, "Pay the premium to instantiate the bond."); // Ensure the amount transferred is the desired premium
            sponsor= payable(_sponsor);
            tiles= _tiles;
            insuredSum = _insuredSum;
            premium= _premium;
            deployDate = block.timestamp;
            expiryDate = _expiryDate;
            threshold = _threshold;
            oracle = _oracle;
            status = Status.OFFER;
        }

    // Use this function to invest in the bond
    function invest() external payable{
        require(block.timestamp <= (deployDate+waitTime), "This bond offer has expired without finding an investor.");
        require(investor == address(0), "An investor has already funded this bond."); // Ensure there are no other investors
        require(msg.value == insuredSum, "Pay the insured sum to invest in this bond."); // Ensure that the transaction can fund the insuredSum
        investor = payable(msg.sender);
        investor.transfer(premium);
        status = Status.LIVE;
    }

    function dissolve() external{
        require(msg.sender == sponsor, "Only the sponsor may dissolve the contract!");
        require(status == Status.OFFER, "An investor has already paid the principal!");
        selfdestruct(sponsor);
    }

    function replaceSponsor(address with) external{
        require(msg.sender == sponsor, "Only a party to the bond may initiate a transfer");
        sponsor = payable(with);
    }

    function replaceInvestor(address with) external{
        require(msg.sender == investor, "Only a party to the bond may initiate a transfer");
        investor = payable(with);
    }

    function decideOutcome() public {
        if(status == Status.LIVE && block.timestamp >= expiryDate){
            investor.transfer(address(this).balance);
            status == Status.BONDEXPIRED;
        } else if(status == Status.EVENTOCCURED){
            sponsor.transfer(insuredSum);
        }

    }

    function checkOutcome(uint8 _indexValue) public {
        require(msg.sender == oracle, "Only the oracle may add an outcome");
        require(status == Status.LIVE, "The catastrophe bond is not live");
        require(block.timestamp <= expiryDate, "The catastrophe bond time has expire call decideOutcome to withdraw coupon");
        index = _indexValue;
        if(_indexValue >= threshold){
            status = Status.EVENTOCCURED;
        }
    }
}


