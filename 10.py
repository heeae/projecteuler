import sys
import math

val = 2000000

sqrt = math.sqrt(val)
primelist = [2, 3, 5, 7, 11]
rst = 28

for i in range(12, val + 1):
    notprime = False
    for j in primelist:
        if i % j == 0:
            notprime = True
            break
    
    if not(notprime):
        sys.stdout.write(f"\r{i:}")
        sys.stdout.flush()
        primelist.append(i)
        rst += i
        
print("\nResult:")
print(rst)

