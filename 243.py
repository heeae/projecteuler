import sys
import math

primelist = {}

with open("prime.txt", "rt") as file:
    for line in file: 
        line = line.strip() #or some other preprocessing
        if int(line) <= 10_000:
            primelist[int(line)] = True
        
print("built the list")
primes = primelist.keys()

def phi(n):
    '''
    Implementation of `Eulers Totient Function
    <https://en.wikipedia.org/wiki/Euler%27s_totient_function>`_ counts the positive integers up to a given integer n that are relatively prime to n

    :param n: An integer

    :returns: An integer, numbers, a, less than n, such that gcd(a, n) = 1
    
    .. code-block:: python
    
        print(phi(20)) #8
        print(phi(100)) #40
        
    '''
    if (type(n) != int):
        return "All values must be integers"
    if n == 1:
        return 1
    phi = 1
    d = 2 
    while n > 1:
        count = 0 
        while n % d == 0:
            count += 1
            n /= d
        if count > 0:
            phi *= (pow(d, count - 1)*(d-1))
        d = d + 1
        if d*d > n:
            if n > 1: 
                phi *= int(n - 1)
            break
    return phi
# def phi(x):  
#     # factor x by primes
#     if x in primelist:
#         return x - 1
#     remainder = x
#     result = 1
#     for i in primes:
#         if i > remainder: 
#             break
#         powercnt = 0
#         while remainder >= i and remainder % i == 0:
#             remainder = remainder / i
#             powercnt += 1
#         if powercnt > 0:
#             result *= i ** (powercnt - 1) * (i - 1)
#     # return mul(prime ^ (power - 1)  * (prime - 1))
#     return result


minval = 999
t = 1
phiT = 1
# step1 find the multiplies of all primes that reach the limit, if co prime, phi(x * y) = phi(x) * phi(y)
# for x in primes:
#     t *= x
#     phiT *= phi(x)
#     if phiT / (t - 1) < 15499 / 94744:
#         print("Result", t, x)
#         exit()

print(phi(111546435), phi(111546435 * 2), phi(111546435 * 4), phi(111546435 * 8)) # phi(2^3 * 3*5*...*23) = 2^3 (1-1/2) * 111546435

# refine the value until the ratio reached, but why that is "minimum"?
for i in range(1, 9999999):
    next = i * 111546435
    if phi(next) / (next - 1) < 15499 / 94744:
        print("Result", next)
        exit()


