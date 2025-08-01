''' n*n격자 m개 구슬
1초에 움직일 수 있는 칸

벽에 부딪히면 방향 반대, 전환 시간소요 x
매 초
    구슬 움직임, 같은 위치 여러구슬 가능

    같은 위치에 k개가 넘는다면 우선순위 높은 구슬 k
        속도가 빠를수록,
        번호가 높을수록
'''
from collections import defaultdict
direction = {'U' : 0, 'R':1, 'D':2, 'L':3}
drs, dcs = [-1,0,1,0],[0,1,0,-1]
import heapq
class Ball:
    def __init__(self,i,r,c,d,v):
        self.id = i
        self.r = r
        self.c = c
        self.d = d
        self.speed = v
        self.is_alive = True

    def __lt__(self,other):
        if self.speed != other.speed:
            return self.speed < other.speed
        if self.id != other.id:
            return self.id < other.id

n,m,t,k = map(int, input().split())
grid = [[[] for _ in range(n)] for _ in range(n)]
balls = []

for i in range(1,m+1):
    r,c,d,v = input().split()
    r = int(r)-1
    c = int(c)-1
    d = direction[d]
    v = int(v)
    ball = Ball(i,r,c,d,v)
    balls.append(ball)

def bounce(pos, dir, dist, limit):
     # {'U' : 0, 'R':1, 'D':2, 'L':3}
    sign = 1 if dir in (1,2) else -1
    cycle = 2*(limit-1)
    d = (pos+ sign * dist) % cycle
    if d<limit: #정방향
        return d, dir
    else:
        return cycle - d, (dir+2)%4 #역방향

def move():
    global grid
    grid = [[[] for _ in range(n)] for _ in range(n)]
    for ball in balls:
        if ball.is_alive == False:
            continue
        r, c = ball.r, ball.c
        d = ball.d
        speed = ball.speed

        dr, dc = drs[d], dcs[d]
        if dr == 0:
            next_r = r
            next_c, new_d = bounce(c,d,speed,n)
        else:
            next_r, new_d  = bounce(r,d,speed,n)
            next_c = c

        ball.d = new_d
        ball.r = next_r
        ball.c = next_c
        # print(f'({r},{c}) -> ({next_r},{next_c}) speed:{speed} dir: {d} -> {new_d}')
        # {'U' : 0, 'R':1, 'D':2, 'L':3}
        heapq.heappush(grid[next_r][next_c],ball )
    

def check():
    for i in range(n):
        for j in range(n):
            if len(grid[i][j]) > k:
                while len(grid[i][j]) > k:
                    del_ball = heapq.heappop(grid[i][j])
                    del_ball.is_alive = False

def print_that(that):
    for a in that:
        print(a)
    print('-----------')

for time in range(t):
    move()
    # print_that(grid)
    check()

ans = 0
for ball in balls:
    if ball.is_alive:
        ans+=1

print(ans)
    
        

