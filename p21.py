import math as m
import numpy as np

import time
start_time = time.time()

def findfac(n):
	faclist = [1]
	for i in range(2, int(m.sqrt(n) + 2)):
		if n%i == 0:
			if i not in faclist:
				faclist.append(i)
				if n/i not in faclist:
					faclist.append(n/i)
	return np.asarray(faclist).sum()

Sum = 0

for i in range(10,10000):
	temp = findfac(i)
	if findfac(temp) == i and i != temp:
		Sum += i

print Sum
print("--- %s seconds ---" % (time.time() - start_time))