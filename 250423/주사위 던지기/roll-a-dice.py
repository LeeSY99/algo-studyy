n, m, r, c = map(int, input().split())
directions = list(input().split())

# Please write your code here.

grid = [[0] * n for _ in range(n)]

def in_range(r,c):
    return 0<=r<n and 0<=c<n

r,c = r-1,c-1
grid[r][c] = 6
#top north east west south bottom
dice = [1,5,3,4,2,6]

def move(dir):
    if dir == 'L':
        dice[0],dice[3],dice[5],dice[2] = dice[2],dice[0],dice[3],dice[5]
        # dr,dc = 0,-1
    elif dir == 'R':
        dice[0],dice[2],dice[5],dice[3] = dice[3],dice[0],dice[2],dice[5]
        # dr,dc = 0,1
    elif dir == 'U':
        dice[0],dice[1],dice[5],dice[4] = dice[4],dice[0],dice[1],dice[5]
        # dr,dc = -1,0
    else:
        dice[0],dice[4],dice[5],dice[1] = dice[1],dice[0],dice[4],dice[5]
        # dr,dc = 1,0
    return dice[5]
    
for dir in directions:
    if dir == 'L':
        dr,dc = 0,-1
    elif dir == 'R':
        dr,dc = 0,1
    elif dir == 'U':
        dr,dc = -1,0
    else:
        dr,dc = 1,0

    nr, nc = r+dr, c+dc
    if not in_range(nr,nc):
        continue
    r, c = nr,nc
    grid[r][c] = move(dir)

ans=0
for row in grid:
    ans += sum(row)
print(ans)