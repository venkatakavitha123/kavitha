#class Solution:
 #   def check(self, nums: List[int]) -> bool:
nums = [3,4,5,1,2]
#nums = [2,1,3,4,5]
count = 0
n = len(nums)
for i in range(n):
    if nums[i] > nums[(i+1) % n]:  # 3 > (3+1)%4  => 3 > 0 TRUE
        count += 1  # increment 0+1 = 1
        if count > 1: 
                print(False)
print(True)



# check the array sorted order
# sorted order return TRUE otherwise return FALSE