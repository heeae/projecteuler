import time, itertools, sys
from functools import lru_cache

@lru_cache(maxsize = 10**5)
def recursiveGenerate(A):
    values = set()
    if len(A) == 1:
        values.add(A[0])
        return values
    
    multiplesFlag = False
    for x in A:
        if A.count(x) > 1:
            multiplesFlag = True
        
    for k in range(1, len(A)):
        
        combs1 = [y for y in itertools.combinations(A, k)]
        combs2 = [y for y in itertools.combinations(A, len(A) - k)]
        
        for i in range(len(combs1)):
            for j in range(len(combs2)):
                
                t = set(combs1[i]).intersection(set(combs2[j]))
                flag = False
                if len(t) == 0:
                    flag = True
                else:
                    if multiplesFlag:
                        flag = True
                        for x in t:
                            xcount = combs1[i].count(x) + combs2[j].count(x)
                            if xcount > A.count(x):
                                flag = False
                if flag:
                    t1 = recursiveGenerate(combs1[i])
                    t2 = recursiveGenerate(combs2[j])
                    for v1 in t1:
                        for v2 in t2:
                            values.add(v1 + v2)
                            values.add(v1 * v2)
                            if v1 - v2 > 0:
                                values.add(v1 - v2)
                            if v2 != 0:
                                values.add(v1 / v2)
    return values

def compute(A):
    v = sorted([int(x) for x in recursiveGenerate(tuple(A)) if int(x) == float(x)])
    maxCurrConsecutive = 0
    for i, x in enumerate(v):
        if i + 1 != x:
            maxCurrConsecutive = i
            break
    return maxCurrConsecutive
    
choice = list(range(10)) * 4
combinations = itertools.combinations(choice, 4)
maxSteak = 0
maxCombination = []
for x in combinations:
    steak = 0
    #print (x)
    steak =  compute(x)
    if steak > maxSteak:
        maxSteak = steak
        maxCombination = x
    sys.stdout.write("\rTesting {x}")
    sys.stdout.flush()

print("Result", maxSteak, maxCombination)
