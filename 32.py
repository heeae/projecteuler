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
def sumRange(m0, mn, n0, nn):
    
    for i in range(m0, mn + 1):
        for j in range(n0, nn + 1):
            if(isPandigital(str(i) + str(j) + str(i * j))):
                product[i * j] = 1
    
sumRange(1, 9, 1234, 9876)
sumRange(12, 98, 123, 987)

rst = 0
for i in product.keys():
    rst += i
print(rst)
