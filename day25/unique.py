list = [0,0,1,1,2,2,3]
fixed_point = 1
for i in range(1,len(list)):
    if list[i-1] != list[i]:
        list[fixed_point] = list[i]
        fixed_point += 1
        print(list)
print(fixed_point)


#  output 0 1 2 3 2 2 3
#  4    => 0 1 2 3
