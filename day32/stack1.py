def check_valid(exp):
    stack = []
    for i in exp:
        if i == "(":
            print("current i:",i)
            stack.append(i)   
        elif i == ")":
            if len(stack) != 0:
                if (i == ")" and stack[-1] == "(") or (i == "]" and stack[-1] == "[") or ( i == "}" and stack[-1] == "{"):
                    stack.pop()
            else:
                return "Invalid"
        else:
            continue
    #print(stack)
    if len(stack)==0:
        print("valid")
    else:
        print("invalid")
    
    
expression = "[(((2)+(3)))]"
check_valid(expression)