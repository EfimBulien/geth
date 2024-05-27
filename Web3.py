from web3 import Web3

web3 = Web3(Web3.HTTPProvider('http://localhost:8545'))

accounts = web3.eth.accounts

for account in accounts:
    balance = web3.eth.get_balance(account)
    print(f'Аккаунт: {account}, Баланс: {web3.from_wei(balance, "ether")} ETH')

#/Users/efim/geth-1.11.6/geth --datadir initBlockchain --networkid 1234 --http --http.corsdomain "*" --unlock 0x115592657925116dC719316450E4862CB1713A30 --allow-insecure-unlock --http.api "eth,web3,personal,net" --nodiscover --verbosity 3 --mine --miner.etherbase 0x115592657925116dC719316450E4862CB1713A30
#/Users/efim/geth-alltools-1.11.6/geth --datadir initBlockchain --networkid 1234 --http --http.corsdomain "*" --unlock 0x115592657925116dC719316450E4862CB1713A30 --allow-insecure-unlock --http.api "eth,web3,personal,net" --nodiscover --verbosity 3 --mine --miner.etherbase 0x115592657925116dC719316450E4862CB1713A30