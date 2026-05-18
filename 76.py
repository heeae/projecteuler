import functools
import sys
import math


@functools.cache
def partitions(number: int, top: int) -> int:
    if number == 0:
        return 0
    if number == 1:
        return 1
    else:
        result = sum(
            partitions(number - x, min(number - x, x)) for x in range(1, top + 1)
        )
        if number <= top:
            result += 1
        return result

print(partitions(100, 100) - 1)

item = list(range(1, 100))
item.reverse()
def decompose(total, basepoint, composition):
    if total == 0:
        # print(composition)
        return 1
    rst = 0
    for i in item:
        if total - i >= 0 and i <= basepoint:
            data = composition.copy()
            data.append(i)
            rst += decompose(total - i, i, data)
    return rst

print(decompose(100, 100, []))