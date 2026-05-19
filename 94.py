import time, itertools, sys, math
from functools import lru_cache


counter = 0
for  i in range(3, 1_000_000_000 + 1):
    if (i + 1 ) % 3 == 0:
        side = ( i + 1 ) // 3
        base = i - 2 * side
    elif  (i - 1) % 3 == 0:
        side = ( i - 1 ) // 3
        base = i - 2 * side
    else:
        continue
    x = 4 * (side **  2) - base ** 2
    if x > 0:
        sqrt = int(math.sqrt(x))
        if sqrt ** 2 == x:
            area = (sqrt) * base 
        
            if area % 4 == 0:
                counter += i
                print("\nPair found", side, base, i, area / 4)
            sys.stdout.write(f"\rTesting {i:}\t\t\t{counter}")
            sys.stdout.flush()
        

print("Result", counter)
