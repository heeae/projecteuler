import sys
import math

val = 600851475143

sqrt = math.sqrt(val)
primelist = [2, 3, 5, 7, 11]

for i in range(12, math.floor(sqrt)):
    notprime = False
    for j in primelist:
        if i % j == 0:
            notprime = True
            break
    
    sys.stdout.write(f"\r{i:}")
    sys.stdout.flush()
    if not(notprime):
        primelist.append(i)
print("built the list")
primelist.reverse()
for j in primelist:
    if val % j == 0:
        print(j)
        break
    
