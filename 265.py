import sys
import math

# 2^5 = 32, value is start from "000001", and it should ends with 1 
binstr = "00000100000000000000000000000001" #67108865
endstr = "00000111111111111111111111111111" #134217727





def isDistinct(input, length):
    txt = input + input
    d = {}
    for i in range(len(input)):
        trunk = txt[i:i+length]
        if trunk in d:
            return False
        d[trunk] = True
    # print(sorted(list(d.keys())))
    return True

def dec2bin(n, length):
    res = ""
    while n > 0:
        res = str(n % 2) + res
        n //= 2
    return ("00000000000000000000000000000000" + res)[-1 * length:]


# isDistinct(dec2bin(131913253))
# exit()

count = 0

for i in range(67108865, 134217727 + 1, 2):
# for i in range(256):
    x = dec2bin(i, 32)
    if isDistinct(x, 5):
        #print(i)
        #print("Find result", i, x)
        count += i

print("Result", count)