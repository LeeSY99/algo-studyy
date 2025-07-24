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

drs,dcs = [-1,1,0,0],[0,0,-1,1]
def move():
    global dist, people, people_rc
    people = [[0]*n for _ in range(n)]
    new_people = []
    for i in range(len(people_rc)):
        r, c = people_rc[i]
        if (r,c) == (goal_r,goal_c):
            continue

        # 상→하→좌→우 우선, 출구까지 거리 감소 여부 확인
        for dr, dc in zip(drs, dcs):
            nr, nc = r+dr, c+dc
            if not in_range(nr,nc) or grid[nr][nc] != 0:
                continue
            before = abs(goal_r-r) + abs(goal_c-c)
            after  = abs(goal_r-nr) + abs(goal_c-nc)
            if after < before:
                dist += 1
                r, c = nr, nc
                break

        # 종료 안 한 참가자만 기록
        if (r,c) != (goal_r,goal_c):
            new_people.append((r,c))
            people[r][c] = 1

        people_rc[i] = (r,c)

    people_rc[:] = new_people

    # print('이동 후 좌표')
    # print(people_rc)

def turn_map():
    global grid, people, people_rc, goal_r, goal_c
    max_size = n+1
    best_sr = best_sc = -1

    # 1) goal 포함 + 사람 최소 1명 → 최소 크기, 같으면 sr,sc 작은 것
    for size in range(1, n+1):
        for sr in range(n-size+1):
            for sc in range(n-size+1):
                er = sr+size-1
                ec = sc+size-1

                if not (sr<=goal_r<=er and sc<=goal_c<=ec):
                    continue

                found = False
                for i in range(sr, er+1):
                    for j in range(sc, ec+1):
                        if people[i][j]:
                            found = True
                            break
                    if found:
                        break

                if found:
                    if size < max_size or (size==max_size and (sr<best_sr or (sr==best_sr and sc<best_sc))):
                        max_size, best_sr, best_sc = size, sr, sc

    # 2) 회전
    new_grid  = [row[:] for row in grid]
    new_people= [row[:] for row in people]
    for i in range(max_size):
        for j in range(max_size):
            r0, c0 = best_sr+i, best_sc+j
            r1 = best_sr + j
            c1 = best_sc + (max_size-1 - i)
            new_grid [r1][c1] = grid [r0][c0]
            new_people[r1][c1] = people[r0][c0]

    # 3) 내구도 1 감소 (오타 수정됨)
    for i in range(max_size):
        for j in range(max_size):
            r1 = best_sr + i
            c1 = best_sc + j
            if new_grid[r1][c1] > 0:
                new_grid[r1][c1] -= 1

    # 4) 출구 좌표 갱신
    rel_r = goal_r - best_sr
    rel_c = goal_c - best_sc
    goal_r = best_sr + rel_c
    goal_c = best_sc + (max_size - 1 - rel_r)

    # 2) 참가자 리스트(old_rc)를 사각형 안팎 구분 없이 회전
    old_rc = people_rc[:]    # 기존 순서와 중복 그대로 보존
    new_people_rc = []
    for r, c in old_rc:
        if best_sr <= r < best_sr + max_size and best_sc <= c < best_sc + max_size:
            tr = r - best_sr
            tc = c - best_sc
            nr = best_sr + tc
            nc = best_sc + (max_size - 1 - tr)
        else:
            nr, nc = r, c
        new_people_rc.append((nr, nc))
    people_rc = new_people_rc

    # 3) boolean grid 재생성
    people = [[0]*n for _ in range(n)]
    for r, c in people_rc:
        if (r, c) != (goal_r, goal_c):  # 탈출한 참가자 제외
            people[r][c] = 1

    # 4) 전역 grid 갱신
    grid = new_grid


def print_that(aa):
    for a in aa:
        print(*a)
    print('-------')


for time in range(k):
    # print(f'{time+1}초')
    # print(f'출구 좌표 :{goal_r} {goal_c}')
    move()
    if not people_rc:
        break
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