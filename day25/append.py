list=[2,4,0,5,1,0,0,2,8]
number = []
zero = []
for i in range(len(list)):
    if list[i] == 0:
        zero.append(0)
    else:
        number.append(list[i]) 
number.extend(zero)
print(number)

# moves zeros last in list use append and extend
        