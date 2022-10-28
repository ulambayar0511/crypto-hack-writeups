from pwn import * # pip install pwntools
import json
from Crypto.Util.number import *
import codecs
r = remote('socket.cryptohack.org', 13377, level = 'debug')

def decrypt(encoding,msg):
    if encoding == "base64":
        encoded = base64.b64decode(msg) # wow so encode
    elif encoding == "hex":
        encoded = bytes.fromhex(msg)
    elif encoding == "rot13":
        encoded = codecs.encode(msg,'rot_13')
    elif encoding == "bigint":
        encoded = bytes.fromhex(msg[2:])
    elif encoding == "utf-8":
        encoded = ''.join([chr(i) for i in msg])
    return encoded

def json_recv():
    line = r.recvline()
    return json.loads(line.decode())

def json_send(hsh):
    request = json.dumps(hsh).encode()
    print("request: ",request)
    r.sendline(request)

for i in range(101):
    received = json_recv()
    print("Received type: ",received["type"])
    encoding = received["type"]
    print("Received encoded value: ",received["encoded"])
    msg = received["encoded"]
    send_data = decrypt(encoding,msg)
    if type(send_data) == bytes:
        send_data = str(send_data)[2:-1]
    to_send = {
        "decoded": send_data
    }
    print(to_send)
    json_send(to_send)

