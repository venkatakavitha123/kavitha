#list1 = list(map(int, input().split()))
list1 = [2,3,43,56,23,46,70,23]
list1 = list1[1:]
print(list1)
cumulative_sum =[]
count = 0
for i in list1:
    count += i
    cumulative_sum.append(count)
print(cumulative_sum)
    
    