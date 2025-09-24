n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

def in_range(r,c):
    return 0<=r<n and 0<=c<n

drs, dcs = [0,1,0,-1],[1,0,-1,0]

def check(r,c):
    if grid[r-1][c] == 0:
        return True
    return False

def flip(r,c):
    grid[r][c] ^= 1
    for dr, dc in zip(drs,dcs):
        nr,nc = r+dr, c+dc
        if in_range(nr,nc):
            grid[nr][nc] ^= 1

cnt = 0
for i in range(1,n):
    for j in range(n):
        if check(i,j):
            flip(i,j)
            cnt += 1

def printans():
    for i in range(n):
        for j in range(n):
            if grid[i][j] == 0:
                return -1
    
    return cnt
print(printans())
