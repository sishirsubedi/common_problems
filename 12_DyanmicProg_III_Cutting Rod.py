# -*- coding: utf-8 -*-
"""
Created on Fri Jun 03 12:05:25 2016

@author: ibm-lenovo
"""

# A Dynamic Programming solution for Rod cutting problem
INT_MIN = -32767
 
# Returns the best obtainable price for a rod of length n and
# price[] as prices of different pieces
def cutRod(price,length, n):
    K = [[0 for x in range(n+1)] for x in range(n+1)]
     
    for i in range(n+1):# 1 to 5
        for w in range(n+1): # 0 to 5
            if w==0 or i ==0:
                K[i][w] = 0
            elif length[i-1] <= w:
                K[i][w] = max(price[i-1]+K[i][w-i],K[i-1][w] )
            else:
                K[i][w] = K[i-1][w]

    return K
 
# Driver program to test above functions
price = [1, 5, 8, 9, 10, 17, 17, 20]
length =[1, 2, 3, 4, 5, 6, 7, 8]
#price=   [2,5,7,8,9] # cost of each length rod
#length = [1,2,3,4,5]
size = len(length)
print("Maximum Obtainable Value is "  + str(cutRod(price,length,size)))