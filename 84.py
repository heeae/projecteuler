# not work soln

import math

def countRectangle(m, n):
    choices = 0
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            row = m - i + 1
            columns = n - j + 1
            choices += row * columns
    return choices


nearestRect = 999999999
nearestArea = 0
for i in range(1, 100):
    for j in range(i, 0, -1):
        rects = countRectangle(i, j)
        if abs(2000000 - rects) < nearestRect:
            nearestRect = abs(2000000 - rects)
            nearestArea = i * j

print(nearestRect, nearestArea)
