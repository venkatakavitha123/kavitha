list = [2,8,49,40,3 ,8,10]
max = list[0]
secondmax = 0
for i in range(len(list)):
    if max < list[i]:
        secondmax = max
        max = list[i]
    elif list[i] > secondmax and list[i] != max:
        secondmax = list[i]

print(secondmax)



#  TC o(n)
# find the second largest number