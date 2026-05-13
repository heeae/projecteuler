import sys
import math

i = 0
j = 1
idx = 1
while True:
    
    k = i + j
    i = j
    j = k
    idx += 1
    if len(str(k)) >= 1000:
        print(idx)
        break