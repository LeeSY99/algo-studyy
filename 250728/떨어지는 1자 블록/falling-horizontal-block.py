n,m,k = map(int, input().split())

grid = [list(map(int, input().split())) for _ in range(n)]

sj = k-1
ej = k-1+m-1
def in_range(r,c):
    return 0<=r<n and 0<=c<n

for i in range(n):
    ok = True
    for j in range(sj, ej+1):
        
        if in_range(i+1,j) and grid[i+1][j] == 1:
            ok = False

    if not ok or i == n-1:
        for j in range(sj, ej+1):
            grid[i][j] = 1
        break

for a in grid:
    print(*a)