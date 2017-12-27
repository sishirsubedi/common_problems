

class BSTNode:
    def __init__(self,parent, k):
        self.key = k
        self.parent = parent
        self.left = None
        self.right = None

    def insert(self, node):
        if node.key < self.key :
            if self.left is None:
                node.parent = self
                self.left= node
            else:
               self.left.insert(node)
        else:
            if self.right is None:
                node.parent = self
                self.right = node
            else:
                self.right.insert(node)

    def delete(self, k):
        if k < self.key:
            self.left.delete(k)
        elif k > self.key:
            self.right.delete(k)
        else:
            self.makedeletion()

    def makedeletion(self):

        tempnode = None

        if self is None:
            return

        # only head or node is a leaf
        elif self.right is None and self.left is None:
          #  if self.parent.left == self:
              #  self.parent.left =None
                del self
           # elif self.parent.right == self:
             #   self.parent.right = None
            #    del self

        elif self.right  is None:
            tempnode = self
           # self.parent.right=self.left
            self = self.left
            del tempnode
        elif self.left is None:
            tempnode = self
            self = self.right
            del tempnode
        else:
            tempnode = self.right
            while tempnode.left:
                tempnode = tempnode.left
            tempnode.left = self.left
            tempnode = self  ## changing self to temp so that it can be deleted
            self = self.right
            del tempnode


    def displaynode (self, node):
        if (node):
            #print node.key
            node.displaynode (node.left)
            print node.key
            node.displaynode (node.right)
            #print node.key

class Binarytree:
    def __init__(self):
        self.root = None

    def insertNode(self,k):
        node = BSTNode(None,k)
        if self.root is None:
            self.root = node
        else:
            self.root.insert(node)

    def display(self):
        self.root.displaynode(self.root)

    def deleteNode(self,k):
        self.root.delete(k)


mytree = Binarytree()
mytree.insertNode(5)
mytree.insertNode(8)
mytree.insertNode(3)
mytree.insertNode(12)
mytree.insertNode(7)

mytree.deleteNode(5)


mytree.display()
