__author__ = 'xueyishu'

import math as m

def is_prime(n):
	if n == 1:
		return False
	elif n in [2,3,5]:
		return True
	else:
		ind = True
		for j in range(2, int(m.sqrt(n) + 2)):
			if n % j == 0:
				ind = False
		return ind

def is_pandigital(x, digits):
	s = [True] * digits
	digits = [i for i in range(1, digits + 1)]
	x = str(x)

	if len(x) < digits[-1]:
		# Your number is incorrect, it needs to contain all the digits 1-n
		return False

	for i in range(len(x)):
		check = int(x[i])
		try:
			if s[check - 1]:
				s[check - 1] = False

			else:
				return False

		except IndexError:
			return False

	return True

n = 7654321
while not(is_pandigital(n, 7) and is_prime(n)):
    n -= 2

print "Project Euler 41 Solution =", n