class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None
        
        
class DoublyLL:
    def __init__(self):
        self.head = None
        self.tail = None
    def __iter__(self):
        node = self.head
        while node:
            yield node
            if node.next == self.head:
                break
            node = node.next
    def count(self):
        count = 0
        node = self.head
        while node:
            if self.tail.next == self.head:
                break
            node = node.next
            count += 1
        return count + 1
    def createCDLL(self,value):
        newNode = Node(value)
        self.head = newNode
        self.tail = newNode
        newNode.prev = newNode
        newNode.next = newNode
    def insertCDLL(self,value, location):
        newNode=Node(value)
        if location == 0:
            if self.head == None:
                self.head = newNode
                self.tail = newNode
                newNode.prev = newNode
                newNode.next = newNode
            else:    
                newNode.next = self.head
                newNode.prev = self.head
                self.head.prev = newNode
                self.tail.next = newNode
                self.head = newNode
        elif location == 1:
             if self.head == None:
                self.head = newNode
                self.tail = newNode
                newNode.prev = newNode
                newNode.next = newNod
             else:

                newNode.prev = self.tail
                newNode.next = self.tail.next
                self.tail.next = newNode
                self.tail = newNode
                self.head.prev = newNode
            
        else:
            tempNode = self.head
            index = 0
            while index < location - 1:
                
                tempNode = tempNode.next
                index += 1
            nextNode = tempNode.next
            nextNode.prev = newNode
            newNode.prev = tempNode
            tempNode.next = newNode
            newNode.next = nextNode
    def traverseCDLL(self):

        if self.head == None:
            print('no linked list exist')
        else:
            tempNode = self.head
            while tempNode:
                print(tempNode.value)
                tempNode = tempNode.next
                if tempNode == self.tail.next:
                    break
                #tempNode = tempNode.next
    def traversereverseCDLL(self):
        if self.head == None:
            print('no linked list exist')
        else:
            tempNode = self.tail
            while tempNode:
                print(tempNode.value)
                tempNode = tempNode.prev
                if tempNode == self.tail:
                    break
    def deleteCDLL(self, location):
        if self.head == None:
            print('no Linked List exist')
        else:
            if location == 0:
                if self.head.next == self.head:
                    self.head.next = None
                    self.tail.prev = None
                    self.head = None
                    self.tail = None
                else:
                    nextNode=self.head.next
                    nextNode.prev = self.tail
                    self.tail.next = nextNode
                    self.head = nextNode

            elif location == 1:
                if self.head.next == self.head:
                    self.head.next = None
                    self.tail.prev = None
                    self.head = None
                    self.tail = None
                else:
                    previousNode = self.tail.prev
                    previousNode.next = self.head
                    self.tail = previousNode
                    self.head.prev = previousNode
            else:
                tempNode = self.head
                index = 0
                while index < location - 1:
                    tempNode = tempNode.next
                    index += 1
                nextNode = tempNode.next
                nextNode.next.prev = tempNode
                tempNode.next = nextNode.next
                nextNode.prev = None
    def deleteentireCDLL(self):
        self.tail.next = None
        
        tempNode = self.head
        while tempNode:
            tempNode.prev = None
            tempNode = tempNode.next
        self.head = None
        self.tail = None
        
                
                    
                    

circularlinkedlist = DoublyLL()
#circularlinkedlist.createCDLL(1)
circularlinkedlist.insertCDLL(1,0)
circularlinkedlist.insertCDLL(0,0)
circularlinkedlist.insertCDLL(2,1)
circularlinkedlist.insertCDLL(3,1)
circularlinkedlist.insertCDLL(4,3)
circularlinkedlist.insertCDLL(2,2)
print([node.value for node in circularlinkedlist])
circularlinkedlist.traverseCDLL()
print('reverse')
circularlinkedlist.traversereverseCDLL()
circularlinkedlist.deleteCDLL(0)


print([node.value for node in circularlinkedlist])
circularlinkedlist.traversereverseCDLL()
circularlinkedlist.deleteentireCDLL()
print([node.value for node in circularlinkedlist])