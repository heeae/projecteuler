import time, math, itertools

def digitalPowerSum(n): 
    val = sum( int(x) for x in str(n))
    if val == 1: 
        return False
    while n > 1:
        if n % val == 0:
            n = n // val
        else: 
            return False
    return True

counter = 16
# Sum found 1 81
# Sum found 2 512
# Sum found 3 2401
# Sum found 4 4913
# Sum found 5 5832
# Sum found 6 17576
# Sum found 7 19683
# Sum found 8 234256
# Sum found 9 390625
# Sum found 10 614656
# Sum found 11 1679616
# Sum found 12 17210368
# Sum found 13 34012224
# Sum found 14 52521875
# Sum found 15 60466176
# Sum found 16 205962976

# for i in range(500000000, 1000000000):
#     rst = digitalPowerSum(i)
#     if rst:
#         counter += 1
#         print("Sum found", counter, i)

# this method seems not always correct as x^y < z^a (where x < z, y > a)
candidate = []
for i in range(2, 80):
    for j in range(2, 50):
        val = i ** j
        if i == sum( int(x) for x in str(val)):
            candidate.append((val, i , j))


rst = sorted(candidate, key = lambda x : x[0])
print(len(rst))
