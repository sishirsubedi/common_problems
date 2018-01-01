# -*- coding: utf-8 -*-
"""
Created on Thu May 19 13:31:09 2016

@author: ibm-lenovo
"""


import sys
# MAXIMUM SUB ARRAY _ BruteForce

def maxsubarray(glist):
    sum = [glist[0],0,0]
    for i in range(0,len(glist)-1):
        temp = 0
        for j in range(i,len(glist)):
            temp += glist[j]
            if(temp>sum[0]):
                sum[0] = temp
                sum[1] = i
                sum[2] = j 
    return sum
    
    
    
# MAXIMUM SUB ARRAY _ Dynamic

def maxsubarray_dynamic(A, low, high):
    if high == low :
        return [low, high, A[low]]
    else:
        mid = (high+low)/2
        left = maxsubarray_dynamic(A,low, mid)
        right = maxsubarray_dynamic(A,mid+1,high)
        cross = maxsubarray_crossing(A, low, mid, high)
    if left[2]>right[2] and left[2]>cross[2]:
        return left
    elif right[2]>left[2] and right[2]>cross[2]:
        return right
    else:
        return cross

def maxsubarray_crossing(A, low, mid, high):
    sum = 0
    left_sum = 0
    right_sum = 0
    max_left = 0
    max_right= 0
    for i in range (mid-1, low):
        sum = sum + A[i]
        if sum>left_sum :
            left_sum = sum
            max_left = i
    sum = 0
    for j in range ( mid, high):
        sum = sum + A[j]
        if sum>right_sum:
            right_sum = sum
            max_right = j
    return [max_left, max_right, left_sum+right_sum]
        
    
    
    
    
givenlist = [1,-3,2,-5,7,6,-1,-4,11,-23]  # 4 to 8 - 19
givenlist2 = [-3,-2,-5,-7,-6,0,-4,-11,-23] # 5 to 5 - -1
givenlist3 = [1,2,3,4,5,6,7,8,9] # 0 to 8 - 45
sum = maxsubarray(givenlist)



sum1= maxsubarray_dynamic(givenlist,0,9)
sum2= maxsubarray_dynamic(givenlist2,0,8)
sum3= maxsubarray_dynamic(givenlist3,0,8)

print sum, sum1, sum2, sum3






