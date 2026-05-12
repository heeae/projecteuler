import sys
import math

cnt = 10000
while True:
    buf = cnt * (cnt + 1) / 2

    
    divisor = 0
    for i in range(1, int(math.sqrt(buf + 1))):
        if buf % i == 0:
            divisor += 2
    
    sys.stdout.write(f"\rTesting: {cnt:} with divisor: {divisor}                              ")
    sys.stdout.flush()
    if divisor >= 500:
        print("\n Result:" + str(buf))
        exit()
    cnt += 1