# As we've seen, we can work within a finite field Fp, adding and multiplying elements, and always obtain another element of the field.

# For all elements g in the field, there exists a unique integer d such that g * d ≡ 1 mod p.

# This is the multiplicative inverse of g.


# What is the inverse element: 3 * d ≡ 1 mod 13?

'''
We can do some magic like this:
Note: i'll use math notation, so a^b means pow(a,b)
        a^(p-1) = 1 (mod p)
        a^(p-1) * a^-1 = a^-1 (mod p)
        a^(p-2) * a * a^-1 = a^-1 (mod p)
        a^(p-2) * 1 = a^-1 (mod p)
So finally we have:
        a^(p-2) = a^-1 (mod p)
So, doing a^(p-2) and then (mod p) we can achieve
our result 
'''

a = 3
p = 13
print(pow(a,p-2) % p)
print(pow(a, -1, p))
for i in range(13):
    if (3 * i) % 13 == 1:
        print(i)