def lgpal():
	max = 0
	for i in range(100,999):
		for j in range(100,999):
			temp = i*j
			if str(temp) == str(temp)[::-1] and temp > max:
				max = temp 
	return max 

print lgpal()