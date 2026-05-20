import math

def divisor(n, rootn):
    pairs = []
    for i in range(1, int(rootn) + 1):
        if n % i == 0:
            pairs.append((i, n//i))
    return pairs



def Divisors_of_n_squared(n):
    factors = []
    d = 2
    while n > 1:
        while n % d == 0:
            factors.append(d)
            n /= d
        d = d + 1
        if d*d > n:
            if n > 1: 
                factors.append(n)
            break
    temp = set(factors)
    
    divisors = 1
    for x in temp:
        divisors *= (2*factors.count(x) + 1)
        
    if divisors % 2 != 0:
        divisors += 1 #account for a = b case
        
    return divisors//2

def diophantineReciprocals(n):
    divisors = divisor(n ** 2, n)
    solns = []
    for div in divisors:
        solns.append((n + div[0], n + div[1]))
    return solns

print(Divisors_of_n_squared(35 ** 2))
exit()

for i in range(614889782588491410, 9000000):
    #rst = diophantineReciprocals(i)
    #rst = divisor(i ** 2, i)
    rst = range(Divisors_of_n_squared(i))
    if len(rst) > 4000000:
        print("Result", i, rst)
        exit()

print(i, rst)
