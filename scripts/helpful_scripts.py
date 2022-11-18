from brownie import network,config,accounts,MockAggregatorV3
from web3 import Web3


decimals=8
startingPrice=200000000
FORKED_BLOCKCHAIN=['mainnet-fork','mainnet-fork-dev']
LOCAL_BLOCKCHAIN=['development','ganache-loacl']

def get_accounts():
    if network.show_active() in LOCAL_BLOCKCHAIN:
        return accounts[0]
    else:
       return accounts.add(config["wallets"]["from_key"])



def deploy_mocks():
    print(f'Active Networks {network.show_active}')
    print('deploying Mock')
    if len(MockAggregatorV3)<=0:
     MockAggregatorV3.deploy(decimals,Web3.toWei(startingPrice,'ethers'),{'from ': account})