

def selection_sort(alist): ## o(n2)
    for i in range(len(alist)-1):
        cmin = i
        for j in range(i+1,len(alist)):
            if alist[cmin]>alist[j]:
                cmin = j
        temp = alist[cmin]
        alist[cmin] = alist[i]
        alist[i] = temp
        print alist


def bubble_sort(alist): ## o(n2)
    moved = True
    while moved==True:
        moved = False
        for i in range(len(alist)-1):
            if alist[i]>alist[i+1]:
                temp = alist[i]
                alist[i] = alist[i+1]
                alist[i+1] = temp
                moved = True
        if moved == False:
            break

def insertion_sort(alist):  ## o(n2)
    for i in range(1, len(alist)):
        current = i
        value = alist[i]
        while( current>0 and alist[current-1]>value):
            alist[current] = alist[current-1]
            current = current-1
        alist[current] = value
        #print alist

def merge(alist,left,mid,right):

    nl = mid - left + 1
    nr = right - mid
    newl = [0] * nl
    newr = [0] * nr
    for i in range(0,nl):newl[i]=alist[left+i]
    for j in range(0,nr): newr[j] = alist[mid+1+j]
    i,j=0,0
    k=left

    while(i<nl and j<nr):
        if newl[i]<=newr[j]:
            alist[k]= newl[i]
            k +=1
            i +=1
        elif newr[j]<newl[i]:
            alist[k]=newr[j]
            k += 1
            j += 1
    while i<nl:
        alist[k] = newl[i]
        k += 1
        i += 1

    while j<nr:
        alist[k] = newr[j]
        k += 1
        j += 1

    #print alist


def merge_sort(alist,left, right):
    if left<right:
        mid = (left+(right-1))/2
        merge_sort(alist,left,mid)
        merge_sort(alist, mid+1,right)
        merge(alist,left,mid, right)


def quick_sort(alist):
   q_sorter(alist,0,len(alist)-1)

def q_sorter(alist,first,last):
   if first<last:
       splitpoint = qsort_partition(alist,first,last)
       q_sorter(alist,first,splitpoint-1)
       q_sorter(alist,splitpoint+1,last)


def qsort_partition(alist,first,last):
    pivotvalue = alist[last]
    i = first -1
    for j in range(first,last):
        if alist[j] <= pivotvalue:
            i += 1
            alist[i],alist[j]= alist[j],alist[i]
    alist[i+1],alist[last]= alist[last], alist[i+1]
    return (i+1)


alist = [54,26,93,17,77,31,44,55,20]
#bubble_sort(alist)
#selection_sort(alist)
#insertion_sort(alist)
#merge_sort(alist,0,len(alist)-1)
quick_sort(alist)
print '--'
print alist