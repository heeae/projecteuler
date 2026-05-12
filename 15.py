import sys
import math

maxx = 20
maxy = 20
buf = {}
    
def lattice(x, y):
    if (x, y) in buf:
        return buf[(x, y)]
    # print(x, y)
    if x >= maxx and y >= maxy:
        return 1
    elif x >= maxx:
        val = lattice(x, y+1)
        buf[(x, y)] = val
        return val
    elif y >= maxy: 
        val = lattice(x + 1, y)
        buf[(x, y)] = val
        return val
    else:
        val = lattice(x, y+1) + lattice(x + 1, y)
        buf[(x, y)] = val
        return val

print(lattice(0, 0))
