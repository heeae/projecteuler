import sys
import math

val = int(sys.argv[1])

sumsquare = 0
squaresum = 0
for i in range(1, val + 1):
    sumsquare += i ** 2
    squaresum += i
 
squaresum = squaresum ** 2
 
print(squaresum - sumsquare)
