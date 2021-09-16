class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        
class CircularLL:
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
            if node.next == self.tail.next:
                break
            node = node.next
            count += 1
        return count+1

    def insertCircularSLL(self,value,location):
        newNode = Node(value)
        if self.head == None:
            self.head = newNode
            self.tail = newNode
            newNode.next = newNode
        else:
            if location == 0:
                self.tail.next = newNode 
                newNode.next = self.head
                self.head = newNode
                
                
            elif location == 1:
                if self.head == None:
                    self.head = newNode
                    self.tail = newNode
                    newNode.next = newNode
                else:
                    
                    newNode.next = self.tail.next
                    self.tail.next = newNode

                    self.tail = newNode
            else:
                tempNode = self.head
                index = 0
                while index < location - 1:
                    tempNode = tempNode.next
                    index += 1
                nextNode = tempNode.next
                tempNode.next = newNode
                newNode.next = nextNode
    def deleteCircularSLL(self, location):
        if self.head == None:
            return "no Linked List Exist"
        else:
            if location == 0:
                if self.head == self.tail:
                    self.tail.next = None
                    self.head = None
                    self.tail = None
                else:
                    self.head = self.head.next
                    self.tail.next=self.head
                    
            elif location == 1:
                if self.head.next == None:
                    self.head.next = None
                    self.head = None
                    self.tail = None
                else:
                    tempNode =self.head
                    while tempNode.next!=self.tail:
                        tempNode = tempNode.next
                        
                    tempNode.next = self.tail.next
                    self.tail = tempNode
            else:
                tempNode = self.head
                index = 0
                while index < location - 1:
                    tempNode = tempNode.next
                    index+=1
                nextNode = tempNode.next
                tempNode.next = nextNode.next

circularlinkedlist = CircularLL()
circularlinkedlist.insertCircularSLL(0,0)
circularlinkedlist.insertCircularSLL(1,1)
circularlinkedlist.insertCircularSLL(2,1)
circularlinkedlist.insertCircularSLL(3,1)
circularlinkedlist.insertCircularSLL(4,3)
circularlinkedlist.insertCircularSLL(5,1)
circularlinkedlist.insertCircularSLL(4,0)
print([node.value for node in circularlinkedlist])
print(circularlinkedlist.count())
circularlinkedlist.deleteCircularSLL(0)
print([node.value for node in circularlinkedlist])