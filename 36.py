import sys
import math

def isPaluibrome(x):
    s = str(x)
    return s == s[::-1]

rst = 0
for i in range(1, 1000000):
    if isPaluibrome(i) and isPaluibrome(bin(i)[2:]):
        print(i)
        rst += i

print("Result: " + str(rst))    
