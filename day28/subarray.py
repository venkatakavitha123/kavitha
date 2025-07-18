arr =[2,1,4,5,1,1,1,1,3,2]
target = 4
i = 0
j = 0  # O(1)
longest = 0
sub = arr[i]
while i<len(arr)-1 and j<len(arr)-1:  #  TC O(n)
    if sub < target: 
        j += 1
        sub += arr[i]
    elif sub > target:
        sub == arr[i] 
        i += 1
    else:
        print(i,j)
        longest = max(j-i+1,longest)
        j += 1
        sub = arr[j]
print(longest)
               
             
    # target = 3 example
    # [2,1] = 2
    # [1,1,1] = 3  target highest subarray length
    # [3] = 1
    
    
               
        