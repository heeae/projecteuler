import functools, math


S = [0]
fabonCnt = 1
def nextVal():
    global S, fabonCnt
    S += [0]
    if fabonCnt <= 55:
        S[fabonCnt] = (100003 - 200003 * fabonCnt + 300007 * fabonCnt **3) % 1000000
    else:
        S[fabonCnt] = (S[fabonCnt - 24] + S[fabonCnt - 55] + 1000000) % 1000000
    fabonCnt += 1
    return S[fabonCnt - 1]
    

#V keeps tracks of which connected component vertex i is in
V = [i for i in range(10**6)]
#These are the connected components of the graph, initially every vertex is in its own connected component
#The head of the connected component is itself
cc = {i:set([i]) for i in range(10**6)}

calls = 0

while True:
    caller = nextVal()
    called = nextVal()

    if caller != called:
        calls += 1
        connectedcaller = V[caller]
        connectedcalled = V[called]
        mergeFrom = connectedcaller if connectedcaller > connectedcalled else connectedcalled
        mergeTo = connectedcaller if connectedcalled > connectedcaller else connectedcalled
        
        if mergeFrom == mergeTo:
            continue


        for i in cc[mergeFrom]:
            V[i] = mergeTo
        cc[mergeTo] |= cc[mergeFrom]
        del cc[mergeFrom]
        
    if len(cc[V[522487]]) > 99 * 10 ** 4 - 1:
        print("Result", calls)
        exit()
