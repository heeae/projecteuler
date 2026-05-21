import time, math, itertools


primelist = {}

with open("prime.txt", "rt") as file:
    for line in file: 
        line = line.strip() #or some other preprocessing
        if(int(line) < 100_000):
            primelist[int(line)] = True
        else: 
            break
        
print("built the list")
primelist = list(primelist.keys())


def rad(n):
    cur = n
    primefactor = set()
    for i in primelist:
        if i > cur:
            break
        while cur % i == 0:
            cur = cur // i
            primefactor.add(i)
    val = 1
    for v in list(primefactor):
        val *= v
    return val


result = []
for i in range(1, 100000 + 1):
    result.append((i, rad(i)))

result = sorted(result, key= lambda x : (x[1], x[0]))
print(result[9999])


    