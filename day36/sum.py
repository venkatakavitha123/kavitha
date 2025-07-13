def sum(n):
    # sum of 5 numbers
    #base condition
    if n == 0: return 0

    return n + sum(n-1)

def fact(n):
    # factorial
    if n == 1 or n == 0:
        return 1
    return n * fact(n-1)

def fibo(n):
    # fibonacci series
    if n == 1 or n == 0:
        return n
    return fibo(n-1) + fibo(n-2)

answer = fibo(6)
print(answer)

result = fact(5)
print(result)

output = sum(4)
print(output)
