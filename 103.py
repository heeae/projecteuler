import time, itertools, sys, math
from functools import lru_cache
import collections



def sumSet(a):
    return sum(a)

def isSetFull(a):
    for blen in range(1, len(a)):
        choices = itertools.combinations(a, blen)
        for b in choices:
            
            choicesC = a.copy()
            for ele in b:
                choicesC.remove(ele)
            
            for clen in range(1, len(a) - blen + 1):
                choicesCombin = itertools.combinations(choicesC, clen)
                for c in choicesCombin:                    
                    #print("Testing", sum(b), b, sum(c), c)
                    if sum(b) == sum(c):
                        return False
                    if len(b) > len(c):
                        if sum(b) <= sum(c):
                            return False
                    # if len(b) < len(c):
                    #     if sum(b) > sum(c):
                    #         return False
    return True



print(isSetFull([20,31,35,36,37,39,42]))

size = 7
maxValue = size * size 
minValue = 20



choices = itertools.combinations(list(range(minValue, maxValue + 1)), size)
minSet = 999999
minList = []
for y in choices:
    x = list(y)
    if isSetFull(x):
        if sum(x) < minSet:
            minSet = sum(x)
            minList = x
            print("Found soln", minSet, minList)

print("Result", minSet, minList)
