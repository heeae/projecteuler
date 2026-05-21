import sys, math

primelist = {}

with open("prime.txt", "rt") as file:
    for line in file: 
        line = line.strip() #or some other preprocessing
        primelist[int(line)] = True
        

val = int(sys.argv[1])
for i in range(max(primelist.keys()) + 1, val):
    notprime = False
    sqrt = math.sqrt(i)
    for j in primelist.keys():
        if j > sqrt:
            break
        if i % j == 0:
            notprime = True
            break
    
    sys.stdout.write(f"\r{i:}")
    sys.stdout.flush()
    if not(notprime):
        primelist[i] = True
print("built the list")
with open("prime.txt", "wt") as file:
    for i in primelist.keys():
        file.write(str(i) + "\n")


