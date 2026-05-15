import sys
import math

def nCr(n, r):
    return math.factorial(n) // (math.factorial(r) * math.factorial(n - r))


cnt = 0
for i in range(1, 101):
    for j in range(0, i + 1):
        if nCr(i, j) > 1000000:
            print("n: " + str(i) + ", r: " + str(j) + ", nCr: " + str(nCr(i, j)))
            cnt += 1
print("Count: " + str(cnt))
