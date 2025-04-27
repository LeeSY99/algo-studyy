n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.

def in_range(r,c):
    return 0<=r<n and 0<=c<n

ans = 0
#1열 down
for j in range(n):
    time = 0
    r,c = 0,j
    dr, dc = 1, 0
    while True:
        time+=1
        if not in_range(r,c):
            ans = max(ans, time)
            break
        if grid[r][c] == 0:
            r,c = r+dr, c+dc
            continue
        elif grid[r][c] ==1:
            dr, dc = -dc, -dr
            r,c = r+dr, c+dc
        elif grid[r][c] == 2:
            dr, dc = dc, dr
            r,c = r+dr, c+dc
#우측 left
for j in range(n):
    time = 0
    r,c = j,n-1
    dr, dc = 0, -1
    while True:
        time+=1
        if not in_range(r,c):
            ans = max(ans, time)
            break
        if grid[r][c] == 0:
            r,c = r+dr, c+dc
            continue
        elif grid[r][c] ==1:
            dr, dc = -dc, -dr
            r,c = r+dr, c+dc
        elif grid[r][c] == 2:
            dr, dc = dc, dr
            r,c = r+dr, c+dc
#아래 up
for j in range(n):
    time = 0
    r,c = n-1,j
    dr, dc = -1, 0
    while True:
        time+=1
        if not in_range(r,c):
            ans = max(ans, time)
            break
        if grid[r][c] == 0:
            r,c = r+dr, c+dc
            continue
        elif grid[r][c] ==1:
            dr, dc = -dc, -dr
            r,c = r+dr, c+dc
        elif grid[r][c] == 2:
            dr, dc = dc, dr
            r,c = r+dr, c+dc
#좌측 right
for j in range(n):
    time = 0
    r,c = j,0
    dr, dc = 0, 1
    while True:
        time+=1
        if not in_range(r,c):
            ans = max(ans, time)
            break
        if grid[r][c] == 0:
            r,c = r+dr, c+dc
            continue
        elif grid[r][c] ==1:
            dr, dc = -dc, -dr
            r,c = r+dr, c+dc
        elif grid[r][c] == 2:
            dr, dc = dc, dr
            r,c = r+dr, c+dc

print(ans)
