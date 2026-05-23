import functools, math

primelist = {}
target = 10 ** 8
primelimit = target // 2 + 100
with open("prime.txt", "rt") as file:
    for line in file: 
        line = line.strip() #or some other preprocessing
        if(int(line) < primelimit):
            primelist[int(line)] = True
        else: 
    
            break
        
print("built the list")
primes = list(primelist.keys())



primcnt = [0] * (primelimit + 1)
idx = 0
for x in range(1, primelimit + 1):
    while True:
        if idx >= len(primes):
            break
        if (primes[idx] > x):
             primcnt[x] = idx
             break
        idx += 1

sumLimit = primcnt[int(math.sqrt(target)) + 1]
count = 0
for x in range(1, sumLimit + 1):
    count += primcnt[int((target / primes[x - 1]))] - x + 1

print("Result", count)
