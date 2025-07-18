list = [1,2,3,4,5,0,3,0,4,0,5,6]
for i in range(len(list)):
    if list[i]!=0:
        print(list[i],end = "")
for i in range(len(list)):
    if list[i] == 0:
        list[-1] = 0
    print(list[-1])
    
    # move the zeeros in last