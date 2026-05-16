import sys
import math

def isGon(tuples):
    minSum = 9999
    maxSum = 0
    for i in tuples:
        tuplesum = sum(i)
        if tuplesum < minSum:
            minSum = tuplesum
        if tuplesum > maxSum:
            maxSum = tuplesum
    return minSum == maxSum

def is5Gon(tuples):
    l = tuples.copy()
    initVector = l.pop(0)
    firstVector = initVector
    while len(l) > 0:
        isfFound = False
        for x in l:
            if initVector[2] == x[1]:
                l.remove(x)
                initVector = x
                isfFound = True
                break
        if not isfFound:
            return False
    if initVector[2] == firstVector[1]:
        return True

def permutatearray(x):
    if len(x) == 1:
        return [x]
    result = []
    for i in x:
        y = x.copy()
        y.remove(i)
        buf = permutatearray(y)
        for j in buf:
            z = [i]
            z.extend(j)
            result.append(z)
    return result


def slice3Gon(input): #abcdefghij => abc, dce, feg, hgi, jib
    return [(input[0], input[1], input[2]), 
            (input[3], input[2], input[4]), 
            (input[5], input[4], input[1])]


def slice5Gon(input): #abcdefghij => abc, dce, feg, hgi, jib
    return [(input[0], input[1], input[2]), 
            (input[3], input[2], input[4]), 
            (input[5], input[4], input[6]), 
            (input[7], input[6], input[8]), 
            (input[9], input[8], input[1])]

def sortTuple(input):
    return input[0]

def tupleString(inputs):
    buf = ""
    tuples = sortTuple(inputs)
    for i in tuples:
        for j in i:
            buf += str(j)
    return buf

def sortTuple(input):
    minTupleIndex = 0
    minTuple = 999
    for i, tup in enumerate(input):
        if tup[0] < minTuple:
            minTuple = tup[0]
            minTupleIndex = i
    x = list(input[minTupleIndex:])
    x.extend(list(input[:minTupleIndex]))
    return x

print(sortTuple(((6, 3, 1), (4, 1, 5), (2, 5, 3))))

solns = {}
soln = permutatearray([1,2,3,4,5,6])
print("Total", len(soln), "combinations")
for x in soln:
    gon = slice3Gon(x)
    if isGon(gon):
        tupleRst = tupleString(gon)

        print("Found soln", tupleRst, gon)
        solns[tupleRst] = 1

sortedkey = sorted(solns.keys())
maxVal = 0
for i in sortedkey:
    if int(i) > maxVal and len(i) == 9:
        maxVal = int(i)
print("Result: ", maxVal)
        


solns = {}
soln = permutatearray([1,2,3,4,5,6,7,8,9,10])
print("Total", len(soln), "combinations")
for x in soln:
    gon = slice5Gon(x)
    if isGon(gon):
        tupleRst = tupleString(gon)
        print("Found soln", tupleRst, gon)
        solns[tupleRst] = 1

sortedkey = sorted(solns.keys())
maxVal = 0
for i in sortedkey:
    if int(i) > maxVal and len(i) == 16:
        maxVal = int(i)
print("Result: ", maxVal)
        