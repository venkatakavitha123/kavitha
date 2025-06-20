t = int(input())
while t > 0:
    n,x,y = map(int,input().split())
    a = list(map(int,input().split()))
    s = 0
    for i in a:
        if i >= y:
            s += y
        else:
            s += i
    if s > x:
        print("COUPON")
    else:
        print("NO COUPON")
        t -= 1