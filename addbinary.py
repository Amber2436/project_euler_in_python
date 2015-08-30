__author__ = 'xueyishu'



def addBinary(a, b):
	summ = 0
	for i in range(len(a)):
		summ += 2 ** i * int(a[::-1][i])
	for j in range(len(b)):
		summ += 2 ** j * int(b[::-1][j])
	binary = ""
	while summ:
		binary += str(summ % 2)
		summ /= 2
	print binary[::-1]

