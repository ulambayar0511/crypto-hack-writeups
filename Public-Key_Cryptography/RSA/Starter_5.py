# I've encrypted a secret number for your eyes only using your public key parameters:

N = 882564595536224140639625987659416029426239230804614613279163

e = 65537
p = 857504083339712752489993810777

q = 1029224947942998075080348647219

phi = (p - 1) * (q - 1)

d = pow(e,-1,phi)
# Use the private key that you found for these parameters in the previous challenge to decrypt this ciphertext:

c = 77578995801157823671636298847186723593814843845525223303932

print(pow(c,d,N))



