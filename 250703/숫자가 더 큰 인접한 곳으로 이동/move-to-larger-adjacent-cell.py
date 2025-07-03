n, r, c = map(int, input().split())

grid = [list(map(int, input().split())) for _ in range(n)]

drs, dcs = [-1,1,0,0],[0,0,-1,1]

r-=1
c-=1

def in_range(r, c):
    return 0<=r<n and 0<=c<n
ans = []
while 1:
    max_num = 0
    now_num = grid[r][c]
    ans.append(now_num)
    for dr, dc in zip(drs, dcs):
        nr, nc = r+dr, c+dc
        if in_range(nr,nc) and grid[nr][nc]>now_num:
            next_r, next_c = nr, nc
            max_num = grid[nr][nc]
            break
    if max_num == 0:
        break
    r, c=next_r, next_c

for a in ans:
    print(a, end = ' ')




