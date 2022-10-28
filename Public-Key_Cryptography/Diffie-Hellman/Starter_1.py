# Given the prime p = 991, and the element g = 209, find the inverse element d such that g * d mod 991 = 1. 



p = 991

g = 209

for i in range(901):
    if g * i % 991 == 1:
        print(i)