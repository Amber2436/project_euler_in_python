from math import factorial 
def digifac():
	i = 1
	while i:
		suma = sum(factorial(int(x)) for x in str(i))
		if suma == i:
			print i 
		i +=1

print digifac()
