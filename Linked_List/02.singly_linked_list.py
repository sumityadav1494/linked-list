class Node:
    def __init__(self,value):
        self.value = value
        self.next = None
    
class Linkedlist:
    def __init__(self):

        self.head = None
        self.tail = None
    def __iter__(self):
        node = self.head
        while node:
            yield node
            node=node.next
    def insertLL(self, value, location):
        newNode=Node(value)
        if self.head is None:
            self.head = newNode
            self.tail = newNode
        else:
            if location == 0:
                newNode.next = self.head
                self.head = newNode
            elif location == 1:
                #newNode.next = None
                self.tail.next = newNode
                self.tail = newNode
            else:
                tempNode = self.head
                index = 0
                while index < location - 1:
                    
                    tempNode = tempNode.next
                    index+=1
                
                newNode.next = tempNode.next
                tempNode.next = newNode
    def traverseLL(self):
        if self.head is None:
            print("No element in linked list")
        else:
            index = self.head
            while index is not None:
                print(index.value)
                index = index.next
    def searchingValue(self, value):
        if self.head is None:
            print("No element in linked list")

        else:
            index = self.head
            while index is not None:

                if index.value == value:
                    return(index.value)
                index = index.next
            return("the value is not in the linked list")

singlyLinkedlist = Linkedlist()
singlyLinkedlist.insertLL(1,1)
singlyLinkedlist.insertLL(2,1)
singlyLinkedlist.insertLL(3,1)
singlyLinkedlist.insertLL(4,2)
singlyLinkedlist.insertLL(4,1)
singlyLinkedlist.insertLL(4,0)
print([node.value for node in singlyLinkedlist])
(singlyLinkedlist.traverseLL())              
print(singlyLinkedlist.searchingValue(4))              
                
    