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
        print(plaintext)
        return plaintext.decode('ascii')
# p = 
for i in range(2,p):

    shared_secret = i
    iv = "0c848ab12ce56007d40b107a2772255e"
    ciphertext = "d169f135de26e4f135009e1bb7bcea8ee41c613f04f72c0e7bb91c9d94728cbb"
    print(decrypt_flag(shared_secret, iv, ciphertext))
