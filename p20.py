def power(n):
	return 2**n 

def sum_digits2(n):
    s = 0
    while n:
        n, remainder = divmod(n, 10)
        s += remainder
    return s

print sum_digits2(power(1000))