import time, math, itertools
##### i dont know how to complete it 
# def find_combinations(elements, target):
#     valid_combinations = []
#     # Loop through all possible combination lengths (from 1 to the length of elements)
#     for r in range(1, len(elements) + 1):
#         for combo in itertools.permutations(elements, r):
#             if sum(combo) == target:
#                 valid_combinations.append(list(combo))
#     return valid_combinations

# trunks = find_combinations([1] * 9 + [2] * 4 + [3] * 3 + [4, 4] + [5, 6, 7, 8, 9], 9)
# print(trunks)

# exit()
# for i in itertools.permutations(range(1, 10), 9):
#     # split into trunks
#     for t in trunks:
#         segment
#     pass


def partition(x, L, show = True):
    '''
    :param x: The number we wish to find partitions of
    :param L: List of numbers allowed to use to form partition
    :param show: Optional, default is True and it will show all the partitions, if False it will simply output how many there are.

    :returns numerator: Number of partitions or the actual partitions based on value of "show"
    
    .. code-block:: python
    
        print(partition(40, [i for i in range(1, 41)], False)) #37338
        print(partition(4, [1,2,3,4])) #[(1, 1, 1, 1), (2, 1, 1), (2, 2), (3, 1), (4,)]
        print(partition(71, prime_sieve(71), False)) #5007, From Project Euler Problem 77
        print(partition(100, [i for i in range(1, 101)], False) - 1) #190569291, From Project Euler Problem 76

    '''
    if 0 in L:
        return "0 cannot be part of L"
    A = [0] * (x + 1)
    A[0] = 1
    P = [[] for _ in range(x + 1)]
    P[0] = [()]
    for y in L:
        for i in range(len(P) - y):
            if show:
                for z in P[i]:
                    P[i + y].append((y,) + z)
            else:
                A[i + y] += A[i]
    if show:
        return P[-1]
    else:
        return A[-1]
    
print(partition(9, range(1, 10)))