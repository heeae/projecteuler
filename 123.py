import time, math, itertools


primelist = {}

with open("prime.txt", "rt") as file:
    for line in file: 
        line = line.strip() #or some other preprocessing
        if(int(line) < 300_000):
            primelist[int(line)] = True
        else: 
            break
        
print("built the list")
primelist = list(primelist.keys())

# binomial expansion 
# (a ^ n - nC1 a^(n-1) + .... + (-1) ^ (n - k) * nCk * a ^ (k) + (-1) ^ n ) + 
# (a ^ n + nC1 a^(n-1) + .... + nCk * a ^ (k) + (-1) ^ n ) +
# if n % 2 == 0: =>
# rmax = a * (a - 1) > 10 ^ 10


def calval(a, n):
    print(a, n, ((a - 1) ** n + (a + 1) ** n) % a **2)


sumMax = 0
for i, a in enumerate(primelist):
    if (i + 1) % 2 == 1 and 2 * a * (i + 1) > 10 ** 10:
        print("Result", i + 1, a, 2 * a * ( i + 1), 2 * a * (i + 1) - 10 ** 10)
        exit()
    
