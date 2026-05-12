import sys
import math

val = str(2**1000)
buf = 0
for x in val:
    buf += int(x)
    
print(buf)