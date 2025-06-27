#class Solution:
  #  def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None

nums1 = [1,2,3,4,8]
nums2 = [5,6,9,10]
m = len(nums1)
n = len(nums2)
x= 0
y = 0
result = []
while x < m  and y < n:
    if nums1[x] < nums2[y]:
        result.append(nums1[x])
        x += 1
    else:
        result.append(nums2[y])
        y += 1
if x == m:
    for i in range(y,n):
        result.append(nums2[i])
if y == n:
    for i in range(x,m):
        result.append(nums1[i])
    for i in range(len(result)):
        nums1[i]=result[i]
print(result)




  # merge
  #  TC  O(n)
  # SC O(n)