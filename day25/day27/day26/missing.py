# use XOR operation
arr = [1 ,0 ,3]
missing = arr[0]
list = range(0 ,len(arr) + 1)
for i in range(1,len(arr)):
     missing ^= arr[i]

for i in list:
    missing ^= i
print(missing)


# TC o(n)
# SC O(n)

# find the missing number in list [1,0,3]   => 2





