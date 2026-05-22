import time, math, itertools
from functools import lru_cache
import sys

primelist = {}

with open("prime.txt", "rt") as file:
    for line in file: 
        line = line.strip() #or some other preprocessing
        if(int(line) < 1_000_000):
            primelist[int(line)] = True
        else: 
            break
        
print("built the list")
primelist = list(primelist.keys())


factorcnt = 1
result = 0
for i in primelist:
    if pow(10, 10 ** 9, 9 *i) == 1:
        print("Factor", i, factorcnt)
        if factorcnt <= 40:
            result += i
        factorcnt += 1

print("Result", result)