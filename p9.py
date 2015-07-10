def findpytha(n):
	a = 0
	b = 0
	n1 = int(float(n)/3)+1
	for i in range(1,n1+1):
		for j in range(n1+1,n-n1+1):
			if (n-i-j)**2==i**2+j**2:
				a = i 
				b = j 
	return a*b*(n-a-b)



print findpytha(1000)