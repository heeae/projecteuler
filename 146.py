import sys
import math


def isPrime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

sum = 0
for i in range(10, 150_000_000, 2):
    square = i ** 2
    if isPrime(square + 1) and isPrime(square + 3) and isPrime(square + 7)  and isPrime(square + 9)  and isPrime(square + 13)  and isPrime(square + 27):
        sum += i
        print("Found", i, sum)
        
        