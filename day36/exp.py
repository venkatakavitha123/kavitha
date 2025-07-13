def fun(n):
    if n == 0: return
    print(n) 
    fun(n-1)
fun(5)

# output 5 4 3 2 1