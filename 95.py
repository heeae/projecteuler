import time, itertools, sys, math
from functools import lru_cache


limit = 1_000_000
values = [0] + [1] * limit

for x in range(2,int(limit/2) + 1):
    for y in range(1,int(limit/x)+1):
        if x*y != x:
            values[x*y] += x
data = {}
for i, j in enumerate(values):
    data[i] = j

print("built the list")

chains = {}
for r in data.keys():
    chaincnts = 0
    x = r
    buf = [x]
    while x in data:
        chaincnts += 1
        buf.append(x)
        x = values[x]
        if x > limit:
            break
        if x in buf:
            break
    if x == r:
        chains[r] = chaincnts


maxChain = max(chains.values())
for i in chains.keys():
    if chains[i] == maxChain:
        print("Result", i, maxChain)

#print(chains)

