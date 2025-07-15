n, h, m = map(int,input().split())

grid = [list(map(int, input().split())) for _ in range(n)]

drs, dcs = [0,1,0,-1],[1,0,-1,0]
from collections import deque

def in_range(r,c):
    return 0<=r<n and 0<=c<n

def push(r,c,d):
    if not visited[r][c]:
        dist[r][c] = d
        visited[r][c] = 1
        q.append((r,c))
    

def bfs():
    while q:
        r, c = q.popleft()
        for dr, dc in zip(drs, dcs):
            nr, nc = r+dr, c+dc
            if in_range(nr,nc) and grid[nr][nc] != 1 and not visited[nr][nc]:
                push(nr,nc,dist[r][c]+1)
    return -1

visited = [[0]*n for _ in range(n)]
dist = [[0]*n for _ in range(n)]
q = deque()


for i in range(n):
    for j in range(n):
        if grid[i][j] == 3:
            push(i,j,0)

bfs()
for i in range(n):
    for j in range(n):
        if grid[i][j] != 2:
            print(0, end = ' ')
        else:
            if not visited[i][j]:
                print(-1, end = ' ')
            else:
                print(dist[i][j], end = ' ')
    print()