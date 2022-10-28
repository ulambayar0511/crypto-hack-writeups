# We say that an integer x is a Quadratic Residue if there exists an a such that a2 = x mod p
# 1 . Quadratic Residue

# Quadratic Residue : An integer called as quadratic residue = >

# a² = x mod p => a²-x =k*p1 . Quadratic Residue

# Quadratic Residue : An integer called as quadratic residue = >

# a² = x mod p => a²-x =k*p
p = 29
ints = [14, 6, 11]

qr = [a for a in range(p) if pow(a,2,p) in ints]
print(f"flag {min(qr)}")