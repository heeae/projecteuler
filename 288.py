import sys
import math, functools

p = 61
ubb = 10 ** 7


def legendre_factorial_single_prime(x, p):
    total = 0
    i = 1
    while pow(p, i) < x:
        total += (math.floor(x//(p**i)))
        i += 1
    return total
    

sequence = [290797] + [0] * ubb
for i in range(1, ubb + 1):
    sequence[i] = sequence[i - 1] ** 2 % 50515093

s = 0
for i in range(ubb + 1):
    s += (sequence[i] % p) * p ** i


facPcount = legendre_factorial_single_prime(s, p)


print(facPcount % (p**10))

