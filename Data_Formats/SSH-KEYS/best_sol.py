from base64 import b64decode
with open('bruce_rsa.pub', 'r') as file:
    raw = file.read()

_, keydata, _ = raw.split()
keydata = b64decode(keydata)
parts = []
while keydata:
    length = int.from_bytes(keydata[:4], 'big')
    parts.append(keydata[4:4+length])
    keydata = keydata[4+length:]

_, e, n = [int.from_bytes(part, 'big') for part in parts]
print(f'{e = }')
print(f'{n = }')