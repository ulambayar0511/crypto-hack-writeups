from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import hashlib

from rsa import encrypt


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

# iv =  "737561146ff8194f45290f5766ed6aba"
# shared_secret = 1547922466740669851136899009270554812141325611574971428561894811681012510829813498961168330963719034921137405736161582760628870855358912091728546731744381382987669929718448423076919613463237884695314172139247244360699127770351428964026451292014069829877638774839374984158095336977179683450837507011404610904412301992397725594661037513152497857482717626617522302677408930050472100106931529654955968569601928777990379536458959945351084885704041496571582522945310187
# ciphertext = "39c99bf2f0c14678d6a5416faef954b5893c316fc3c48622ba1fd6a9fe85f3dc72a29c394cf4bc8aff6a7b21cae8e12c"
# print(decrypt_flag(shared_secret,iv,ciphertext))


# a = {"iv": "ea9261f0cad99d612332455a703c25d0", "encrypted_flag": "864f938eafdeab8f9b3fd5c0c84694ed635d05be180e4e8e8b9f8ef92bb9907d"}
# b = {"B": "0x4f783c39acde31cc26c22d4b3dbe5cf43f3c38fe775d1cce00f515a5e876f661dbb7bcbc580ced5240a4451d6ea3fca9c0ea8e03a89524d26ee11afe60f812696dd12218afea99d502e292dc05ed4fb2a29d49c7693823321646bde1e431f3397655d8d716c4901f202eaecb7093f950182624cacf2463cb6c27132c96bdb39630482bad46eca8cabe9c6e5d00661c8a290dfe73cd5efe68ea6a3029d9ccfc326d52adc685dc8285f268d9b7a5ac38b7aa5191332ceb8da8c638360da69ee4b9"}

# I sent Alice's info to Bob and then I didn't care about Bob answer :
# I just sent {B:"0x1"} (which is possible because g is supposed to be a generator) to Alice so that I know the shared key which is 1 ^^
shared_secret = 1
iv = "cb08876ff75cf9c13d42c038e439c5a0"
ciphertext = "e5a11b7dd03bfee8db4988f371cb8780e1f8c453b625a13d0e1bbb5620612bd9"
print(decrypt_flag(shared_secret, iv, ciphertext))

# crypto{n1c3_0n3_m4ll0ry!!!!!!!!}