# -*- coding: utf-8 -*-
"""
Created on Thu Jun 02 21:47:12 2016

@author: ibm-lenovo
"""

# A Dynamic Programming based Python Program for 0-1 Knapsack problem
# Returns the maximum value that can be put in a knapsack of capacity W
def knapSack(W, wt, val, n):
    K = [[0 for x in range(W+1)] for x in range(n+1)]
 
    # Build table K[][] in bottom up manner
    for i in range(n+1):
        for w in range(W+1):
           
            if i==0 or w==0:
                K[i][w] = 0
            elif wt[i-1] <= w:
                K[i][w] = max(val[i-1] + K[i-1][w-wt[i-1]],  K[i-1][w])
            else:
                K[i][w] = K[i-1][w]
                
                
                
    return K


def knapsack_rec(W,wt, val, n,arr):
    if n == 0 : return 0
    if arr[n][W] != 0 : return arr[n][W]
    if wt[n-1] > W : result = knapsack_rec(W, wt, val, n-1,arr)
    else:
        result = max (val[n-1]+knapsack_rec(W-wt[n-1],wt,val,n-1,arr), knapsack_rec(W,wt,val,n-1,arr))
        arr[n][W] = result
    return result


# Driver program to test above function
val = [12, 10, 6]
wt = [1, 2, 3]
W = 5
n = len(val)

arr = [[0 for x in range(W+1)] for x in range(n+1)]
#print arr
result = (knapSack(W, wt, val, n))
for i in result:
    print i
knapsack_rec(W, wt, val, n,arr)
for i in arr:
    print i