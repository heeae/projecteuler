
import sys
import math

def iteration(n):
    if n == 0:
        return (1, 2)
    else:
        val = iteration(n - 1)
        return (val[1], 2 * val[1] + val[0])

def nextIteration(x):
    return  (x[1], 2 * x[1] + x[0])

def convergents(x):
    return (x[1] + x[0], x[1])

rst = 0
lastTuple = (1, 2)

for i in range(1, 1000):
    lastTuple = nextIteration(lastTuple)
    val = convergents(lastTuple)
    if len(str(val[0])) > len(str(val[1])):
        rst += 1
print("Result ", rst)

