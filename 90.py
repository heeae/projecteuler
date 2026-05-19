import math
from itertools import combinations

candidate = ["01",  "04", "09", "16",  "25", "36", "49",  "64", "81"]
def canPair(set1, set2):
    for x in candidate:
        x = x.replace("9", "6")
        if (x[0] not in set1 or x[1] not in set2) and (x[0] not in set2 or x[1] not in set1):
            return False
    return True

comb = list(combinations(["0", "1", "2", "3", "4", "5", "6", "7", "8", "6"], 6)) # 6 and 9 are the same but 2 different set
print(len(comb))
result = 0
for i in comb:
    for j in comb:

        if canPair(i, j):
           result += 1 
           print("Pair", i, j)

print("Result",  result / 2) # as i and j will be double counted


