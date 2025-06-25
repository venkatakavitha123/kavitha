list = [0,0,1,2,4,3,5,0,3,0,2,5,0,0,2,3]
move = 0
for i in range(len(list)):
    if list[i] != 0:
        list[move] = list[i]
        move += 1
for i in range(move,len(list)):
    list[i] = 0
print(list)


# output  [1, 2,4,3,5,3,2,5,2,3,0,0,0,0,0] zeros moves to last 
    