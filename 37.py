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



def rotationString(x):
    if x == "":
        return [""]
    result = []
    for i in range(1, len(x)):
        result.append(x[i:])
    for i in range(1, len(x)):
        result.append(x[:-i])
    return result
    
rst = 0
for i in primelist:
    allPrime = True
    for j in rotationString(str(i)):
        if int(j) not in primelist:
            allPrime = False
    if allPrime:
        print(i)
        rst += i
        
print("Result: " + str(rst))
