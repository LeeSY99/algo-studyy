''' r행 c열 격자 1-based 
동 서 남은 벽으로 막힘 정령은 북쪽으로 들어올 수 있음 

k명의 정령 골렘을 타고 숲 탐색

골렘
    십자 모양 -중앙칸 포함 5칸
    중앙을 제외한 4칸 중 하나는 출구
정령은 어느방향에서 골렘을 탈 수 있음
내릴때에는 출구를 통해서만 

i번째로 숲을 탐색하는 골렘은 북쪽 바깥에서 시작-> 골렘중앙이 c_i열이 되도록 내려옴
초기 골렘의 출구 d_i(북동남서)

골렘의 이동(우선순위)
    1) 남쪽으로 한칸
        아래에 비어있어야
    2) 1)불가시 서쪽
        출구가 반시계 방향으로 이동
    3) 동쪽
        출구가 시계방향

가장 남쪽에 도달하면 정령은 골램 내 상하좌우 인접한 칸으로 이동
- 현재 위치한 골렘의 출구가 다른 골렘과 인접하다면 다른 골렘으로 이동가능

최대한 이동했지만 골렘의 몸 일부가 숲 밖이면
답에 포함 x
숲이 텅 빈 상태에서 다시 시작
        '''
from collections import deque
R,C,K = map(int, input().split())
grid = [[0] * (C) for _ in range(R+3)]
drs, dcs = [-1,0,1,0],[0,1,0,-1]

def in_range(r,c):
    return 0<=r<R+3 and 0<=c<C

#0-based 


def can_go(r,c): #(r,c)로 이동할 수 있는지?
    drc = [(-2,0), 
    (-1,-1), (-1,0), (-1,1), 
    (0,-1), (0,0), (0,1) , 
    (1,0)]

    for dr, dc in drc:
        nr, nc = r+dr, c+dc
        if not in_range(nr,nc) or grid[nr][nc] != 0:
            return False
    return True

def golem_move(c,d):
    r = 1
    while 1:
        if can_go(r+1,c):
            r, c = r+1, c
        elif can_go(r+1, c-1):
            r, c = r+1, c-1
            d = (d-1)%4
        elif can_go(r+1, c+1):
            r, c = r+1, c+1
            d = (d+1)%4
        else:
            break
    
    grid[r][c] = num
    for dr, dc in zip(drs, dcs):
        nr, nc = r+dr, c+dc
        grid[nr][nc] = num

    e_r, e_c = r+drs[d], c+dcs[d]
    grid[e_r][e_c] = -num

    # for g in grid:
    #     print(*g)
    # print('p-----')
    return (r,c,d)

def reset_map():
    global grid
    for i in range(R+3):
        for j in range(C):
            grid[i][j] = 0

def move(r,c): #bfs로 가장 아래로 가기
    q = deque()
    visited = [[False] * C for _ in range(R+3)]

    q.append((r,c))
    visited[r][c] = True
    best_r = r

    while q:
        cur_r, cur_c = q.popleft()
        for dr, dc in zip(drs,dcs):
            nr, nc = cur_r+dr, cur_c + dc
            if not in_range(nr,nc) or grid[nr][nc] == 0 or visited[nr][nc]:
                continue
            if abs(grid[cur_r][cur_c]) == abs(grid[nr][nc]) or grid[cur_r][cur_c] < 0:
                q.append((nr,nc))
                visited[nr][nc] = True
                best_r = max(best_r, nr)
    return best_r



        
score = 0
for num in range(1,K+1):
    # print(f'------{num}번째---------')
    c, d = map(int, input().split())
    c-=1
    r,c,d = golem_move(c,d)

    if r>=4:
        final_r = move(r,c)
        score += final_r -2
    else:
        reset_map()

print(score)


