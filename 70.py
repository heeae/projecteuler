import sys
import math

primelist = {}


def sortString(input):
    return "".join(sorted(list(str(input))))


with open("prime.txt", "rt") as file:
    for line in file: 
        line = line.strip() #or some other preprocessing
        if int(line) < 10000:
            primelist[int(line)] = True
        
print("built the list")
primes = primelist.keys()

minRat = 1000
minN = 0
# based on fact that, if a value is a prime, then the phi is minium as all of them are primary prime
for i in primes:
    for j  in  primes:
        if i < j and i  * j < 10 ** 7:
            phi = (i - 1) * (j - 1)
            n = i * j  
            if sortString(n) == sortString(phi):
                print("Candidate", n, n/phi)
                if  n/phi < minRat:
                    minRat = n/phi 
                    minN  = n

print("Result", minN,  minRat)

    
