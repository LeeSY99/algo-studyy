n,m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

drs, dcs = [0,1,0,-1],[1,0,-1,0]

def in_range(r,c):
    return 0<=r<n and 0<=c<m

from collections import deque
import copy
def bfs(grid):
    new_grid = copy.deepcopy(grid)
    visited = [[0]*m for _ in range(n)]
    visited[0][0] = 1
    while q:
        r, c = q.popleft()
        for dr, dc in zip(drs, dcs):
            nr, nc = r+dr, c+dc
            if in_range(nr,nc) and not visited[nr][nc]:
                visited[nr][nc]=1
                new_grid[nr][nc] = 0
                if not grid[nr][nc]:
                    q.append((nr,nc))
    return new_grid

def check(grid):
    count = 0
    for i in range(n):
        for j in range(m):
            if grid[i][j]:
                count+=1
    return count

count = 0
last = check(grid)
while 1:
    now = check(grid)
    if now == 0:
        break
    else:
        last = now
    q = deque()
    q.append((0,0))
    grid = bfs(grid)
    count += 1

print(count, last)

