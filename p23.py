__author__ = 'xueyishu'

import math as m
import numpy as np

def check(n):
	s = 0
	for i in xrange(1, n/2 + 1):
		if n%i == 0:
			s += i
	return s > n

abundants = []
for i in range(12, 28123):
	if check(i):
		abundants.append(i)

ind = [False] * 28123

for i in xrange(len(abundants)):
	for j in xrange(i,len(abundants)):
		if abundants[i] + abundants[j] < 28123:
			ind[abundants[i] + abundants[j]] = True

print sum([i for i in xrange(len(ind)) if not (ind[i])])
