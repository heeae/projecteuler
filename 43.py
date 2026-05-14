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

def isTarget(n):
    value = [2, 3, 5, 7, 11, 13, 17]
    for i in range(1, len(str(n)) - 2):
        val = int(str(n)[i:i+3])
        if(val % value[i-1] != 0):
            return False
    return True

rst = 0
for i in permutatestring("1234567890"):
    if str(i)[0] == "0":
        continue
    if isTarget(int(i)):
        rst += int(i)
        print(i)

print("\n Result: " + str(rst))
