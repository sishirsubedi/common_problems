
def  patindex(pattern):

    mat = [0 for x in range(len(pattern))]

    i = 1
    j = 0

    while i<len(pattern):

        if pattern[i]==pattern[j]:
            j += 1
            mat[i] = j
            i += 1

        else:
            if j != 0:
                j = mat[j-1] # tricky here to jump j so that size of suffix is same as prefix
            else:
                mat[i] = 0
                i += 1

    return mat


def kmp(word,pattern):

    pindex = patindex(pattern)

    wl = len(word)
    pl = len(pattern)

    i = 0 # for word
    j = 0 # for pattern

    while i<wl:

        if word[i] == pattern[j]:
            i += 1
            j += 1

        if j == pl:
            print ' pattern occurs at ', i-j
            j = pindex[j-1]

        elif i<wl and pattern[j] != word[i]:
            if j !=0 :
                j = pindex[j-1]
            else:
                i += 1


word ="ABABDABACDABABCABAB"
pattern = "ABABCABAB"


kmp(word,pattern)