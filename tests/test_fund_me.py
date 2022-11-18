from contracts.scripts.helpful_scripts import LOCAL_BLOCKCHAIN
from scripts.fund_and_withdraw import fund
from scripts.helpful_scripts import get_account
from scripts.deploy import deploy_fund_me, fund_me
from brownie import exceptions,network,accounts

def can_fund_and_withdraw():
    accounts = get_accounts()
    fund_me = deploy_fund_me()
    entranceFee = fund_me.getEntramceFee()
    tx = fund_me.fund({'from':accounts,'value':entranceFee })
    tx.wait(1)
    assert fund_me.addressToAmountFunded(accounts.address)== entranceFee    
    tx2 = fund_me.withdraw({'from':account,'value':entranceFee  })
    tx2.wait(1)
    assert fund_me.addressToAmountFunded(accounts.address) == 0
def only_owner_withdraw():
    if network.show_active() not in LOCAL_BLOCKCHAIN:
        pytest.skip('only for local test')
    fund_me=deploy_fund_me( )
    bad_actor=accounts.add()
    fund_me.withdraw({'from':bad_actor})
    with pytest.raises(exceptions.VirtualMachineError):
     fund_me.withdraw({'from':bad_actor})   

def main():
    can_fund_and_withdraw()