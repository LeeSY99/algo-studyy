m,n = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(m)]
colored = [[False] * n for _ in range(m)]
from collections import deque

for i in range(m):
    arr = list(map(int, input().split()))
    for j in range(n):
        if arr[j] == 1:
            colored[i][j] = True

def in_range(r,c):
    return 0<=r<m and 0<=c<n

drs, dcs = [0,1,0,-1],[1,0,-1,0]



def check(D):
    visited = [[False] * n for _ in range(m)]
    for i in range(m):
        for j in range(n):
            if colored[i][j] and not visited[i][j]:
                bfs(i,j,visited,D)
    
    if DEBUG:
        if D < 30:
            print(D)
            for v in visited:
                print(*v)

    for i in range(m):
        for j in range(n):
            if colored[i][j] and not visited[i][j]:
                return False
    
    return True


def bfs(r,c,visited, D):
    q = deque()
    q.append((r,c))
    # visited[r][c] = True

    while q:
        cr,cc = q.popleft()
        for dr, dc in zip(drs,dcs):
            nr,nc = cr+dr, cc+dc
            if in_range(nr,nc) and abs(grid[nr][nc] - grid[cr][cc]) <= D and not visited[nr][nc]:
                visited[nr][nc] = True
                q.append((nr,nc))

left = 0
right = 10**9
ans = float('inf')
DEBUG = False
while left <= right:
    mid = (left + right) // 2
    if check(mid):
        right = mid - 1
        ans = min(ans, mid)
    else:
        left = mid + 1

print(ans)
