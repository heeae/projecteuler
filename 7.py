import sys
import math

val = 10001

primelist = [2, 3, 5, 7, 11]
i = 12
while len(primelist) < val:
#for i in range(12, math.floor(sqrt)):
    notprime = False
    for j in primelist:
        if i % j == 0:
            notprime = True
            break
    
    sys.stdout.write(f"\r{i:}")
    sys.stdout.flush()
    if not(notprime):
        primelist.append(i)
        
    i += 1
print("built the list")
primelist.reverse()
print(primelist[0])
    
