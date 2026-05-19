# not work soln

import math
from itertools import combinations

cnt = 0
for x1 in range(0, 51):
    for y1 in range(0, 51):
        if x1 == 0 and y1 == 0:
            continue
        for x2 in range(0, 51):
            for y2 in range(0, 51):
                if x2 == 0 and y2 == 0:
                    continue
                a  = (x2 - x1) ** 2 + (y2 - y1) ** 2
                b = x2 ** 2 + y2 ** 2
                c = x1 ** 2  + y1 ** 2
                
                #print((x1, y1), (x2, y2), a, b, c)
                if  c > a and c > b:
                    if 2 * x2 ** 2 - 2 * x2 * x1 + 2 * y2 ** 2 - 2 * y2 * y1 == 0:
                        cnt += 1
                        print((x1, y1), (x2, y2))
                if  a > b and a > c:
                    if 2 * x2 * x1 + 2 * y2 * y1 == 0:
                        cnt += 1
                        print((x1, y1), (x2, y2))
                if  b > a and b > c:
                    if 2 * x1 ** 2 - 2 * x1 * x2 + 2 * y1 ** 2 - 2 * y2 * y1 == 0:
                        cnt += 1
                        print((x1, y1), (x2, y2))
print("Result", cnt / 2) # x1,y1 and x2,y2 is mutable