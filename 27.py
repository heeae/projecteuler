import sys
import math


val = 5000000000

sqrt = math.sqrt(val)
primelist = [2, 3, 5, 7, 11]

for i in range(12, math.floor(sqrt)):
    notprime = False
    for j in primelist:
        if i % j == 0:
            notprime = True
            break
    
    sys.stdout.write(f"\r{i:}")
    sys.stdout.flush()
    if not(notprime):
        primelist.append(i)
print("built the list")

def quadf(a, b, n):
    return n**2 + a*n + b


maxn = 0
maa = 0
mab = 0
for a in range(-999, 1000):
    for b in range(-1000, 1001):
        n = 0
        while quadf(a, b, n) in primelist:
            n += 1
        if n > maxn:
            maxn = n
            maa = a
            mab = b

print(maa, mab, maxn, maa * mab)
