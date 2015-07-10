__author__ = 'xueyishu'

def coinsum():
	amount = int(raw_input("Please put in the amount that you would like to decompose: "))
	counter = 0
	for p1 in range(0,amount/1 + 1):
		for p2 in range(0, amount/2 + 1):
			for p5 in range(0, amount/5 + 1):
				for p10 in range(0, amount/10 + 1):
					for p20 in range(0, amount/20 + 1):
						for p50 in range(0, amount/50 + 1):
							for p100 in range(0, amount/100 + 1):
								for p200 in range(0, amount/200 + 1):
									if p1 + 2*p2 + 5*p5 + 10*p10 + 20*p20 + 50*p50 + 100*p100 + 200*p200 == amount:
										counter += 1
	print counter

coinsum()