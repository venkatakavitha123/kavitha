arr = [0,2]
n = len(arr)
missing_number = (n* (n+1) // 2) - sum(arr)
print(missing_number)


#sc => O(1)
#TC => O(n) 

# n(n+1)/2 2 => 2 * 3/2 => 6/2 => 3 - 2 => 1

# sum - sum(question) => missing