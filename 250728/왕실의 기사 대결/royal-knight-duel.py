''' L*L 체스판 (1,1)로 시작
기사 - 상대를 밀쳐냄
    초기 위치 (r,c),
    체력 k
    방패: (r,c)를 좌측상단으로 h * w직사각형 형태 
    
1) 기사 이동 ->O(n * )
    상하좌우 한칸 이동
    다른기사가 있으면 그 기사도 밀려남 연쇄적으로 계속
    벽이 있으면 이동하지 못함
    사라진 기사에게 명령 내릴시 반응 없음
    
2) 대결 대미지 -> L^3*N*Q 그래서 prefix_sum으로 데미지 계산
    기사가 다른 기사를 밀치면 데미지
    기사가 이동한 곳에서 w*h 내에 있는 함정의 수만큼 피해
    체력 0이면 체스판에서 사라짐
    명령받은 기사는 데미지 없음
    기사는 모두 밀린 후 데미지
    
->생존한 기사들이 받은 데미지 합 출력'''


l,n,q=map(int, input().split())

grid = [[0]*(l+1)]
for _ in range(l):
    a = [0]
    a.extend(list(map(int, input().split())))
    grid.append(a)

wall_prefix_sum = [[0]*(l+1) for _ in range(l+1)]
for i in range(1,l+1):
    for j in range(1,l+1):
        is_wall = 1 if grid[i][j] == 1 else 0
        wall_prefix_sum[i][j] = wall_prefix_sum[i-1][j] + wall_prefix_sum[i][j-1] - wall_prefix_sum[i-1][j-1] + is_wall

def print_that(that):
    for a in that:
        print(*a)
    print('--------')

class Knight:
    def __init__(self,i,r,c,h,w,k):
        self.id = i
        self.r = r
        self.c = c
        self.health = k
        self.h = h
        self.w = w
        self.damaged = 0

alive_knights = {}
knights_on_chess = [[0]*(l+1) for _ in range(l+1)]
recent_moved = []
recent_moved_id = []
all_move = True

drs,dcs = [-1,0,1,0],[0,1,0,-1]
def in_range(r,c):
    return 1<=r<=l and 1<=c<=l



def move(knight,d):
    global recent_moved, all_move
    
    now_id = knight.id
    recent_moved.append(now_id)
    r,c = knight.r, knight.c
    w,h = knight.w, knight.h
    dr, dc = drs[d], dcs[d]
    for i in range(r,r+h):
        for j in range(c,c+w):
            nr,nc = i+dr, j+dc
            if in_range(nr,nc) and knights_on_chess[nr][nc] != 0 and knights_on_chess[nr][nc] != now_id:
                move(alive_knights[knights_on_chess[nr][nc]], d)
            elif not in_range(nr,nc) or grid[nr][nc] == 2:
                all_move = False
                
    return all_move

def move_knight(i, d):
    global recent_moved, all_move, knights_on_chess

    if i not in alive_knights:
        return

    recent_moved = []
    all_move = True
    knight = alive_knights[i]
    move(knight,d)
    # print(f" 모두 이동가능? -> {all_move}")

    if all_move:
        dr, dc = drs[d], dcs[d]
        for knight_id in recent_moved:
            nr = alive_knights[knight_id].r + dr
            nc = alive_knights[knight_id].c + dc
            alive_knights[knight_id].r = nr
            alive_knights[knight_id].c = nc

        knights_on_chess = [[0]*(l+1) for _ in range(l+1)]
        for knight in alive_knights.values():
            r = knight.r
            c = knight.c
            w,h = knight.w, knight.h
            for i in range(r,r+h):
                for j in range(c,c+w):
                    if in_range(i,j):
                        knights_on_chess[i][j]= knight.id
    # print_that(knights_on_chess)
    # return True

    
def calc_damage():
    global alive_knights, knights_on_chess,recent_moved
    for i, id in enumerate(recent_moved):
        if i == 0:
            continue
        knight = alive_knights[id]
        sr,sc = knight.r, knight.c
        er,ec = min(sr+knight.h-1,l), min(sc+knight.w-1,l)

        damage = wall_prefix_sum[er][ec] - wall_prefix_sum[sr-1][ec] - wall_prefix_sum[er][sc-1] + wall_prefix_sum[sr-1][sc-1]
        knight.health = knight.health - damage
        knight.damaged = knight.damaged+ damage
        if knight.health <= 0:
            del alive_knights[id]
            for r in range(sr,er+1):
                for c in range(sc,ec+1):
                    knights_on_chess[r][c] = 0
    
    # print_that(knights_on_chess)


    
        
for id in range(1,n+1):
    r,c,h,w,k = map(int, input().split())
    knight = Knight(id,r,c,h,w,k)
    alive_knights[id] = knight
    for i in range(r,r+h):
        for j in range(c,c+w):
            knights_on_chess[i][j] = id

for _ in range(q):
    i, d = map(int,input().split())
    move_knight(i,d)
    # print(recent_moved)
    if all_move:
        calc_damage()
    # for knight in alive_knights.values():
    #     print(f'{knight.id}기사 위치:{knight.r},{knight.c} 체력: {knight.health}')

ans = 0
for knight in alive_knights.values():
    ans += knight.damaged

print(ans)