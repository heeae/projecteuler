import time, math, itertools


# binomial expansion 
# (a ^ n - nC1 a^(n-1) + .... + (-1) ^ (n - k) * nCk * a ^ (k) + (-1) ^ n ) + 
# (a ^ n + nC1 a^(n-1) + .... + nCk * a ^ (k) + (-1) ^ n ) +
# if n % 2 == 0: =>


def calval(a, n):
    print(a, n, ((a - 1) ** n + (a + 1) ** n) % a **2)

sumMax = 0
for a in range(3, 1000 + 1):
    if a % 2 == 1:
        rMax = a * ( a - 1)
    else:
        rMax = a * (a - 2)
    sumMax += rMax
print("Reuslt", sumMax)
