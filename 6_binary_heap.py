
class BinHeap:
    def _init (self):
        self.currentsize =0
        self.heapList =[0]
        
    def Buildheap(self, alist):
        self.currentsize = len(alist)
        self.heapList =[0] + alist[:]
        i = len(alist)//2
        while (i>0):
            self.minimize(i)
            #self.maxmize(i)
            i = i -1
    
    def minimize(self, i):
        left = (i *2)+1
        right = i*2
        lowest = i
        if left<= self.currentsize and self.heapList[left] < self.heapList[lowest]:
            lowest = left
        if right<= self.currentsize and self.heapList[right] < self.heapList[lowest]:
            lowest = right
        if lowest != i:
            self.heapList[i], self.heapList[lowest] = self.heapList[lowest], self.heapList[i] 
            self.minimize(lowest)
    
    
    def maxmize(self, i):
        left = (i *2)+1
        right = i*2
        
        if left<= self.currentsize and self.heapList[left] > self.heapList[i]:
            largest = left
        else:
            largest = i
        if right<= self.currentsize and self.heapList[right] > self.heapList[largest]:
            largest = right
        if largest != i:
            self.heapList[i], self.heapList[largest] = self.heapList[largest], self.heapList[i] 
            self.maxmize(largest)    
    
    
    
    def getHeap(self):
        return self.heapList
        
    def deletetop(self):
        val = self.heapList[1]
        self.heapList[1]= self.heapList[self.currentsize]
        self.currentsize = self.currentsize-1
        self.heapList.pop()
        self.minimize(1)
        #self.maxmize(1)
        return val

alist = [33,17,27,14,28,9,5,11,19,21]

newheap = BinHeap()
newheap.Buildheap(alist)

newheap.deletetop()

print newheap.getHeap()
