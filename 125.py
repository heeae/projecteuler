import time, math, itertools

def isPalindromicSum(x):
    if str(x) != str(x)[::-1]:
        return False
    for i in range(1, int((x / 2) ** 0.5) + 1):
        sum = 0
        cnt = 0
        while sum <= x:
            sum += (i + cnt) ** 2
            if sum == x: 
                return True
            cnt += 1
    return False


result = 0
for i in range(1, 10 ** 8):
    if isPalindromicSum(i):
        result += i
        print("Found ", i, "match the case")

print(result)