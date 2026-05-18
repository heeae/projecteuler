import sys
import math
import collections
import itertools

# Pythagorean triple

L = 1500000
solutions =  collections.defaultdict(set)
for m in range(1, int(L ** 0.5)):
    for n in range(1, m):
        a = m ** 2 -  n ** 2
        b = 2 * m * n
        c  = m ** 2 + n ** 2
        l = a + b + c
        if l > L:
            break
        k = 1
        while True:
            if  k * (l) <= L:
                solutions[k * (l)].add((min(k * a, k * b), max(k * a, k * b), k * c))
                k += 1
            else:
                break


print("Result",  sum(len(ele) == 1 for ele in solutions.values()))


exit()
# brute force method 
# a + b + c = L
# a^2 + b^2 = c^2
# a + b < c

rst = 0
for L in range(1, 1500000 + 1):
    trianglefound = 0
    for a  in range(1, L):
        for b in range(a, L - a):
            c = L - b - a
            if a ** 2 + b ** 2 == c ** 2:
                trianglefound += 1
    if trianglefound == 1:
        #print("One Triangle found ", L)
        
        sys.stdout.write(f"\r{L:}")
        sys.stdout.flush()
        rst += 1
print("Rst", rst)

