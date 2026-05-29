import sys
import math, functools

p = 61
ubb = 10 ** 7

@functools.cache
def legendre_factorial_single_prime(x, p):
    total = 0
    i = 1
    while pow(p, i) < x:
        total += (math.floor(x//(p**i)))
        i += 1
    return total
    
def countPrime(x, prime):
    result = 0
    power = prime
    while power <= x:
        result += x // power
        power *= prime
    return result

sequence = [290797] + [0] * ubb
for i in range(1, ubb + 1):
    sequence[i] = (sequence[i - 1] ** 2 % 50515093) 

s = 0
maxPower = 1
cacheDict = {}
for i in range(ubb + 1):
    # sys.stdout.write(f"\rTesting {i}")
    val =  (sequence[i] % p) * maxPower
    if val in cacheDict: 
        rst = cacheDict[val]
    else:
        rst = countPrime(val, p)
        cacheDict[val] = rst

    s += rst
    s %= p ** 10
    if maxPower < p ** 10:
        maxPower *= p


print("Result",s)



modulo = pow(61, 10)
maxPower = 1
s = 290797
result = 0
cachedict = {}
for i in range(ubb + 1):
    t = s % p
    product = t * maxPower
    if product in cachedict:
        result += cachedict[product]
    else:
        current = countPrime(product, p)
        cachedict[product] = current
        result += current
    result %= modulo
    if maxPower < modulo:
        maxPower *= p
    s *= s
    s %= 50515093

print("Result", f"{result}")
