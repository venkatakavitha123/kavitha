l=[11,12,15,22,35,35,60,70,70,80]
freq_max = 0
freq_max_element = 0
count =  1
for i in range(len(l)):
    for j in range(i+1,len(l)):
        count+=1
        if freq_max < count:
            freq_max = count
            freq_max_element = l[i]
print(freq_max_element)