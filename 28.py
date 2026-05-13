import sys
import math

def spiralmatrix(n):
    data = []
    for i in range(n):
        row = []
        for j in range(n):
            row.append(0)
        data.append(row)

    startx = n - 1
    starty = 0
    directionx = -1
    directiony = 0
    for i in range(n ** 2, 0, -1):
        data[starty][startx] = i
        
        # check need to change direction 
        if(directionx < 0 and directiony == 0): # left
            if(startx == 0 or data[starty][startx + directionx] != 0):
                directionx, directiony = 0, 1
        elif(directionx == 0 and directiony > 0): # down
            if(starty >= n - 1 or data[starty + directiony][startx] != 0):
                directionx, directiony = 1, 0
        elif(directionx == 0 and directiony < 0): # up
            if(starty == 0 or data[starty + directiony][startx] != 0):
                directionx, directiony = -1, 0
        elif(directionx > 0 and directiony == 0): # right
            if(startx == n - 1 or data[starty][startx + directionx] != 0):
                directionx, directiony = 0, -1
        
        startx += directionx
        starty += directiony

    return data

data = spiralmatrix(1001)
rst = 0
for i in range(1001):
    rst += data[i][i]
    rst += data[i][1000 - i]
print(rst - 1)
