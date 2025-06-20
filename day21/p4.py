t = int(input())
while t>0:
    n = int(input())
    a = list(map(int,input().split()))
    max=a[0]
    for i in range(n):
        max = min(a[i],max)
    count = 0
    for i in range(n):
        if a[i] == max:
            count += 1
    print(n-count)
    t -= 1