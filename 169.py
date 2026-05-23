
import functools, sys


@functools.cache
def a(n):
    if n == 0:
        return 0 
    if n == 1:
        return 1
    if n % 2 == 0:
        return a(n//2)
    else:
        return a((n - 1)//2) + a((n - 1)//2 + 1)


print(a(10**25 + 1))