import sys
import math

sys.setrecursionlimit(1500)

def toss(total, current, ratio, balance):
    if total == current:
        return 0.5 * (balance + balance * ratio) + 0.5 * (balance - balance * ratio)
    return  0.5 * (balance + balance * toss(total, current + 1, ratio, balance)) + 0.5 * (balance - balance * toss(total, current + 1, ratio, balance)) 

print(toss(1000, 0, 0.25, 1))
