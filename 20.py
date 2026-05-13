import sys
import math

val = str(math.factorial(100))
rst = 0
for x in val:
    rst += int(x)

print(rst)
