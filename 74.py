import sys
import math


def iteration(x):
    cnt = 0
    for i in str(x):
        cnt += math.factorial(int(i))
    return cnt

index = {}
def resolveList(x):
    chainlist = {}
    v = x
    # if v in index:
    #     return index[v]
    iterationcnt = 1
    #print(v)
    while v not in chainlist:        
        chainlist[v] = True
        v = iteration(v)
        #print(v)
        # if v in index:
        #     iterationcnt += index[v]
        #     break
        iterationcnt += 1
    index[x] = iterationcnt - 1
    return iterationcnt - 1

rst = 0
for i in range(1, 1000000+1):
    iteracnt = resolveList(i)
    #print("testing", i, iteracnt)
    if iteracnt == 60:
        rst += 1
        print("Record found ", i, iteracnt )
        #exit()
    
print("Result", rst)