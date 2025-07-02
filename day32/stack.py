expression = "[(((2)+(3)))]"
stack = []
for i in expression:
    if i == "(":
        #print("current i:",i)
        stack.append(i)   
    elif i == ")":
        stack.pop()
    else:
        continue
    #print(stack)
if len(stack)==0:
    print("valid")
else:
    print("invalid")