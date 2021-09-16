from Linked_list_CLASS import Linkedlist
def sumNode(ll1, ll2):
    ll3 = Linkedlist()
    Node1 = ll1.head
    Node2 = ll2.head
    carry=0
    while Node1:

        sum = (Node1.value + Node2.value)
        a = sum % 10
        ll3.add(a + carry)
        carry = sum // 10
        Node1 = Node1.next
        Node2 = Node2.next
    return ll3
    




custom = Linkedlist()
control=Linkedlist()
ll1 = custom.add(9)
ll1 = custom.add(7)
ll1 = custom.add(5)
ll2 = control.add(7)
ll2 = control.add(5)
ll2 = control.add(2)

print(ll1)
print(ll2)
print(len(ll1))
print(sumNode(ll1,ll2))

