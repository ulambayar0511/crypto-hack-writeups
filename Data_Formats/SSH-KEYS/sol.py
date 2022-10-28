from Crypto.PublicKey import RSA
# Extract the private key d as a decimal integer from this PEM-formatted RSA key.
key = RSA.importKey(open('/home/ulmaa/ctf/cryptohack/Data_Formats/SSH-KEYS/brute_rsa.pub').read())

print(f"n: {key.n}")

## aliter method is to convert the .pub file into a .pem file using : ssh-keygen -f bruce_rsa.pub -e -m pem 