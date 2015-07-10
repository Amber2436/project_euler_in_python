from numpy import append
def digisum(n):
	summ = 0
	for i in str(n):
		summ += int(i)
	return summ 

def findmax(n):
	max = 0
	a = ()
	for i in range(1, n):
		for j in range(1, n):
			a = append(a,digisum(i**j))
	return a 

print max(findmax(100))

