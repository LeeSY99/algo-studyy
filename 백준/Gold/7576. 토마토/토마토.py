from collections import deque
m,n = map(int, input().split())

grid = [list(map(int, input().split())) for _ in range(n)]
all_box = 0
for i in range(n):
    for j in range(m):
        if grid[i][j] != -1:
            all_box += 1
def in_range(i,j):
    return 0<=i<n and 0<=j<m
dis, djs = [0,1,0,-1],[1,0,-1,0]


tomato = [[0] * m for _ in range(n)]
visited = [[False]*m for _ in range(n)]

def bfs():
    q = deque()
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 1:
                q.append((i,j))
                visited[i][j] = True

    while q:
        ci, cj = q.popleft()
        for di, dj in zip(dis, djs):
            ni,nj = ci+di, cj+dj
            if in_range(ni,nj) and not visited[ni][nj] and grid[ni][nj] == 0:
                tomato[ni][nj] = tomato[ci][cj] + 1
                q.append((ni, nj))
                visited[ni][nj] = True

all_tomato = True
ans = 0
bfs()
for i in range(n):
    for j in range(m):
        if grid[i][j] == -1:
            continue
        if grid[i][j] == 0 and tomato[i][j] == 0:
            all_tomato = False
        else:
            ans = max(ans, tomato[i][j])

# for t in tomato:
#     print(*t)
if all_tomato:
    print(ans)
else:
    print(-1)
