

## this is for in order(not adjacent) longest common sub sequence

def maxCommonSubstring2(word1, word2):
    len1 = len(word1)
    len2 = len(word2)
    mat = [[0 for x in range(len1 + 1)] for y in range(len2 + 1)]


    for i in range(len1):
        for j in range(len2):
            if word1[i-1]==word2[j-1]:
                mat[i][j] = mat[i-1][j-1] + 1
            else:
                mat[i][j] = max(mat[i][j-1],mat[i-1][j])

    return mat


# Driver program to test above functions


X = "abcdaf"
Y = "acbcf"

# X = "AGGTAB"
# Y = "GXTXAYB"

mat = maxCommonSubstring2(X, Y)

for i in mat:
    print i