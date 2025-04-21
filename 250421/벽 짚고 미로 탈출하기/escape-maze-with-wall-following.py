N = int(input())
x, y = map(int, input().split())

grid = [["."] * (N + 1) for _ in range(N + 1)]
for i in range(1, N + 1):
    row = input()
    for j in range(1, N + 1):
        grid[i][j] = row[j - 1]

# Please write your code here.

dx, dy = [1,0,-1,0], [0,-1,0,1]

def in_range(r,c):
    return 0<r<=N and 0<c<=N

def solve():
    global x,y
    time = 0
    i = 0
    x,y = y,x
    while 1:
        time+=1
        grid[y][x]=0
        while 1:
            count = 0
            if in_range(x+dx[i], y+dy[i]):
                if grid[y+dy[i]][x+dx[i]] == '#':
                    count+=1
                    i = (i+1) % 4
                    if count>=4:
                        return -1
                elif grid[y+dy[i]][x+dx[i]] == '.':
                    x = x+dx[i]
                    y = y+dy[i]
                    nextx = x+ dx[(i-1)%4]
                    nexty = y+ dy[(i-1)%4]
                    if in_range(nextx,nexty) and grid[nexty][nextx] != '#':
                        i = (i-1)%4
                    break
                elif grid[y+dy[i]][x+dx[i]] == 0:
                    return -1
            else:
                return time

print(solve())
    
