n = int(input("number:"))
prime_flag = True
for i in range(2 ,n):
    if n % i == 0:
        prime_flag = False
if prime_flag:
    print("prime")
else:
    print("not prime")