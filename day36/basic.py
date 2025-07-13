# use count  
def rec(count,end):
    if count == end:
        return
    print(count) 
    count += 1 
    rec(count,end) 
result = int(input())
rec(1,result)
