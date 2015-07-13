__author__ = 'xueyishu'

import math as m 

def is_prime(number):
	if number in [2, 3, 5]:
		return True
	else:
		cap = int(m.sqrt(number)) + 2
		for each in range(3, cap, 2):
			if number % each == 0:
				return False 
		return True

answer = 0

for each in range(1,1000000,2):
	if is_prime(each): # skip this number if it is a prime
		pass
	else:
		ind = False
		for number in range(each):
			diff = each - 2*number**2
			if diff < 0:
				ind = True
				answer = each
				break
			if is_prime(diff): # if it still satisfies the conjecture
				break
		if ind:
			print(answer)
			break
