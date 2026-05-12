import sys
import math

buf = {}
    
def collatz(input, iterate):
    global buf
    # print(input, iterate)
    if input in buf:
        return iterate + buf[input]
    if input == 1:
        return iterate + 1
    if input % 2 == 0:
        return collatz(input / 2, iterate + 1)
    else:
        return collatz(3 * input + 1, iterate + 1)


maxv = 0
maxi = 0
#print(collatz(3, 0))
for i in range(1, 1000001):
    val = collatz(i, 0)
    buf[i] = val
    # print(buf)
    if val > maxv:
        maxv = val
        maxi = i
    
    sys.stdout.write(f"\rTesting: {i:} with chain: {val}                              ")
    sys.stdout.flush()

print("\nresult", maxi, maxv)    
#print(buf)