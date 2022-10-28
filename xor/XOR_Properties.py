# There are four main properties we should consider when we solve challenges using the XOR operator


# Commutative: A ⊕ B = B ⊕ A
# Associative: A ⊕ (B ⊕ C) = (A ⊕ B) ⊕ C
# Identity: A ⊕ 0 = A
# Self-Inverse: A ⊕ A = 0 
from pwn import xor

KEY1 = "a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313"
# KEY2 ^ KEY1 = 37dcb292030faa90d07eec17e3b1c6d8daf94c35d4c9191a5e1e
result = "37dcb292030faa90d07eec17e3b1c6d8daf94c35d4c9191a5e1e"
KEY2 = bytes([i ^ j for i, j in zip(bytes.fromhex(KEY1),bytes.fromhex(result))])
# KEY2 ^ KEY3 = c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1
result = "c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1"
KEY3 = bytes([i ^ j for i, j in zip(KEY2,bytes.fromhex(result))])
# FLAG ^ KEY1 ^ KEY3 ^ KEY2 = 04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf 
result = "04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf"
flag = bytes([i ^ j ^ k^m for i, j,k,m in zip(KEY2,KEY3,bytes.fromhex(KEY1),bytes.fromhex(result))])
print(flag)


## best solution

# from pwn import xor
# k1=bytes.fromhex('a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313')
# k2_3=bytes.fromhex('c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1')
# flag=bytes.fromhex('04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf')
# print(xor(k1,k2_3,flag))  