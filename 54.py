import functools
import sys
import math
import itertools


card = {"2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "T": 10, "J": 11, "Q": 12, "K": 13, "A": 14}
cardtype = {"S": 4, "H": 3, "C": 2, "D": 1}

def resolveCard(x):
    return (card[x[0]], cardtype[x[1]])

def pokerRank(a1, a2, a3, a4, a5): # return tuple of rank
    cards = [resolveCard(a1), resolveCard(a2), resolveCard(a3), resolveCard(a4), resolveCard(a5)]
    cards.sort(key=functools.cmp_to_key(lambda x, y: x[0] - y[0] if x[0] != y[0] else x[1] - y[1]))
    # 1 = high card, 2 = one pair, 3 = two pair, 4 = three of a kind, 5 = straight, 6 = flush, 7 = full house, 8 = four of a kind, 9 = straight flush, 10 = royal flush

    maxcnt = 0
    maxcard= 0
    twopaircnt = 0

    cardgroup = itertools.groupby(cards, key = lambda x : x[0])
    for xy, g in cardgroup:
        groupcnt = len(list(g))
        if groupcnt > maxcnt:
            maxcnt = groupcnt
            maxcard = xy
        if groupcnt == 2:
            twopaircnt += 1

    if cards[0][0] + 1 == cards[1][0] and cards[1][0] + 1 == cards[2][0] and cards[2][0] + 1 == cards[3][0] and cards[3][0] + 1 == cards[4][0]:
        if cards[0][0] == 10:
            if cards[0][1] == cards[1][1] == cards[2][1] == cards[3][1] == cards[4][1]:
                return (10, cards[4][0], cards[4][1])
            else:
                return (5,  cards[4][0], cards[4][1])
        else:
            if cards[0][1] == cards[1][1] == cards[2][1] == cards[3][1] == cards[4][1]:
                return (9, cards[4][0], cards[4][1])
            else:
                return (5, cards[4][0], cards[4][1])
    elif  cards[1][0] == cards[2][0] == cards[3][0] and (cards[0][0] == cards[1][0] or cards[4][0] == cards[1][0]):
        return (8, cards[3][0], cards[3][1])
    elif cards[0][0] == cards[1][0] == cards[2][0] and cards[3][0] == cards[4][0]:
        return (7, cards[0][0], cards[2][1])
    elif cards[2][0] == cards[3][0] == cards[4][0] and cards[0][0] == cards[1][0]:
        return (7, cards[2][0], cards[2][1])
    elif cards[0][1] == cards[1][1] == cards[2][1] == cards[3][1] == cards[4][1]:
        return (6, (cards[4][0], cards[3][0], cards[2][0], cards[1][0], cards[0][0]), cards[4][1])
    elif maxcnt == 3:
        return (4, maxcard, 0)
    elif twopaircnt == 2:
        # find the cnt 
        data = itertools.groupby(cards, key = lambda x : x[0])
        datadict = []
        for x, g in data:
            lg = list(g)
            datadict.append(((x, lg[0][1]), len(lg)))
        groupedcnt = list(sorted(datadict, key=lambda x: x[1] * 100 + x[0][0], reverse=True))
        return (3, (groupedcnt[0][0][0], groupedcnt[1][0][0], groupedcnt[2][0][0]), (groupedcnt[0][0][1], groupedcnt[1][0][1], groupedcnt[2][0][1]))
    elif twopaircnt == 1:
        data = itertools.groupby(cards, key = lambda x : x[0])
        datadict = []
        for x, g in data:
            lg = list(g)
            datadict.append(((x, lg[0][1]), len(lg)))
        groupedcnt = list(sorted(datadict, key=lambda x: x[1] * 100 + x[0][0], reverse=True))
        return (2, (groupedcnt[0][0][0], groupedcnt[1][0][0], groupedcnt[2][0][0], groupedcnt[3][0][0]), (groupedcnt[0][0][1], groupedcnt[1][0][1], groupedcnt[2][0][1], groupedcnt[3][0][1]))
    else:
        return (1, (cards[4][0], cards[3][0], cards[2][0], cards[1][0], cards[0][0]), cards[4][1])

def comparerank(a1, a2):
    if isinstance(a1, int) and  isinstance(a2, int):
        return a1 - a2
    if a1[0] > a2[0]:
        return 1
    elif a1[0] < a2[0]: 
        return -1
    else:
        rst = comparerank(a1[1], a2[1])
        if rst == 0:
            return comparerank(a1[2], a2[2])
        else:
            return rst



primelist = {}
cnt = 0
with open("54.txt", "rt") as file:
    for line in file: 
        line = line.strip() #or some other preprocessing
        trunk = line.split(" ")
        player1 = pokerRank(trunk[0], trunk[1], trunk[2], trunk[3], trunk[4])
        player2 = pokerRank(trunk[5], trunk[6], trunk[7], trunk[8], trunk[9])
        rst = comparerank(player1, player2)
        
        if rst == 1:
            print("A", player1, player2)
            cnt +=1
        else:
            print("B", player1, player2)

print(" Result: " + str(cnt))
        