import time, math, itertools
from functools import lru_cache
import sys

def isReversible(n):
    x = str(n)
    if x[0] == "0" or x[-1] == "0":
        return False
    reverseN = int(x[::-1])
    sum = str(n + reverseN)
    for x in sum:
        if x in ["0", "2", "4", "6", "8"]:
            return False
    return True


count = 0
for i in range(1, 1000000000):
    if isReversible(i):
        #print(i)
        count += 1

print("Result", count)
