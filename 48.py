import sys
import math

sum = 0
for i in range(1, 1001):
    sum += i ** i
print("Sum: " + str(sum))
print(str(sum)[-10:])
