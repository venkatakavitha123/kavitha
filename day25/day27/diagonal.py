#class Solution:
 #   def diagonalSum(self, mat: List[List[int]]) -> int:
mat = [[1,2,3],
       [4,5,6],
       [7,8,9]]
n = len(mat)
diagonalSum = 0
for i in range(n):
    diagonalSum +=  mat[i][i]
    diagonalSum +=  mat[i][n-1-i]
if n%2 == 1:
    diagonalSum -= mat[n//2][n//2]
print(diagonalSum)


# diagonal matrix => sum   1+5+9+7+3 = 25
# TC O(n)

            
