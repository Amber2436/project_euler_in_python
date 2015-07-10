a = 9**5 *5
from numpy import *

def findlist(n):
	b = arange(0)
	for i in range(2,n+1):
		if sum( [ int(x)**5 for x in str(i) ] ) == i:
			b = append(b,i)
	return b 

print sum(findlist(a))
