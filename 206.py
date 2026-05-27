import functools, math

maxVal = 1929394959697989990
minVal = 1020304050607080900

print(math.sqrt(maxVal))
print(math.sqrt(minVal))

for i in range(1010101010, 1389026623, 10): # as square val ends of "0", which it should be end with "0" as well
    val = str(i ** 2)
    if val[0] == "1" and val[2] == "2" and val[4] == "3" and val[6] == "4" and val[8] == "5" and val[10] == "6" and val[12] == "7" and val[14] == "8" and val[16] == "9" and val[18] == "0":
        print("Result", i, val)
        exit()
        