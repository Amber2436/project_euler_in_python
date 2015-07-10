def findsol(n):
	count = 0
	for i in range(1,int(n/3)+1):
		for j in range(int(n/3)-1,2*int(n/3)+1):
			if i**2+j**2 == (n-i-j)**2:
				count +=1
	return count

def maxsol(n):
	max = 0
	for i in range(1,n+1):
		temp = findsol(i)
		if temp == 7:
			print i 

print maxsol(1000)