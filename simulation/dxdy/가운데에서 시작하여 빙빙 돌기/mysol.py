n=int(input())

nums=[[0]*n for _ in range(n)]

r,c=n//2,n//2
num=1
nums[r][c]=num
index=0

dr,dc=[0,-1,0,1],[1,0,-1,0]
a=1
count=0
for k in range(1,n*n):
    for i in range(a):
        r,c=r+dr[index],c+dc[index]
        num+=1
        nums[r][c]=num
        if num>=n*n:
            break
    if num==n*n:
        break
    index=(index+1)%4
    count+=1
    if count==2:
        a+=1
        count=0

for n in nums:
    print(*n)
