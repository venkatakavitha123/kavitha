num = input()
if len(num) <= 1:
    result = num
else:
    result = num[-1] + num[1:-1] + num[0]
print(result)