import sys


i = 0
j = 1 
buf = 0
while True: #for x in range(1, int(sys.argv[1]) + 1):
    k = i + j
    i = j
    j = k
    
    if k % 2 == 0:
        buf += k
    if k >= int(sys.argv[1]):
        break
    sys.stdout.write(f"\r{k:}")
    sys.stdout.flush()
print("\n" + str(buf))