n = int(input())

grid = [list(map(int, input().split())) for _ in range(n)]

drs, dcs = [0,1,0,-1],[1,0,-1,0]
from collections import deque

left = 0
right = 1000000

def in_range(r,c):
    return 0<=r<n and 0<=c<n



def check(D):
    visited = [[False] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if visited[i][j]: continue
            if bfs(D, visited, i,j) * 2 >= n*n:
                return True
    
    return False

def bfs(D, visited, r, c):
    q = deque()
    q.append((r,c))
    visited[r][c] = True
    count = 1

    while q:
        cr, cc = q.popleft()
        for dr, dc in zip(drs,dcs):
            nr, nc = cr+dr, cc+dc
            if in_range(nr,nc) and not visited[nr][nc] and abs(grid[nr][nc] - grid[cr][cc]) <= D:
                visited[nr][nc] = True
                count += 1
                q.append((nr,nc))
    
    return count


    
    


left = 0
right = 1000000
ans = float('inf')
while left<= right:
    mid = (left + right) // 2
    if check(mid):
        right = mid - 1
        ans = min(ans, mid)
    else:
        left = mid + 1

print(ans)