# -*- coding: utf-8 -*-
"""
Created on Fri May 20 22:25:50 2016

@author: ibm-lenovo
"""

# Binary Search Tree in Python

class Node:
    def __init__(self, val):
        self.value = val
        self.leftChild = None
        self.rightChild = None
        self.parent = None
        self.balancefactor=0
  
    def insert(self, data): ### here insert is used to just add value without caring for balancing tree
        if self.value == data:
            return False
        elif self.value > data:
            if self.leftChild:
                return self.leftChild.insert(data)
            else:
                newnode = Node(data)
                self.leftChild = newnode
                newnode.parent = self
                return True
        else:
            if self.rightChild:
                return self.rightChild.insert(data)
            else:
                newnode = Node(data)
                self.rightChild = newnode
                newnode.parent = self
                return True

    def find(self, data):
        if(self.value == data):
            return True
        elif self.value > data:
            if self.leftChild:
                return self.leftChild.find(data)
            else:
                return False
        else:
            if self.rightChild:
                return self.rightChild.find(data)
            else:
                return False

    def preorder(self):
        if self:
            print (str(self.value))
            if self.leftChild:
                self.leftChild.preorder()
            if self.rightChild:
                self.rightChild.preorder()

    def postorder(self):
        if self:
            if self.leftChild:
                self.leftChild.postorder()
            if self.rightChild:
                self.rightChild.postorder()
            print (str(self.value))

    def inorder(self):
        if self:
            if self.leftChild:
                self.leftChild.inorder()
            print (str(self.value)) , self.balancefactor
            if self.rightChild:
                self.rightChild.inorder()

