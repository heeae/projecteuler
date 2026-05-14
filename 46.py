import sys
import math


val = 100000
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

for i in range(4, 99999):
    if i in primelist or i % 2 == 0:
        continue
    isFound = False
    # print("checking: " + str(i))
    for j in filter(lambda x: x < i, primelist):
        # print("checking: " + str(i) + " - " + str(j))
        for k in range(1, math.floor(math.sqrt(i - j)) + 1):
            # print("checking: " + str(i) + " - " + str(j) + " - " + str(k))
            if i - j == 2 * k**2:
                print(i, j, k)
                isFound = True
                break
        if isFound:
            break
    if not isFound:
        print("value is found: " + str(i))
        break


