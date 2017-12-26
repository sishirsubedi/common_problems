import numpy as np

def subsetsum(arr,n):

    arr= np.sort(arr)

    mat = [[0 for x in range(n+1)] for y in range(len(arr))]

    for i in range(len(arr)):
        for j in range(n+1):

            if j==0: mat[i][j]=1

            elif i ==0 and arr[i]!= j:
                mat[i][j] =0

            elif  i == 0 and arr[i] == j:
                mat[i][j] = 1

            elif j >= arr[i]:
                mat[i][j] = mat[i-1][j-arr[i]]

            else:
                mat[i][j] = mat[i-1][j]

    return mat


# Driver program to test above functions

arr = [5,2,7,3]
n= 13

mat = subsetsum(arr,n)

for i in mat:
    print i


