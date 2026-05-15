import sys

triangle = []
square = []
pentagon = []
hexagon = []
heptgon = []
octagon = []

def candidate(inputlist, val):
    output = []
    lbound = val * 100
    ubound = (val + 1) * 100
    for c in inputlist:
        if c <lbound or c >= ubound:
            continue
        output.append(c)
    return output

def candidateSet(inputlists, val):
    output = []
    for x in inputlists:
        rst = candidate(x, val)
        if len(rst) > 0:
            y = inputlists.copy()
            y.remove(x)
            output.append((y, rst))
    return output


for i in range(1, 20000):
    p3 = int(i * (i + 1) / 2)
    p4 = i * i
    p5 = int(i * (3 * i - 1) / 2)
    p6 = i * (2 * i - 1)
    p7 = int(i * (5 * i - 3) / 2)
    p8 = i * (3 * i - 2)
    if p3 >= 1000 and p3 <= 9999:
        triangle.append(p3)
    if p4 >= 1000 and p4 <= 9999:
        square.append(p4)
    if p5 >= 1000 and p5 <= 9999:
        pentagon.append(p5)
    if p6 >= 1000 and p6 <= 9999:
        hexagon.append(p6)
    if p7 >= 1000 and p7 <= 9999:
        heptgon.append(p7)
    if p8 >= 1000 and p8 <= 9999:
        octagon.append(p8)
        
print(triangle)
print(square)
print(pentagon)
print(hexagon)
print(heptgon)
print(octagon)
for i in triangle:
    s3 = i % 100
    c4 = candidateSet([square, pentagon, hexagon, heptgon, octagon], s3)
    for j in c4:
        for jx in j[1]:
            s4 = jx % 100
            c5 = candidateSet(j[0], s4)
            for k in c5:
                for kx in k[1]:
                    s5 = kx % 100
                    c6 = candidateSet(k[0], s5)
                    for l in c6:
                        for lx in l[1]:
                            s6 = lx % 100
                            c7 = candidateSet(l[0], s6)
                            for m in c7:
                                for mx in m[1]:
                                    s7 = mx % 100
                                    c8 = candidateSet(m[0], s7)
                                    for n in c8:
                                        for nx in n[1]:
                                            s8 = nx % 100
                                            if i // 100 == s8:
                                                print("result", i, jx, kx, lx, mx, nx, i + jx + kx + lx + mx + nx)
                                                #exit()
                

