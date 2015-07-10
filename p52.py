from numpy import append 
def makedig(n):
	setdi = ()
	for i in str(n):
		setdi = append(setdi,i)
	return set(setdi)

for i in range(100000,166666):
	if makedig(i)==makedig(2*i)==makedig(3*i)==makedig(4*i)==makedig(5*i)==makedig(6*i):
		print i 