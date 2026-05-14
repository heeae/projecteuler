import sys
import math

def isPandigital(n):
    s = str(n)
    if len(s) != 9:
        return False
    for i in range(1, 10):
        if str(i) not in s:
            return False
    return True


def permutatestring(x):
    if x == "":
        return [""]
    result = []
    for i in x:
        buf = permutatestring(x.replace(i, "", 1))
        for j in buf:
            result.append(i + j)
    return result

def isPrime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

for i in permutatestring("123456789"):
    if isPrime(int(i)):
        print(i)

for i in permutatestring("12345678"):
    if isPrime(int(i)):
        print(i)
        
for i in permutatestring("1234567"):
    if isPrime(int(i)):
        print(i)
        
for i in permutatestring("123456"):
    if isPrime(int(i)):
        print(i)
        
for i in permutatestring("12345"):
    if isPrime(int(i)):
        print(i)
        
for i in permutatestring("1234"):
    if isPrime(int(i)):
        print(i)
        