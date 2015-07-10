def sqdig(n):
	a = 0
	for i in str(n):
		a += int(i)**2
	return a 

def findsqdig(k):
	n = 1
	count = k-1;
	while n < k:
		temp = n
		while temp != 89:
			temp = sqdig(temp)
			if temp == 1:
				count -= 1
				break
		n += 1
	return count

print findsqdig(10000000)