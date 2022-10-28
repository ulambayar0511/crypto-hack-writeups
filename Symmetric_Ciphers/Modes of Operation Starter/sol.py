#!/usr/bin/env python

"""
Cryptohack - Block Cipher Mode Starter
Solution using the requests Python module
Ref:
    https://docs.python-requests.org/en/master/user/quickstart
"""

import requests

BASE_URL = "http://aes.cryptohack.org/block_cipher_starter"

# 1) get the ciphertext of the encrypted flag
r = requests.get(f"{BASE_URL}/encrypt_flag")
data = r.json()
ciphertext = data["ciphertext"]
print("ciphertext", ciphertext)

# 2) send the ciphertext to the decrypt function
r = requests.get(f"{BASE_URL}/decrypt/{ciphertext}")
data = r.json()
plaintext = data["plaintext"]
print("plaintext", plaintext)

# 3) convert from hex to ASCII to have the flag
print("flag", bytearray.fromhex(plaintext).decode())