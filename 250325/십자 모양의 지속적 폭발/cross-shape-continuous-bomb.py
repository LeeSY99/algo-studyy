n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
commands = [int(input()) for _ in range(m)]

# Please write your code here.
def in_range(i,j):
    return 0<=i<n and 0<=j<n

def gravity(grid):
    for j in range(n):
        col = [grid[i][j] for i in range(n)]
        col = [num for num in col if num != 0]
        new_col = [0] * (n-len(col))
        new_col += col
        for i in range(n):
            grid[i][j] = new_col[i]
    return grid


def solve(grid):
    for c in commands:
        c=c-1
        for r in range(n):
            if r == n-1 and grid[r][c]==0:
                return grid
            if grid[r][c] != 0:
                time = grid[r][c]
                i,j = r,c
                break
        for t in range(time):
            if in_range(r+t,c):
                grid[r+t][c] = 0
            if in_range(r,c+t):
                grid[r][c+t] = 0
            if in_range(r-t,c):
                grid[r-t][c] = 0
            if in_range(r,c-t):
                grid[r][c-t] = 0
        grid = gravity(grid)
    return grid

grid = solve(grid)
for row in grid:
    print(*row)


