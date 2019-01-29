import secrets
from generations import generate_private_address, generate_public_address

PUBLIC_ADDRESS = '1PMycacnJaSqwwJqjawXBErnLsZ7RkXUAs'


def find_match():
    while True:
        private_hex = secrets.token_hex(32)
        private_wif = generate_private_address(private_hex)
        public_address = generate_public_address(private_wif)

        if public_address == PUBLIC_ADDRESS:
            print(private_hex)
            print(private_wif)
            break


if __name__ == '__main__':
    find_match()
