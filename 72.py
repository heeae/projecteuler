import sys
import math

primelist = {}

with open("prime.txt", "rt") as file:
    for line in file: 
        line = line.strip() #or some other preprocessing
        if int(line) <= 1000000:
            primelist[int(line)] = True
        
print("built the list")
primes = primelist.keys()


def phi(x):  
    # factor x by primes
    if x in primelist:
        return x - 1
    remainder = x
    result = 1
    for i in primes:
        if i > remainder: 
            break
        powercnt = 0
        while remainder >= i and remainder % i == 0:
            remainder = remainder / i
            powercnt += 1
        if powercnt > 0:
            result *= i ** (powercnt - 1) * (i - 1)
    # return mul(prime ^ (power - 1)  * (prime - 1))
    return result


phicnt = 0
for i in range(2, 1000000+1):
    phiy = phi(i)
    phicnt += phiy
    sys.stdout.write(f"\r{i:}")
    sys.stdout.flush()
print("\n result",  phicnt)
