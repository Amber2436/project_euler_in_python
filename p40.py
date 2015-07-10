from numpy import append
a = "1"
for i in (range(2,200000)):
	a += str(i)
#print a,len(str(a))

prod = 1
for j in (0,9,99,999,9999,99999,999999):
	prod = prod * int(a[j])

print prod 