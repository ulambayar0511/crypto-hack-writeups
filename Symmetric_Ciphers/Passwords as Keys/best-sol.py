from Crypto.Cipher import AES
import hashlib

ciphertext = bytes.fromhex('c92b7734070205bdf6c0087a751466ec13ae15e6f1bcdd3f3a535ec0f4bbae66')

with open("/home/ulmaa/ctf/cryptohack/Symmetric_Ciphers/Passwords as Keys/words.txt") as f:
    words = [w.strip() for w in f.readlines()]

for w in words:
    key = hashlib.md5(w.encode()).digest()

    cipher = AES.new(key, AES.MODE_ECB)
    decrypted = cipher.decrypt(ciphertext)

    if b'crypto' in decrypted:
      print("plaintext", decrypted)
      print("password_hash", key.hex())
      exit