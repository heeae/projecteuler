import time, math, itertools
from functools import lru_cache
import sys


def is_sq(x):
    sqrt = (x ** (1 / 2))
    if round(sqrt) ** 2 == x:
        return True
    return False

def compute():
    for b in range(1, 1000):
        for a in range(b + 2, 1000, 2):
            x = (a*a + b*b)//2
            y = a*a - x
            if x < y:
                break
            else:
                for c in range(int(math.sqrt(x)), a):
                    z = c*c - x
                    if z > y:
                        break
                    else:
                        if all([is_sq(x - z), is_sq(y + z), is_sq(y - z)]):
                            print(x, y, z, a, b, c)
                            return x + y + z
                        
print(compute())
exit()

# 434657 420968 150568

limit = 5000
perfectSquare = []
for i in range(2, limit):
    perfectSquare.append(i ** 2)



tuple = []

for x in range(2, limit):
    for y in range(1, x):
        if x + y in perfectSquare and x - y in perfectSquare:
            tuple.append((x, y))

for a in tuple:
    for b in tuple:
        if a[1] == b[0]:
            for c in tuple:
                if b[1] == c[1] and a[0] == c[0]:
                    print(a, b, c)
                    exit()


