import sys
import math

buffer = ""
i = 1
while len(buffer) < 1000000:
    buffer += str(i)
    i += 1

print(int(buffer[0]) * int(buffer[9]) * int(buffer[99]) * int(buffer[999]) * int(buffer[9999]) * int(buffer[99999]) * int(buffer[999999]))  
