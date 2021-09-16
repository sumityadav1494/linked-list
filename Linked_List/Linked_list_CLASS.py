from random import randint

class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None
        self.tail = None
    def __str__(self):
        return str(self.value)
class Linkedlist:
    def __init__(self):
        self.head = None
        self.tail = None
        
    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next
    def __str__(self):
        values = [str(x.value) for x in self]
        return '-->'.join(values)
    def __len__(self):
        count = 0
        tempnode = self.head
        while tempnode:
            tempnode = tempnode.next
            count += 1
        return count 
    def add(self,value):
        if self.head is None:
            newNode = Node(value)
            self.head = newNode
            self.tail = newNode
        else:
            self.tail.next=Node(value)
            self.tail = self.tail.next
        return self
    def generate(self, n, min_value, max_value):
        self.head = None
        self.tail = None
        for i in range(n):
            self.add(randint(min_value, max_value))
        return self


costomLL=Linkedlist()
costomLL.generate(10, 1, 99)
print(costomLL)
print(len(costomLL))
n = Node(5)
print(n)