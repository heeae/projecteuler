import sys
import math



def divisor_sum(buf):
    divisor = 0
    for i in range(1, buf):
        if buf % i == 0:
            divisor += i


    return divisor

rst = 0
abundant = []
for i in range(1, 28124):
    divisor = divisor_sum(i)
    if divisor > i:
        abundant.append(i)

sumabundant = {}
for i in abundant:
    for j in abundant:
        sumabundant[i + j] = True
for i in range(1, 28124):
    if i not in sumabundant:
        rst += i
        print(i)

print("\n Result:" + str(rst))
