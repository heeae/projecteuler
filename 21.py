import sys
import math



def divisor_sum(buf):
    divisor = 0
    for i in range(1, buf):
        if buf % i == 0:
            divisor += i


    return divisor

rst = 0

for cnt in range(1, 10000):
    divisorsum = divisor_sum(cnt)
    divisorsum2 = divisor_sum(divisorsum)
    if(cnt == divisorsum2 and cnt != divisorsum):
        rst += cnt

print("\n Result:" + str(rst))
