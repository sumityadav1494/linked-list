from Linked_list_CLASS import Linkedlist
def reorder(ll, x):
    currentNode = ll.head
    ll.tail = ll.head
    while currentNode:
        nextNode = currentNode.next
        currentNode.next = None
        if currentNode.value < x:
            currentNode.next = ll.head
            ll.head = currentNode
        else:
            ll.tail.next = currentNode
            ll.tail = currentNode
            ll.tail.next=None
            
        currentNode = nextNode
    return ll
custom = Linkedlist()
custom.generate(10,1,99)
print(custom)
reorder(custom,50)
print(custom)       
        
    

    