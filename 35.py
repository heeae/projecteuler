import sys
import math


val = 1000000

primelist = [2, 3, 5, 7, 11]

for i in range(12, val):
    notprime = False
    for j in primelist:
        if i % j == 0:
            notprime = True
            break
    
    sys.stdout.write(f"\r{i:}")
    sys.stdout.flush()
    if not(notprime):
        primelist.append(i)
print("built the list")

def permutatestring(x):
    if x == "":
        return [""]
    result = []
    for i in x:
        buf = permutatestring(x.replace(i, "", 1))
        for j in buf:
            result.append(i + j)
    return result


def rotationString(x):
    if x == "":
        return [""]
    result = []
    for i in range(len(x)):
        result.append(x[i:] + x[:i])
    return result
    
rst = 0
for i in primelist:
    allPrime = True
    for j in rotationString(str(i)):
        if int(j) not in primelist:
            allPrime = False
    if allPrime:
        print(i)
        rst += 1
        
print("Result: " + str(rst))
