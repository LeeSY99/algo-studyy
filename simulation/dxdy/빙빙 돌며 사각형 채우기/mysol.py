n,m=map(int,input().split())

nums=[[0]*m for _ in range(n)]
first=65
r,c=0,0
nums[r][c]=first

def in_range(r,c):
    return 0<=r and r<n and 0<=c and c<m

index=0
dr,dc=[0,1,0,-1],[1,0,-1,0]
for i in range(1,n*m):
    nr,nc=r+dr[index],c+dc[index]
    if not in_range(nr,nc) or nums[nr][nc]!=0:
        index=(index+1)%4
    r,c=r+dr[index],c+dc[index]
    first+=1
    if first==91:
        first=65
    nums[r][c]=first

for num in nums:
    for n in num:
        print(chr(n),end=' ')
    print()
