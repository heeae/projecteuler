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


def first9Digit(n) :
    
    # Find total number of digits - 1
    digits = (int)(math.log10(n))

    # Find first digit
    n = (int)(n // pow(10, digits - 8))

    # Return first digit
    return n;

x1 = 0
x2 = 1

iteration = 1
while True:
    x3 = x1 + x2 
    x1 = x2
    x2 = x3 
    iteration += 1
    if isPandigital(x2 % 1_000_000_000) and isPandigital(first9Digit(x2)):
        print("Pandigital", iteration)
        exit()

