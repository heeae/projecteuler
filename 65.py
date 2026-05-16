import sys
import math


def periodLength(N):

    nk = 0
    dk = 1
    ak = math.floor(math.sqrt(N))
    a0 = ak

    length = 0
  
    if a0 * a0 != N:
        while True:
            nk = ak * dk - nk
            dk = (N - nk * nk) / dk
            ak = math.floor((a0 + nk) / dk)
            print(length, nk, dk, ak)
            length += 1
            if 2 * a0 == ak:
                break
    return length



def nextIteration(x, coefficent):
    return  (x[1], coefficent * x[1] + x[0])

def convergents(x, base):
    return (base* x[1] + x[0], x[1])

rst = 0
i = 1
tup = [2]
terms = 100
while len(tup) < terms:
    tup.extend([1, 2*i, 1])
    i += 1
while len(tup) > terms:
    tup.pop()
print(tup)

lastTuple = (1, tup.pop())
for i in tup[::-1]:
    lastTuple = nextIteration(lastTuple, i)

print(sum(int(i) for i in str(lastTuple[1])))
print (lastTuple)
#     val = convergents(lastTuple, 2)
#     print(val)
#     if len(str(val[0])) > len(str(val[1])):
#         rst += 1
# print("Result ", rst)

