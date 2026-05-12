import sys
import math

val = 1000

for i in range(1, val):
	for j in range(i, val):
		for k in range(j, val):
			if(i + j + k) == val:
				if(i ** 2 + j ** 2) == k ** 2:
					print(i * j * k)
