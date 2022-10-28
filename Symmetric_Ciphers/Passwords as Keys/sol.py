import requests
import hashlib
from Crypto.Cipher import AES

BASE_URL = "http://aes.cryptohack.org/passwords_as_keys"

with open("/home/ulmaa/ctf/cryptohack/Symmetric_Ciphers/Passwords as Keys/words.txt") as f:
    words = [w.strip() for w in f.readlines()]


r = requests.get(BASE_URL+"/encrypt_flag/")
ciphertext_hex = r.json()['ciphertext']

ciphertext = bytes.fromhex(ciphertext_hex)

for i in words:
    key = hashlib.md5(i.encode()).hexdigest()
    r = requests.get(BASE_URL+"/decrypt/"+ciphertext+'/'+key+'/')
    flag = bytes.fromhex(r.json()['plaintext'])
    check = str(flag)[2:-1]
    if check.startswith("crypto"):
        print(flag)


