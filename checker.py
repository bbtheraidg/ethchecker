from web3 import Web3

while True:
    # Your code here
    print("ETH_Eater!")  # Create an Ethereum account
w3 = Web3()
account = w3.eth.account.create()

# Print the private key and address
print(f"Private Key: {w3.to_hex(account.key)}")
print(f"Address: {account.address}")

web3.eth.get_balance("Address: {account.address}")
