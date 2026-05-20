import time, itertools, sys, math
from functools import lru_cache
import collections


# (x / L) * ((x - 1) / (L - 1)) = 1/2
# 2x ^ 2 - 2x = L ^ 2 - L
# 2x ^ 2 - 2x - L ^ 2 + L = 0
# https://www.alpertron.com.ar/QUAD.HTM

# Recursive solutions:

# xn+1 = 3 ⁢xn + 2 ⁢yn - 2 ⁢
# yn+1 = 4 ⁢xn + 3 ⁢yn - 3 ⁢


def iteration(tuple):
    x1 = 3 * tuple[0] + 2 * tuple[1] - 2
    y1 = 4 * tuple[0] + 3 * tuple[1] - 3
    return (x1, y1)


initial = (15, 21)
while initial[1] < 1_000_000_000_000:
    initial = iteration(initial)
    print(initial)

print("Result", initial)

exit()
def quadratic(a, b, c, l):
    q = b ** 2 - 4 * a * c
    if q < 0 or int(math.sqrt(q)) ** 2 != q:
        return -1
    x1 = (-1 * b + math.sqrt(q))
    x2 = (-1 * b - math.sqrt(q))
    

    if x1 > x2:
        if x1 % (2 * a) == 0 and x1 > 0 and x1 < l * 2 * a:
            return x1 / 2 / a 
        elif x2 % (2 * a) == 0 and x2 > 0 and x2 < l * 2 * a:
            return x2 / 2 / a
        return -1
    else:
        if x2 % (2 * a) == 0 and x2 > 0 and x2 < l * 2 * a:
            return x2 / 2 / a
        elif x1 % (2 * a) == 0 and x1 > 0 and x1 < l * 2 * a:
            return x1  / 2 / a
        return -1

j = 1_000_000_000_000
#j = 1001241019767 
#j = 21
while True:
    rst = quadratic(2, -2, j - j ** 2, j)
    if rst != -1:
        print("Result", j, rst)
        exit()
    j += 1