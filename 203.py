import functools, math

def squarefree(buf):
    divisor = 2
    while True:
        divisorcnt = 0
        while buf % divisor == 0:
            buf = buf // divisor
            divisorcnt += 1
        if divisorcnt >= 2:
            return False
        divisor += 1
        if divisor > buf:
            return True
    return True

        

def nCr(n, r):
    return math.comb(n, r)

numSet = set()

for i in range(0, 51):
    for j in range(i + 1):
        numSet.add(nCr(i , j))

result = 0
for i in numSet:
    if squarefree(i):
        result += i

print("Result", result)