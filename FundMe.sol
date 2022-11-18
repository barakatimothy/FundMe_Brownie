// SPDX-License-Identifier: MIT
pragma solidity ^0.6.6 <0.9.0;
import "@chainlink/contracts/src/V0.6/interfaces/AggregatorV3Interfaces.sol";
import "@chainlink/contracts/src/V0.6/vendor/SafeMathchainliink.sol";
contract FundMe{
using SafeMathchainliink for uint256; 
AggregatorV3Interface public priceFeed;
mapping (address =>uint256) addressToamountFunded;
address public owner;
address[] public funders;
constructor (address _priceFeed) public{
    priceFeed =AggregatorV3Interface(_priceFeed);

     owner = msg.sender; 
}

function Fund() public payable{

    uint256 minimumUSD = 50 * 10 **18;
    require (getConversionRate(msg.value)=>minimumUSD, "You Need To spend More Eth!!");

    addressToamountFunded[msg.sender] += msg.value;
    funders.push(msg.sender);
    //ETH to USD conversion rate 
}
function getVersion()public view returns(uint256){
     
         return priceFeed.version();
}

function getPrice()public view returns(uint256 ){
 
    (,int256 answer,,,)=priceFeed.latestRoundData();
  return uint256(answer * 1000000000000);
}

function getConversionRate(uint256 ethAmount)public view returns(uint256){
    uint256 ethPrice = getPrice();
    uint256 ethAmountInUsd = (ethPrice*ethAmount) * 1000000000000000000;
    return ethAmountInUsd;  
}

modifier onlyOwner{
    //require owner 
    require (msg.sender == owner);
    _;
}
 function getEntranceFee()public view returns(uint256 ){
     uint256 minimumUSD = 50 *10  **18;
     uint256 price = getPrice();
     uint256 precision= 1 * 10 ** 18;
     return(minimumUSD * precision )/price ;
 }
 
function withdraw() payable public {
     msg.sender .transfer(address(this).balance);
    for(uint256 fundersIndex=0; fundersIndex < funders.length; fundersIndex++){
        address funder = funders[fundersIndex];
        addressToamountFunded [funder] = 0;
    }
   funders = new address[](0);
}

}
