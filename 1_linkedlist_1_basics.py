

#linked list

class Node:
    def __init__(self,number):
        self.num = number
        self.next = None
        self.prev = None

class Linkedlist:
    def __init__(self):
        self.head = None
    
    def append (self, num):
        node = Node(num)
        if self.head == None:
            self.head = node
        else:
            currentnode = self.head
            while currentnode.next != None:
                currentnode = currentnode.next
            currentnode.next = node
            node.prev = currentnode
            
    def display (self):
        temp = self.head
        while temp:
            print "----"
            print "current node", temp.num
            if temp.prev != None:
                print "prev node", temp.prev.num
            if temp.next != None:
                print "next node", temp.next.num
            print "----"
            temp = temp.next


    def insertnode (self, number):
        newnode = Node(number)
        
        if(self.head ==None):
            self.head = newnode
        else:
            temp = self.head
            previousnode = None
            while temp != None and temp.num < newnode.num:
                previousnode = temp                
                temp = temp.next
            if previousnode == None:
                self.head =newnode
                newnode.next = temp
                temp.prev = newnode
            else:
                previousnode.next = newnode
                newnode.prev =previousnode
                newnode.next = temp
                temp.prev = newnode
                
    def deletenode (self, number):
        temp = None
        previousnode = None
        if(self.head == None):
            print 'list is empty'
            return
        if self.head.num == number:
            temp = self.head.next
            self.head = temp
            self.head.prev = None
        else:
            temp = self.head
            while temp != None and temp.num != number:
                previousnode = temp
                temp = temp.next
            if temp.num == number:
                previousnode.next = temp.next
                temp.next.prev = previousnode
                del temp
                
    
    
mylist = Linkedlist()
mylist.append(3)

mylist.append(5)
#mylist.append(30)

mylist.insertnode(4)
#

mylist.display()

mylist.deletenode(4)
         
mylist.display()
    