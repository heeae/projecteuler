import sys
import math

# throught, to meet the "sequence", the incrementation should have a pattern, e.g. U which mean increment is "3", UD mean start with 1 and increment 9, UDDD mean start with 1 and increment 81, repeat the process until the fulfill the result 


finalString = "UDDDUdddDDUDDddDdDddDDUDDdUUDd"
targetString =  "U" #"UDDDUdddDDUDDddDdDddDDUDDdUUDd"


def modifiedCollatz(buf, originalN, N):
    
    if targetString[0:len(buf)] != buf:
        return buf
    if buf == targetString:
        print("Found", originalN)
        return buf
        
    if N == 1:
        return buf
    remainder = N % 3
    if remainder == 0:
        return modifiedCollatz(buf + "D", originalN, N // 3)
    elif remainder == 1:
        return modifiedCollatz(buf + "U", originalN, (4 * N  + 2) // 3 )
    elif remainder == 2:
        return modifiedCollatz(buf + "d", originalN, (2 * N - 1) // 3)

startValue = 10 ** 15 + 1
lastI = 0
increment = 1
while targetString != finalString:
    for i in range(startValue, 10 ** 15 + 100000000000000000000, increment):
        val = modifiedCollatz("", i, i)
        if val == targetString:
            if lastI != 0:
                print("Increment", i - lastI)
                startValue = lastI
                increment = i - lastI
                targetString = finalString[0:len(targetString) + 1]
                lastI = 0
                break
            lastI = i
print("Result", i)
        