import functools
import sys
import math


primelist = {}

with open("prime.txt", "rt") as file:
    for line in file: 
        line = line.strip() #or some other preprocessing
        if int(line) <= 10000:
            primelist[int(line)] = True
        
print("built the list")
primes = primelist.keys()

item = list(primes)
item.reverse()
def decompose(total, basepoint, composition):
    # if total > basepoint:
    #     return 0
    if total == 0:
        #print(composition)
        return 1
    rst = 0
    for i in item:
        if total - i >= 0 and i <= basepoint:
            data = composition.copy()
            data.append(i)
            rst += decompose(total - i, i, data)
    return rst

print(decompose(10, 10, []))
for i in range(1, 10000):
    if decompose(i, i, []) > 5000:
        print("Result", i)