import time, math, itertools
from functools import lru_cache
import sys
sys.set_int_max_str_digits(1000000000)


def repUnit(n):
    return int("".join(["1"] * n))
primelist = {}

with open("prime.txt", "rt") as file:
    for line in file: 
        line = line.strip() #or some other preprocessing
        if(int(line) < 100_000):
            primelist[int(line)] = True
        else: 
            break
        
print("built the list")


for n in range(2, 1000):
    sys.stdout.write(f"\r{n}")
    sys.stdout.flush()
    if str(n)[-1] in ["1", "3", "7", "9"]:    
        isFound = False
        for k in range(1, 1_000_000 + 1):
            if repUnit(k) % n == 0:
                #print("found", n, k)
                isFound = True
                
                if k in primelist and (n - 1) % k == 0:
                    print("found found", n, k)
                break
        if not isFound:
            print(f"A({n}) > {k}")
            exit()
