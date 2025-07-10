n,m = map(int, input().split())

grid = [[0] * n for _ in range(n) ]


drs,dcs = [0,0,1,-1],[1,-1,0,0]

def in_range(r,c):
    return 0<=r<n and 0<=c<n

def check(r,c):
    count = 0
    for dr, dc in zip(drs,dcs):
        nr,nc = r+dr, c+dc
        if in_range(nr,nc) and grid[nr][nc] == 1:
            count+=1
    if count == 3:
        return 1
    return 0


for _ in range(m):
    r, c = map(int, input().split())
    r=r-1
    c=c-1
    grid[r][c] = 1
    print(check(r,c))




