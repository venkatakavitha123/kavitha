n = int(input("enter a number:"))
if n % 2 != 0:
    print("weird")
else:
    if n >= 2 and n <= 6:
        print("not weird")
    elif n >= 8 and n <= 20:
        print("weird")
    elif n > 20:
        print("not weird")