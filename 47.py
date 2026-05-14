import sys
import math

val = 1000000
primelist = {}

with open("prime.txt", "rt") as file:
    for line in file: 
        line = line.strip() #or some other preprocessing
        primelist[int(line)] = True
        
print("built the list")


def calprimefactor(x):
    result = {}
    tmp = x
    if x in primelist:
        return 1
    for i in filter(lambda k : k <= x, primelist.keys()):
        j = 0
        while tmp % i == 0:
            j += 1
            tmp = tmp // i
            result[i] = j
    return len(result.keys())

for i in range(100000, val):
    isFound = True
    sys.stdout.write(f"\rTesting: {i:}                ")
    sys.stdout.flush()
    for j in range(i, i + 4):
        if calprimefactor(j) != 4:
            isFound = False
            break
    if isFound:
        print("value is found: " + str(i))
        break

