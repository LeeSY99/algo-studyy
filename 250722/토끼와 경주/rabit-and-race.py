''' 
1. 경주 준비
    n*m 격자 p마리 토끼
    토끼
        번호 pid_i, 움직여야 할 거리 d_i
    처음 모든 토끼는 1행 1열에 있음
2. 경주 진행
    k번 반복
    가장 우선순위 높은 토끼 -> 멀리 보내줌
    우선순위
        점프 횟수 적음
        현재 행+열 작음
        행 작음
        열 작음
        고유번호 작음
    상하좌우 4방향으로 d_i만큼 이동했을 때 위치
    격자를 벗어나면 방향 바꿔 한칸 이동
    4개 중 우선순위가 높은 곳으로 이동
    우선순위
        행 + 열 큼
        행 큼
        열 큼
    우선순위가 높은 칸의 위치를 (r_i, c_i), 나머지 토끼는 r_i+c_i만큼 점수를 동시에 얻음

k번 반복 후
    우선순위
        행 + 열 큼
        행 큼
        열 큼
        고유번호 큼
    단 1번이라도 경주한 토끼만 골라야 함
3. 이동거리 변경
    pid_t인 토끼의 이동거리를 L배
4. 최고의 토끼 선정
    가장 높은 점수 출력
    '''
import heapq
q = int(input())
rabbits = {}
class Rabbit:
    def __init__(self,id,dist):
        self.id = id
        self.r = 1
        self.c = 1
        self.dist = dist
        self.score = 0
        self.jump_count = 0
        self.last_jump = 0

def select_run_rabbit():
    while run_rabbits:
        jc, rc_sum, r, c, rid = heapq.heappop(run_rabbits)
        rabbit = rabbits[rid]
        if (jc, rc_sum, r, c) == (rabbit.jump_count, rabbit.r + rabbit.c, rabbit.r, rabbit.c):
            return rabbit

def in_range(r,c):
    return 0<r<=n and 0<c<=m

def bounce(pos, dist, limit):
    cycle = 2 * (limit-1)
    d = (pos-1+dist) % cycle #-1하는 이유는 0-based 맞추고
    if d < limit: #정방향
        return d+1  #여기서 다시 +1
    else:   # 역방향
        return 2 * limit - (d+1)

def select_best_position(rabbit,rnd):
    drs, dcs = [0,1,0,-1],[1,0,-1,0]
    positions = []
    for dr, dc in zip(drs,dcs):
        if dr != 0:
            new_r = bounce(rabbit.r, dr * rabbit.dist, n)
            new_c = rabbit.c
        else:
            new_r = rabbit.r
            new_c = bounce(rabbit.c, dc * rabbit.dist, m)
        heapq.heappush(positions,(-new_r-new_c, -new_r, -new_c))
    best_pos = positions[0]
    best_r = -best_pos[1]
    best_c = -best_pos[2]
    # print(rabbit.id)
    # print(best_r, best_c)
    # print('------')
    rabbit.r = best_r
    rabbit.c = best_c
    rabbit.jump_count += 1
    rabbit.last_jump = rnd
    priority = (rabbit.jump_count, rabbit.r+rabbit.c, rabbit.r, rabbit.c, rabbit.id)
    heapq.heappush(run_rabbits, priority)
    for r in rabbits.values():
        if r.id == rabbit.id:
            continue
        r.score += (best_r+best_c)
        # print(r.id, r.score)
        # print('---------')

def plus_score(s,rnd):
    compare = []
    for rabbit in rabbits.values():
        priority = (-(rabbit.r+rabbit.c), -rabbit.r, -rabbit.c, -rabbit.id)
        heapq.heappush(compare, priority)
    
    while compare:
        com = heapq.heappop(compare)
        plus_rabbit_id = -com[3]
        if rabbits[plus_rabbit_id].last_jump == rnd:
            rabbits[plus_rabbit_id].score += s
            break



run_rabbits = []
for rnd in range(q):
    to_do, *remain = map(int, input().split())
    to_do = int(to_do)
    if to_do == 100:
        n,m,p = remain[0], remain[1], remain[2]
        for i in range(p):
            id, dist = remain[3 + i*2], remain[4 + i*2]
            rabbit = Rabbit(id, dist)
            rabbits[id] = rabbit
            priority = (rabbit.jump_count, rabbit.r+rabbit.c, rabbit.r, rabbit.c, rabbit.id)
            heapq.heappush(run_rabbits, priority)
    elif to_do == 200:
        k, s = remain[0], remain[1]
        for _ in range(k):
            best_rabbit = select_run_rabbit()
            select_best_position(best_rabbit,rnd)
        plus_score(s,rnd)
    elif to_do == 300:
        pid, L = remain[0], remain[1]
        rabbits[pid].dist *= L
        # print(rabbits[pid].dist)
    elif to_do == 400:
        best_score = 0
        for rabbit in rabbits.values():
            best_score = max(best_score, rabbit.score)
        print(best_score)
