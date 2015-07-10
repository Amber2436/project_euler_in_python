import numpy as np 
def fibonacci(n):
	tsum = 0
	a = np.zeros(n)
	a[0] = 1
	a[1] = 2
	for i in range(2,n):
		a[i] = a[i-1] + a[i-2]
	
	a = a[a % 2 ==0]
	return sum(a[a<4000000])

print(fibonacci(50))
