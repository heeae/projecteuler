import sys
import math
from math import gcd
def p33():
	nums, dens = 1, 1
	for a in range(1, 10):
		for b in range(a, 10):
			for c in range(1, 10):
				if (10*a + b) * c == (10*b + c) * a and a < c:
					nums *= a
					dens *= c
	return dens // gcd(nums, dens)

print(p33())