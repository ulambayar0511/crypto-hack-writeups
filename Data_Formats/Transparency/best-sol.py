import hashlib
from Crypto.PublicKey import RSA

pem = open('transparency.pem', 'r').read()

key = RSA.importKey(pem).public_key()

der = key.exportKey(format='DER')

sha256 = hashlib.sha256(der)

sha256_fingerprint = sha256.hexdigest()

print(f"Public Key SHA256: {sha256_fingerprint}")
