import sys
import math



def continued_fraction(x):
    m0 = 0
    d0 = 1
    a0 = math.floor(math.sqrt(x)) #These are the starting values
    temp_list = [a0]
    while True:
        mn = int(d0*a0 - m0) 
        dn = int((x - mn**2)/d0)
        an = int(math.floor((math.sqrt(x) + mn) / dn)) #new values
        temp_list.append(an)
        #if an == 2*math.floor(math.sqrt(x)):
            #break
        if len(temp_list) == 100:
            break
        m0 = mn
        d0 = dn
        a0 = an #Replace values
        
    return temp_list
def convergent(D):
    cf = continued_fraction(D)
    h0, h1 = 1, cf[0]
    k0, k1 = 0, 1
    if h1**2 - D*k1**2 == 1:
        return [h1, k1, D]
    else:
        x = 1
        while True:
            hn = cf[x]*h1 + h0
            kn = cf[x]*k1 + k0
            if hn**2 - D*kn**2 == 1:
                break
            h0 = h1
            h1 = hn
            k0 = k1
            k1 = kn
            x += 1
    return [hn, kn, D]


maxX = 0 # 61, 12903201, 97 20740792
maxD = 0
for D in range(2, 1001):
    if int(math.sqrt(D)) ** 2 == D:
        continue
    rst = convergent(D)
    print("Solution is found for ", D, "is x=", rst[0], "and y=", rst[1])
    if rst[0] > maxX:
        maxX = rst[0]
        maxD = D
    isFound = True

print("Result=", maxX, maxD)


exit()

for D in range(98, 1000 + 1):
    if int(math.sqrt(D)) ** 2 == D:
        continue
    isFound = False
    x = 2
    while not isFound: 
        # print(D, x, math.floor(math.sqrt((x ** 2 - 1) / D)) + 1)
        val = (x ** 2 - 1) / D
        if int(math.sqrt(val)) ** 2 == val:
            print("Solution is found for ", D, "is x=", x, "and y=", math.sqrt(val))
            if x > maxX:
                maxX = x
            isFound = True
            break
        x += 1

        sys.stdout.write(f"\rtesting... {x:}\t\t\t ")
        sys.stdout.flush()

print("Result=", maxX)

