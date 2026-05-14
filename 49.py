import sys
import math

primelist = {}

with open("prime.txt", "rt") as file:
    for line in file: 
        line = line.strip() #or some other preprocessing
        if(int(line) < 10000):
            primelist[int(line)] = True
        
print("built the list")
def permutatestring(x):
    if x == "":
        return [""]
    result = []
    for i in x:
        buf = permutatestring(x.replace(i, "", 1))
        for j in buf:
            result.append(i + j)
    return result

for i in range(1000, 10000):
    if i in primelist:
        entity = permutatestring(str(i))
        target = list(filter(lambda x : int(x) in primelist and int(x) > i, entity))
        for j in list(target):
            #print("Checking: " + str(i) + ", " + str(j) + ", " + str(i + (int(j) - i) * 2))
            if  str(i + (int(j) - i) * 2) in target:
                print(i, j, i + (int(j) - i) * 2)
                #exit()
