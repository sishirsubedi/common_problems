# -*- coding: utf-8 -*-
"""
Created on Thu May 19 18:45:05 2016

@author: ibm-lenovo
"""

#matrix multiplication

import numpy as np
'''
# Create a new array from which we will select elements
a = np.array([[1,2,3], [4,5,6], [7,8,9], [10, 11, 12]])

print a 

print a[0][2]
'''

def matmult(A,B):
    n = (A.size)/2
    C = np.array([[0,0], [0,0]])
    
    if n == 1:
        C[0][0]=A[0][0]* B[0][0]
    else:
        C[0][0]=matmult(A[0][0],B[0][0]) + matmult(A[0][1],B[1][0])
        C[0][1]=matmult(A[0][0],B[0][1]) + matmult(A[0][1],B[1][1])
        C[1][0]=matmult(A[1][0],B[0][0]) + matmult(A[1][1],B[1][0])
        C[1][1]=matmult(A[1][0],B[0][1]) + matmult(A[1][1],B[1][1])
    print C    
    return C
















mat1 = np.array([[1,2], [3,4]])
mat2 = np.array([[5,6], [7,8]])

result = np.array([[0,0], [0,0]])

print mat1.size

for i in range(0,2):
    for j in range (0,2):
        for k in range (0,2):
            result[i][j] += mat1[i][k]*mat2[k][j]
print result

result = matmult(mat1,mat2)
        
        

