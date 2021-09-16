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
            node = node.next
    def count(self):
        count = 0
        node = self.head
        while node:
            node = node.next
            count += 1
        return count + 1
    def insertDLL(self,value,location):
        newNode = Node(value)
        if self.head is None:
            newNode.next=None
            newNode.prev = None
            self.head = newNode
            self.tail=newNode
        else:
            if location == 0:
                self.head.prev = newNode
                newNode.next = self.head
                self.head = newNode
                
            elif location == 1:
                if self.head is None:
                    newNode.next=None
                    newNode.prev = None
                    self.head = newNode
                    self.tail = newNode
                else:
                    newNode.prev = self.tail
                    self.tail.next = newNode
                    self.tail = newNode
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
                
    def traverseDLL(self):
        if self.head == None:
            print('no linked list exist')
        else:
            tempNode = self.head
            while tempNode:
                print(tempNode.value)
                tempNode = tempNode.next
    def traversereverseDLL(self):
        if self.head == None:
            print('no linked list exist')
        else:
            tempNode = self.tail
            while tempNode:
                print(tempNode.value)
                tempNode = tempNode.prev
    def deleteDLL(self, location):
        if self.head == None:
            print('no linked list exist')
        else:
            if location == 0:
                if self.head.next == None:
                    
                    self.head = None
                    self.tail = None
                else:
                    self.head.next.prev = None
                    self.head = self.head.next
            elif location == 1:
                if self.head.next == None:
                    
                    self.head = None
                    self.tail = None
                else:
                    previousNode=self.tail.prev
                    previousNode.next = None
                    self.tail = previousNode
            else:
                tempNode = self.head
                index = 0
                while index < location - 1:
                    tempNode = tempNode.next
                    index += 1
                nextNode = tempNode.next
                tempNode.next = nextNode.next
                nextNode.next.prev=tempNodecircularlinkedlist = DoublyLL()
    def deleteentireDLL(self):
        tempNode = self.head.next
        while tempNode:
            tempNode.prev = None
            tempNode = tempNode.next
        self.head = None
        self.tail = None
circularlinkedlist = DoublyLL()       
circularlinkedlist.insertDLL(0,0)
circularlinkedlist.insertDLL(1,1)
circularlinkedlist.insertDLL(2,1)
circularlinkedlist.insertDLL(3,1)
circularlinkedlist.insertDLL(4,3)
circularlinkedlist.insertDLL(5,1)
circularlinkedlist.insertDLL(4,0)
print([node.value for node in circularlinkedlist])
circularlinkedlist.deleteDLL(4)
print([node.value for node in circularlinkedlist])
circularlinkedlist.deleteentireDLL()
print([node.value for node in circularlinkedlist])
#circularlinkedlist.traverseDLL()
#print('reverse')
#circularlinkedlist.traversereverseDLL()