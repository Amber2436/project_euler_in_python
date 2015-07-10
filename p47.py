__author__ = 'xueyishu'

import math as m

def is_prime(number):
	if number == 1:
		return False
	elif number in [2, 3, 5]:
		return True
	elif number%2 == 0:
		return False
	else:
		cap = int(m.sqrt(number)) + 2
		for each in range(3, cap, 2):
			if number % each == 0:
				return False
		return True

def findprimefactor(n):
	mylist = []
	for i in range(2, int(m.sqrt(n) + 1)):
		if n%i == 0:
			if i not in mylist:
				mylist.append(i)
			if n/i not in mylist:
					mylist.append(n/i)
	newlist = []
	for number in mylist:
		if is_prime(number) == True:
			newlist.append(number)
	return newlist


n = 1000

while True:
	temp1 = findprimefactor(n)
	temp2 = findprimefactor(n+1)
	temp3 = findprimefactor(n+2)
	temp4 = findprimefactor(n+3)
	if len(temp1) == 4 and len(temp2) == 4 and len(temp3) == 4 and len(temp4) == 4:
		print n, n+1, n+2, n+3
		break
	n += 1