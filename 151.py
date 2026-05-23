import sys
import math


def calculate(A2, A3, A4, A5):
    papers = A2 + A3 + A4 + A5
    
    if papers == 0:
        return 0
    if A2 + A3 + A4 == 0 and A5 > 0:
        return 1
    probability = 0.0
    if A2 > 0:
        probability += A2 * calculate(A2 - 1, A3 + 1, A4 + 1, A5 + 1) / papers
    if A3 > 0:
        probability += A3 * calculate(A2, A3 - 1, A4 + 1, A5 + 1) / papers
    if A4 > 0:
        probability += A4 * calculate(A2, A3, A4 - 1, A5 + 1) / papers
    if A5 > 0:
        probability += A5 * calculate(A2, A3, A4, A5 - 1) / papers
    return probability

print(calculate(1, 1, 1, 1))