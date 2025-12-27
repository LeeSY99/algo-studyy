from itertools import combinations
from collections import deque
n,m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

can_wall = []
for i in range(n):
    for j in range(m):
        if grid[i][j] == 0:
            can_wall.append((i,j))

drs, dcs = [0,1,0,-1],[1,0,-1,0]
def in_range(r,c):
    return 0<=r<n and 0<=c<m

def bfs(r,c):
    q = deque()
    q.append((r,c))
    visited[r][c] = True
    while q:
        r,c = q.popleft()
        for dr, dc in zip(drs,dcs):
            nr, nc = r+dr, c+dc
            if in_range(nr,nc) and new_grid[nr][nc] == 0 and not visited[nr][nc]:
                visited[nr][nc] = True
                new_grid[nr][nc] = 2
                q.append((nr,nc))

ans = 0
c = 0
for wall in combinations(can_wall,3):
    new_grid = [g[:] for g in grid]
    for (i, j) in wall:
        new_grid[i][j] = 1
    visited = [[False] * m for _ in range(n)]

    for i in range(n):
        for j in range(m):
            if new_grid[i][j] == 2 and not visited[i][j]:
                bfs(i,j)

    count = 0
    c+=1
    for i in range(n):
        for j in range(m):
            if new_grid[i][j] == 0:
                count += 1
    ans = max(ans, count)
print(ans)
# print(c)

