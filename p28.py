import numpy
def spdiag(n):
	a = numpy.array([1])
	for i in range(1,n+1):
		a = numpy.append(a,[a[-1]+2*i,a[-1]+4*i,a[-1]+6*i,a[-1]+8*i])
	return a 

print sum(spdiag(500))


###王屌的大法 

a = 1 
for i in range(0,500):
	a = a + 4*(1001-2*i)**2 - 6 * (1001 - 2*i -1)
print a 