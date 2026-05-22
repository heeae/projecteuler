import time, math, itertools
from functools import lru_cache
import sys
sys.set_int_max_str_digits(1000000000)

def repUnit(n):

    return int("".join(["1"] * n))


target = 1_000_000
n = 1_000_000
while True:
    if int(str(n)[-1]) in [1, 3, 7, 9]:
        expoent = 1
        while True:
            if pow(10, expoent, 9 * n) == 1:
                break
            expoent += 1
            if expoent > target:
                print("Result", n)
                exit()
    n += 1