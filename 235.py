import functools, math, sys

def formula(r):
    return (897 - (897 - 15000) * r ** 5000) / (1 - r) + (-3 * r * (1 - r ** 5000)) / (1-r)**2 + 600000000000

# print(formula(0.9999999999999991))

# exit()

goal = -600000000000
r = 1.0023221086329 # manual calculation for approximation

def u(k, r):
    return (900 - 3*k) * (r ** (k - 1))

def S(r):
    val = 0
    for i in range(1, 5000 + 1):
        val += u(i, r)
    return val

r = "1."

for j in range(1, 14):
    buf = r
    lastk = -1
    for k in range(10):
        val = float(buf + str(k))
        s = S(val) - goal
        if s < 0:
            r = r + str(k - 1)
            break

print("Result", r)


print("Result", r, val - goal)