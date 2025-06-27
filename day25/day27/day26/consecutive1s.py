nums = [1,1,0,0,5,7,1,1,1]
count = 0
max_count = 0
for i in range(len(nums)):
    if nums[i] == 1:  # check the list in 1
        count += 1 #count increment
        if count > max_count:
            max_count = count
    else:
        count = 0
print(max_count)
        
        
        # TC O(n)
        # SC O(n)
        
        # check the highest number of ones  [1,1,0,1,1,1,6,7,1,1,1,1]  => 4