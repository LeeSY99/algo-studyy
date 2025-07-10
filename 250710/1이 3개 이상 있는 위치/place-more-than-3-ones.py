n = int(input())

grid = [list(map(int, input().split())) for _ in range(n)]

def in_range(r,c):
    return 0<=r<n and 0<=c<n

drs,dcs = [0,0,1,-1],[1,-1,0,0]
ans = 0
for r in range(n):
    for c in range(n):
        count = 0
        for dr, dc in zip(drs,dcs):
            nr, nc = r+dr, c+dc
            if in_range(nr,nc) and grid[nr][nc] == 1:
                count+=1
        if count >=3:
            ans+=1
print(ans)