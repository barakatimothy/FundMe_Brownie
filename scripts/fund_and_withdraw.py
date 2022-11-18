from webbrowser import get
from brownie import FundMe
from scripts.helpful_scripts import get_account
def fund():
    fund_me =FundMe[-1]
    accounts= get_accounts()
    entranceFee = fund_me.getaEntranceFee()
    print(entranceFee)
    print(f'the entrence fee is {entranceFee}')
    fund_me.fund({'from':accounts,'value': entranceFee})
def Withdraw():
   fund_me=FundMe[-1]
   accounts= get_account()
   fund_me.withdraw({'from':accounts,})


def main():
 fund()
 withdraw( )