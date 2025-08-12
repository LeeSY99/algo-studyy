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

ans = 0
from collections import deque
import copy
def check():
    global ans
    now_grid = copy.deepcopy(grid)
    for rock_r, rock_c in removed_rock:
        now_grid[rock_r][rock_c] = 0
    
    visited = [[0]*n for _ in range(n)]
    q = deque()
    for sr, sc in start:
        visited[sr][sc]=1
        q.append((sr,sc))
    
    count = 0
    while q:
        nowr, nowc = q.popleft()
        count += 1
        for dr, dc in zip(drc, dcc):
            nr, nc = nowr+dr, nowc+dc
            if in_range(nr, nc) and not visited[nr][nc] and not now_grid[nr][nc]:
                visited[nr][nc]=1
                q.append((nr, nc))
    ans = max(ans, count)

backtrack(0,0)
print(ans)


    

