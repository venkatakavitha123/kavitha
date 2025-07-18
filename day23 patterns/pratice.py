n = int(input())
for i in range(n):
    for j in range(i+1):
        print(j+1,end="")
    print() 
    
    
for i in range(1,n+1):
    print((str(i)+'')* i)
print()


for i in range(0,n+1):
    for j in range(n,n-i,-1):
        print(j,end = "")
    print()
    
    # 5
    # 5 4
    # 5 4 3
    # 5 4 3 2
    # 5 4 3 2 1