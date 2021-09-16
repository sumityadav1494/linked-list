#return to kth element from last
from Linked_list_CLASS import Linkedlist
def returnLL(ll,n):
    control1 = ll.head
    for i in range(n-1):
        control1 = control1.next
    control2 = ll.head
    while control1.next:
        control1 = control1.next
        control2 = control2.next
    return control2.value
    
        

custom = Linkedlist()
custom.generate(10,1,99)
print(custom)
#print(len(custom))
print(returnLL(custom,2))
