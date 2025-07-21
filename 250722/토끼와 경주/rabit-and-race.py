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

def select_run_rabbit():
    run_rabbits = []
    for rabbit in rabbits.values():
        priority = (rabbit.jump_count, rabbit.r+rabbit.c, rabbit.r, rabbit.c, rabbit.id)
        heapq.heappush(run_rabbits, priority)
    # print(run_rabbits)
    id =  run_rabbits[0][-1]
    # print(id)
    return rabbits[id]

def in_range(r,c):
    return 0<r<=n and 0<c<=m

def select_best_position(rabbit):
    drs, dcs = [0,1,0,-1],[1,0,-1,0]
    distance = rabbit.dist
    positions = []
    for d in range(4):
        r = rabbit.r
        c = rabbit.c
        nr,nc = r,c
        for _ in range(1, distance+1):
            nr += drs[d] 
            nc += dcs[d]
            if not in_range(nr,nc):
                d = (d+2)%4
                nr += 2*drs[d] 
                nc += 2*dcs[d]
        heapq.heappush(positions,(-nr-nc, -nr, -nc))
    best_pos = positions[0]
    best_r = -best_pos[1]
    best_c = -best_pos[2]
    # print(rabbit.id)
    # print(best_r, best_c)
    # print('------')
    rabbit.r = best_r
    rabbit.c = best_c
    rabbit.jump_count += 1
    for r in rabbits.values():
        if r.id == rabbit.id:
            continue
        r.score += (best_r+best_c)
        # print(r.id, r.score)
        # print('---------')

def plus_score(s):
    compare = []
    for rabbit in rabbits.values():
        priority = (-(rabbit.r+rabbit.c), -rabbit.r, -rabbit.c, -rabbit.id)
        heapq.heappush(compare, priority)
    
    for com in compare:
        plus_rabbit_id = -com[3]
        if rabbits[plus_rabbit_id].jump_count == 0:
            continue
        rabbits[plus_rabbit_id].score += s
        # print(plus_rabbit_id,rabbits[plus_rabbit_id].score)
        # print('-------')
        break

def jump_count_zero():
    for rabbit in rabbits.values():
        rabbit.jump_count = 0 

for _ in range(q):
    to_do, *remain = map(int, input().split())
    to_do = int(to_do)
    if to_do == 100:
        n,m,p = remain[0], remain[1], remain[2]
        for i in range(p):
            id, dist = remain[3 + i*2], remain[4 + i*2]
            rabbit = Rabbit(id, dist)
            rabbits[id] = rabbit
    elif to_do == 200:
        k, s = remain[0], remain[1]
        for _ in range(k):
            best_rabbit = select_run_rabbit()
            select_best_position(best_rabbit)
        plus_score(s)
        jump_count_zero()
    elif to_do == 300:
        pid, L = remain[0], remain[1]
        rabbits[pid].dist *= L
        # print(rabbits[pid].dist)
    elif to_do == 400:
        best_score = 0
        for rabbit in rabbits.values():
            best_score = max(best_score, rabbit.score)
        print(best_score)
