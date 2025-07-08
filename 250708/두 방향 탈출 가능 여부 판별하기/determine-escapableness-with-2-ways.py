n, m = map(int, input().split())

grid = [list(map(int, input().split())) for _ in range(n)]
visited = [[0] * m for _ in range(n)]

drs, dcs = [1,0],[0,1]

def in_range(r,c):
    return 0<=r<n and 0<=c<m

def dfs(r, c):
    visited[r][c] = 1
    if r == n-1 and c==m-1:
        print(1)
        exit()

    for dr, dc in zip(drs, dcs):
        nr = r+dr
        nc = c+dc
        if in_range(nr, nc) and grid[nr][nc] and not visited[nr][nc]:
            dfs(nr,nc)

dfs(0,0)
print(0)