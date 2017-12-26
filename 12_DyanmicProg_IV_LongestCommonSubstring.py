# -*- coding: utf-8 -*-
"""
Created on Fri Jun 03 14:50:29 2016

@author: ibm-lenovo
"""

def maxCommonSubstring(str1,str2):
    len1 = len(str1) 
    len2 = len(str2)
    common =[]
    
    K = [[0 for x in range(len2+1)] for x in range(len1+1)]
     
    for i in range(len1+1):# 0 to n
        for j in range(len2+1): # 0 to n
            if i==0 or j==0:
                K[i][j] = 0
            elif str1[i-1]==str2[j-1]:
                K[i][j] = K[i-1][j-1] + 1
                if str2[j-1] not in common:
                    common.append(str2[j-1]) # this to show which are common ones 
            else:
                K[i][j] = max(K[i-1][j],K[i][j-1])

    return common#K


def maxCommonSubstring2(word,pattern):
    len1 = len(word)
    len2 = len(pattern)
    mat = [[0 for x in range(len1 + 1)] for y in range(len2 + 1)]
    for p in range(1,len2 + 1):
        for w in range(1,len1+1):
            if word[w-1]==pattern[p-1]:
                mat[p][w] = mat[p-1][w-1] + 1
            else:
                mat[p][w] = max(mat[p-1][w] ,mat[p][w-1])
    return mat




# Driver program to test above functions
string1 = ['a','b','c','d','e','f']
string2 =['a','c','b','c','f']
#price=   [2,5,7,8,9] # cost of each length rod
#length = [1,2,3,4,5]
#print(string1, string2, "Common max sequence is "  + str(maxCommonSubstring(string1,string2) ))

print str(maxCommonSubstring(string1,string2))

pattern = ['b','c','d']
word =['a','b','c','d','e']

mat = maxCommonSubstring(word,pattern)

for i in mat:
    print i

X = "zxabcdezy"
y = "yzabcdezx"

mat = maxCommonSubstring2(X, y)

for i in mat:
    print i