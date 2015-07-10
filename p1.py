def msearch(n):
	number = 1
	sum = 0
	while number < n :
		if number % 3==0 or number %5==0:
			sum = sum + number 
		number = number +1
	return sum


a = msearch(1000)
print a