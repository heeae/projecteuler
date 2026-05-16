import sys
import math


def isCube(x):
    return int(math.cbrt(x)) ** 3 == x

def permutatestring(x):
    if x == "":
        return [""]
    result = []
    for i in x:
        buf = permutatestring(x.replace(i, "", 1))
        for j in buf:
            result.append(i + j)
    return list(set(result))

cubicdata = {}
for k in range(1, 10000):
    x = k ** 3
    data = "".join(sorted(list(str(k**3))))
    if data not in cubicdata:
        cubicdata[data] = [x] 
    else:
        cubicdata[data].append(x)
        if len(cubicdata[data]) == 5:
            print("Result: ", data, cubicdata[data][0] )
            exit()






# for k in range(1668, 10000):
#     i = k ** 3
#     sys.stdout.write(f"\rtesting: {k:}  {i:}              ")
#     sys.stdout.flush()
#     matchcnt = 1
#     for j in permutatestring(str(i)):
#         if int(j) > i and int(j) in cubicdata:
#             matchcnt += 1
#     if matchcnt == 5:
#         print (i)
#         for j in permutatestring(str(i)):
#             if int(j) > i and isCube(int(j)):
#                 print("Permutate: ", j)
#         exit()
