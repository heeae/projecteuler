import sys
import math
import collections

total = 1_000_000
data = [0] * (total + 1)

for i in range(3, total // 4 + 1 + 1):
    sys.stdout.write(f"\r{i}")
    numsquare = i ** 2
    if i % 2 == 0: # if even
        for j in range(i - 2, 1, -2 ):
            val = numsquare - j ** 2
            if val <= total:
                data[val] += 1
                #print("val", val, i, j)
            else:
                break
    else:
        for j in range(i - 2, 0, -2 ):
            val = numsquare - j ** 2
            if val <= total:
                #print("val", val, i, j)
                data[val] += 1
            else:
                break


cntmatrix = [0] * 11
for j in data:
    if j > 0 and j <= 10:
        cntmatrix[j] += 1
    
print("result", sum(cntmatrix[1:]))

