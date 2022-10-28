A = 4542574910172459638

p = 16007670376277647657

for a in range(2,p):
    if A == pow(2,a,p):
        print(a)
        break