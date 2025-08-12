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
r,c,k = map(int, input().split())
grid = [[0] * (c+1) for _ in range(r+1)]
exit = [[0] * (c+1) for _ in range(r+1)]
dis, djs = [-1,0,1,0],[0,1,0,-1]

def in_range(i,j):
    return 0<i<=r and 0<j<=c

#0-based 

class Golem:
    def __init__(self, c, d):
        self.i = 0
        self.j = c
        self.d = d
        self.id = num

    def turn_clock(self):
        self.d = (self.d + 1)%4

    def turn_reverse_clock(self):
        self.d = (self.d - 1)%4


    def can_right(self):
        up = (self.i-1, self.j+1)
        right = (self.i, self.j+2)
        down = (self.i+1, self.j+1)
        right2 = (self.i+1, self.j+2)
        down2 = (self.i+2, self.j+1)

        if not grid[up[0]][up[1]] and not grid[right[0]][right[1]] and not grid[down[0]][down[1]]:
            return True
        return False

    def __str__(self):
        return f'위치: ({self.i},{self.j}), 출구{self.d}'
     

golems = [None] * (k+1)

def can_down(i,j):
    left = (i+1, j-1)
    down = (i+2, j)
    right = (i+1, j + 1)

    if in_range(down[0],down[1]) and not grid[left[0]][left[1]] and not grid[down[0]][down[1]] and not grid[right[0]][right[1]]:
        return True
    return False

def can_left(i,j):
    up = (i-1, j-1)
    left = (i, j-2)
    down = (i+1, j-1)
    if 0<left[1]<=c and not grid[up[0]][up[1]] and not grid[left[0]][left[1]] and not grid[down[0]][down[1]]:
        if can_down(i,j-1):
            return True
    return False

def can_right(i, j):
    up = (i-1, j+1)
    right = (i, j+2)
    down = (i+1, j+1)

    if 0<right[1]<=c and not grid[up[0]][up[1]] and not grid[right[0]][right[1]] and not grid[down[0]][down[1]]:
        if can_down(i, j+1):
            return True
    return False


def golem_move():
    global ans, grid, exit
    golem = golems[num]
    while 1:
    # for i in range(1):
        i, j = golem.i, golem.j
        if can_down(i, j):
            # print('아래이동')
            golem.i +=1
            continue
        if can_left(i, j):
            # print('좌측이동')
            golem.i += 1
            golem.j -=1
            golem.turn_reverse_clock()
            continue
        if can_right(i, j):
            # print('우측이동')
            golem.i += 1
            golem.j += 1
            golem.turn_clock()
            continue
        break
    # print(golem)
    # print('이동완료')

    in_grid = True
    i, j = golem.i, golem.j
    for di, dj in zip(dis, djs):
        ni, nc = i+di, j+dj
        if not in_range(ni, nc):
            # print(f'좌표 벗어남 ({ni},{nc})')
            # print(c)
            in_grid = False
            break

    if not in_grid: ## 초기화
        grid  = [[0] * (c+1) for _ in range(r+1)]
        exit = [[False] * (c+1) for _ in range(r+1)]
        return
    # print('점수계산')
    grid[i][j] = num

    for di, dj in zip(dis, djs):
        ni, nc = i+di, j+dj
        grid[ni][nc] = num

    exit_i, exit_j = i+ dis[golem.d] , j+djs[golem.d]
    exit[exit_i][exit_j] = True
    ans += bfs(exit_i, exit_j,i,j)

    # for g in grid:
    #     print(*g)
    # print(ans)

def bfs(exit_i, exit_j, starti, startj):
    visited = [[False] * (c+1) for _ in range(r+1)]
    q = deque()
    q.append((exit_i, exit_j))
    visited[exit_i][exit_j] = True
    best_i, best_j = starti+1, startj
    while q:
        i, j = q.popleft()
        for di, dj in zip(dis, djs):
            ni, nj = i+di, j+dj
            if in_range(ni, nj) and not visited[ni][nj]:
                if exit[i][j] and grid[ni][nj] or grid[i][j] == grid[ni][nj]:
                    visited[ni][nj] = True
                    q.append((ni,nj))
                    if ni > best_i:
                        best_i = ni
                        best_j = nj  
    # print(f'best: {best_i}')     
    return best_i

        
ans = 0
for num in range(1,k+1):
    # print(f'------{num}번째---------')
    c_i, d = map(int, input().split())
    golem = Golem(c_i,d)
    golems[num] = golem
    golem_move()

print(ans)


