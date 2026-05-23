import sys
import math


def max_consecutive_sum(arr):
    if not arr:
        return 0
    
    current_max = arr[0]
    global_max = arr[0]
    
    for i in range(1, len(arr)):
        current_max = max(arr[i], current_max + arr[i])
        if current_max > global_max:
            global_max = current_max
            
    return global_max

row = 1000
# row = 5

total = (1  + row) * row // 2
fabon = [0] * (total) 

t = 0
pow20 = pow(2, 20)
pow19 = pow(2, 19)
for i in range(1, total + 1):
    t = (615949 * t + 797807) % pow20
    fabon[i - 1] = t - pow19


# for i, j in enumerate(fabon):
#     fabon[i] = i

matrix = []
sumMatrix = []
startcell = 0
for i in range(0, row):
    startcell = startcell + i
    endcell = startcell + i
    matrix.append(fabon[startcell:endcell + 1])
    sumMatrix.append(fabon[startcell:endcell + 1])


for row in range(len(sumMatrix)):
    sumMatrix[row].insert(0,0) 
    for col in range(1, len(sumMatrix[row])):
        sumMatrix[row][col] += sumMatrix[row][col-1]
# start from bottom row, 
# find 

# for each cell
# build array for triangle sum
# find the min 
minSum = 99999999999999
for i, drow in enumerate(matrix):
    for j, cell in enumerate(drow):
        # collect the cell sum of row into array
        # put to max_consecutive_sum 
        rowsum = cell
        curry = j + 2
        if rowsum < minSum:
                minSum = rowsum
        for x in range(i + 1, row):
            rowsum += sumMatrix[x][curry] - sumMatrix[x][j] # to reduce one more loop on calculate the row sum
            # for y in range(j, j + x - i + 1):
            #     rowsum += matrix[x][y]
            if rowsum < minSum:
                minSum = rowsum
            curry += 1


print("Result", minSum)