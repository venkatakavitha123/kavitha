n = int(input())
for i in range(0,n+1):
    for j in range(n,n-i,-1):
        print(j,end=" ")
    print()
        
   # 5                     5-0=5
   # 5 4                   5-1= 4  
   # 5 4 3                staring_val  5-2 = 3   end_val
   # 5 4 3 2
   # 5 4 3 2 1