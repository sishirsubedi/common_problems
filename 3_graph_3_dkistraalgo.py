
import sys


class Vertex:
    def __init__(self, node):
        self.id = node
        self.adjacent = {}
        # Set distance to infinity for all nodes
        self.distance = sys.maxint
        # Mark all nodes unvisited
        self.visited = False
        # Predecessor
        self.previous = None

    def add_neighbor(self, neighbor, weight=0):
        self.adjacent[neighbor] = weight

    def get_connections(self):
        return self.adjacent.keys()

    def get_id(self):
        return self.id

    def get_weight(self, neighbor):
        return self.adjacent[neighbor]

    def set_distance(self, dist):
        self.distance = dist

    def get_distance(self):
        return self.distance

    def set_previous(self, prev):
        self.previous = prev

    def get_previous(self):
        return self.previous

    def set_visited(self):
        self.visited = True

    def __str__(self):
        return str(self.id) + ' adjacent: ' + str([x.id for x in self.adjacent])


class Graph:
    def __init__(self):
        self.vert_dict = {}
        self.num_vertices = 0

    def __iter__(self):
        return iter(self.vert_dict.values())

    def add_vertex(self, node):
        self.num_vertices = self.num_vertices + 1
        new_vertex = Vertex(node)
        self.vert_dict[node] = new_vertex
        return new_vertex

    def get_vertex(self, n):
        if n in self.vert_dict:
            return self.vert_dict[n]
        else:
            return None

    def add_edge(self, frm, to, cost=0):
        if frm not in self.vert_dict:
            self.add_vertex(frm)
        if to not in self.vert_dict:
            self.add_vertex(to)
        self.vert_dict[frm].add_neighbor(self.vert_dict[to], cost)

    def get_vertices(self):
        return self.vert_dict.keys()

    def set_previous(self, current):
        self.previous = current

    def get_previous(self, current):
        return self.previous


def shortest(v, path):
    ''' make shortest path from v.previous'''
    if v.previous:
        path.append(v.previous.get_id())
        shortest(v.previous, path)
    return


import heapq
from pythonds.graphs import PriorityQueue

def dijkstra(aGraph, start):
    print "Dijkstra's shortest path for ", start.get_id()
    # Set the distance for the start node to zero
    start.set_distance(0)

    # Put tuple pair into the priority queue
    pq = [(v.get_distance(), v) for v in aGraph]
    heapq.heapify(pq)

    while len(pq):
        # Pops a vertex with the smallest distance
        uv = heapq.heappop(pq)
        current = uv[1]
        current.set_visited()

        # for next in v.adjacent:
        for next in current.adjacent:
            # if visited, skip
            # if next.visited:
            #     continue
            new_dist = current.get_distance() + current.get_weight(next)
            if new_dist < next.get_distance():
                next.set_distance(new_dist)
                next.set_previous(current)

def prims(aGraph, start):

    mse =[]
    print "prims from ", start.get_id()
    start.set_distance(0)
    pq = PriorityQueue()
    pq.buildHeap([(v.get_distance(), v) for v in aGraph])

    while not pq.isEmpty():
        currentvertex = pq.delMin()
        #print currentvertex

        mse.append([currentvertex.get_id(),currentvertex.get_distance()])

        currentvertex.set_visited()
        for childvertex in currentvertex.adjacent:
            #print childvertex.get_id()
            newcost = currentvertex.get_weight(childvertex)
            if childvertex in pq and newcost< childvertex.get_distance():
                childvertex.set_distance(newcost)
                childvertex.set_previous(currentvertex)
                pq.decreaseKey(childvertex, newcost)

    for i in mse:
        print i

g = Graph()


g.add_edge('a', 'b', 2)
g.add_edge('a', 'c', 3)
g.add_edge('c', 'f', 5)
g.add_edge('f', 'g', 1)
g.add_edge('b', 'e', 4)
g.add_edge('b', 'd', 1)
g.add_edge('b', 'c', 1)
g.add_edge('d', 'e', 1)


print 'Graph data:'
for v in g:
    for w in v.get_connections():
        vid = v.get_id()
        wid = w.get_id()
        print '( %s , %s, %3d)' % (vid, wid, v.get_weight(w))

prims(g, g.get_vertex('a'))


### floyd warshall algorithm for all vertex shortest path

from pythonds.graphs import Graph, Vertex


def floyd_Warshall(aGraph):
    distmat = [[100 for x in range(0,aGraph.numVertices+1)] for y in range(0,aGraph.numVertices+1)]

    for row in distmat:
        print row

    for num in range(0,aGraph.numVertices+1):
        distmat[num][num] = 0

    for v1 in aGraph.getVertices():
        currentvertex = aGraph.getVertex(v1)
        for childvertex in currentvertex.getConnections():
            print currentvertex.getWeight(childvertex)
            print int(v1), int(childvertex.getId())
            distmat[int(v1)][int(childvertex.getId())] = currentvertex.getWeight(childvertex)

    numofvertices = aGraph.numVertices+1

    for k in range(1,numofvertices):
        for i in range(1, numofvertices):
            for j in range(1, numofvertices):
                if distmat[i][j] > distmat[i][k]+ distmat[k][j]:
                    distmat[i][j] = distmat[i][k] + distmat[k][j]

    print 'floydwarshall result is : '
    for row in distmat:
        print row



newGraph = Graph()
newGraph.addEdge('1','3',-2)
newGraph.addEdge('3','4',2)
newGraph.addEdge('2','1',4)
newGraph.addEdge('2','3',3)
newGraph.addEdge('4','2',-1)
floyd_Warshall(newGraph)