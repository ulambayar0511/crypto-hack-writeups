from pwn import * # pip install pwntools
import json

r = remote('socket.cryptohack.org', 13377, level = 'debug')
def nice(encoding,msg):

    if encoding == "base64":
        encoded = base64.b64decode(msg) # wow so encode
    elif encoding == "hex":
        encoded = self.challenge_words.encode().hex()
    elif encoding == "rot13":
        encoded = codecs.encode(self.challenge_words, 'rot_13')
    elif encoding == "bigint":
        encoded = hex(bytes_to_long(self.challenge_words.encode()))
    elif encoding == "utf-8":
        encoded = [ord(b) for b in self.challenge_words]
def json_recv():
    line = r.recvline()
    return json.loads(line.decode())

def json_send(hsh):
    request = json.dumps(hsh).encode()
    r.sendline(request)


received = json_recv()

print("Received type: ")
print(received["type"])
print("Received encoded value: ")
print(received["encoded"])

to_send = {
    "decoded": "changeme"
}
json_send(to_send)

json_recv()
