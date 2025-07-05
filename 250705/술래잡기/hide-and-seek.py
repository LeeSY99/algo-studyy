# debugging help function
def print_trees():
    for row in tree:
        print(" ".join(map(str, row)))
    print()

def pirnt_hiders():
    for row in hiders:
        new_row = list(map(len, row))
        print(" ".join(map(str, new_row)))
    print()

n, m, h, k = map(int, input().split())


hiders = [
    [
        [] for _ in range(n)
    ] for _ in range(n)
]

next_hiders = [
    [
        [] for _ in range(n)
    ] for _ in range(n)
]

for _ in range(m):
    x,y,d = map(int, input().split())
    hiders[x-1][y-1].append(d)


tree = [[0]*n for _ in range(n)]
for _ in range(h):
    r,c = map(int, input().split())
    tree[r-1][c-1] = 1

def in_range(r,c):
    return 0<=r<n and 0<=c<n



def move_hider(x,y):
    '''
    술래와 거리가 3이하만
    격자 밖은 안되고 넘어가게 되면 반대로
    이동할 곳에 술래가 있으면 안움직임
    '''
    #도망 x
    if abs(seeker_x-x) + abs(seeker_y-y) >3:
        next_hiders[x][y].extend(hiders[x][y])
        return
    #거리 3이하
    for hider_dir in hiders[x][y]:
        nx, ny = x+dxs[hider_dir], y+dys[hider_dir]
        if not in_range(nx,ny):
            hider_dir = (hider_dir+2)%4
        nx, ny = x+dxs[hider_dir], y+dys[hider_dir]
        #술래가 없을때만 움직임
        if (nx,ny) == (seeker_x, seeker_y):
            next_hiders[x][y].append(hider_dir)
        else:
            next_hiders[nx][ny].append(hider_dir)


def move_hiders():
    for i in range(n):
        for j in range(n):
            if len(hiders[i][j]) > 0: #해당 칸에 도망자 있음
                move_hider(i,j)
    
    #해당턴 움직임 처리 끝났으면 hiders 반영 후 초기화
    for i in range(n):
        for j in range(n):
            hiders[i][j] = next_hiders[i][j]
            next_hiders[i][j] = []

def move_seeker():
    '''달팽이 형태로 움직임 '''
    global seeker_x, seeker_y, seeker_dir

    ## 이동
    seeker_x += dxs[seeker_dir]
    seeker_y += dys[seeker_dir]

    # x-y=-1 선상 , x가 n//2미만 
    # 위 -> 오른쪽, 왼쪽-> 아래
    if seeker_x-seeker_y == -1 and seeker_x<n//2:
        if seeker_dir ==0:
            seeker_dir=1
        elif seeker_dir == 3:
            seeker_dir =2
    # x+y=n-1, x가 x//2 미만
    # 오른 -> 아래, 위-> 왼
    if seeker_x+seeker_y == n-1 and seeker_x<n//2:
        if seeker_dir ==1:
            seeker_dir=2
        elif seeker_dir == 0:
            seeker_dir =3

    # x=y 선상, x가 n//2초과
    #아래-> 왼, 오른 -> 위
    if seeker_x-seeker_y == 0 and seeker_x > n//2:
        if seeker_dir ==2:
            seeker_dir=3
        elif seeker_dir == 1:
            seeker_dir =0

    #x+y = n-1, x가 n//2초과
    #왼->위, 아래->오른
    if seeker_x+seeker_y == n-1 and seeker_x > n//2:
        if seeker_dir ==3:
            seeker_dir=0
        elif seeker_dir == 2:
            seeker_dir =1

    #(0,0)에 왔을 때
    if seeker_x ==0 and seeker_y ==0 and seeker_dir ==0:
        seeker_dir=2
    
    #가운데 왓을 떄
    if seeker_x ==n//2 and seeker_y ==n//2 and seeker_dir ==2:
        seeker_dir=0

def catch_hider(t):
    '''술래가 바라보는 방향 3칸 (나무 없는 곳에)
    점수 t*해당 턴 잡은 술래 수
    점수 리턴
    '''
    global score
    for dist in range(3):
        nx, ny = seeker_x + dist*dxs[seeker_dir], seeker_y + dist * dys[seeker_dir]

        if not in_range(nx,ny) or tree[nx][ny]:
            continue

        score += t* len(hiders[nx][ny])
        hiders[nx][ny] = []

seeker_x, seeker_y = n//2, n//2
seeker_dir = 0
score = 0
dxs, dys = [-1,0,1,0],[0,1,0,-1] #위, 오, 아래, 왼
def in_range(x,y):
    return 0<=x<n and 0<=y<n

for t in range(1,k+1):
    move_hiders()
    # pirnt_hiders()
    move_seeker()
    catch_hider(t)

print(score)