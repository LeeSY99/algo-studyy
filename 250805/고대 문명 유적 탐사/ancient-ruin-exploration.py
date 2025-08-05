''' 5*5격자 7가지 유물(1~7)

1) 탐사진행
    3*3격자 선택 
    90, 180, 270도 회전 가능
    목표
        1차 획득 가치 최대화
        회전한 각도가 작은 방법
        좌표 행,열이 작은 곳

2) 유물획득
    1차획득
        상하좌우 인접한 같은 종류 유물조각은 연결되어 있음
        3개이상 연결시 사라짐
        가치: 모인 조각 개수

    벽면 1~7 숫자가 m개 적힘
    조각이 사라졌을때 새로 생겨나는 조각 정보
    조각이 사라지고 빈 공간에 차례대로 조각이 생겨남
        열 번호 작음
        행 번호 큼
    다시 사용할 수 없음(벽면에서 사라짐)


    연쇄획득
        새 조각이 생기고 3개 이상 연결될 수 있음
        같은 방식으로 유물이 되고 사라짐
        사라진위치에 새 조각이 생김
        유물이 될 수 없을 때 까지 반복

3) 탐사 반복
    1~2작업을 1턴 -> 총 k턴 수행
    각 턴마다 획득한 유물 가치 출력
    도중에 유물획득 불가시 종료 -> 출력 x
'''
from collections import deque
k, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(5)]
wall = list(map(int, input().split()))
best_treasure = 0
wall_index = 0
best_grid = [g[:] for g in grid]
ans = []

def turn(r,c, time, best_grid2):
    global grid
    new_grid2 = [g[:] for g in best_grid2]
    for _ in range(time):
        for i in range(3):
            for j in range(3):
                new_grid2[j+r-1][c+1-i] = best_grid2[i+r-1][j+c-1]
        best_grid2 = [g[:] for g in new_grid2]

    return new_grid2



def search1():
    global best_grid, best_treasure
    best_treasure = 0
    best_grid2 = [g[:] for g in best_grid]
    for rot_time in range(1,4):
        for c in range(1,4):
            for r in range(1,4):
                new_grid = turn(r,c,rot_time,best_grid2)
                count_sum, after_grid = bfs(new_grid)
                if best_treasure < count_sum:
                    best_treasure = count_sum
                    best_grid = [g[:] for g in after_grid]
    if best_treasure == 0:
        return False
    # for g in best_grid:
    #     print(*g)
    # print('-----')
    return True
                
def fill():
    global wall_index
    for j in range(5):
        for i in range(4,-1,-1):
            if best_grid[i][j] == 0:
                best_grid[i][j] = wall[wall_index]
                wall_index+=1

def search2():
    global best_grid, best_treasure, ans
    global wall_index
    for _ in range(2):
        fill()

        count_sum, best_grid = bfs(best_grid)

        if count_sum == 0:
            break
        best_treasure += count_sum
        fill()

    ans.append(best_treasure)

def bfs(new_grid):
    visited = [[0] * 5 for _ in range(5)]
    q = deque()
    count_sum = 0
    for i in range(5):
        for j in range(5):
            to_zero = []
            if not visited[i][j]:
                now_num = new_grid[i][j]
                count = 1
                visited[i][j] = 1
                q.append((i,j))
                to_zero.append((i,j))
                while q:
                    r,c = q.popleft()
                    for dr, dc in zip(drs,dcs):
                        nr, nc = r+dr, c+dc
                        if in_range(nr,nc) and not visited[nr][nc] and new_grid[nr][nc] == now_num:
                            to_zero.append((nr,nc))
                            visited[nr][nc]=1
                            count += 1
                            q.append((nr,nc))
                if count >=3:
                    count_sum += count
                    for r, c in to_zero:
                        new_grid[r][c] = 0
    return count_sum, new_grid

                
drs, dcs = [0,1,0,-1],[1,0,-1,0]
def in_range(r,c):
    return 0<=r<5 and 0<=c<5


    
    

for _ in range(k):
    if not search1():
        # print('search1')
        break
    search2()

print(*ans)
    