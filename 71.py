import sys
import math


maxPair = (1, 7)
for d in range(2, 1000001):
    n = math.floor((3*d - 1) / 7)
    if maxPair[1] * n > maxPair[0] * d :
        maxPair = (n, d)

print("Result", 3/7,  maxPair)

    
