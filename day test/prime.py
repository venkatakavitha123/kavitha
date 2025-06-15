n = int(input())
for n in range(2,n+1):
    prime_flag = True
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            prime_flag = False
    if prime_flag:
        print(n,end=' ')