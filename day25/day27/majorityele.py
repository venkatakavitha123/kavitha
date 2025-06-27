#class Solution:
 #   def majorityElement(self, nums: List[int]) -> int:
nums = [1,2,2,4,4,4,1,1] 
majority = 0
element = 0
for i in range(len(nums)):
    if majority == 0:
        element = nums[i]  
    if nums[i] == element:
        majority +=1
    else:
        majority -= 1
        
print(element)
        
# majority element print in list
#TC O(n)
#SC O(n)