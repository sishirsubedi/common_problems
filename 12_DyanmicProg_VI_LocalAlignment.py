def global_align(str1,str2,score):
    len1 = len(str1) 
    len2 = len(str2)
    
    
    A = [[0 for x in range(len2+1)] for x in range(len1+1)]
    
    A[0][0]= 0 #score.match    
    
    for i in range(1,len1+1):
        A[i][0] = i * score.gap 
        
    
    for i in range(1,len2+1):
        A[0][i] = i * score.gap 

    best = 0
    optloc = (0,0) 
    for i in range(1,len1+1):# 0 to n
        for j in range(1,len2+1): # 0 to n
           # the local alignment recurrance rule:
           A[i][j] = max(
                     A[i][j-1] + score.gap,
                     A[i-1][j] + score.gap,
                     A[i-1][j-1] + (score.match if str1[i-1] == str2[j-1] else score.mismatch)
                     
           )
           # track the cell with the largest score
           if A[i][j] >= best:
              best = A[i][j]
              optloc = (i,j)

    #return best,optloc
    return A


def local_align(str1,str2,score):
    len1 = len(str1) 
    len2 = len(str2)
    
    
    A = [[0 for x in range(len2+1)] for x in range(len1+1)]
    
    best = 0
    optloc = (0,0) 
    for i in range(1,len1+1):# 0 to n
        for j in range(1,len2+1): # 0 to n
           # the local alignment recurrance rule:
           A[i][j] = max(
                     A[i][j-1] + score.gap,
                     A[i-1][j] + score.gap,
                     A[i-1][j-1] + (score.match if str1[i-1] == str2[j-1] else score.mismatch),
                     0
           )
           # track the cell with the largest score
           if A[i][j] >= best:
              best = A[i][j]
              optloc = (i,j)

    #return best,optloc
    return A

def local_backtrack(x,y,mat):
    solution = []
    j,k = len(x),len(y)
    while mat[j][k]>0:
        if x[j-1] == y[k-1]:
            solution.append(x[j-1])
            j -=1
            k -=1
        elif mat[j-1][k] >= mat[j][k-1]:
            j -=1
        else:
            k -=1
    return solution


def global_backtrack(x,y,mat):
    solution = []
    gap = '_'
    j,k = len(x),len(y)
    while mat[j][k]!= 0:
        if x[j-1] == y[k-1]:
            solution.append(x[j-1])
            j -=1
            k -=1
        elif mat[j-1][k] >= mat[j][k-1]:
            j -=1
            solution.append(gap)
        else:
            k -=1
            solution.append(gap)
    return solution
    
class ScoreParam:
    def __init__(self, gap, match, mismatch):
       self.gap = gap
       self.match = match
       self.mismatch = mismatch 
       
       
       
'''       
# Driver program to test above functions
string2 = ['a','g','c','g','t','a','g']
string1 =['c','t','c','g','t','c']
score = ScoreParam(-7,10,-5)

#test for global alignment
string2 = ['a','g','c']
string1 =['a','a','a','c']
score = ScoreParam(-2,1,-1)
'''

#test for global alignment
string2 = ['a','a','g','a']
string1 =['t','t','a','a','g']
score = ScoreParam(-7,10,-5)





mat = local_align(string2,string1,score)
mat2 = local_backtrack(string2,string1,mat)
for i in mat:
    print (i)
for i in mat2:
    print (i)

mat = global_align(string1,string2,score)
mat2 = global_backtrack(string1,string2,mat)
for i in mat:
   print (i)
for i in mat2:
   print (i)
   