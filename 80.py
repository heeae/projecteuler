import functools
import itertools
import decimal
import math
import re
import collections


decimal.getcontext().prec = 102 

rst = 0
#print(decimal.Decimal(2).sqrt())
for i in range(2, 101):
    if int(i **  0.5) ** 2 == i:
        continue
    val = str(decimal.Decimal(i).sqrt())
    decimals = val.replace(".", "")[0:100]

    valtrunk = 0
    for j in decimals:
        valtrunk += int(j)
    rst += valtrunk
    print(i, valtrunk)

print("Result ", rst)
