import sys
import math

def isPandigital(n):
    s = str(n)
    if len(s) != 9:
        return False
    for i in range(1, 10):
        if str(i) not in s:
            return False
    return True

product = {}


for i in range(1, 100000):
    buffer = ""
    pandigital = False
    for j in range(1, 6):
        buffer += str(i * j)
        if(isPandigital(buffer)):
            print(buffer, i, j)
            pandigital = True
            break
        elif len(buffer) > 9:
            break
