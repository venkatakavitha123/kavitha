stack = []
stack.append(5)
stack.append(4)
stack.append(6)
stack.append(7)
stack.append(8)
stack[-1]       # peak element
stack.pop()
print(stack)
print("-----")
print(stack.append(5))  # output None
print(stack[-1])          # return to the top of the element
print(stack.pop())