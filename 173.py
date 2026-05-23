import sys
import math



total = 1_000_000
result = 0
for i in range(3, total // 4 + 1 + 1):
    sys.stdout.write(f"\r{i}")
    numsquare = i ** 2
    if i % 2 == 0: # if even
        for j in range(i - 2, 1, -2 ):
            val = numsquare - j ** 2
            if val <= total:
                #print("val", val, i, j)
                result += 1
            else:
                break
    else:
        for j in range(i - 2, 0, -2 ):
            val = numsquare - j ** 2
            if val <= total:
                #print("val", val, i, j)
                result += 1
            else:
                break

print("Result", result)