import math
primelist = {}

with open("prime.txt", "rt") as file:
    for line in file: 
        line = line.strip() #or some other preprocessing
        if int(line) <= 7072:
            primelist[int(line)] = True
        
print("built the list")
primes = primelist.keys()

def mid(a, b, c):
    if a >= b and a >= c:
        if b > c:
            return b
        else:
            return c
    elif b >= a and b >= c:
        if a > c:
            return a
        else:
            return c
    elif c >= a and c >= b:
        if a > b:
            return a
        else:
            return b
        
resultmap = set()
maxval = 50_000_000
for i in primes:
    if i ** 2 > maxval:
        break
    for j in primes:
        if i ** 2 + j ** 3 > maxval:
            break
        for k in primes:
            val = i ** 2 + j ** 3  + k ** 4
            if val > maxval:
                break
            resultmap.add(val)

print("Result", len(resultmap))
exit()


# solnCnt = 0

# for i in range(2, 50_000_000 + 1):
#     solnFound = False
#     for j in primes:
#         if j ** 2 > i:
#             break
#         for k in primes:
#             if max(j, k) ** 2 + min(j, k) ** 3 > i:
#                 break
#             for l in primes:
#                 if max(j, k, l) ** 2 + mid(j, k, l)  ** 3 + min(j, k, l) ** 4 > i:
#                     break
#                 if j  ** 2 + k ** 3 + l ** 4 == i:
#                     solnFound = True
#                     break
#             if solnFound:
#                 break
#         if solnFound:
#             break
#     if solnFound:
#         solnCnt += 1
#         print("soln find for", i)

# print("Result", solnCnt)

