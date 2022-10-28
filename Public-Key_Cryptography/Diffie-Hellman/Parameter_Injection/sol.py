from pwn import *
import json
from random import randint
# nc socket.cryptohack.org 13371
io = remote("socket.cryptohack.org",13371)
intercepted = {"p": "0xffffffffffffffffc90fdaa22168c234c4c6628b80dc1cd129024e088a67cc74020bbea63b139b22514a08798e3404ddef9519b3cd3a431b302b0a6df25f14374fe1356d6d51c245e485b576625e7ec6f44c42e9a637ed6b0bff5cb6f406b7edee386bfb5a899fa5ae9f24117c4b1fe649286651ece45b3dc2007cb8a163bf0598da48361c55d39a69163fa8fd24cf5f83655d23dca3ad961c62f356208552bb9ed529077096966d670c354e4abc9804f1746c08ca237327ffffffffffffffff", "g": "0x02", "A": "0x7ea16778cc6cecda997493df4b4295a0f1858c4d0b4490f21fd17b3d2c71456e83780c08317d16b19ba3d6d150cb064a63ef7c08482109c2fe8dfa1bab1d10ef4198e4be7e6459ad1ef376ff7339bdbdaae1b520b4721ae1558e4650352668fad28a09a790ac7d9b48d939f5c5482ff41ddfd12fdd4f28776a9c2858716db98d4e906bfdfd83e64d6502b16e177d3cd756aa0743f2b5c5118d2f67ed438836a37c8df41de6fafb8aa3caacbf91e7c959fa254c377ba39a76d92c2985988980ec"}

p = int(intercepted['p'],16)
g = int(intercepted['g'],16)
A = int(intercepted['A'],16)

b = randint(1,p)

s = pow(A,b,p)
B = pow(g,b,p)

bob = {"p" : hex(p),"g" : hex(g),"B" : hex(B)}
print(bob)
# def json_recv():
#     line = io.recvline()
#     return json.loads(line.decode())


# data = json_recv()