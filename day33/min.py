num ="14302219"
k = 4
stack = []
#if k == len(num): 
#   print(0)  
while k:
    for i in num:
        while stack and i < stack[-1] and k:
            stack.pop()
            k -= 1
        stack.append(i)
result=''.join(stack).lstrip("0")
print(result)

# minimum  value  
# k = 4 remove the elements
