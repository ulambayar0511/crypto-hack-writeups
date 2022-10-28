from pwn import xor

# I've encrypted the flag with my secret key, you'll never be able to guess it. 
flagBytes = bytes.fromhex('0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104')
key = xor(flagBytes, b"crypto{")
print(key)
flag = xor(flagBytes, b"myXORkey").decode('utf-8')
print(flag)

# print(''.join(chr(c ^ key) for c in input_str))
