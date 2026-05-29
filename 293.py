import sys
import math, functools


primelist = {}

with open("prime.txt", "rt") as file:
    for line in file: 
        line = line.strip() #or some other preprocessing
        if int(line) <= 29: #sum of primes until 4999
            primelist[int(line)] = True
        else:
            break
        
print("built the list")
primes = primelist.keys()

# s = 1
# for i in primes:
#     s *= i
#     if s > 10 ** 9:
#         print("maxi", i)
#         break

def isAdmissible(x):
    z = x
    for y in primes:
        isFound = False
        while z % y == 0:
            z /= y
            isFound = True
        if not isFound:
            return False
        if z == 1:
            return True


def isPrime(x):
    if x % 2 == 0:
        return False
    for i in range(3, int(math.sqrt(x) + 1), 2):
        if x % i == 0:
            return False
    return True

s = 0
dictionary = set()
for i in range(2, 10 ** 9, 2):
    if isAdmissible(i):
        sys.stdout.write(f"\rTesting: {i}               ")
        for j in range(3, i, 2):
            if isPrime(i + j):
                # print("Pseudo - Fortunate", i, j)
                s += j
                dictionary.add(j)
                break

print("Result", s, sum(list(dictionary)))