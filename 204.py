import functools, math

primesSet = set([2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97])
target = 10 ** 9

count = 0
while True:
    buf = []
    sortedList = sorted(list(primesSet))
    
    for i in sortedList:
        for j in sortedList:
            # print(primesSet[i], j, primesSet[i] * j)
            v = i * j
            if v <= target:
                buf.append(v)
            else: 
                break

    
    before = len(primesSet)
    primesSet.update(buf)
    after = len(primesSet)
    print("Cycle", before, after)
    if before == after:
        print("Result", len(primesSet) + 1) # 1 should also included
        exit()


# this method take too long 

def isHammingnumber100(n):
    for i in primes:
        while n % i == 0:
            n = n // i
    if n > 100:
        return False
    return True

count = 0
for i in range(1, 10**9 + 1):
    if isHammingnumber100(i):
        # print("Hamming", i)
        count += 1

print("Result", count)