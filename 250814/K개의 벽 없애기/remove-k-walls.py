from collections import deque
n, k = map(int, input().split())

grid = [list(map(int, input().split())) for _ in range(n)]
sr,sc = map(int, input().split())
sr-=1
sc-=1
er,ec = map(int, input().split())
er-=1
ec-=1

walls = []
for i in range(n):
    for j in range(n):
        if grid[i][j] == 1:
            walls.append((i,j))
drs, dcs = [0,0,1,-1],[1,-1,0,0]
def in_range(r,c):
    return 0<=r<n and 0<=c<n

def search():
    new_grid = [g[:] for g in grid]
    for i,j in selected_wall:
        new_grid[i][j] = 0
    q = deque()
    q.append((sr,sc))
    visited = [[float('inf')] * n for _ in range(n)]
    visited[sr][sc] = 0

    while q:
        r, c = q.popleft()
        for dr, dc in zip(drs,dcs):
            nr, nc = r+dr, c+dc
            if in_range(nr,nc) and new_grid[nr][nc] == 0 and visited[r][c] + 1 < visited[nr][nc]:
                q.append((nr,nc))
                visited[nr][nc] = visited[r][c] + 1
    # print(selected_wall)
    # for g in new_grid:
    #     print(*g)
    # for d in visited:
    #     print(*d)
    # print('-----')
    
    return visited[er][ec]

ans = float('inf')
selected_wall = []
def select_wall(index, count):
    global ans
    if index == len(walls):
        if count == k:
            dist = search()
            ans = min(ans,dist)
        return
    
    
    selected_wall.append(walls[index])
    select_wall(index+1 ,count + 1)
    selected_wall.pop()
    select_wall(index+1 ,count)


select_wall(0,0)
if ans == float('inf'):
    ans = -1
print(ans)

