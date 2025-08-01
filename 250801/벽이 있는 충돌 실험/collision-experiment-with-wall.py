t = int(input())

direction = {'U' : 0, 'R':1, 'D':2, 'L':3}
dxs, dys = [-1,0,1,0],[0,1,0,-1]

def in_range(r,c,n):
    return 0<=r<n and 0<=c<n
for _ in range(t):
    n,m = map(int, input().split())
    balls = []
    for tc in range(m):
        x,y,d = input().split()
        x = int(x)-1
        y = int(y)-1
        
        balls.append((x,y,direction[d]))

    for i in range(2*n):
        grid = [[0] * n for _ in range(n)]
        for i, (x,y,d) in enumerate(balls):
            nx,ny = x+dxs[d], y+dys[d]
            if in_range(nx,ny,n):
                grid[nx][ny] += 1
                balls[i] = (nx,ny,d)
            else:
                grid[x][y] += 1
                balls[i] = (x,y,(d+2)%4)
        
        remain_ball = []
        for i, (x,y,d) in enumerate(balls):
            if grid[x][y] == 1:
                remain_ball.append(balls[i])

        balls = remain_ball
    # print(balls)
    print(len(balls))


