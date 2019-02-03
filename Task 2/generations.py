from btctools import *


def generate_private_address(private_hex):
    private_wif = PrivateKey.from_hex(private_hex)
    return private_wif.wif(compressed=False)


def generate_public_address(private_wif):
    private_key = PrivateKey.from_wif(private_wif)
    public_key = private_key.to_public()
    public_address = public_key.to_address('P2PKH', compressed=False)
    return public_address
