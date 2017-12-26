

## this is for in order(not adjacent) longest common sub sequence

def minedit(word1, word2):
    len1 = len(word1)
    len2 = len(word2)
    mat = [[0 for x in range(len2 + 1)] for y in range(len1 + 1)]

    print mat
    for i in range(len1):
        for j in range(len2):
            print i,j
            if i ==0: mat[i][j]=j   # add each
            elif j==0: mat[i][j]=i  # delete each

            elif word1[i-1]==word2[j-1]:
                mat[i][j] = mat[i-1][j-1]
            else:
                mat[i][j]= 1 + min(
                    mat[i-1][j-1],
                    mat[i][j-1],
                    mat[i-1][j]
                )


    return mat


# Driver program to test above functions

#
# X = "abcdaf"
# Y = "acbcf"

# X = "AGGTAB"
# Y = "GXTXAYB"

X = "sunday"
Y = "saturday"

mat = minedit(X, Y)

for i in mat:
    print i

