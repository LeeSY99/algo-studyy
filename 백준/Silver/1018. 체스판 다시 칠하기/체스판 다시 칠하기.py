from collections import deque
n,m = map(int, input().split())
grid = [list(input()) for _ in range(n)]

drs,dcs = [0,1,0,-1],[1,0,-1,0]

def in_range(r, c, sr, sc):
    return sr <= r < sr + 8 and sc <= c < sc + 8


def bfs(r, c, color):
    if color == 0:
        start_color = 'B'
    else:
        start_color = 'W'
    q = deque([(r, c)])
    visited = [[False] * (m) for _ in range(n)]
    visited[r][c] = True
    count = 0
    if grid[r][c] != start_color:
        count += 1

    while q:
        cr, cc = q.popleft()
        for dr, dc in zip(drs, dcs):
            nr, nc = cr + dr, cc + dc
            if in_range(nr, nc, r, c) and not visited[nr][nc]:
                q.append((nr, nc))
                visited[nr][nc] = True
                if (abs(nr - r) + abs(nc - c)) % 2 == 0:
                    if grid[nr][nc] != start_color:
                        count += 1
                else:
                    if grid[nr][nc] == start_color:
                        count += 1
    return count

ans = float('inf')
for sr in range(n-8+1):
    for sc in range(m-8+1):
        ans = min(ans, bfs(sr,sc,0))
        ans = min(ans, bfs(sr,sc,1))
print(ans)