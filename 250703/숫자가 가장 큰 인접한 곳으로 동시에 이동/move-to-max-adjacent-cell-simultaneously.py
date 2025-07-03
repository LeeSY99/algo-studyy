n,m,t = map(int, input().split())

grid = [list(map(int, input().split())) for _ in range(n)]

drs, dcs = [-1,1,0,0],[0,0,-1,1]
start = []
for _ in range(m):
    r, c = map(int, input().split())
    start.append((r-1,c-1))

def in_range(r,c):
    return 0<=r<n and 0<=c<n

for i in range(t):
    new_grid = [[0]*n for _ in range(n)]
    for r, c in start:
        now_val = 0
        for dr, dc in zip(drs, dcs):
            nr, nc = r+dr, c+dc
            if in_range(nr,nc) and grid[nr][nc]>now_val:
                now_val = grid[nr][nc]
                next_r, next_c = nr, nc
        new_grid[next_r][next_c] += 1
    start = []
    count = 0
    for r in range(n):
        for c in range(n):
            if new_grid[r][c] == 1:
                start.append((r,c))
                count+=1

print(count)

    