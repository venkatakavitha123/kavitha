    
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
result = []
def display_linked_list(current):
    result = []
    while current != None:
        result.append(str(current.val))
        current = current.next  
    print('=>'.join(result))
    
    
    length = 0
    current = head
    while current != None:
        length += 1
        current = current.next

        current = head
        count = 0
    while current != None:
        count += 1
        if count == length // 2 + 1:
            print("middle Element = " , current.val)
            current = current.next
            
    display_linked_list(head)
    

     
        # middle linked list      1 2 3 4 5 => 3