def printer(n):
    #Base Condition
    if n == 0: return
    
    printer(n-1)  # function calling recursion
    
    #operation
    print(n)

#main code 
printer(5)

# output 1 2 3 4 5