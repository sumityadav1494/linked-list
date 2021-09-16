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
            node=node.next

    def creatingCircularLL(self,value):
        newNode = Node(value)
        newNode.next = newNode
        self.head = newNode
        self.tail=newNode

circularlinkedlist = CircularLL()
circularlinkedlist.creatingCircularLL(1)
print([node.value for node in circularlinkedlist])
