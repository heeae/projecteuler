import sys
import math

val = {}

for i in range(1, 10000):
    val[i * (3*i - 1) // 2] = True

print("built the list")

minval = 9999999999
for i in val.keys():
    for j in val.keys():
        if i == j or i > j:
            continue
        if j - i in val and (j + i) in val:
            print(i, j, j - i)
            if j - i < minval:
                minval = j - i
                print(i, j, j-i)
            #sys.exit(0)



print("\n Result: " + str(minval))
