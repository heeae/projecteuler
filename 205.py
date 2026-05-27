import functools, math


probaMatrixPeter = [0] * 37
probaMatrixColin = [0] * 37

for i1 in range(1, 4 + 1):
    for i2 in range(1, 4 + 1):
        for i3 in range(1, 4 + 1):
            for i4 in range(1, 4 + 1):
                for i5 in range(1, 4 + 1):
                    for i6 in range(1, 4 + 1):
                        for i7 in range(1, 4 + 1):
                            for i8 in range(1, 4 + 1):
                                for i9 in range(1, 4 + 1):
                                    probaMatrixPeter[i1 + i2 + i3 + i4 + i5 + i6 + i7 + i8 + i9] += 1 #/ (4 ** 9)

for i1 in range(1, 6 + 1):
    for i2 in range(1, 6 + 1):
        for i3 in range(1, 6 + 1):
            for i4 in range(1, 6 + 1):
                for i5 in range(1, 6 + 1):
                    for i6 in range(1, 6 + 1):
                        probaMatrixColin[i1 + i2 + i3 + i4 + i5 + i6] += 1 #/ (6 ** 6)

print(probaMatrixPeter)
print(sum(probaMatrixPeter))
print(probaMatrixColin)
print(sum(probaMatrixColin))
# P(Peter Win) 
# = P(Peter get 36 and Colin get < 36) | P(Peter get 35 and Colin get < 35) | .... 
# = P(P36) * P(C6 + C7 + ... + C35 )  | P(P35) * P(C6 + ... C34) ...

probability = 0.0
for i in range(36, 9 - 1, -1):
    print("Peter", i)
    peterP = probaMatrixPeter[i] 
    colinP = 0
    for j in range(i - 1, 6 - 1, -1):
        print("Colin", j)
        colinP += probaMatrixColin[j] / 6 ** 6
    probability += peterP * colinP / 4 ** 9


print(probability)

