n = int(input())
for i in range(n):
    if i <= n//2:
        for j in range(i+1):
            print("*",end = "")
    if i > n//2:
        for j in range(n-i):
            print("*",end="")
    print()
    
    # n = 4
    # 0<=4//2  0<=2 True
    # 0+1 = 1  1+1=2 2+1=3 
    # 3 > 2 True
    # 5-3 = 2 print * *
    