# Read 4x4 grid
grid = [list(map(int, input().split())) for _ in range(4)]

# Read direction
dir = input()

def compress(row):
    new_row = [num for num in row if num != 0]
    new_row += [0] * (4 - len(new_row))
    return new_row

def play(row):
    for i in range(3):
        if row[i] != 0 and row[i] == row[i+1]:
            row[i] *=2
            row[i+1] =0
    return row

def move_left(grid):
    for i in range(4):
        row = compress(grid[i])
        row = play(row)
        grid[i] = compress(row)
    return grid

def move_right(grid):
    for i in range(4):
        row = grid[i][::-1]
        row = compress(row)
        row = play(row)
        grid[i] = compress(row)[::-1]
    return grid

def move_up(grid):
    for j in range(4):
        col = [grid[i][j] for i in range(4)]
        col = compress(col)
        col = play(col)
        col = compress(col)
        for i in range(4):
            grid[i][j] = col[i]
    return grid

def move_down(grid):
    for j in range(4):
        col = [grid[i][j] for i in range(4)][::-1]
        col = compress(col)
        col = play(col)
        col = compress(col)
        col = col[::-1]
        for i in range(4):
            grid[i][j] = col[i]
    return grid

if dir == 'L':
    grid = move_left(grid)
elif dir == 'R':
    grid = move_right(grid)
elif dir == 'U':
    grid = move_up(grid)
elif dir == 'D':
    grid = move_down(grid)   

for r in grid:
    print(*r)
                       