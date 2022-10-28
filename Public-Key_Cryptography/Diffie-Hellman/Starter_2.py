# Every element of a finite field Fp can be used to make a subgroup H under repeated action of multiplication. In other words, for an element g: H = {g, g^2, g^3, ...}

# A primitive element of Fp is an element whose subgroup H = Fp, i.e., every element of Fp, can be written as g^n mod p for some integer n. Because of this, primitive elements are sometimes called generators of the finite field.

# For the finite field with p = 28151 find the smallest element g which is a primitive element of Fp. 

# g: H = {g, g^2, g^3, ...}

def is_generator(k, p):
  for n in range(2, p):
    if pow(k, n, p) == k:
      return False
  return True

p = 28151
for k in range(p):
  if is_generator(k, p):
    print(k)