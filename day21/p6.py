t = int(input())
for i in range(t):
    n = int(input())
    ans = 0
    for j in range(n):
        a = int(input())
        ans ^= a
    print(ans)


# 1 test case
# n = 3  a = 1 2 1      1 is pair print only 2