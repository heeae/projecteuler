import sys
import math

item = [1, 2, 5, 10, 20, 50, 100, 200]
item.reverse()
def decompose(total, basepoint, composition):
    if total == 0:
        print(composition)
        return 1
    rst = 0
    for i in item:
        if total - i >= 0 and i <= basepoint:
            data = composition.copy()
            data.append(i)
            rst += decompose(total - i, i, data)
    return rst

print(decompose(200, 200, []))