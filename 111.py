import time, math, itertools

def is_prime(x):  # Test if giving value is a prime
    if x <= 1:
        return False
    elif x <= 3:
        return True
    elif x % 2 == 0:
        return False
    else:
        for i in range(3, int(math.sqrt(x)) + 1, 2):
            if x % i == 0:
                return False
        return True
    
def S(n, d):
    for x in range(n):
        L = set()
        for y in itertools.product([i for i in range(10)], repeat = x):
            for z in set([x for x in itertools.permutations([d]*(n - x) + list(y), n)]):
                if z[0] != 0:
                    #print(z)
                    v = int("".join([str(i) for i in z]))
                    
                    if is_prime(v):
                        L.add(v)
        if len(L) > 0:
            #print("M:", x)
            #print("N:", len(L))
            return sum(L)
    
s = 0
for i in range(10):
    s += S(10, i)
print("Result", s)
