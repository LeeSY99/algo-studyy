n, k = map(int, input().split())

grid = [list(map(int, input().split())) for _ in range(n)]

from collections import deque

q = deque()
visited = [[0]*n for _ in range(n)]
rotten = [[-2]*n for _ in range(n)]

def push(r,c,d):
    visited[r][c] = 1
    rotten[r][c] = d
    q.append((r,c))

drs, dcs = [0,0,1,-1],[1,-1,0,0]

def in_range(r,c):
    return 0<=r<n and 0<=c<n

def bfs():
    while q:
        r,c = q.popleft()
        for dr, dc in zip(drs,dcs):
            nr, nc = r+dr, c+dc
            if in_range(nr,nc) and not visited[nr][nc] and grid[nr][nc] == 1:
                push(nr,nc,rotten[r][c]+1)


for i in range(n):
    for j in range(n):
        if grid[i][j] == 2:
            push(i,j,0)
bfs()

for i in range(n):
    for j in range(n):
        if grid[i][j] == 0:
            print(-1, end = ' ')
        else:
            print(rotten[i][j], end = ' ')
    print()

            
