import functools
import sys
import math
import itertools



def isPaluibrome(x):
    s = str(x)
    return s == s[::-1]

def nextIteration(x):
    return x + int(str(x)[::-1])

cnt = 0
for i in range(1, 10000):
    x = i
    found = False
    x = nextIteration(x)
    for j in range(0, 50):
        if isPaluibrome(x):
            found = True
            print("Lychrel number ", i, " found in ", j)
            break
        else:
            x = nextIteration(x)
    if not found:
        print("Lychrel number found", i)
        cnt += 1

print("result: ", cnt)