class Tree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root:
            return self.root.insert(data)
        else:
            self.root = Node(data)
            return True

    def find(self, data):
        if self.root:
            return self.root.find(data)
        else:
            return False

    def getRoot(self):
        return self.root.value

    def remove(self, data):
        # empty tree
        if self.root is None:
            return False

        # data is in root node
        elif self.root.value == data:
            # root does not have any children
            if self.root.leftChild is None and self.root.rightChild is None:
                self.root = None
            # no rightchild
            elif self.root.leftChild and self.root.rightChild is None:
                self.root = self.root.leftChild
            # no leftchild
            elif self.root.leftChild is None and self.root.rightChild:
                self.root = self.root.rightChild
            # has both children - go to right and then leftmost, connect to left and change right to root
            elif self.root.leftChild and self.root.rightChild:
                tempnode = self.root.rightChild
                while tempnode.leftChild:
                    tempnode = tempnode.leftChild

                tempnode.leftChild = self.root.leftChild
                self.root.leftChild.parent = tempnode
                tempnode = self.root
                self.root = self.root.rightChild
                tempnode = None

            return True

        ## now if delete node is not root then find which node to delete in the tree

        parent = None
        currentnode = self.root


        while currentnode and currentnode.value != data:
            parent = currentnode
            if data < currentnode.value:
                currentnode = currentnode.leftChild
            elif data > currentnode.value:
                currentnode = currentnode.rightChild

        # case 1: data not found
        if currentnode is None or currentnode.value != data:
            print ('Data not in the tree')
            return False

        # case 2: remove-node has no children
        elif currentnode.leftChild is None and currentnode.rightChild is None:
            if data < parent.value:
                parent.leftChild = None
                currentnode.parent = None
            else:
                parent.rightChild = None
                currentnode.parent = None
            return True

        # case 3: remove-node has left child only
        elif currentnode.leftChild and currentnode.rightChild is None:
            if data < parent.value:
                parent.leftChild = currentnode.leftChild
                currentnode.leftChild.parent = parent
                currentnode.parent = None
                currentnode.leftChild = None

            else:
                parent.rightChild = currentnode.leftChild
                currentnode.leftChild.parent = parent
                currentnode.parent = None
                currentnode.leftChild = None
            return True

        # case 4: remove-node has right child only
        elif currentnode.leftChild is None and currentnode.rightChild:
            if data < parent.value:
                parent.leftChild = currentnode.rightChild
                currentnode.rightChild.parent = parent
                currentnode.parent = None
                currentnode.rightChild = None
            else:
                parent.rightChild = currentnode.rightChild
                currentnode.rightChild.parent = parent
                currentnode.parent = None
                currentnode.rightChild = None
            return True

        # case 5: remove-node has both left and right children
        else:# we have parent and node , here node is the one that needs to be deleted


            # just go to right of the node and get leftmost node
            tempnodeparent = currentnode.rightChild
            tempnode = currentnode.rightChild
            while tempnode.leftChild:
                tempnodeparent= tempnode
                tempnode = tempnode.leftChild

            tempnode.leftChild = currentnode.leftChild
            currentnode.leftChild.parent = tempnode

            if parent.value > currentnode.value: # deleting node is on left of parent
                if tempnode.rightChild:

                    tempnodeparent.leftChild = tempnode.rightChild
                    tempnode.rightChild.parent = tempnodeparent

                    tempnode.rightChild = currentnode.rightChild
                    currentnode.rightChild.parent = tempnode

                    parent.leftChild = tempnode
                    tempnode.parent = parent

                    currentnode = None

                else:
                    tempnode.rightChild = currentnode.rightChild
                    currentnode.rightChild.parent = tempnode

                    parent.leftChild = tempnode
                    tempnode.parent = parent

                    currentnode = None
            else:
                if tempnode.rightChild:

                    tempnodeparent.leftChild = tempnode.rightChild
                    tempnode.rightChild.parent = tempnodeparent

                    tempnode.rightChild = currentnode.rightChild
                    currentnode.rightChild.parent = tempnode

                    parent.rightChild = tempnode
                    tempnode.parent = parent

                    node = None
                    
                else:
                    tempnode.rightChild = currentnode.rightChild
                    currentnode.rightChild.parent = tempnode

                    parent.rightChild = tempnode
                    tempnode.parent = parent

                    node = None

    def preorder(self):
        if self.root is not None:
            print("PreOrder")
            self.root.preorder()
        
    def postorder(self):
        if self.root is not None:
            print("PostOrder")
            self.root.postorder()

    def inorder(self):
        if self.root is not None:
            print("InOrder")
            self.root.inorder()
            
    def put(self,value): ## put is used to insert data in tree with maintaining balance
        if self.root:
            self._put(value,self.root)
        else:
            self.root = Node(value)
            
    def _put(self, value, currentnode):
        if value<currentnode.value:
            if currentnode.leftChild :
                self._put(value,currentnode.leftChild)
            else:
                currentnode.leftChild = Node(value)
                currentnode.leftChild.parent = currentnode
                self.updatebalance(currentnode.leftChild)
        else:
            if currentnode.rightChild:
                self._put(value, currentnode.rightChild)
            else:
                currentnode.rightChild = Node(value)
                currentnode.rightChild.parent = currentnode
                self.updatebalance(currentnode.rightChild)
                
    def updatebalance(self, node):
        if node.balancefactor > 1 or node.balancefactor < -1:
            self.rebalancetree (node)
            return
        if node.parent != None:
            if node.parent.leftChild == node:
                node.parent.balancefactor += 1
            elif node.parent.rightChild == node:
                node.parent.balancefactor -= 1
                
            if node.parent.balancefactor != 0:
                self.updatebalance(node.parent)
        
    
    def rotateleft(self, node):
        newnode = node.rightChild
        node.rightChild = newnode.leftChild
        if newnode.leftChild != None:
            newnode.leftChild.parent = node
        newnode.parent = node.parent
        
        if node == self.root:
            self.root = newnode
        else:
            if node.parent.leftChild == node:
                node.parent.leftChild = newnode
            else:
                node.parent.rightChild = newnode
        newnode.leftChild = node
        node.parent = newnode
        node.balancefactor = node.balancefactor +1 - min(newnode.balancefactor,0)
        newnode.balancefactor = newnode.balancefactor +1 + max (node.balancefactor,0)
        
        
        
    def rotateright(self, node):
        newnode = node.leftChild
        node.leftChild = newnode.rightChild
        if newnode.rightChild != None:
            newnode.rightChild.parent = node
        newnode.parent = node.parent
        
        if node == self.root:
            self.root = newnode
        else:
            if node.parent.leftChild == node:
                node.parent.leftChild = newnode
            else:
                node.parent.rightChild = newnode
        newnode.rightChild = node
        node.parent = newnode
        node.balancefactor = node.balancefactor -1 - max(newnode.balancefactor,0)
        newnode.balancefactor = newnode.balancefactor -1 + min (node.balancefactor,0)
    
    def rebalancetree(self,node):
       if node.balancefactor < 0:

         if node.rightChild.balancefactor > 0:
            self.rotateright(node.rightChild)
            self.rotateleft(node)
         else:
            self.rotateleft(node)

       elif node.balancefactor > 0:

         if node.leftChild.balancefactor < 0:
            self.rotateleft(node.leftChild)
            self.rotateright(node)
         else:
            self.rotateright(node)
        
    
        

