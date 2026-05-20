import time, math, itertools

def isBouncy(n):
    hasIncrease = False
    hasDecrease = False
    val = str(n)
    for x in range(len(val) - 1):
        if val[x] < val[x+1]:
            hasIncrease = True
        elif val[x] > val[x+1]:
            hasDecrease = True
        if hasIncrease and hasDecrease:
            return True
    if not hasIncrease and not hasDecrease:
        return False
    return False




n = 100
I = [1]*9
D = [1]*10
total = 0
for d in range(n):
    for i in range(9):
        I[i] = sum(I[i:])
        D[9 - i] = sum(D[:9 - i + 1])
    total += I[0]
    total += D[9]
print(total - 9*n - n)
