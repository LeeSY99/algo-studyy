''' n*n 격자에 나무개수, 벽의 정보
제초제 : k의 범위만큼 대각선으로 퍼짐, 벽이 있으면 전파 x

1년동안 나무의 성장과 억제
    1. 인접한 4개의 칸 중 나무가 있는 칸의 수만큼 성장(동시에)
    2. 기존 나무는 인접한 4개의 칸 중 벽, 다른 나무, 제초제가 없는 칸에 번식
       번식된 나무는 각 칸의 나무개수// 번식 가능한 칸의 수(동시에)
    3. 제초제를 나무가 가장 많이 박멸되는 칸에 뿌림.
        나무가 없는 칸에 뿌리면 그대로 끝
        나무가 있는 칸에 뿌리면 대각선으로 k칸만큼 전파
        전파하다가 나무가 없거나 벽이면 전파 x
        c년만큼 제초제가 남아있음

'''
n,m,k,c = map(int, input().split())

grid = [list(map(int, input().split())) for _ in range(n)]
#-1:벽, 0:빈칸, 양수:나무 수
kill_medicine =  [[0]*n for _ in range(n)]

def in_range(r,c):
    return 0<=r<n and 0<=c<n

drs, dcs = [0,1,0,-1],[1,0,-1,0]

#나무 성장
def grow():
    global grid
    new_grid = [g[:] for g in grid]
    #나무 탐색:
    for r in range(n):
        for c in range(n):
            if grid[r][c] <=0:
                continue
            for dr, dc in zip(drs,dcs):
                nr, nc = r+dr, c+dc
                if in_range(nr,nc) and grid[nr][nc]>0:
                    new_grid[r][c] +=1
    grid = new_grid

#나무 번식
def spread():
    global grid
    tree_count = [g[:] for g in grid]

    for i in range(n):
        for j in range(n):
            if grid[i][j] <=0:
                continue
            count = 0
            for dr, dc in zip(drs,dcs):
                nr, nc = i+dr, j+dc
                if in_range(nr,nc) and grid[nr][nc] == 0 and kill_medicine[nr][nc] == 0:
                    count+=1
            for dr, dc in zip(drs,dcs):
                nr, nc = i+dr, j+dc
                if in_range(nr,nc) and grid[nr][nc] == 0 and kill_medicine[nr][nc] == 0:
                    tree_count[nr][nc] += (grid[i][j]//count)

    grid = tree_count


#제초제
def kill():
    #최적의 제초제 위치 탐색
    global ans
    global grid
    kdrs, kdcs = [1,1,-1,-1],[1,-1,-1,1]
    max_kill = 0
    kr,kc = 0,0
    # kill =[[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if grid[i][j] <= 0:
                continue
            kill_count = grid[i][j]
            for dr, dc in zip(kdrs,kdcs):
                for dist in range(1,k+1):
                    nr,nc = i+dr*dist, j+dc*dist
                    if not in_range(nr,nc) :
                        break
                    if grid[nr][nc] != -1:    
                        kill_count += grid[nr][nc]  
                    if  grid[nr][nc] <= 0:
                        break
            if kill_count > max_kill:
                kr=i
                kc=j
                max_kill = kill_count
    ans += max_kill
            # kill[r][c] = kill_count
    # print(kill)
    # print(kr,kc,max_kill)

    #제초
    new_grid = [g[:] for g in grid]
    new_grid[kr][kc] = 0
    kill_medicine[kr][kc]+=(c+1)
    for dr, dc in zip(kdrs,kdcs):
        for dist in range(1,k+1):
            nr,nc = kr+dr*dist, kc+dc*dist
            if not in_range(nr,nc): 
                continue
            if grid[nr][nc] != -1:
                new_grid[nr][nc] = 0
                kill_medicine[nr][nc]=(c+1)
            if grid[nr][nc] <= 0:
                break
    grid = new_grid

def one_year_after():
    for i in range(n):
        for j in range(n):
            if kill_medicine[i][j]:
                kill_medicine[i][j] -=1
#디버깅용
def print_grid():
    for g in grid:
        print(*g)
    print('---------')

def pirnt_medicine():
    for a in kill_medicine:
        print(*a)
    print()

ans = 0
for year in range(m):
    # print(f'{year}년')
    # print_grid()
    grow()
    # print_grid()
    spread()
    # print_grid()
    kill()
    # print_grid()
    one_year_after()
    # pirnt_medicine()
    
print(ans)
