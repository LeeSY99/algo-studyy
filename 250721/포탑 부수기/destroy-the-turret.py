'''n*m격자 모든 위치에 포탑
각 포탑 : 공격력 (변동가능)
    공격력 0이하가 되면 파괴
    애초에 0인 포탑 가능


각 턴(k번 반복)
    1. 공격자 선정
        기준
            공격력 가장 낮음
            가장 최근에 공격한 포탑
            포탑 행과 열의 합아 가장 큰 포탑
            포탑 위치의 열값이 가장 큰

        공격력 n+m만틈 증가
        
    2. 공격자의 공격
    자신을 제외한 가장 강한 포탑 공격
        기준
            공격력 가장 높음
            공격한지 가장 오래된 포탑
            행과 열의 합이 가장 작음
            열 값이 가장 작음

    레이저 공격
        레이저는 상하좌우 4방향
        부서진 포탑위로는 못지나감
        범위 밖일 시 반대푠으로 나옴
    우 하 좌 상 순으로 움직인 경로
    공격 성공시
        공격자의 공력력만큼 피해 
        피해 포탑은 그 수치만큼 공격력이 줄어듬
        레이저의 경로에 있는 포탑은 절반의 피해


    포탄 공격
        공격력만큼 피해
        주위 8방향에는 절반의 피해(공격자는 피해x)
            가장자리일 댸 반대격자에 영향 줌
    3. 포탑 부서짐 처리
    4. 포탑 정비
        부서지지 않은 포탑 중 공격과 무관한 포탑 +1


'''

n,m,k = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
class Tower:
    def __init__(self,r,c,power,la):
        self.power=power
        self.r = r
        self.c = c
        self.lastattack = la

def select_attacker():
    attacker = []
    for i in range(n):
        for j in range(m):
            if grid[i][j] > 0:
                tower = Tower(i,j,grid[i][j],lastattack[i][j])
                attacker.append(tower)
    attacker.sort(key = lambda x: (x.power,-x.lastattack, -(x.r+x.c), -x.c ))
    return attacker[0]

def select_strongest(attacker):
    strongest = []
    for i in range(n):
        for j in range(m):
            if grid[i][j] <= 0 or (i,j) == (attacker.r, attacker.c):
                continue
            tower = Tower(i,j,grid[i][j],lastattack[i][j])
            strongest.append(tower)
    strongest.sort(key = lambda x: (-x.power, x.lastattack, (x.r+x.c), x.c))
    return strongest[0]

from collections import deque

drs, dcs = [0,1,0,-1],[1,0,-1,0]
lastattack = [[0]*m for _ in range(n)]
def can_laserattack(rnd):
    s_r, s_c = strongest.r, strongest.c
    e_r, e_c = attacker.r, attacker.c

    effected[e_r][e_c] = 1
    lastattack[e_r][e_c] = rnd
    visited = [[0] * m for _ in range(n)]
    dist = [[n*m] * m for _ in range(n)]
    dist[s_r][s_c] = 0
    visited[s_r][s_c] = 1

    q = deque()
    q.append((s_r,s_c))
    while q:
        r, c = q.popleft()
        for dr, dc in zip(drs,dcs):
            nr, nc = (r+dr)%n, (c+dc)%m
            if not visited[nr][nc] and grid[nr][nc] > 0:
                visited[nr][nc] = 1
                q.append((nr,nc))
                dist[nr][nc] = dist[r][c]+1
    # print_that(visited)
    # print_that(dist)
    if visited[e_r][e_c] == 0:
        return False, []
    min_dist = dist[e_r][e_c]
    road = []
    while 1:
        for dr, dc in zip(drs,dcs):
            nr, nc = (e_r+dr)%n, (e_c+dc)%m
            if dist[nr][nc]<min_dist:
                min_dist = dist[nr][nc]
                e_r = nr
                e_c = nc
                break
        if (e_r,e_c) == (s_r,s_c):
            break
        road.append((nr,nc))
    return True, road

def laser_attack():
    # print(f'road: {road}')
    for r, c in road:
        grid[r][c] -= attacker.power//2
        effected[r][c] = 1
    grid[strongest.r][strongest.c] -= attacker.power
    effected[strongest.r][strongest.c] = 1

def bomb_attack():
    drs1, dcs1 = [-1,-1,0,1,1,1,0,-1],[0,1,1,1,0,-1,-1,-1]
    for dr, dc in zip(drs1,dcs1):
        nr, nc = (strongest.r+dr)%n, (strongest.c+dc)%m
        if (nr,nc) == (attacker.r,attacker.c):
            continue
        grid[nr][nc] -= attacker.power//2
        effected[nr][nc] = 1
    grid[strongest.r][strongest.c] -= attacker.power
    effected[strongest.r][strongest.c] = 1

def tower_break():
    for i in range(n):
        for j in range(m):
            if grid[i][j] <0:
                grid[i][j] = 0

def maintain_tower():
    for i in range(n):
        for j in range(m):
            if grid[i][j] > 0 and effected[i][j] == 0:
                grid[i][j] += 1
def print_that(a):
    for b in a:
        print(*b)
    print('-------')

def count_unbroken():
    count = 0
    for i in range(n):
        for j in range(m):
            if grid[i][j] > 0:
                count +=1
    return count

for r in range(1,k+1):
    if count_unbroken() == 1:
        break

    # print(f'{r}라운드')
    attacker = select_attacker()
    attacker.power += (n+m)
    grid[attacker.r][attacker.c] += (n+m)
    # print(f'공격자 {attacker.r}, {attacker.c}')
    # print_that(grid)

    strongest = select_strongest(attacker)

    effected =  [[0] * m for _ in range(n)]
    # can_laserattack(r)
    can_laser, road = can_laserattack(r)
    if can_laser:
        laser_attack()
    else:
        bomb_attack()

    # print_that(grid)
    tower_break()

    maintain_tower()
    # print_that(grid)

power = 0
for i in range(n):
    for j in range(m):
        if grid[i][j] > power:
            power = grid[i][j]
print(power)