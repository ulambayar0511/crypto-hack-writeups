# Python program to demonstrate working of extended
# Euclidean Algorithm

# Let a and b be positive integers.

# The extended Euclidean algorithm is an efficient way to find integers u,v such that

# a * u + b * v = gcd(a,b)
# function for extended Euclidean Algorithm
def gcdExtended(a, b):
	# Base Case
	if a == 0 :
		return b,0,1
			
	gcd,x1,y1 = gcdExtended(b%a, a)
	
	# Update x and y using results of recursive
	# call
	x = y1 - (b//a) * x1
	y = x1
	
	return gcd,x,y
	

# Driver code
a, b = 26513,32321
g, x, y = gcdExtended(a, b)
print("gcd(", a , "," , b, ") = ", x,y,g)
