import functools, math, sys

p1 = 1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679
p2 = 8214808651328230664709384460955058223172535940812848111745028410270193852110555964462294895493038196


def DAB(target):
    pn2 = str(p1)
    pn1 = str(p2)

    pn = pn2 + pn1
    while len(pn) < target:
        pn2 = pn1
        pn1 = pn
        pn = pn2 + pn1
    return pn[target]


def DABCalculation(target):
    pn2 = len(str(p1))
    pn2T = "A"
    pn1 = len(str(p2))
    pn1T = "B"

    pn = pn2 + pn1
    pnT = pn2T + pn1T
    while pn < target:
        pn2 = pn1
        pn2T = pn1T
        pn1 = pn
        pn1T = pnT
        pn = pn2 + pn1
        pnT = pn2T + pn1T
    return (pnT, pn)


DABCalculation((127 + 19 * 17) * 7 ** 17)
        
