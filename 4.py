import sys
import math


maxh = 0
for i in range(999, 100, -2):
    for j in range(999, 100, -2):
        val = str(i * j)
        
        firsthalf = val[0:(int(len(val)/2))][::-1]
        if val.endswith(firsthalf):
            if maxh < i * j:
                maxh = i * j
            #print(firsthalf)
            #print(i, j, val)
            #exit()

print(maxh)
