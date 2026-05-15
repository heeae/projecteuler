import sys
import math


def permutatestring(x):
    if x == "":
        return [""]
    result = []
    for i in x:
        buf = permutatestring(x.replace(i, "", 1))
        for j in buf:
            result.append(i + j)
    return result

for i in range(1, 10000000):
    choices = permutatestring(str(i))
    if str(i) in choices and str(i * 2) in choices and str(i * 3) in choices and str(i * 4) in choices and str(i * 5) in choices and str(i * 6) in choices:
        print(i)
        break
