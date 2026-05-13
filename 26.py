import sys
import math

# long division 


def long_division(num, den):
    res = ""
    rem = num
    step = 0
    remainders = {}
    while rem != 0 and step < 1000:
        res += str(rem * 10 // den)
        rem = (rem * 10) % den
        #print(res, rem)
        if rem in remainders:
            break
        remainders[rem] = step
        step += 1
    return res

for i in range(1, 1000):
    print(i, len(long_division(1, i)))