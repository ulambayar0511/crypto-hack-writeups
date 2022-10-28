# we will restrict ourselves to the case when p is prime.

# The integers modulo p define a field, denoted Fp.

# A finite field Fp is the set of integers {0,1,...,p-1}, and under both addition and multiplication there is an inverse element b for every element a in the set, such that a + b = 0 and a * b = 1.

# This is because the identity when acted with the operator should do nothing: a + 0 = a and a * 1 = a.

'''
Looking at Fermat's little theorem...
if p is prime, for every integer a:
        pow(a, p) = a mod p
and, if p is prime and a is an integer coprime with p:
        pow(a, p-1) = 1 mod p
So lets check
        pow(273246787654, 65536) mod 65537
Notice that 65536 is exactly 65537-1,
If 273246787654 and 65537 are coprime,
        then the result is one
'''
from math import gcd

a = 273246787654
p = 65537

if gcd(a,p)==1: #a and p are coprime
        print(1)