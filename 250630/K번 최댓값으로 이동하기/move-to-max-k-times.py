n, k =  map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
r, c = map(int, input().split())


def in_range(r, c):
    return 0<=r<n and 0<=c<n

drc, dcc = [0,1,0,-1],[1,0,-1,0]

def bfs(q, value):
    global max_val
    while q:
        now_r, now_c = q.popleft()
        
        for dr, dc in zip(drc, dcc):
            n_r, n_c = now_r + dr, now_c + dc
            if in_range(n_r, n_c) and grid[n_r][n_c] < value and not visited[n_r][n_c]:
                visited[n_r][n_c]=1
                max_val = max(max_val, grid[n_r][n_c])
                q.append((n_r,n_c))

from collections import deque    
r-=1
c-=1

for k in range(k):
    q = deque()
    q.append((r,c))
    visited = [[0]*n for _ in range(n)]
    max_val = 0
    bfs(q, grid[r][c])
    ok = False

    if max_val == 0:
        break

    for i in range(n):
        for j in range(n):
            if grid[i][j] == max_val and visited[i][j]:
                ok=True
                r = i
                c = j
                break
        if ok:
            break
    
print(r+1, c+1)
    
    