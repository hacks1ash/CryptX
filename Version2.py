import requests
import secrets
from btctools import *


### es yvela functionali unda iyos aseve asynqronuli rata bevriu userze imushaos

def generate_bitcoin_address():
    private_hex = secrets.token_hex(32)  # 64 Character hexdemical private key
    private_key = PrivateKey.from_hex(private_hex)  # WIF
    public_key = private_key.to_public()  # Public Key
    public_address = public_key.to_address('P2PKH')  # Public Address starting with 1
    return public_address


def check_balance(bitcoin_public_address):
    response = requests.get(
        'https://chain.so/api/v2/address/BTC/' + bitcoin_public_address)  # Chain.so API for Checking balances
    if response.status_code == 200:
        content = response.json()
        network = content['data']['network']
        address = content['data']['address']
        balance = float(content['data']['balance'])
        print("Name:", network)
        print("Address:", address)
        print("Total Balance:", balance)
    ########
    # aqedan ukve chaiwereba bazashi monacemebi


def check_balanaces(bitcoin_public_address_list):
    for address in bitcoin_public_address_list:
        check_balance(address)
