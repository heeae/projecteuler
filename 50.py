import sys
import math

primelist = {}

with open("prime.txt", "rt") as file:
    for line in file: 
        line = line.strip() #or some other preprocessing
        if(int(line) < 1000000):
            primelist[int(line)] = True
        
print("built the list")
primelist = list(primelist.keys())

maxterm = 505
maxprime = 950000

for i, prime in enumerate(primelist):
    if prime < maxprime:
        continue
    for k in range(i-1):
        if k * maxterm > prime:
            continue
        buf = primelist[k]
        terms = 1
        
        for j in primelist[k + 1:i]:
            buf += j
            if buf < prime:
                terms += 1
            elif buf == prime:
                terms += 1
                break
            else:
                terms = 0
                break
          
        if terms > maxterm:
            maxterm = terms
            maxprime = buf
            print("max term is updated: " + str(maxterm) + ", prime is " + str(prime))

print("max term is " + str(maxterm) + ", prime is " + str(maxprime))
