import functools
import itertools
import sys
import math
import re
import collections

#idea from IVL, 
# only 0, 1, 2, 3, 6, 7, 8, 9 in the list
# check the linked list of the input,  which "what is appeared before the input, e.g. 3 is before 1 and 1 is before 9 for 319,"
# there are  only "7" have nothing before it, put 7 in the list
# and only "3" have nothing before it except 7, so 73
# continue,  "1", then "6",  "2",  "8", "9", "0" comes out
# if  there are some non decisive, i think it need to do permutation from that point

candidate = ['0', '1', '2', '3', '6',  '7',  '8',  '9']

validate = [319, 680, 180, 690, 129, 620, 762, 689, 762, 318, 368, 710, 720, 710, 629, 168, 160, 689, 716, 731, 736, 729, 316, 729, 729, 710, 769, 290, 719, 680, 318, 389, 162, 289, 162, 718, 729, 319, 790, 680, 890, 362, 319, 760, 316, 729, 380, 319, 728, 716]


iteration = collections.defaultdict(set)

for x in validate:
    y = str(x)
    iteration[y[2]].add(y[1])
    iteration[y[1]].add(y[0])

print(iteration)




"73162890"