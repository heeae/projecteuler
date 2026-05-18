import functools
import itertools
import sys
import math

#????????????????????????

def PentagonalNumberTheorem(N):
    p = [1] + [0]*(N + 1) #Initalise array
        
    for n in range(1,len(p)):
        y = 1
        while True:            
            if y % 2 == 0: #Find sign
                sign = -1
            else:
                sign = 1
            
            pen = (3*y*y - y)//2 #Pentagonal number
            if pen > n: #if pen > n => 0 > n - pen so we can stop here
                break
            
            p[n] += sign*p[n-pen] #Update the cell
            
            pen += y #Hmm why am I adding a y here? Think about the difference between p(k) and p(-k)
            if pen > n:
                break
            
            p[n] += sign*p[n-pen]
            y += 1 #Increment y to get the next pentagonal number
        
        if p[n] % 10**6 == 0:
            return n

print(PentagonalNumberTheorem(60000))