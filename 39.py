import sys
import math


for i in range(1, 1001):
    soln = 0
    for j in range(1, 1000):
        for k in range(1, i - j):
            if i - j - k <= 0:
                break
            if j ** 2 + k ** 2 == (i - j - k) ** 2:
                soln += 1
    if(soln > 0):
        print(i, soln)
