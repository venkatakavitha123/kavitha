mat = [[1,2,3,4],
       [5,6,7,8],
       [9,10,11,12],
       [13,14,15,16]]
n = 4
col = 4
result = []
top =0
bottom =n-1
right=n-1 
left = 0
while top < bottom and left < right:
    for i in range(left , right+1):
        result.append(mat[top][i])
    top +=1
    for i in range(top , bottom+1,):
        result.append(mat[i][right])
    right -=1
    for i in range(right ,left-1,-1):
        result.append(mat[bottom][i])
    bottom -=1
    for i in range(bottom ,top-1,-1):
        result.append(mat[i][left])
    left +=1
print(result)
    