import functools, math


def simplifyTuple(x):
    gcd = math.gcd(x[0], x[1])
    return (x[0] // gcd, x[1] // gcd)

result = 0
for i in range(5, 10000 + 1):
    maxI = round(i / math.exp(1))
    fraction = simplifyTuple((i ** maxI, maxI  ** maxI))

    remainder = fraction[1]
    if i == 81:
        pass
    while remainder % 2 == 0:
        remainder = remainder // 2
    while remainder % 5 == 0:
        remainder = remainder // 5

    if int(remainder) == 1:
        #print("i terminating", i, maxI, fraction)
        result -= i
    else:
        #print("i non terminating", i, maxI, remainder, fraction)
        result += i

print("Result", result)
