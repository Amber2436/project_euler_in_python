from numpy import *
def sumdif(n):
	a = arange(n)+1
	b = sum(a**2)
	c = (sum(a))**2
	print "the difference is %s" %(c-b)

sumdif(100)
