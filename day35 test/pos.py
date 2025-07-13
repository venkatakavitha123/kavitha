arr = [0,1,2,3,4,5]
for i in range(0,len(arr)-1,2):
    arr[i],arr[i+1] = arr[i+1],arr[i]  
print(arr)

# change the positions
# output = [1,0,3,2,5,4]