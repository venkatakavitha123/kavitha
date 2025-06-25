#class Solution:
 #   def singleNumber(self, nums: list[int]) -> int:
 
list1 = [2,1,2,1,3]
singleNumber = 0
for i in range(len(list1)):
    singleNumber ^= list1[i]
print(singleNumber)



#  2 2 1  =>   print 1