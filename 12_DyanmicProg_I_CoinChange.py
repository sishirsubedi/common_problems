# -*- coding: utf-8 -*-
"""
Created on Fri May 27 08:40:49 2016

@author: ibm-lenovo
"""

# dynamic program - coin change 

# this is fatal because of lack of dynamic programming..there is dublicate in calculation

def findnumofchange(change,n):
    K = [[0 for x in range(n+1)] for x in range(len(change)+1)]

    for i in range(1,(len(change)+1)):  # 1 to 5
        for w in range(1, n + 1):  # 0 to 5
            if w == 1 and i == 1:
                K[i][w] = 1
            elif i ==1:
                K[i][w] = K[i][w-1] + 1
            elif w == change[i-1]:
                K[i][w] = 1
            elif w > change[i-1]:
                K[i][w] = min(K[i][change[i-1]]+ K[i][w - change[i-1]], K[i - 1][w])
                #
                # K[i][w] = min(K[i][change[i-1]]+ K[i-1][w - change[i-1]], K[i - 1][w])
            else:
                K[i][w] = K[i - 1][w]

    return K




mat = (findnumofchange([1,5,10],16))
for i in mat:
    print i



def recDC(coinValueList,change,knownResults):
   minCoins = change
   if change in coinValueList:
      knownResults[change] = 1
      return 1
   elif knownResults[change] > 0:
      return knownResults[change]
   else:
       for i in [c for c in coinValueList if c <= change]: # i will be 1,5,10,and 25
         numCoins = 1 + recDC(coinValueList, change-i,
                              knownResults)
         if numCoins < minCoins:
            minCoins = numCoins
            knownResults[change] = minCoins
            #print change, knownResults
   return minCoins

print 'minimum coins : ' , (recDC([1,5,10,25],45,[0]*64))

