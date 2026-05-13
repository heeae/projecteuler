import sys
import datetime

suncnt = 0
for i in range(1901, 2001):
    for j in range(1, 13):
        x = datetime.datetime(i, j, 1)
        if x.strftime("%a") == "Sun":
            suncnt += 1
print(suncnt)