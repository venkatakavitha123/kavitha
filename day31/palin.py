class Solution:
    def __init__(self, head=0,val = 0,next=None):
        self.head = head
        self.next = next
        self.val = val
head = Solution(1)
head.next=Solution(2)  
head.next.next=Solution(1)   
list_vals = []
while head:
    list_vals.append(head.val)
    head = head.next
    left, right = 0, len(list_vals) - 1
    while left < right and list_vals[left] == list_vals[right]:
        left += 1
        right -= 1
print(left >= right)