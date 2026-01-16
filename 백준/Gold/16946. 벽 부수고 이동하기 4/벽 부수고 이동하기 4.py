from collections import deque
n,m = map(int, input().split())

grid = [list(map(int, input())) for _ in range(n)]
new_grid = [[0]*m for _ in range(n)]

drs,dcs = [0,1,0,-1],[1,0,-1,0]
def in_range(r,c):
    return 0<=r<n and 0<=c<m
visited = [[False]*m for _ in range(n)]

idx_to_cnt = [0]
def bfs(i,j,index):
    q = deque()
    q.append((i,j))
    visited[i][j] = True
    new_grid[i][j] = index
    count = 1

    while q:
        r, c = q.popleft()
        for dr, dc in zip(drs,dcs):
            nr, nc = r+dr, c+dc
            if in_range(nr,nc) and grid[nr][nc] == 0 and not visited[nr][nc]:
                visited[nr][nc] = True
                q.append((nr,nc))
                new_grid[nr][nc] = index
                count += 1
    idx_to_cnt.append(count)
idx = 1
for i in range(n):
    for j in range(m):
        if grid[i][j] == 0 and not visited[i][j]:
            bfs(i,j,idx)
            idx += 1

ans = [[0]*m for _ in range(n)]
for i in range(n):
    for j in range(m):
        if grid[i][j] == 1:
            s = set()
            for dr, dc in zip(drs,dcs):
                nr,nc = i+dr, j+dc
                if in_range(nr,nc) and grid[nr][nc] == 0 and new_grid[nr][nc] not in s:
                    s.add(new_grid[nr][nc])
                    ans[i][j] += idx_to_cnt[new_grid[nr][nc]]
            ans[i][j] += 1
            ans[i][j] %= 10
# for g in new_grid:
#     print(*g)
# print(idx_to_cnt)
for a in ans:
    for b in a:
        print(b, end='')
    print()
