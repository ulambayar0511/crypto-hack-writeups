from Crypto.PublicKey import RSA
# Extract the private key d as a decimal integer from this PEM-formatted RSA key.
key = RSA.importKey(open('/home/ulmaa/ctf/cryptohack/Data_Formats/Privacy-Enhanced Mail/privacy_enhanced_mail.pem').read())
print(key.d)
print(key.n)
print(key.e)
print(key.p)
print(key.q)
