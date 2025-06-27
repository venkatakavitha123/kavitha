#class Solution:
 #   def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]: num1 = []
nums1 = [2,4,4,5,2]
nums2 = [2,4,3,5,2]
intersection = {}
result = []
for i in nums1:
    intersection[i] = 1
for i in nums2:
    if i in intersection and intersection[i] == 1:
        result.append(i)
        intersection[i]=0
print(result)


# compare the two list commom values return
# output [2,4,5]
# TC O(n)
# SC O(n)