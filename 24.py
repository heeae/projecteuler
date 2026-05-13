import sys
import math

def lexicographic(prefix, input):
    if len(input) == 0:
        return [prefix]
    buf = []
    for i, val in enumerate(input):
        step = input.copy()
        step.pop(i)
        buf.extend(lexicographic(prefix + str(val), step))
    return buf


dat = lexicographic("", [0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

print(dat[999999])
