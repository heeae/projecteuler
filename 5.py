import sys
import math

val = int(sys.argv[1])

primelist = [2, 3, 5, 7, 11, 13, 17, 19]
primecnt = [0, 0, 0, 0, 0, 0, 0, 0]
for i in range(2, val):
    pnt = i
    for idx, prime in enumerate(primelist):
        primefactor = 0
        while pnt % prime == 0:
            primefactor += 1
            pnt = pnt / prime
        if primecnt[idx] < primefactor:
            primecnt[idx] = primefactor

rst = 1;
for idx, prime in enumerate(primelist):
    if primecnt[idx] == 0: 
        continue
    print(prime, primecnt[idx], prime ** primecnt[idx])
    rst = rst *  prime ** primecnt[idx]
print(rst)
