import sys
import math

matchcnt = 0
for i in range(1, 99): # digit of x
    
    for j in range(1, 99): # test point
        k = j ** i
        if len(str(k)) == i:
            print("Match: ", i, j, k)
            matchcnt += 1
        elif len(str(k)) > i:
            break
print("Result: ", matchcnt)