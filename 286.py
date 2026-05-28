import sys
import math, functools

@functools.cache
def calculation(q, score, shot, needed):
    if score > needed:
        return 0
    if shot > 50: 
        if score == needed:
            return 1
        return 0
    return (1 - shot / q) * calculation(q, score + 1, shot + 1, needed) + (shot / q) * calculation(q, score, shot + 1, needed)


low = 50
high = 60
goal = 0.02
target = 10 ** -12
while high - low > target:
    mid = (high + low) / 2
    rst = calculation(mid, 0, 1, 20)
    print("Iterating", mid, rst)
    if rst < goal:
        high = mid
    else:
        low = mid

print("Result", high, low, mid)
