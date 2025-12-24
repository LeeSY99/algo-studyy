from collections import deque
n,m = map(int, input().split())

grid = [list(map(int, input().split())) for _ in range(n)]
def in_range(r,c):
    return 0<=r<n and 0<=c<m

drs, dcs = [0,1,0,-1],[1,0,-1,0]

def check_out():

    q = deque()
    q.append((0,0))

    while q:
        r,c = q.popleft()
        for dr, dc in zip(drs, dcs):
            nr, nc = r+dr, c+dc
            if in_range(nr,nc) and grid[nr][nc] == 0:
                grid[nr][nc] = 2
                q.append((nr,nc))


def melt():
    global new_grid
    for r in range(n):
        for c in range(m):
            if new_grid[r][c] == 1:
                count = 0
                for dr, dc in zip(drs,dcs):
                    nr, nc = r+dr, c+dc
                    if in_range(nr,nc) and grid[nr][nc] == 2:
                        count += 1
                if count >= 2:
                    new_grid[r][c] = 0

def change():
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 2:
                grid[i][j] = 0



time = 0
while True:
    new_grid = [g[:] for g in grid]
    time += 1
    check_out()
    # for g in grid:
    #     print(*g)
    melt()
    change()
    # print(time)
    # for g in grid:
    #     print(*g)
    # print('---')
    # for g in new_grid:
    #     print(*g)
    # break
    if grid == new_grid:
        break
    else:
        grid = new_grid

print(time-1)