
def lisubseq(arr):

    lc = [1 for x in range(len(arr))]

    print lc

    for i in range(len(arr)):
        for j in range(i):
            if arr[j]<arr[i]:
                lc[i] = max(lc[i],lc[j]+1)

    return lc
test1 = [3,4,-1,0,6,2,3]
print lisubseq(test1)

test2 = [1,2,3,4,5,-1,-2,-3]
print lisubseq(test2)