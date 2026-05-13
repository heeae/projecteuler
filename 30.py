import sys
import math

rst = 0
for i in range(10, 1000000):
    x = str(i)
    sum = 0
    for y in x:
        sum += int(y) ** 5
    if sum == i:
        print(i)
        rst += i

print()
print(rst)