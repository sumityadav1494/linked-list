
class Node:
    def __init__(self, value):
        
        self.value = value
        self.next=None

class Linkedlist:
    def __init__(self):

        self.Head = None
        self.Tail = None
    def __iter__(self):
        node = self.Head
        while node:
            yield node
            node = node.next
    def insertSLL(self, value, location):
        newNode = Node(value)
        if self.Head is None:
            self.Head = newNode
            self.Tail = newNode
        else:
            if location == 0:
                newNode.next = self.Head
                self.Head = newNode
            elif location == 1:
                newNode.next = None
                self.Tail.next = newNode
                self.Tail = newNode
            else:
                tempNode = self.Head
                index = 0
                while index < location - 1:
                    tempNode = tempNode.next
                    index += 1
                nextNode=tempNode.next
                tempNode.next = newNode
                newNode.next=nextNode
                        
                        
                
                    
    

    

creatingLinkedlist=Linkedlist()
creatingLinkedlist.insertSLL(1,1)
creatingLinkedlist.insertSLL(2,1)
creatingLinkedlist.insertSLL(3,1)
creatingLinkedlist.insertSLL(4,0)
creatingLinkedlist.insertSLL(4,2)

print([node.value for node in creatingLinkedlist])















