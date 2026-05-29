import sys
import math

import time, math
start_time = time.time()

def list_primality(n):
    result = [True] * (n + 1)
    result[0] = result[1] = False
    for i in range(int(math.sqrt(n)) + 1):
        if result[i]:
            for j in range(2 * i, len(result), i):
                result[j] = False
    return result

def list_primes(n):
    return [i for (i, isprime) in enumerate(list_primality(n)) if isprime]
    
def compute(limit):
    mod = 10**16
    primes = list_primes(limit)
    SUM = sum(primes)
    primality = list_primality(SUM)
    array = [1] + [0]*SUM
    
    curr_largest = 1
    for p in primes:
        for x in reversed(range(curr_largest)):
            array[x + p] += array[x]
            array[x + p] %= mod
        curr_largest += p
                
    return sum([array[x] for x in range(len(array)) if primality[x]]) % mod

print(compute(5000))

# primelist = {}

# with open("prime.txt", "rt") as file:
#     for line in file: 
#         line = line.strip() #or some other preprocessing
#         if int(line) <= 1548136: #sum of primes until 4999
#             primelist[int(line)] = True
#         else:
#             break
        
# print("built the list")
# primes = primelist.keys()

# S = []
# for i in primes:
#     if i <= 4999:
#         S.append(i)


# n = len(S)
# subsets = []
    
# count = 0
#     # 1 << n is mathematically equivalent to 2^n
# for mask in range(1 << n):
#     current_subset = 0
#     for i in range(n):
#         # Check if the i-th bit is set in the current mask
#         if (mask & (1 << i)) != 0:
#             current_subset + S[i]
    
#     if current_subset in primelist:
#             sys.stdout.write(f"\rFind subset", current_subset)
#             count += 1
    
print("Result", count)
