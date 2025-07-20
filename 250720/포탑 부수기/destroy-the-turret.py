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
def in_range(r,c):
    return 0<=r<n and 0<=c<m
drs, dcs = [0,1,0,-1],[1,0,-1,0]
lastattack = [[0]*m for _ in range(n)]
def attack(r):
    #레이저
    s_r, s_c = strongest.r, strongest.c
    e_r, e_c = attacker.r, attacker.c

    lastattack[e_r][e_c ] = r
    effected[e_r][e_c] = 1
    visited = [[0]*m for _ in range(n)]
    dist = [[n*m]*m for _ in range(n)]
    visited[s_r][s_c] = 1
    dist[s_r][s_c] = 0

    while 1:
        
        q = deque()
        q.append((s_r,s_c))
        while q:
            r, c = q.popleft()
            for dr, dc in zip(drs,dcs):
                nr, nc = (r+dr)%n, (c+dc)%m
                if not visited[nr][nc] and grid[nr][nc]>0:
                    visited[nr][nc] = 1
                    q.append((nr,nc))
                    dist[nr][nc] = dist[r][c] + 1
        min_dist = n*m
        for dr, dc in zip(drs,dcs):
            nr, nc = (e_r+dr)%n, (e_c+dc)%m
            if dist[nr][nc] < min_dist:
                min_dist = dist[nr][nc]
                next_r = nr
                next_c = nc
        if min_dist == n*m:
            break
        else:
            e_r = next_r
            e_c = next_c
            effected[e_r][e_c] = 1
            if (s_r,s_c) == (e_r,e_c):
                grid[e_r][e_c] -= attacker.power
                return
            grid[e_r][e_c] -= attacker.power//2
        
    #포탄
    grid[s_r][s_c] -= attacker.power
    for dr, dc in zip ((-1,-1,0,1,1,1,0,-1),
                        (0,1,1,1,0,-1,-1,-1)):
        nr, nc = (s_r+dr)%n, (s_c+dc)%m
        if (nr,nc) == (e_r,e_c):
            continue
        effected[nr][nc] = 1
        grid[nr][nc] -= attacker.power//2

    

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
    # print(attacker.r, attacker.c)
    # print_that(grid)

    strongest = select_strongest(attacker)
    # print(strongest.r, strongest.c)
    
    effected = [[0]*m for _ in range(n)]
    attack(r)
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