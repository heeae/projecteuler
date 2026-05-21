import time, math, itertools


def probability(times):
    winStack = times // 2 + 1 if times % 2 == 0 else math.ceil(times / 2)
    permutation = set()
    for i in range(winStack, times + 1):
        for choice in itertools.permutations(["B"] * i + ["R"] * (times - i), times):
            permutation.add(choice)
    
    print(permutation)

#print(probability(15)) # not work for n = 15


# P(B), P(R) = (1/2, 1/2)
# P(BB), P(BR), P(RR) = P(B, 1) * P(B, 2), P(B, 1) * P(R, 2) + P(R, 1) * P(B, 2) + P(R, 2) * P(R, 1)
# P(BBB), P(BBR), P(BRR), P(RRR) = P(BB) * P(B, 3), P(BB) * P(R, 3) + P(BR) * P(B, 3), P(RR) * P(B, 3) + P(BR) * P(R, 3), P(RR) * P(R, 3)
# P(BBBB),          P(BBBR),                             P(BBRR),                            P(BRRR),                           P(RRRR) = 
# P(BBB) * P(B, 4), P(BBB) * P(R, 4) + P(BBR) * P(B, 4), P(BBR) * P(R, 4) + P(BRR) * P(B, 4),P(BRR) * P(R, 4) + P(RRR) * P(B, 4),   P(RRR) * P(R, 4)

def tupleMultiply(x, y):
    return (x[0] * y[0], x[1] * y[1])

def tupleSum(x, y):
    return (x[0] * y[1] + y[0] * x[1], x[1] * y[1])

def probability(color, row):
    if color == "R": 
        n = row
        #print((n, n + 1))
        return (n, n + 1)
    if color == "B":
        n = row
        #print((1, n + 1))
        return (1, n + 1)

def simplifyTuple(x):
    gcd = math.gcd(x[0], x[1])
    return (x[0] // gcd, x[1] // gcd)

def calprobability(numB, numR):
    #print("cal", numB, numR)
    if numB + numR == 1:
        return (1, 2)
    if numR == 0:
        return tupleMultiply(calprobability(numB - 1, 0), probability("B", numB + numR))
    elif numB == 0:
        return tupleMultiply(calprobability(numR - 1, 0), probability("R", numB + numR))
    else:
        return tupleSum(tupleMultiply(calprobability(numB, numR - 1), probability("R", numB + numR)), 
                        tupleMultiply(calprobability(numB - 1, numR), probability("B", numB + numR)))

initTuple = (0, 1)
turn = 15
winStack = turn // 2 + 1 if turn % 2 == 0 else math.ceil(turn / 2)
for i in range(turn, winStack - 1, -1):
    initTuple = simplifyTuple(tupleSum(initTuple, calprobability(i, turn - i)))
    
print(initTuple)

result = initTuple[1] // initTuple[0]
print(initTuple[0] / initTuple[1])
print("Fund", result)

# (3068737037
#  6974263296000)