import sys
import math

primelist = {}

with open("prime.txt", "rt") as file:
    for line in file: 
        line = line.strip() #or some other preprocessing
        primelist[int(line)] = True
        
print("built the list")
primes = primelist.keys()

buf = 1

# based on fact that, if a value is multiply of primes, the number of the relative prime will be smallest, as all of them are factors 
for i in primes:
    if buf * i > 1000000:
        break
    buf *= i
print("Result: ", buf)
    

# brute force soln
maxRatio = 0
maxN = 0
for i in range(2, 1000001):
    phi = 0
    for j in range(1, i):
        if math.gcd(i, j) == 1:
            phi += 1
    if i/phi > maxRatio:
        maxRatio = i/phi
        maxN = i

    1
    sys.stdout.write(f"\rtesting...{i:}\t\t{maxN}\t{maxRatio}")
    sys.stdout.flush()

print("Result: ", maxN, maxRatio)