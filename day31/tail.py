class Node:
    def __init__(self ,value=0,nextNode=None):
        self.val=value
        self.next=nextNode

head = Node(100)
head.next = Node(200)
head.next.next = Node(300)
head.next.next.next = Node(400)
head.next.next.next.next = Node(500)    
current = head

result =[]
def display_linked_list(current):
    result= []
    while current != None:
        result.append(str(current.val))
    #print(current.val,end=" ")
        current = current.next
    
#print()   
#print(length)
    print('=>'.join(result))
    
# insert the start value
print("---insert the starting value---")
newNode = Node(90)
newNode.next=head
head = newNode
display_linked_list(head)



#add item to the tail of linkedlist
print("---insert the value in tail---")
current = head
while current.next != None:
    current = current.next
current.next = Node(600)
display_linked_list(head)
