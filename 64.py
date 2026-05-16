import sys
import math


def periodLength(N):

    nk = 0
    dk = 1
    ak = math.floor(math.sqrt(N))
    a0 = ak

    length = 0
  
    if a0 * a0 != N:
        while True:
            nk = ak * dk - nk
            dk = (N - nk * nk) / dk
            ak = math.floor((a0 + nk) / dk)
            length += 1
            if 2 * a0 == ak:
                break
    return length

rst = 0
for i in range(2, 10000 + 1):
    rst += periodLength(i) % 2

print ("Result: ", rst)
