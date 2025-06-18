n = int(input())
list1 =[]
for i in range(n):
    dict = {}
    dict["name"] = input()
    dict["id"] = input()
    list1.append(dict)
print(list1)


search = input()
filter_list1=[]
for i in  list1:
    if search.lower() in ["id"].lower():
        filter_list1.append(i)
print(filter_list1)
        
        
    