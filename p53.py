from math import factorial

def comb(n, r):
    return factorial(n) // factorial(r) // factorial(n-r)

def numerate(n):
	count = 0
	for i in range(23, n+1):
		for j in range(1, i):
			if comb(i, j) > 1000000:
				count += 1
	return count

print numerate(100)