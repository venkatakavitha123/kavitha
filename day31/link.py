class Node:
    def __init__(self ,value=0,nextNode=None):
        self.val=value
        self.next=nextNode
        
#item1 =Node(100)
#item2= Node(200)
#item3 =Node(300)
#item4 =Node(400)
#item5 =Node(500)
#item1.next = item2
#item2.next = item3
#item3.next = item4
#item4.next = item5
#print(item1.val)
#print(item1.next.val)
#print("--------------")


head = Node(100)
head.next = Node(200)
head.next.next = Node(300)
head.next.next.next = Node(400)
head.next.next.next.next = Node(500)    

result = []
current = head
length =0

while current != None:
    length += 1
    #result.append(str(current.val))
    print(current.val,end=" ")
    current = current.next  
    
print()   
print(length)
#print('=>'.join(result))
print("-------------------")  

#add item to the tail of linkedlist
current = head
while current.next != None:
    current = current.next
current.next = Node(600)
print(current.val)
