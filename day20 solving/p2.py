list1 = input().split()
print(list1)
keyword = input()
filtered_list1 = []
for i in list1:
    if keyword in i:
    #if keyword.lower() in i.lower():
        filtered_list1.append(i)
print(filtered_list1)