

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

    def listlen(self):

        if self.head == None:
            print 'no length for empty list'
            return

        temp = self.head

        l=1

        while temp.next != None:
            temp = temp.next
            l += 1
        return l

def sumlist (list1,list2):

    if list1.listlen() == list2.listlen():
        print 'same size'

        temp1 = list1.head
        temp2 = list2.head

        l1 =[]
        l2 =[]

        while temp1 != None:
            l1.append(temp1.num)
            l2.append(temp2.num)
            temp1 = temp1.next
            temp2= temp2.next

        newnum = str(int(reduce(lambda x, y: str(x) + str(y), l1)) + int(reduce(lambda x, y: str(x) + str(y),l2)))


        newlist = Linkedlist()

        for x in newnum:
            newlist.append(x)

        return newlist


    else :
        print 'diff size'



list1 = Linkedlist()
list1.append(1)
list1.append(2)


list2 = Linkedlist()
list2.append(1)
list2.append(4)


slist = sumlist(list1, list2)
slist.display()