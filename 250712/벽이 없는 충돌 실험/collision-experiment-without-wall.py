'''좌표에 n개의 구슬
모든 구슬은 2초에 동일한 속도록 정해진 방향으로 움직임
진행도중 출돌시 영향력이 큰것만 남음 (무게가 가장 크거나, 같은게 여려개면 번호가 가장 클떄)
이동하는 도중에도 충돌이 일어남

가장 마지막으로 충돌이 일어난 시간'''

T = int(input())

def move(ball):
    after = {}
    for (x,y),(w,d) in ball.items():
        if d == 'U':
            y+=0.5
        elif d=='D':
            y-=0.5
        elif d=='R':
            x+=0.5
        else:
            x-=0.5
        if (x,y) not in after or after[(x,y)][0] <=w:
            after[(x,y)] = (w,d)
    return after


for _ in range(T):
    n = int(input())
    ball = {}
    for c in range(n):
        x,y,w,d =  input().split()
        x,y,w = int(x), int(y), int(w)
        ball[(x,y)] = (w,d)
    time = 0
    while 1:
        after=move(ball)
        after=move(after)
        if len(ball) == len(after):
            if time == 0:
                print(-1)
                break
            print(time)
            break
        else:
            ball = after
            time +=2
        
    



