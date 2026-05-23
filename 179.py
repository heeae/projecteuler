import sys
import math

total = 10**7

buf = [0] + [1] * total
for x in range(2, total // 2 + 1):
    for y in range(1, total // x + 1):
        buf[x * y] += 1

rst = 0

for cnt in range(1, 10 ** 7 - 1):
    if buf[cnt] == buf[cnt + 1]:
        rst += 1
    
print("\n Result:" + str(rst))
