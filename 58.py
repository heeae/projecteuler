import sys
import math

def spiralmatrix(n):
    data = []
    for i in range(n):
        row = []
        for j in range(n):
            row.append(0)
        data.append(row)

    startx = n - 1
    starty = 0
    directionx = -1
    directiony = 0
    for i in range(n ** 2, 0, -1):
        data[starty][startx] = i
        
        # check need to change direction 
        if(directionx < 0 and directiony == 0): # left
            if(startx == 0 or data[starty][startx + directionx] != 0):
                directionx, directiony = 0, 1
        elif(directionx == 0 and directiony > 0): # down
            if(starty >= n - 1 or data[starty + directiony][startx] != 0):
                directionx, directiony = 1, 0
        elif(directionx == 0 and directiony < 0): # up
            if(starty == 0 or data[starty + directiony][startx] != 0):
                directionx, directiony = -1, 0
        elif(directionx > 0 and directiony == 0): # right
            if(startx == n - 1 or data[starty][startx + directionx] != 0):
                directionx, directiony = 0, -1
        
        startx += directionx
        starty += directiony

    return data

primeCache = {}
def isPrime(n):
    if n in primeCache:
        return primeCache[n]
    if n < 2:
        primeCache[n] = False
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            primeCache[n] = False
            return False
    primeCache[n] = True
    return True



# for i in range(26211, 28000, 2):
#     data = spiralmatrix(i)
#     primecnt = 0
#     valcnt = 0
#     for j in range(i):
#         if isPrime(data[j][j]):
#             primecnt += 1
#         if isPrime(data[j][i - 1 - j]):
#             primecnt += 1
#         valcnt += 2
    
#     print("rst", i, primecnt, valcnt - 1, primecnt / (valcnt - 1), data[i - 1][i - 1])
#     if primecnt / (valcnt - 1) * 10 < 1:
#         print("rst", i, primecnt, valcnt - 1)
#         break


def spirlNumber(n): 
    value = [1]
    for i in range(3, n + 1, 2):
        
        value.append(i ** 2 - 3 * (i - 1))
        value.append(i ** 2 - 2 * (i - 1))
        value.append(i ** 2 - (i - 1))
        value.append(i ** 2)
    return value

print(spirlNumber(7))

for i in range(26211, 28000, 2):
    data = spirlNumber(i)
    primecnt = 0
    valcnt = 0
    for j in data:
        if isPrime(j):
            primecnt += 1
        valcnt += 1
    
    print("rst", i, primecnt, valcnt, primecnt / (valcnt), data[-1])
    if primecnt / (valcnt ) * 10 < 1:
        print("rst", i, primecnt, valcnt)
        break