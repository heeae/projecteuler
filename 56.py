import functools
import sys
import math
import itertools

def sumDigit(x):
    s = str(x)
    j = 0
    for i in s:
        j += int(i)
    return j

maxsum = 0
for a in range(1, 100):
    for b in range(1, 100):
        sum = sumDigit(a ** b)
        if sum > maxsum:
            maxsum = sum

print(" result: ", maxsum)
