import sys
import math, functools


primelist = {}

with open("prime.txt", "rt") as file:
    for line in file: 
        line = line.strip() #or some other preprocessing
        if int(line) <= 1000003: #sum of primes until 4999
            primelist[int(line)] = True
        else:
            break
        
print("built the list")
primes = list(primelist.keys())

# conseutive prime 
result = 0
target = 999966663333
for i in range(len(primes) - 1):
    
    prime = primes[i]
    nextprime = primes[i + 1]
    sys.stdout.write(f"\rTesting: {prime} vs {nextprime}              ")
    # instead of checking one by one, but if prime * x is within the range, and nextprime * y is within the range 
    candidate = []
    for j in range((prime) ** 2 + prime, min(target, nextprime ** 2), prime):
        candidate.append(j)
    lbb = int(math.ceil(prime ** 2 / nextprime) * nextprime)
    for j in range(lbb, min(target, nextprime ** 2), nextprime):
        if j in candidate:
            candidate.remove(j)
        else:
            candidate.append(j)
    # print("candidate", candidate)

    result += sum(candidate)
    # for j in range((prime) ** 2 + 1, nextprime ** 2):
    #     lpsdivisible = j % prime == 0
    #     upsdivisible = j % nextprime == 0
    #     if lpsdivisible and not upsdivisible or not lpsdivisible and upsdivisible:
    #         result += j
    #         print("one of simidivisible", j)

    # if primes[i] == 17:
    #     exit()

# for each value is divisible by one of the prime only
# add the result


print("Result", result)