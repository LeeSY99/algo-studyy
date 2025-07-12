'''좌표에 n개의 구슬
모든 구슬은 2초에 동일한 속도록 정해진 방향으로 움직임
진행도중 출돌시 영향력이 큰것만 남음 (무게가 가장 크거나, 같은게 여려개면 번호가 가장 클떄)
이동하는 도중에도 충돌이 일어남

가장 마지막으로 충돌이 일어난 시간'''

t = int(input())
balls = []
next_balls = []

next_ball_index = [[-1]*4001 for _ in range(4001)]

mapper = {'U':0, 'R':1, 'L':2, 'D':3}
def move(ball):
    dxs, dys = [0, 1, -1, 0], [1, 0, 0, -1]
    x,y,w,d,num = ball
    nx,ny = x+dxs[d] , y+dys[d]
    return (nx,ny,w,d,num)

#해당 좌표에 충돌인지
def find_collision(ball):
    x,y,_,_,_ = ball
    return next_ball_index[x][y]

#충돌 시 조건에 맞는 구슬 살아남음
def collision(ball1,ball2):
    _,_,weight1,_,num1 = ball1
    _,_,weight2,_,num2 = ball2

    if weight1>weight2 or (weight1==weight2 and num1>num2):
        return ball1
    else:
        return ball2

#구슬이 이미 격자를 벗어나면
def out_range(ball):
    x,y,_,_,_ = ball
    return x<0 or x>4000 or y<0 or y>4000

#다음 구슬 목록 반영
def push_next_ball(ball):
    global time
    if out_range(ball):
        return
    index = find_collision(ball)
    #구슬이 없으면 추가
    if index == -1:
        next_balls.append(ball)
        x,y,_,_,_ = ball
        next_ball_index[x][y] = len(next_balls) -1
    #있으면
    else:
        next_balls[index] = collision(next_balls[index], ball)
        time = curr_time

def simulate():
    global balls, next_balls
    for ball in balls:
        next_ball = move(ball)
        push_next_ball(next_ball)
    balls = next_balls[:]

    for x,y,_,_,_ in next_balls:
        next_ball_index[x][y] = -1

    next_balls = []

    



for _ in range(t):
    balls = []
    time = -1
    n = int(input())
    for i in range(1,n+1):
        x,y,w,d = tuple(input().split())
        x,y,w = int(x), int(y), int(w)

        #2초에 1칸이라 1초에 한칸으로 이동하게 바꿈
        x,y = x*2, y*2

        #좌표를 모두 양수로
        x +=2000
        y+=2000
        balls.append((x,y,w,mapper[d],i))

    #격자 크기만큼 이동하면 밖으로 나가게되어 결국은 충돌을 하지 않음
    for i in range(1, 4001):
        curr_time = i
        simulate()
    print(time)


    



