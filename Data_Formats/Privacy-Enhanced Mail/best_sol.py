"""
Well, I found here a good description of ASN.1 field structure for a RSA PEM file
https://tls.mbed.org/kb/cryptography/asn1-key-structures-in-der-and-pem
RSAPrivateKey ::= SEQUENCE {
  version           Version,
  modulus           INTEGER,  -- n
  publicExponent    INTEGER,  -- e
  privateExponent   INTEGER,  -- d
  prime1            INTEGER,  -- p
  prime2            INTEGER,  -- q
  exponent1         INTEGER,  -- d mod (p-1)
  exponent2         INTEGER,  -- d mod (q-1)
  coefficient       INTEGER,  -- (inverse of q) mod p
  otherPrimeInfos   OtherPrimeInfos OPTIONAL
}
Using the description, we can try to parse the file w/o Crypto package (from Crypto.PublicKey import RSA)
As for the challenge, we should extract d
 aka privateExponent
I used this library to sort out
https://python-asn1.readthedocs.io/en/latest/readme.html
"""

import asn1
import base64

struct_fields = (
    'version',
    'modulus',
    'publicExponent',
    'privateExponent',
    'prime1',
    'prime2',
    'exponent1',
    'exponent2',
    'coefficient',
)


def read_file(file_path):
    """Read bytes form the file"""
    with open(file_path, 'r') as pem_file:
        b64str = ''.join(line.rstrip() for line in pem_file if not line.startswith('-----'))
    return base64.b64decode(b64str)


def decode_pem(enc_bytes):
    decoder = asn1.Decoder()

    # Read sequence (see the format above)
    decoder.start(enc_bytes)
    # read() returns a tuple (tag_info, value). The value of the sequence tag is asn.1 encoded items
    seq = decoder.read()[1]

    # Read elements of the sequence
    decoder.start(seq)
    # Create a dictionary for all rsa fields. In fact, no need to read all fields to solve the challenge, just curious.
    # Python asn package returns int for all asn.1 INTEGER - so we do not need to decode tag values.
    decoded_fields = {field: decoder.read()[1] for field in struct_fields}
    return decoded_fields


if __name__ == '__main__':
    enc_rsa = read_file('/home/ulmaa/ctf/cryptohack/Data_Formats/Privacy-Enhanced Mail/privacy_enhanced_mail.pem')
    dec_rsa = decode_pem(enc_rsa)
    print('d key:', dec_rsa['privateExponent'])