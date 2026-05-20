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



cnt = 1
bouncy = 0

while True:
    
    if isBouncy(cnt):
        bouncy += 1
    if bouncy / cnt > 0.99:
        break
    cnt += 1

print("Result", cnt - 1)