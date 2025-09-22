from collections import deque
n,m = map(int, input().split())

grid  = [list(map(int, input().split())) for _ in range(n)]

def in_range(r,c):
    return 0<=r<n and 0<=c<m


drs,dcs = [0,1,0,-1],[1,0,-1,0]
visited = [[False]*m for _ in range(n)]

def clear_visited():
    for i in range(n):
        for j in range(m):
            visited[i][j] = False

def check(d):
    for lo in range(1,501):
        clear_visited()

        hi = lo + d

        if lo <= grid[0][0] <= hi:
            bfs(lo, hi)
        if visited[n-1][m-1]:
            return True
    return False

def bfs(lo, hi):
    q = deque([(0,0)])
    visited[0][0] = True

    while q:
        r, c = q.popleft()
        for dr, dc in zip(drs,dcs):
            nr, nc = r+dr, c+dc
            if in_range(nr,nc) and (lo <= grid[nr][nc] <= hi) and not visited[nr][nc]:
                visited[nr][nc] = True
                q.append((nr,nc))
        



left = 0
right = 500
ans = 500

while left <= right:
    mid = (left + right) // 2
    if check(mid):
        right = mid-1
        ans = min(ans, mid)
    else:
        left = mid + 1

print(ans)

