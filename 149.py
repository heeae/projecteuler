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

row = 2000
# row = 4

fabon = [0] * row ** 2

for i in range(1, 55 + 1):
    fabon[i - 1] = (100003 - 200003 * i + 300007 * i **3) % 1000000 - 500000

for i in range(56, 2000 ** 2 + 1):
    fabon[i - 1] = (fabon[i - 24 - 1] + fabon[i - 55 - 1] + 1000000) % 1000000 - 500000

# for i, j in enumerate(fabon):
#     fabon[i] = i


matrix = []
for i in range(0, row):
    matrix.append(fabon[i * row:(i + 1) * row])

maxSum = 0
for x in matrix: 
    
    buf = x
    sumrow = max_consecutive_sum(buf)

    if sumrow >  maxSum: 
        maxSum = sumrow

for y in range(0, row): 
    sumcolumn = 0
    buf = []
    for x in range(0, row):
        buf.append(matrix[x][y])
    sumcolumn = max_consecutive_sum(buf)
    if sumcolumn >  maxSum: 
        maxSum = sumcolumn

for x in range(0, row + row):
    sumdiagonal = 0
    buf = []
    for y in range(0, x + 1):
        z = x - y
        if z < row and y < row:
            buf.append(matrix[z][y])
        
    sumdiagonal = max_consecutive_sum(buf)
    if sumdiagonal > maxSum:
        maxSum = sumdiagonal

for x in range(0, row + row):
    sumdiagonal = 0
    buf = []
    for y in range(0, x + 1):
        z = x - y
        if z < row and y < row:
            buf.append(matrix[row - z - 1][y])
        
    sumdiagonal = max_consecutive_sum(buf)
    if sumdiagonal > maxSum:
        maxSum = sumdiagonal

print("Result", maxSum)