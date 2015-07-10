__author__ = 'xueyishu'

import math as m

def primegen(n):
    primelist = [1009]
    i = 1011
    while primelist[-1] < n:
        ind = 0
        for j in range(2,int(m.sqrt(i))+1):
            if i%j == 0:
                ind += 1
        if ind == 0:
            primelist.append(i)
            i += 2
        else:
            i+= 2
    return primelist


primelist = primegen(10000)

for i in range(len(primelist)):
	a = primelist[i]
	for j in range(i+1, len(primelist)):
		b = primelist[j]
		for k in range(j+1, len(primelist)):
			c = primelist[k]
			temp1 = set(list(str(a)))
			temp2 = set(list(str(b)))
			temp3 = set(list(str(c)))
			if temp1 == temp2 and temp2 == temp3 and b - a == c - b and a != b:
				print a, b, c