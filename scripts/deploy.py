import imp
from browmie import  FundMe,MockAggregatorV3, config
from contracts.scripts.helpful_scripts import FORKED_BLOCKCHAIN
from scripts.helpful_scripts import deploy_mocks, get_accounts,LOCAL_BLOCKCHAIN


def deploy_fund_me():
    
 account=get_account()
 if network.show_active() not in LOCAL_BLOCKCHAIN or network.show_active() in FORKED_BLOCKCHAIN:
    price_feed_address= config['networks'][networks.show_active()]['eth_usd_pricefeed']
 else:
   deploy_mocks() 
   price_feed_address= MockAggregatorV3[-1].address
    

   fund_me=FundMe.deploy('0x',{'from':account},publish_source=config['networks'][networks.show_active()].get('verify'))
   print(f'contract deployed to {fund_me.address}')
   return fund_me

def main():
    deploy_fund_me()