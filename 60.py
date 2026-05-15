import sys
import math
import collections
import itertools
import re

import math

def is_prime(n):
    """快速質數判定 (試除法)"""
    if n < 2: return False
    if n in (2, 3): return True
    if n % 2 == 0 or n % 3 == 0: return False
    for i in range(5, int(math.sqrt(n)) + 1, 6):
        if n % i == 0 or n % (i + 2) == 0:
            return False
    return True

def is_pair_prime(p1, p2):
    """檢查兩個質數雙向拼接後是否仍為質數"""
    return is_prime(int(f"{p1}{p2}")) and is_prime(int(f"{p2}{p1}"))

def solve_project_euler_60():
    # 1. 透過埃拉托斯特尼篩法生成 10000 以內的所有質數
    limit = 10000
    sieve = [True] * limit
    primes = []
    for p in range(2, limit):
        if sieve[p]:
            primes.append(p)
            for i in range(p*p, limit, p):
                sieve[i] = False
    
    # 排除 2 和 5 (因為任何數與 5 或 2 拼接結尾會是 2, 5, 0，必不是質數)
    primes = [p for p in primes if p != 2 and p != 5]
    
    # 2. 建立鄰接表：儲存每個質數與哪些「比它大」的質數可以配對
    adj = {p: [] for p in primes}
    for i in range(len(primes)):
        for j in range(i + 1, len(primes)):
            if is_pair_prime(primes[i], primes[j]):
                adj[primes[i]].append(primes[j])

    # 3. 使用 DFS / 回溯法尋找 5-Clique
    def find_clique(current_clique):
        if len(current_clique) == 5:
            return current_clique
        
        # 尋找與當前 clique 中所有頂點都相連的候選下一個頂點
        # 取出 clique 中第一個頂點的鄰居作為基礎候選池
        first_node = current_clique[0]
        candidates = set(adj[first_node])
        
        # 與後續頂點的鄰居取交集，確保新加入的點與現有所有的點都相連
        for node in current_clique[1:]:
            candidates &= set(adj[node])
            
        # 排序候選者以確保從小到大遍歷，最先找到的五元組其和往往最小
        for next_node in sorted(candidates):
            # 確保搜尋順序遞增，避免重複排列
            if next_node > current_clique[-1]:
                result = find_clique(current_clique + [next_node])
                if result:
                    return result
        return None

    # 從每個質數出發嘗試尋找
    for p in primes:
        res = find_clique([p])
        if res:
            print(f"找到的 5 個質數集合: {res}")
            print(f"最小和為: {sum(res)}")
            return sum(res)

if __name__ == "__main__":
    solve_project_euler_60()

exit()

primekey = {}

with open("prime.txt", "rt") as file:
    for line in file: 
        line = line.strip() #or some other preprocessing
        if(int(line) < 7999994):
            primekey[int(line)] = True
        
print("built the list")
primelist = list(primekey.keys())

preprime = [3, 7, 109, 673]

primeCache = {}
def isPrime(n):
    if n < 7999994:
        return n in primekey
    if n in primeCache:
        return primeCache[n]
    if n < 2:
        primeCache[n] = False
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            primeCache[n] = False
            return False
    primeCache[n] = True
    return True

concatenate = lambda a, b: int(f"{a}{b}")
def gen_k_prime_set(n, k):
    # Precompute compatible primes
    primes = Euler.prime_sieve(n)
    compatible = collections.defaultdict(list)
    for p1, p2 in itertools.combinations(primes, 2):
        if Euler.is_prime_MR(concatenate(p1, p2)) and Euler.is_prime_MR(concatenate(p2, p1)):
            compatible[p1].append(p2)
            compatible[p2].append(p1)

    # Recursive search for k-clique
    def search(clique, candidates):
        if len(clique) == k:
            yield clique
            return
        for p in candidates:
            new_candidates = [q for q in compatible[p] if q > p and all(q in compatible[m] for m in clique)]
            yield from search(clique + [p], new_candidates)

        return {frozenset(combo) for p in primes for combo in search([p], compatible[p]) if len(combo) == k}
    
N, K = 50000, 5
k_primes = gen_k_prime_set(N, K)

# Sort and print the sets based on the sum of their elements
print(*sorted(sum(s) for s in k_primes), sep='\n') 

# for prime in range(674, 500000):
#     # if prime != 11053:
#     #     continue
#     allPrime = True
#     for j in preprime:
#         # print(int(str(prime) + str(j)), int(str(j) + str(prime)), isPrime(110533), isPrime(311053))
#         if not isPrime(int(str(prime) + str(j))) or not isPrime(int(str(j) + str(prime))):
#             allPrime = False
#             break
#     if allPrime:
#         print("Result: ", prime, 3 + 7 + 109 + 673 + prime )
#         # exit()

