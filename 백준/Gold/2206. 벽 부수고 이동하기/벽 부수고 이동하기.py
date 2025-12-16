from collections import deque
n,m = map(int, input().split())
k=1

grid = [list(map(int, input())) for _ in range(n)]

def in_range(r,c):
    return 0<=r<n and 0<=c<m

drs, dcs = [0,1,0,-1],[1,0,-1,0]
# print(grid)
def bfs():
    dist = [[[-1] * (k+1) for _ in range(m)] for _ in range(n)]
    q= deque([(0,0,0)])
    dist[0][0][0] = 1

    while q:
        r, c, broken = q.popleft()
        for dr, dc in zip(drs,dcs):
            nr, nc = r+dr, c+dc
            if in_range(nr, nc):
                if grid[nr][nc] == 0 and dist[nr][nc][broken] == -1:
                    dist[nr][nc][broken] = dist[r][c][broken]+1
                    q.append((nr,nc,broken))
                elif broken < k and grid[nr][nc] == 1 and dist[nr][nc][broken+1] == -1:
                    dist[nr][nc][broken+1] = dist[r][c][broken] + 1
                    q.append((nr,nc,broken+1))

    return dist[n-1][m-1]

ans = float('inf')
can = bfs()
for c in can:
    if c ==-1:
        continue
    ans = min(ans, c)

if ans == float('inf'):
    ans = -1
print(ans)

