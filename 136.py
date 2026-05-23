import time, math, itertools
from functools import lru_cache
import sys

def isSqrt(n):
    return int(n ** 0.5) ** 2 == n
# x-m, x, x+m which (x+m)^2 - x^2 - (x-m)^2 = n, (m is the arithmetic value)
# => 4mx - x^2 = n
# => x^2 - 4mx + n = 0
# => x = (4m (+/-) sqrt((4m)^2 - 4n)) / 2
# => x = 2m (+/-) sqrt(4m^2 - n)
# => x, m, n are integer, which 4m^2 - n need to be perfect square 
# => 4m^2 - n = k^2 
# => n = 4m^2 - k^2  > 0

# on the other hand n = x (4m - x) 
# 4m - x > 0 => m > x / 4 
# and x - m > 0 => m < x 
# ==> x > m > x / 4

# the other properties for n is much greater then x, hence dont need to loop larger than 1,000,000

buffer = [0] * (50 * 10**6 + 1)
for x in range(1, 50_000_000):
    for m in range(x // 4 + 1, x):
        n = x * (4*m - x)
        if n < 50 * 10 ** 6:
            buffer[n] += 1
        else:
            break
counter = 0
for x in buffer:
    if x == 1:
        counter += 1

print("Result", counter)
