import functools, math, sys


target = 64_000_000
buf = [0] + [1] * (target - 1)

for x in range(2, target):
    sys.stdout.write(f"\rtesting {x}")
    sys.stdout.flush()
    for y in range(x, target, x):
        buf[y] += x ** 2

# print(buf)

result = 0
for i, x in enumerate(buf):
    if int(x ** 0.5) ** 2 == x:
        result += i

print("Result", result)
