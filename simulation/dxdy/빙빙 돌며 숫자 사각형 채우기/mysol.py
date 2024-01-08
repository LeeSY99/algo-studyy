n,m=map(int,input().split())
answer=[]
dr,dc=[0,1,0,-1],[1,0,-1,0]
for _ in range(n):
    answer.append(list([0]*m))

def in_range(nr,nc):
    return 0<=nr<n and 0<=nc<m

r,c=0,-1
dir=0
num=0
while(num<n*m):
    nr=r+dr[dir]
    nc=c+dc[dir]
    if in_range(nr,nc) and answer[nr][nc]==0:
        num+=1
        r,c=nr,nc
        answer[r][c]=num
    else:
        dir=(dir+1)%4

for a in answer:
    print(*a)
