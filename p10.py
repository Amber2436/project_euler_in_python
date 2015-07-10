def is_prime(n):
    # look for factors of 2 first
    if n % 2 == 0: return False
    # now look for odd factors
    p = 3
    while p < n**0.5+1:
        if n % p == 0: return False
        p += 2
    return True

def sumprime(n):
	summ = 0
	i = 1
	for i in range(1,n+1):
		if is_prime(i) ==True:
			summ = summ + i 
			i = i + 2
	return summ 

print sumprime(2000000)