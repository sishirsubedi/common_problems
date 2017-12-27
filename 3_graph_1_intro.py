# -*- coding: utf-8 -*-
"""
Created on Mon May 23 14:32:20 2016

@author: ibm-lenovo
"""
''' example of simple dictionary      
mydict = {"red": 1, "yellow":2, "green" :3}

print mydict["red"] # prints 1

'''

class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0,item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)
        

class Vertex:
    def __init__(self, key):
        self.id = key
        self.connectedTo = {}
        self.color = 'white'
      
    
    def addNeighbor (self, nbr, weight =0):
        self.connectedTo[nbr]=weight

    def getConnections(self):
        return self.connectedTo.keys()
    
    def getId(self):
        return self.id
    
    def getweight(self, nbr):
        return self.connectedTo[nbr]
    
    def __str__(self):
        return str(self.id) + ' connectedTo: ' + str([x.id for x in self.connectedTo])
        
    def setColor(self,col):
        self.color = col
    
    def getColor(self):
        return self.color

class Graph:
    
    def __init__(self):
        self.vertList = {}
        self.numVertices = 0
    
    def addVertices(self, key):
        self.numVertices = self.numVertices + 1
        newvertex = Vertex(key)        
        self.vertList[key]= newvertex
        return newvertex
    
    def getVertex(self, n):
        if n in self.vertList:
            return self.vertList[n]
        else:
            return None
    
    def __contains__ (self, n):
        return n in self.vertList
    
    
    def addEdge(self, head, tail, cost = 0):
        if head not in self.vertList:
            self.addVertices(head)
        if tail not in self.vertList:
            self.addVertices(tail)
        self.vertList[head].addNeighbor(self.vertList[tail], cost)
        
    def getVertices(self):
        return self.vertList.keys()

    def __iter__(self):
        return iter(self.vertList.values())
        
    def breadthfirst (g, startvertex):
        currentvertex = g.getVertex(startvertex)
        print currentvertex
        currentq = Queue()
        currentq.enqueue(currentvertex)
        while currentq.size()>0:
            currentvertex = currentq.dequeue()
            neighborlist = currentvertex.getConnections()
            for nbr in neighborlist:
                print nbr
                if nbr.getColor() == 'white':
                    nbr.setColor ='gray'
                    currentq.enqueue(nbr)

    def depthfirst (self, startvertex, currentstack):
        currentvertex = startvertex
        print currentvertex
        currentstack.append(currentvertex)
        neighborlist = startvertex.getConnections()
        done = False
        if len(neighborlist) >0:
            for nbr in neighborlist:
                done = self.depthfirst(nbr,currentstack)
        else:
            currentstack.pop()
            done = True
            
            
        return done



                     
'''
for i in range(6):
    g.addVertices(i)

vertex = g.getVertices() 
print vertex  



g.addEdge(0,1,500) 
g.addEdge(0,5,200)
g.addEdge(1,2,400)
g.addEdge(2,3,900)
g.addEdge(3,4,700)
g.addEdge(3,5,300)
g.addEdge(4,0,100)
g.addEdge(5,4,800)
g.addEdge(5,2,100)
'''


g = Graph()
g.addEdge('A','B',4)
g.addEdge('A','H',8)
g.addEdge('B','C',8)
g.addEdge('B','H',11)
g.addEdge('C','I',2)
g.addEdge('C','F',4)
g.addEdge('C','D',7)
g.addEdge('D','E',9)
g.addEdge('D','F',24)
g.addEdge('E','F',10)
g.addEdge('F','G',2)
g.addEdge('G','I',6)
g.addEdge('G','H',1)





'''
for vertices in g:
   for neighbors in vertices.getConnections():
       print ("( vertix is  %s, neighbor is %s, weight is %s)" % 
       (vertices.getId(), neighbors.getId(), vertices.getweight(neighbors) ))
'''
print 'breadth first search is :'
g.breadthfirst('A')


print 'depth first search is :'
stck = []
startv = g.getVertex('A')
g.depthfirst(startv,stck)
