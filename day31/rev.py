# reverse the linked list
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
head = ListNode([1,2,3,4,5])
current = head
prev = None
while current != None:
    next_node = current.next
    current.next = prev
    prev = current
    current = next_node
print(prev)

# leetcode problem
# input [1,2,3,4,5]
# output [5,4,3,2,1]