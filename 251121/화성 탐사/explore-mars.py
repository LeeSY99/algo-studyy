from collections import deque
n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

drs,dcs = [0,1,0,-1],[1,0,-1,0]
def in_range(r,c):
    return 0<=r<n and 0<=c<n

def bfs(r,c):
    dist = [[0] * n for _ in range(n)]
    q = deque([(r,c)])
    visited = [[False]*n for _ in range(n)]
    visited[r][c] = True

    while q:
        cr,cc = q.popleft()
        for dr,dc in zip(drs,dcs):
            nr, nc = cr+dr, cc+dc
            if in_range(nr,nc) and not visited[nr][nc] and grid[nr][nc] != -1:
                dist[nr][nc] = dist[cr][cc]+1
                visited[nr][nc] = True
                q.append((nr,nc))

    return dist

edges = []
for i in range(n):
    for j in range(n):
        if grid[i][j] == 1:
            start = (i,j)
        if grid[i][j] == 1 or grid[i][j] == 2:
            dist = bfs(i,j)
            start_node = i*n + j
            for ii in range(n):
                for jj in range(n):
                    if ii == i and jj == j:
                        continue
                    if grid[ii][jj] == 1 or grid[ii][jj] == 2:
                        end_node = ii*n + jj
                        if dist[ii][jj] == 0:
                            print(-1)
                            exit()
                        edges.append((start_node, end_node, dist[ii][jj]))

edges.sort(lambda x: x[2])
uf = [i for i in range(n*n)]

def union(a,b):
    A = find(a)
    B = find(b)
    if A == B:
        return
    uf[A] = B

def find(x):
    if uf[x] == x:
        return x
    uf[x] = find(uf[x])
    return uf[x]

ans = 0
for a,b,d in edges:
    if find(a) == find(b):
        continue
    union(a,b)
    ans += d
    
print(ans)                 


