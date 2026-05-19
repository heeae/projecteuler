import sys
import math

buf = {}

def sumSquareDigit(x):
    if x in buf:
        return buf[x]
    sum = 0
    for i in str(x):
        sum += int(i) ** 2
    
    return sum

def iteration(input):
    x = input
    while x != 89 and x != 1:
        x = sumSquareDigit(x)
    
    buf[input] = x
    return x
    
print(iteration(44))
rst = {1: 0, 89: 0}
for i in range(1, 10_000_001):
    val = iteration(i)
    rst[val] = rst[val] + 1
    
    sys.stdout.write(f"\rTesting: {i:}                              ")
    sys.stdout.flush()

print("\nresult", rst[89])    
#print(buf)