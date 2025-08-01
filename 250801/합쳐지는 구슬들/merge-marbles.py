n, m, t = map(int, input().split())

balls = []
grid = [[-1]*(n+1) for _ in range(n+1)]

direction = {'U':0, 'R':1, 'D':2, 'L':3}
for i in range(1,m+1):
    r,c,d,w = input().split()
    r = int(r)
    c=int(c)
    w=int(w)
    d = direction[d]
    balls.append((r,c,d,w,i))

drs, dcs = [-1,0,1,0],[0,1,0,-1]
def in_range(r,c):
    return 0<r<=n and 0<c<=n

def move(ball):
    global grid
    
    r,c,d,w,i = ball
    nr, nc = r+drs[d], c+dcs[d]
    if in_range(nr, nc):
        return (nr,nc,d,w,i)
    else:
        return (r,c,(d+2)%4,w,i)

def find_collision(ball):
    r,c,_,_,_ = ball
    return grid[r][c]

def collision(ball1,ball2):
    r1,c1,d1,weight1,i1 = ball1
    r2,c2,d2,weight2,i2 = ball2
    if i1>i2:
        return (r1,c1,d1,weight1+weight2,i1)
    else:
        return (r2,c2,d2,weight1+weight2,i2)

next_balls = []
def push_ball(ball):
    index = find_collision(ball)
    if index == -1:
        next_balls.append(ball)
        r,c,_,_,_ = ball
        grid[r][c] = len(next_balls) - 1

    else:
        next_balls[index] = collision(next_balls[index],ball)

def simulate():
    global balls, next_balls
    for ball in balls:
        next_ball = move(ball)
        push_ball(next_ball)
    balls = next_balls[:]

    for r,c,_,_,_ in next_balls:
        grid[r][c] = -1

    next_balls=[]


for time in range(t):
    simulate()

max_weight = 0
# print(balls)
for ball in balls:
    _,_,_,w,_ = ball
    max_weight = max(max_weight,w)
print(len(balls), max_weight)
    