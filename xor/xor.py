# XOR is a bitwise operator which returns 0 if the bits are the same, and 1 otherwise. In textbooks the XOR operator is denoted by ⊕, but in most challenges and programming languages you will see the caret ^ used instead.



data = "label"

flag = ''.join([chr(13 ^ ord(i)) for i in data])

print("crypto{" + flag  +'}')