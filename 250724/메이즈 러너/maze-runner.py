'''
n*n 미로 - 좌상단 (1,1) 1-based
1. 빈칸 - 이동가능
2. 벽 - 이동불가
    1~9 내구도
    회전 시 내구도 1 감소
    0되면 빈칸
3. 출구 -> 참가자 도달 시 탈출

1초마다 모든 참가자 한칸 움직임(동시에)
    상하좌우, 벽으로는 불가
    출구와 가깝게 이동
    갈 수 있는 길이 2개 이상시 상하 움직음 우선
    움직일 수 없으면 움직이지 않음

미로 회전
    참가자와 출구를 포함한 가장 작은 정사각형
    정사각형 여러개 시 r,c작은 것
    정사각형은 시계방향 90도 회전 화전한 벽은 내구도 1 감소

'''

n,m,k = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
people_rc = []
people = [[0] * n for _ in range(n)]
for _ in range(m):
    r,c = map(int, input().split())
    people_rc.append((r-1,c-1))
    people[r-1][c-1] = 1
r,c = map(int, input().split())
goal_r, goal_c = r-1, c-1
dist = 0
def in_range(r,c):
    return 0<=r<n and 0<=c<n
def move():
    global dist, people, people_rc
    people = [[0] * n for _ in range(n)]
    new_people_rc = []
    # print(people_rc)
    for i, (p_r, p_c) in enumerate(people_rc):
        # print(p_r,p_c)
        if p_r > goal_r:
            if in_range(p_r-1,p_c) and grid[p_r-1][p_c] == 0:
                dist += 1
                people_rc[i] = (p_r-1, p_c)
                continue
        if p_r < goal_r:
            if in_range(p_r+1,p_c) and grid[p_r+1][p_c] == 0:
                dist += 1
                people_rc[i] = (p_r+1, p_c)
                continue
        if p_c > goal_c:
            if in_range(p_r,p_c-1) and grid[p_r][p_c-1] == 0 :
                dist += 1
                people_rc[i] = (p_r, p_c-1)
                continue
        if p_c < goal_c:
            if in_range(p_r,p_c+1) and grid[p_r][p_c+1] == 0 :
                dist += 1
                people_rc[i] = (p_r, p_c+1)
                continue


    for p_r, p_c in people_rc:
        if (p_r,p_c) == (goal_r,goal_c):
            continue
        new_people_rc.append((p_r,p_c))
        people[p_r][p_c] = 1
    people_rc = new_people_rc
    # print('이동 후 좌표')
    # print(people_rc)

def turn_map():
    global grid, people, people_rc
    global goal_r, goal_c
    max_size = n+1
    best_sr=-1
    best_sc=-1
    for size in range(1, n + 1):
        for sr in range(n - size + 1):
            for sc in range(n - size + 1):
                er = sr + size - 1
                ec = sc + size - 1

                # goal이 이 정사각형 안에 포함되는지 확인
                if not (sr <= goal_r <= er and sc <= goal_c <= ec):
                    continue

                # 사람 있는지 확인
                has_person = False
                for i in range(sr, er + 1):
                    for j in range(sc, ec + 1):
                        if people[i][j]:
                            has_person = True
                            break
                    if has_person:
                        break

                # 조건 만족하면 갱신
                if has_person:
                    if size < max_size or (size == max_size and (sr < best_sr or (sr == best_sr and sc < best_sc))):
                        max_size = size
                        best_sr = sr
                        best_sc = sc
    # print('best_sr,sc:',best_sr,best_sc, max_size)
    new_grid = [row[:] for row in grid]
    for i in range(max_size):
        for j in range(max_size):
            new_grid[best_sr+j][best_sc - i + max_size - 1] = grid[best_sr+i][best_sc+j]

    new_people = [row[:] for row in people]
    for i in range(max_size):
        for j in range(max_size):
            new_people[best_sr+j][best_sc - i + max_size - 1] = people[best_sr+i][best_sc+j]
    people = new_people
    # print_that(people)

    people_rc= []
    for i in range(n):
        for j in range(n):
            if people[i][j]:
                people_rc.append((i,j))

    
    rel_r = goal_r - best_sr
    rel_c = goal_c - best_sc
    new_goal_r = best_sr + rel_c
    new_goal_c = best_sc + (max_size - 1 - rel_r)
    goal_r, goal_c = new_goal_r, new_goal_c

    grid = new_grid
    for r in range(max_size):
        for c in range(max_size):
            if grid[best_sr+r][best_sr+c]>0:
                grid[best_sr+r][best_sr+c]-=1


def print_that(aa):
    for a in aa:
        print(*a)
    print('-------')


for time in range(k):
    # print(f'{time+1}초')
    # print(f'출구 좌표 :{goal_r} {goal_c}')
    move()
    # print('이동 후')
    # print_that(people)
    # print('맵')
    turn_map()
    # print('회전 후')
    # print_that(people)
    # print_that(grid)
    # print(f'출구 좌표 :{goal_r} {goal_c}')
    # print(f'{time+1}초 이동거리: {dist} ,출구: {goal_r,goal_c}')
print(dist)
print(goal_r+1,goal_c+1)