bst = Tree()


bst.insert(5)
bst.insert(8)
bst.insert(3)
# bst.insert(12)
# bst.insert(7)
# bst.insert(9)
# bst.insert(15)
# bst.insert(1)
# bst.insert(20)
# bst.insert(8.5)
# bst.insert(11)
# bst.remove(9)

# bst.insert(17)
# bst.insert(5)
# bst.insert(35)
# bst.insert(2)
# bst.insert(11)
# bst.insert(29)
# bst.insert(38)
# bst.insert(9)
# bst.insert(16)
# bst.insert(7)
# bst.insert(8)
# bst.insert(37)
# bst.insert(36)
# bst.insert(36.5)
# bst.insert(40)
#
# bst.remove(17)



# bst.put(17)
# bst.put(5)
# bst.put(35)
# bst.put(2)
# bst.put(11)
#
# bst.put(9)
# bst.put(16)


#bst.remove(35)

bst.inorder()
print 'root is : ', bst.getRoot()

print bst.find(5)





# class BSTNode:
#     def __init__(self,parent, k):
#         self.key = k
#         self.parent = parent
#         self.left = None
#         self.right = None

#     def insert(self, node):
#         if node.key < self.key :
#             if self.left is None:
#                 node.parent = self
#                 self.left= node
#             else:
#                self.left.insert(node)
#         else:
#             if self.right is None:
#                 node.parent = self
#                 self.right = node
#             else:
#                 self.right.insert(node)

#     def delete(self, k):
#         if k < self.key:
#             self.left.delete(k)
#         elif k > self.key:
#             self.right.delete(k)
#         else:
#             self.makedeletion()

#     def makedeletion(self):

#         tempnode = None

#         if self is None:
#             return

#         # only head or node is a leaf
#         elif self.right is None and self.left is None:
#           #  if self.parent.left == self:
#               #  self.parent.left =None
#                 del self
#            # elif self.parent.right == self:
#              #   self.parent.right = None
#             #    del self

#         elif self.right  is None:
#             tempnode = self
#            # self.parent.right=self.left
#             self = self.left
#             del tempnode
#         elif self.left is None:
#             tempnode = self
#             self = self.right
#             del tempnode
#         else:
#             tempnode = self.right
#             while tempnode.left:
#                 tempnode = tempnode.left
#             tempnode.left = self.left
#             tempnode = self  ## changing self to temp so that it can be deleted
#             self = self.right
#             del tempnode


#     def displaynode (self, node):
#         if (node):
#             #print node.key
#             node.displaynode (node.left)
#             print node.key
#             node.displaynode (node.right)
#             #print node.key

# class Binarytree:
#     def __init__(self):
#         self.root = None

#     def insertNode(self,k):
#         node = BSTNode(None,k)
#         if self.root is None:
#             self.root = node
#         else:
#             self.root.insert(node)

#     def display(self):
#         self.root.displaynode(self.root)

#     def deleteNode(self,k):
#         self.root.delete(k)


# mytree = Binarytree()
# mytree.insertNode(5)
# mytree.insertNode(8)
# mytree.insertNode(3)
# mytree.insertNode(12)
# mytree.insertNode(7)

# mytree.deleteNode(5)


# mytree.display()
