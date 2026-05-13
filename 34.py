import sys
import math

for i in range(10, 10000000):
	s = str(i)
	sum = 0
	for j in s:
		sum += math.factorial(int(j))
	if sum == i:
		print(i)

