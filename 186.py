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
    

# V keep the mapping to the head of the list of friends
V = [i for i in range(10**6)]

# cc keep the friends list with the head of the friends as the key, ("head" mean the smallest one)
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
        
        if mergeFrom == mergeTo: # they are already friends
            continue

        for i in cc[mergeFrom]: # put all friends from the larger one to the smaller one
            V[i] = mergeTo # set the head of the friends
        cc[mergeTo] |= cc[mergeFrom]  # merge both set
        del cc[mergeFrom] 
        
    if len(cc[V[522487]]) > 99 * 10 ** 4 - 1:
        print("Result", calls)
        exit()
