import sys

def isTriangle(n):
    y = 8 * n + 1
    return int((y**0.5)) ** 2 == y 

def isHexagonaL(n):
    y = 8 * n + 1
    return (int((y**0.5)) + 1) % 4 == 0

for i in range(1, 1000000):
    pentaglenumber = i * (3*i - 1) // 2
    if isHexagonaL(pentaglenumber) and isTriangle(pentaglenumber):
        print(pentaglenumber)

