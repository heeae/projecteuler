import sys
import math


phicnt = 0
for i in range(2, 12000+1):
    phi = 0
    for j in range(math.floor(i / 3), i):
        if j * 2 >=  i:
            break
        if j * 3 > i:
            if math.gcd(i, j) == 1:
                phi += 1
    phicnt += phi
    sys.stdout.write(f"\rtesting...{i:}\t\t{phicnt}")
    sys.stdout.flush()

print("\n result",  phicnt)
