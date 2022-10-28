#! /usr/bin/env python3
import json
import pwn

from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import hashlib

def is_pkcs7_padded(message):
    padding = message[-message[-1]:]
    return all(padding[i] == len(padding) for i in range(0, len(padding)))


def decrypt_flag(shared_secret: int, iv: str, ciphertext: str):
    # Derive AES key from shared secret
    sha1 = hashlib.sha1()
    sha1.update(str(shared_secret).encode('ascii'))
    key = sha1.digest()[:16]
    # Decrypt flag
    ciphertext = bytes.fromhex(ciphertext)
    iv = bytes.fromhex(iv)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    plaintext = cipher.decrypt(ciphertext)

    if is_pkcs7_padded(plaintext):
        return unpad(plaintext, 16).decode('ascii')
    else:
        return plaintext.decode('ascii')


def main():
    remote = pwn.remote("socket.cryptohack.org", 13371)

    remote.recvuntil("Intercepted from Alice: ")
    intercepted_from_alice = json.loads(remote.recvline())
    # intercepted_from_alice['p'] = "1"
    remote.recvuntil("Send to Bob: ")
    print(intercepted_from_alice)
    remote.sendline(json.dumps(intercepted_from_alice))

    # We just forward Bobs request.
    remote.recvuntil("Intercepted from Bob: ")
    intercepted_from_bob = json.loads(remote.recvline())
    intercepted_from_bob["B"] = "0x1"
    print(intercepted_from_bob)
    remote.sendline(json.dumps(intercepted_from_bob))

    remote.recvuntil("Intercepted from Alice: ")
    alice_ciphertext = json.loads(remote.recvline())

    shared_secret = 1
    flag = decrypt_flag(shared_secret, alice_ciphertext["iv"], alice_ciphertext["encrypted_flag"])
    pwn.log.info(flag)


if __name__ == "__main__":
    main()

# https://github.com/onealmond/hacking-lab/blob/master/cryptohack/parameter-injection/exploit.py

# crypto{n1c3_0n3_m4ll0ry!!!!!!!!}