import time, math, itertools
from functools import lru_cache
import sys

primelist = {}

with open("prime.txt", "rt") as file:
    for line in file: 
        line = line.strip() #or some other preprocessing
        if(int(line) < 1_000_100):
            primelist[int(line)] = True
        else: 
            break
        
print("built the list")
primelist = list(primelist.keys())

sumS = 0
for i, prime in enumerate(primelist):
    if prime < 5:
        continue
    if prime > 1_000_000:
        break
    cnt = 1
    nextprime = primelist[i+1]

    k = 10**len(str(prime))
    m = -prime * pow(k, nextprime-2, nextprime) % nextprime
    S = m * k + prime
    print("Found", prime, nextprime, S)
    sumS += S
    
print("Result", sumS)
