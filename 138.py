import time, math, itertools
from functools import lru_cache
import sys


def isSqrt(n):
    print(n)
    return int(n ** 0.5) ** 2 == n


# x = 0
# y = -1
# xn+1 = - 9 ⁢xn + 8 ⁢yn + 8 ⁢
# yn+1 = 10 ⁢xn - 9 ⁢yn - 8 ⁢


# x = 0
# y = 1

# xn+1 = - 9 ⁢xn + 8 ⁢yn - 8 ⁢
# yn+1 = 10 ⁢xn - 9 ⁢yn + 8 ⁢

def iteration1(x, y):
    x1 = -9 * x - 8 * y + 8
    y1 = -10 * x - 9 * y + 8
    return (x1, y1)

def iteration2(x, y):
    x1 = -9 * x - 8 * y - 8
    y1 = -10 * x - 9 * y - 8
    return (x1, y1)

start = (0, -1)
result = 0
for i in range(12):
    val = iteration1(start[0], start[1])
    start = val
    result += abs(val[1])
    print(val)

start = (0, 1)
result = 0
for i in range(12):
    val = iteration2(start[0], start[1])
    start = val
    result += abs(val[1])
    print(val)

print("Result", result)
exit()
