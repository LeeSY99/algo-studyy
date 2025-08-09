n = int(input())

grid = [list(map(int, input().split())) for _ in range(n)]

drs, dcs = [0,1,0,-1],[1,0,-1,0]
from collections import deque

left = 1
right = 1000000

def in_range(r,c):
    return 0<=r<n and 0<=c<n

visited = []
def check(d):
    visited = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if visited[i][j]:
                continue
            count, visited = bfs(i,j,d,visited)
            
            if count >= (n*n + 1) //2:
                # print(d,count)
                return True
    return False

def bfs(r,c,d,visited):
    q = deque()
    q.append((r,c))
    visited[r][c] = 1
    count = 1
    while q:
        r, c = q.popleft()
        for dr, dc in zip(drs,dcs):
            nr, nc = r+dr, c+dc
            if in_range(nr,nc) and not visited[nr][nc] and abs(grid[nr][nc] - grid[r][c]) <=d:
                q.append((nr,nc))
                visited[nr][nc] = 1
                count +=1
    return count, visited
        
ans = 1000000
while left<=right:
    mid = (left+right)//2
    if check(mid):
        ans = min(ans, mid)
        right = mid-1
    else:
        left = mid+1

print(ans)
