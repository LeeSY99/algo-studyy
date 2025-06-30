n, k, m = map(int, input().split())

grid = [list(map(int, input().split())) for _ in range(n)]
start = []
for _ in range(k):
    r, c = map(int, input().split())
    start.append((r-1,c-1))

rock = []
for i in range(n):
    for j in range(n):
        if grid[i][j]:
            rock.append((i,j))

removed_rock = []
def backtrack(index, count):
    if index == len(rock):
        if count == m:
            check()
        return
    removed_rock.append(rock[index])
    backtrack(index+1, count +1)
    removed_rock.pop()

    backtrack(index+1, count)
    

def in_range(r,c):
    return 0<=r<n and 0<=c<n

drc, dcc = [0,1,0,-1],[1,0,-1,0]
def bfs(q,visited,now_grid):
    count=1
    while q:
        nowr, nowc = q.popleft()
        for dr, dc in zip(drc, dcc):
            nr, nc = nowr+dr, nowc+dc
            if in_range(nr, nc) and not visited[nr][nc] and not now_grid[nr][nc]:
                visited[nr][nc]=1
                count+=1
                q.append((nr, nc))
    return visited


ans = 0
from collections import deque
import copy
def check():
    global ans
    now_grid = copy.deepcopy(grid)
    for rock_r, rock_c in removed_rock:
        now_grid[rock_r][rock_c] = 0
    all_visited = [[0]*n for _ in range(n)]
    for sr, sc in start:
        q = deque()
        q.append((sr,sc))
        visited = [[0]*n for _ in range(n)]
        visited[sr][sc]=1
        visited = bfs(q,visited,now_grid)
        for a in range(n):
            for b in range(n):
                if visited[a][b]:
                    all_visited [a][b] = 1
    count = 0
    for a in range(n):
        for b in range(n):
            if all_visited[a][b]:
                count+=1
    ans = max(ans, count)


    

backtrack(0,0)
print(ans)


    

