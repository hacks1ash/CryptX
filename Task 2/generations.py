from cryptotools.btctools import *


def generate_private_address(private_hex):
    private_wif = PrivateKey.from_hex(private_hex)
    return private_wif


def generate_public_address(private_wif):
    public_key = private_wif.to_public()
    public_address = public_key.to_address('P2PKH')
    return public_address
