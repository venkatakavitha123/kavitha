nums = [1,2,220,45,66,88,90,100]
target = 92
index_dict = {}  # SP O(n)
for i in range(len(nums)):   # TC O(n)
    index_dict[nums[i]] = i
for i in range(len(nums)): # TC O(n)
    find = target-nums[i]   # ST O(n)
    if find in index_dict and index_dict[find] != i:
        print([i,index_dict[find]])
        break
# array to sort and present the previous index values of two sum
# 90+2 => 92 index value [1,6]