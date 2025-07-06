from collections import deque
queue = deque()

n = int(input("Enter number of elements:"))
for i in range(n):
    student = {}
    while student:
        name = str(input("enter name:"))
        priority_order = int(input("enter order:"))
        print(name) 
        print(priority_order)
# ATM