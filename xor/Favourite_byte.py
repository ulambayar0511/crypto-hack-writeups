# I've hidden some data using XOR with a single byte, but that byte is a secret?
output = bytes.fromhex("73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d")
for key in range(256):
    flag = [chr(key ^ byte) for byte in output]
    if ''.join(flag).startswith("crypto"):
        print(f"{key} : {''.join(flag)}")

## BEST SOLUTION

# input_str = bytes.fromhex('73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d')

# key = input_str[0] ^ ord('c')
# print(''.join(chr(c ^ key) for c in input_str))
