import functools, math


val = 1
lastval = 1
for i in range(1855):
    val = pow(1777, lastval, 10 ** 8)
    lastval = val

print(val)
