n = int(input())

grid = [list(map(int, input().split())) for _ in range(n)]

drs, dcs = [0,1,0,-1],[1,0,-1,0]
ans = 0
for i in range(n):
    for j in range(n):
        ans = max(ans, grid[i][j])
def roll(grid,time):
    global ans
    if time == 5:
        # for g in grid:
        #     print(*g)
        # print()
        return
    #up
    new_grid = [g[:] for g in grid]
    mixed = [[False] * n for _ in range(n)]
    for j in range(n):
        ni = 0
        for i in range(n):
            if new_grid[i][j] == 0:
                continue
            new_grid[ni][j] = new_grid[i][j]
            if ni != i:
                new_grid[i][j] = 0
            if ni > 0 and not mixed[ni-1][j] and new_grid[ni-1][j] == new_grid[ni][j]:
                new_grid[ni-1][j] *= 2
                new_grid[ni][j] = 0
                mixed[ni-1][j] = True
                ans = max(ans, new_grid[ni-1][j])
            else:
                ni += 1
    roll(new_grid, time + 1)

    # right
    new_grid = [g[:] for g in grid]
    mixed = [[False] * n for _ in range(n)]
    for i in range(n):
        nj = n-1
        for j in range(n-1,-1,-1):
            if new_grid[i][j] == 0:
                continue
            new_grid[i][nj] = new_grid[i][j]
            if nj != j:
                new_grid[i][j] = 0
            if nj < n-1 and not mixed[i][nj+1] and new_grid[i][nj+1] == new_grid[i][nj]:
                new_grid[i][nj+1] *= 2
                new_grid[i][nj] = 0
                mixed[i][nj+1] = True
                ans = max(ans, new_grid[i][nj+1])
            else:
                nj -= 1
    roll(new_grid, time + 1)

    #down
    new_grid = [g[:] for g in grid]
    mixed = [[False] * n for _ in range(n)]
    for j in range(n):
        ni = n-1
        for i in range(n-1,-1,-1):
            if new_grid[i][j] == 0:
                continue
            new_grid[ni][j] = new_grid[i][j]
            if ni != i:
                new_grid[i][j] = 0
            if ni < n-1 and not mixed[ni+1][j] and new_grid[ni+1][j] == new_grid[ni][j]:
                new_grid[ni+1][j] *= 2
                new_grid[ni][j] = 0
                mixed[ni+1][j] = True
                ans = max(ans, new_grid[ni+1][j])
            else:
                ni -= 1
    roll(new_grid, time + 1)

    # left
    new_grid = [g[:] for g in grid]
    mixed = [[False] * n for _ in range(n)]
    for i in range(n):
        nj = 0
        for j in range(n):
            if new_grid[i][j] == 0:
                continue
            new_grid[i][nj] = new_grid[i][j]
            if nj != j:
                new_grid[i][j] = 0
            if nj > 0 and not mixed[i][nj-1] and new_grid[i][nj-1] == new_grid[i][nj]:
                new_grid[i][nj-1] *= 2
                new_grid[i][nj] = 0
                mixed[i][nj-1] = True
                ans = max(ans, new_grid[i][nj-1])
            else:
                nj += 1
    roll(new_grid, time + 1)

roll(grid, 0)
print(ans)




