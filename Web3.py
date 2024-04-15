from web3 import Web3

web3 = Web3(Web3.HTTPProvider('http://localhost:8545'))

accounts = web3.eth.accounts

for account in accounts:
    balance = web3.eth.get_balance(account)
    print(f'Аккаунт: {account}, Баланс: {web3.from_wei(balance, "ether")} ETH')

