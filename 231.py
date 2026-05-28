import functools, math, sys


def prime_sieve(limit, segment = False, values = True):
    '''
    A prime sieve I made with a few different options
    

    :param limit: The limit up till which the function will generate primes
    :param segment: Optional boolean value, if segment == True, it will perform a segmented sieve 
    :param values: Optional boolean value, if values == False, it will return an array such that array[x] = True if x is prime

    :returns: All primes < limit
    
    .. code-block:: python
    
        print(prime_sieve(50)) #[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
        print(prime_sieve(10, values = False)) #[False, False, True, True, False, True, False, True, False, False, False]
        
        print([i for (i, isprime) in enumerate(prime_sieve(10, values = False)) if isprime]) #[2, 3, 5, 7]
        
    '''
    if (type(limit) != int) or (type(segment) != bool) or (type(values) != bool):
        return "n must be an integer"
    
    if segment:
        primes = []
        sqrtN = int(math.sqrt(limit))
        result = [True]*(sqrtN + 2)
        result[0] = result[1] = False
        for i in range(2, sqrtN + 1):
            if result[i]:
                primes.append(i)
                for j in range(2*i, sqrtN + 1, i):
                    result[j] = False
        all_primes = []
        marker = [0]*len(primes)
        block_size = sqrtN
        for k in range(1, limit//block_size):
            block_start = k*block_size + 1
            block_end = (k + 1)*block_size
            curr_result = [True]*block_size
            if k == 1:
                for p_index, p in enumerate(primes):
                    count = 0
                    while (block_start + count) % p != 0:
                        count += 1
                    for j in range(block_start + count, block_end + 1, p):
                        curr_result[j - block_start] = False
                        marker[p_index] = j
            else:
                for p_index, p in enumerate(primes):
                    for j in range(marker[p_index] + p, block_end + 1, p):
                        curr_result[j - block_start] = False
                        marker[p_index] = j
            if values:
                all_primes += [block_start + i for (i, isprime) in enumerate(curr_result) if isprime]
            else:
                all_primes = all_primes[:block_start + 1] + curr_result
        if values:
            return primes + all_primes
        else:
            return result[:sqrtN + 1] + all_primes
    else:
        result = [True] * (limit + 1)
        result[0] = result[1] = False
        for i in range(int(math.sqrt(limit)) + 1):
            if result[i]:
                for j in range(2 * i, len(result), i):
                    result[j] = False
        if values:
            return [i for (i, isprime) in enumerate(result) if isprime]
        else:
            return result

def legendre_factorial(x):
    '''
    Implementation of `Legendres' Formula
    <https://en.wikipedia.org/wiki/Legendre%27s_formula>`_

    :param x: An integer

    :returns: A dictionary containing the prime factorisation of x!
    
    .. code-block:: python
    
        print(legendre_factorial(6)) #{2: 4, 3: 2, 5: 1} 
        
    '''
    if (type(x) != int):
        return "All values must be integers"
    primes = prime_sieve(x)
    prime_fac = {}
    for y in primes:
        total = 0
        for i in range(1, int(math.floor(math.log(x,y))) + 1):
            total += int(math.floor(x/(y**i)))
        prime_fac[y] = total
    return prime_fac

n = 20_000_000
r = 15_000_000

factors = legendre_factorial(n)
deductfactors = legendre_factorial(r)
deductfactors2 = legendre_factorial(n-r)

for i in deductfactors.keys():
    factors[i] -= deductfactors[i]

for i in deductfactors2.keys():
    factors[i] -= deductfactors2[i]


result = 0
for j in factors.keys():
    result += j * factors[j]

print("Result", result)

exit()

def primefactor(n):
    buf = []
    while n % 2 == 0:
        buf.append(2)
        
        n //= 2
    
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        while n % i == 0:
            buf.append(i)
            n //= i
        if n < i:
            break

    if n > 2:
        buf.append(n)
    return buf


primeslist = []
for i in range(n, r, -1):
    sys.stdout.write(f"\r Generating prime {i}")
    primeslist += primefactor(i)



deductfactor = []
for i in range(n - r, 1, -1):
    sys.stdout.write(f"\r Generating deducting prime {i}")
    deductfactor += primefactor(i)


for j in deductfactor:
    primeslist.remove(j)

# primeslist should be the remaining factor

result = 0
for j in primeslist:
    result += j

print("Result", result)