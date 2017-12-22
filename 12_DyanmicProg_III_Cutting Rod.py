
# A Dynamic Programming solution for Rod cutting problem
# Returns the best obtainable price for a rod of length n and
# price[] as prices of different pieces


def cutRod2(price,length, n):
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

### better version
def cutrod(price,rlen):
    mat = [[0 for x in range(rlen+1)] for y in range(rlen+1)]
    for p in range(1,rlen+1):
        for rl in range(1,rlen+1):
            if rl>=p:
                mat[p][rl]= max(price[p-1] + mat[p][rl-p],mat[p-1][rl])
            elif rl<p:
                mat[p][rl] = mat[p-1][rl]
    return mat
 
# Driver program to test above functions
price = [1, 5, 8]
length =[1, 2, 3]
size = len(length)

plist1 = cutRod2(price,length,size)
for i in plist1:
    print i

plist2 = cutrod(price,size)
for i in plist2:
    print i