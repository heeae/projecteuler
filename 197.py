import functools, math

def f(x):
    return math.floor(pow(2, 30.403243784 - x **2)) * 10**-9

u0 = -1
ulast = u0
for i in range(1000):
    u = f(ulast)
    print(u)
    ulast = u
print(f(u) + ulast)

