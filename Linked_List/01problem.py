#remove duplicates
from Linked_list_CLASS import Linkedlist
def remove_duplicates(ll): #-------------->t.c=O(n)    S.c=O(n)
    if ll.head is None:
        return
    
    else:
        
        currentNode = ll.head
        set1 = set([currentNode.value])#----------> O(n) Space
        while currentNode.next:
            if currentNode.next.value in set1:
                currentNode.next = currentNode.next.next
            else:
                set1.add(currentNode.next.value)
                currentNode=currentNode.next
        return ll

def remove_duplicates1(ll):  #time complexity O(N^2)  but space complexity O(1)
    if ll.head is None:
        return
    else:
        currentNode = ll.head
        while currentNode:
            tempNode=currentNode
            while tempNode.next:
                if tempNode.next.value==currentNode.value:
                    tempNode.next = tempNode.next.next
                tempNode = tempNode.next
            currentNode = currentNode.next
        return ll
                
                    


costomLL = Linkedlist()
costomLL.generate(10,1,99)
print(costomLL)
remove_duplicates(costomLL)
print(costomLL)
remove_duplicates1(costomLL)
print(costomLL)