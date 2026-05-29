import sys
import math, functools



def isPrime(x):
    if x % 2 == 0:
        return False
    for i in range(3, int(math.sqrt(x) + 1), 2):
        if x % i == 0:
            return False
    return True

def fermat_primality_test(n, tests):
    if n < 10**5:
        return isPrime(n)
    else:
        for x in range(tests):
            if pow(2*(x + 2), n - 1, n) != 1:
                return False
        return True


target = 5 * 10 **15

count = 0
for i in range(1, int(math.sqrt(target / 2) + 1)):
    
    val = i ** 2 + (i + 1) ** 2
    sys.stdout.write(f"\rTesting {val}")
    if val < target:
        if fermat_primality_test(val, 5):
            # print("Panaitopol Primes", val)
            count += 1
    else:
        break

print("Result", count)