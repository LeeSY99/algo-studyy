n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]
r, c, m1, m2, m3, m4, dir = map(int, input().split())

# Please write your code here.

temp = grid[r-1][c-1]
nowx, nowy = r-1,c-1

if dir:#시계방향
    dx,dy = [-1,-1,1,1],[1,-1,-1,1]

    #1번구간
    x,y = dx[0],dy[0]
    for i in range(m1):
        nextx,nexty = nowx+x, nowy+y
        grid[nowx][nowy] = grid[nextx][nexty]
        nowx, nowy = nextx, nexty

    #2번구간
    x,y = dx[1],dy[1]
    for i in range(m2):
        nextx,nexty = nowx+x, nowy+y
        grid[nowx][nowy] = grid[nextx][nexty]
        nowx, nowy = nextx, nexty

    #3번구간
    x,y = dx[2],dy[2]
    for i in range(m3):
        nextx,nexty = nowx+x, nowy+y
        grid[nowx][nowy] = grid[nextx][nexty]
        nowx, nowy = nextx, nexty

    #4번구간:
    for i in range(m4-1):
        nextx,nexty = nowx+x, nowy+y
        grid[nowx][nowy] = grid[nextx][nexty]
        nowx, nowy = nextx, nexty
    grid[nowx][nowy] = temp

else: #반시계
    dx,dy = [-1,-1,1,1],[-1,1,1,-1]

    #4번구간
    x,y = dx[0],dy[0]
    for i in range(m4):
        nextx,nexty = nowx+x, nowy+y
        grid[nowx][nowy] = grid[nextx][nexty]
        nowx, nowy = nextx, nexty
    
    #3
    x,y = dx[1],dy[1]
    for i in range(m3):
        nextx,nexty = nowx+x, nowy+y
        grid[nowx][nowy] = grid[nextx][nexty]
        nowx, nowy = nextx, nexty

    #2
    x,y = dx[2],dy[2]
    for i in range(m2):
        nextx,nexty = nowx+x, nowy+y
        grid[nowx][nowy] = grid[nextx][nexty]
        nowx, nowy = nextx, nexty

    #1
    x,y = dx[3],dy[3]
    for i in range(m1-1):
        nextx,nexty = nowx+x, nowy+y
        grid[nowx][nowy] = grid[nextx][nexty]
        nowx, nowy = nextx, nexty
    grid[nowx][nowy] = temp
    
for row in grid:
    print(*row)



