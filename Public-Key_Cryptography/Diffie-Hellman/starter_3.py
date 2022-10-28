# The Diffie-Hellman protocol is used because the discrete logarithm is assumed to be a "hard" computation for carefully chosen groups.

# The first step of the protocol is to establish a prime p and some generator of the finite field g. These must be carefully chosen to avoid special cases where the discrete log can be solved with efficient algorithms. For example, a safe prime p = 2*q +1 is usually picked such that the only factors of p - 1 are {2,q} where q is some other large prime. This protects DH from the Pohlig–Hellman algorithm.

# The user then picks a secret integer a < p and calculates g^a mod p. This can be transmitted over an insecure network and due to the assumed diffculty of the discrete logarithm, if the protocol has been implemented correctly the secret integer should be infeasible to compute.

# Given the NIST parameters:

g  = 2

p = 2410312426921032588552076022197566074856950548502459942654116941958108831682612228890093858261341614673227141477904012196503648957050582631942730706805009223062734745341073406696246014589361659774041027169249453200378729434170325843778659198143763193776859869524088940195577346119843545301547043747207749969763750084308926339295559968882457872412993810129130294592999947926365264059284647209730384947211681434464714438488520940127459844288859336526896320919633919

# Calculate the value of g^a mod p for

a =  972107443837033796245864316200458246846904598488981605856765890478853088246897345487328491037710219222038930943365848626194109830309179393018216763327572120124760140018038673999837643377590434413866611132403979547150659053897355593394492586978400044375465657296027592948349589216415363722668361328689588996541370097559090335137676411595949335857341797148926151694299575970292809805314431447043469447485957669949989090202320234337890323293401862304986599884732815


print(a < p)

print(pow(g,a,p))