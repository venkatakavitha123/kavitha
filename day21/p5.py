t = int(input())
while t > 0:
    n,x = map(int,input().split())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    c = 0
    for i in range(n):
        if a[i] >= x:
            c += b[i]
    print(c)
    t -= 1
        
            