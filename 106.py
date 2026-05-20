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
                    # if 65 in c and 46 in b:
                    #print("Testing", sum(b), b, sum(c), c)
                    if sum(b) == sum(c):
                        return False
                    if len(b) > len(c):
                        if sum(b) <= sum(c):
                            return False
                    if len(b) < len(c):
                        if sum(b) >= sum(c):
                            return False
    return True

for i in range(25):
    if isSetFull([i + 1, i + 2, i + 3, i + 4]):
        print("fullfill", [i + 1, i + 2, i + 3, i + 4])
