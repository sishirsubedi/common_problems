
import Queue


class node:
    def __init__(self,_id):
        self.id = _id
        self.neighbors ={}

    def add_neighbor(self,nnode,weight=1):
        self.neighbors[nnode]= weight

    def get_id(self):
        return self.id

    def get_neighbors(self):
        return self.neighbors.keys()

    def get_nweight(self,nnode):
        return self.neighbors[nnode]

class graph:

    def __init__(self):
        self.nodes ={}
        self.n_total = 0

    def add_node(self, _id):
        newnode = node(_id)
        self.nodes[_id] = newnode
        self.n_total += 1

    def add_edge(self,from_node, to_node,weight=1):

        if from_node not in self.nodes:
            self.add_node(from_node)

        if to_node not in self.nodes:
            self.add_node(to_node)

        self.nodes[from_node].add_neighbor(self.nodes[to_node],weight)

    def get_nodes(self):
        return self.nodes.keys()

    def display_graph(self):
        for node in self.nodes:
            print self.nodes[node].get_id()
            for nodes in self.nodes[node].get_neighbors():
                print '-->' , nodes.get_id()

    def bfs(self,root):
        q = Queue.Queue() # FIFO
        q.put(root)
        while not q.empty():
            currentnode = self.nodes[q.get()]
            print currentnode.get_id()
            for neighbors in currentnode.get_neighbors():
                #print '--',neighbors.get_id()
                q.put(neighbors.get_id())

    def dfs(self,root):
        q = Queue.LifoQueue()
        q.put(root)
        while not q.empty():
            currentnode = self.nodes[q.get()]
            print currentnode.get_id()
            for neighbors in currentnode.get_neighbors():
                #print '--',neighbors.get_id()
                q.put(neighbors.get_id())

    def prim(self):
        q= Queue.PriorityQueue()

        for node in self.nodes:
            for nbr in self.nodes[node].get_neighbors():
                print node, nbr.get_id(), self.nodes[node].get_nweight(nbr)
                q.put(self.nodes[node].get_nweight(nbr),str(node + nbr.get_id()))

        while not q.empty():
            print q.get()





## THIS is for dfs and bfs

# newgraph = graph()
# newgraph.add_edge('A','B')
# newgraph.add_edge('A','C')
# newgraph.add_edge('B','D')
# newgraph.add_edge('B','E')
# newgraph.add_edge('C','F')
# newgraph.add_edge('C','G')
# newgraph.add_edge('D','H')
# newgraph.add_edge('D','I')
#
# print 'bfs'
# newgraph.bfs('A')
#
# print 'dfs'
# newgraph.dfs('A')


## this is for prim's algorithm


newgraph = graph()
newgraph.add_edge('A','B',1)
newgraph.add_edge('A','D',4)
newgraph.add_edge('A','C',3)
newgraph.add_edge('B','C',2)
newgraph.add_edge('D','C',5)
#newgraph.display_graph()

newgraph.prim()