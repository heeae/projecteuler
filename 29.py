import sys
import math
value = {}
for i in range(2, 101):
    for j in range(2, 101):
        val = i ** j
        if val not in value:
            value[val] = 1


print(len(value.keys()))
