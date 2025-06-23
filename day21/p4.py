t = int(input())

while t > 0:
    n = int(input())
    a = list(map(int,input().split()))
    max = a[0]
    for i in range(n):
        max = min(a[i],max)
    count = 0
    for i in range(n):
        if a[i] == max:
            count += 1
    print(n-count)
    t -= 1
    
    # min to max value in list 
    # output 1 2 min val is 1 and n=4   2 2 4 6 max val is 2