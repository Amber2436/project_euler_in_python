from datetime import date, timedelta

d0 = date(1901, 1, 1)
d1 = date(2000, 12, 31)
numdays = d1 - d0

base = d0

a, b = [], []
count = 0
for x in range(0, 36524):
	temp = base + timedelta(days = x)
	if temp.weekday() == 6 and temp.day == 1:
		count += 1

print count

