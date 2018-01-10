
import sys


'''
THIS is topological sorting using simple DFS and black color and separate done_list. 
This is different done using color than other examples, where time and set is used.

'''


class Graph:
    def __init__(self):
        self.vertices = {}
        self.numVertices = 0
        self.time = 0
        self.done_list =[] ## graph will have its own topologically sorted list of its graph
        
    def addVertex(self,key):
        self.numVertices = self.numVertices + 1
        newVertex = Vertex(key)
        self.vertices[key] = newVertex
        return newVertex
    
    def getVertex(self,n):
        if n in self.vertices:
            return self.vertices[n]
        else:
            return None

    def __contains__(self,n):
        return n in self.vertices
    
    def addEdge(self,f,t,cost=0):
            if f not in self.vertices:
                 self.addVertex(f)
            if t not in self.vertices:
                 self.addVertex(t)
            self.vertices[f].addNeighbor(self.vertices[t],cost)
    
    def getVertices(self):
        return list(self.vertices.keys())
        
    def __iter__(self):
        return iter(self.vertices.values())


    def topo_sort(self):
        for aVertex in self:
            aVertex.setColor('white')
            aVertex.setPred(-1)
        for aVertex in self:
            if aVertex.getColor() == 'white':
                self.dfsvisit(aVertex)

    def dfsvisit(self,startVertex):
        startVertex.setColor('gray')
        self.time += 1
        startVertex.setDiscovery(self.time)
        for nextVertex in startVertex.getConnections():
            if nextVertex.getColor() == 'white':
                nextVertex.setPred(startVertex)
                self.dfsvisit(nextVertex)
        startVertex.setColor('black')
        self.done_list.append(startVertex.getId())
        self.time += 1
        startVertex.setFinish(self.time)

    def print_graph(self):
        for node in self.vertices:
            print node
            for nodechild in self.vertices[node].getConnections():
                print 'child--',nodechild.getId()
            print '--'
                
class Vertex:
    def __init__(self,num):
        self.id = num
        self.connectedTo = {}
        self.color = 'white'
        self.dist = sys.maxsize
        self.pred = None
        self.disc = 0
        self.fin = 0

    # def __lt__(self,o):
    #     return self.id < o.id
    
    def addNeighbor(self,nbr,weight=0):
        self.connectedTo[nbr] = weight
        
    def setColor(self,color):
        self.color = color
        
    def setDistance(self,d):
        self.dist = d

    def setPred(self,p):
        self.pred = p

    def setDiscovery(self,dtime):
        self.disc = dtime
        
    def setFinish(self,ftime):
        self.fin = ftime
        
    def getFinish(self):
        return self.fin
        
    def getDiscovery(self):
        return self.disc
        
    def getPred(self):
        return self.pred
        
    def getDistance(self):
        return self.dist
        
    def getColor(self):
        return self.color
    
    def getConnections(self):
        return self.connectedTo.keys()
        
    def getWeight(self,nbr):
        return self.connectedTo[nbr]
                
    def __str__(self):
        return str(self.id) + ":color " + self.color + ":disc " + str(self.disc) + ":fin " + str(self.fin) + ":dist " + str(self.dist) + ":pred \n\t[" + str(self.pred)+ "]\n"
    
    def getId(self):
        return self.id
        
        

        
g = Graph()

# g.addEdge('D','C',50)
# g.addEdge('D','B',50)
# g.addEdge('B','A',50)
# g.addEdge('A','F',50)
# g.addEdge('E','C',50)
# g.addEdge('E','F',50)
# g.addVertex('x')


g.addEdge('iw1','pant',1)
g.addEdge('iw1','iw2',1)
g.addEdge('pant','belt',1)
g.addEdge('pant','socks',1)
g.addEdge('iw2','shirt',1)
g.addEdge('shirt','pant',1)
g.addEdge('socks','shoes',1)
g.addEdge('watch','wallet',1)




g.print_graph()


print g.done_list

g.topo_sort()

print g.done_list




