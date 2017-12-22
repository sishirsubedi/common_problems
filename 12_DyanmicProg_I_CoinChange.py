# -*- coding: utf-8 -*-
"""
Created on Fri May 27 08:40:49 2016

@author: ibm-lenovo
"""

# dynamic program - coin change

def findnumofchange2(change,n):
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


def findnumofchange(change,n):
    mat = [[0 for x in range(n+1)] for x in range(len(change)+1)]

    for c in range(1,(len(change)+1)):
        for m in range(1, n + 1):
            if change[c-1] ==m :
                mat[c][m] = 1
            elif m>change[c-1] and change[c-1]==1:
                mat[c][m] = 1 + mat[c][m - change[c - 1]]

            elif m>change[c-1] and change[c-1]!=1:
                mat[c][m] = min(mat[c-1][m],1+ mat[c][m-change[c-1]])

            elif m<change[c-1]:
                mat[c][m] = mat[c-1][m]

    return mat


mat = (findnumofchange([1,5,10,25],42))
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

print 'minimum coins : ' , (recDC([1,6,10],45,[0]*64))

