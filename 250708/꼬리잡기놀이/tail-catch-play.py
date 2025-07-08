'''n*n격자 3명이상 한 팀
맨 앞 -> 머리사람, 맨 뒤 -> 꼬리사람
라운드별
    각 팀은 머리사람을 따라 한칸씩 이동
    공이 던져짐 공은 좌 하 우 상 
    공이 던져지고 최초로 만나는 사람이 공을 얻고 점수를 얻음
        점수: 머리사람 시작해서 k번째 사람이면 k^2만큼 얻음
    공을 획득한 팀은 머리와 꼬리가 바뀜


입력 - n,m(팀 개수) ,k(라운드 수)
1:머리, 2:나머지, 3:꼬리, 4:경로
'''

n,m,k = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]


def in_range(r,c):
    return 0<=r<n and 0<=c<n
from collections import deque
team_index = [deque() for _ in range(m)]
visited = [[0]*n for _ in range(n)]
def seperate_team():
    idx = 0
    for i in range(n):
        for j in range(n):
            if grid[i][j] == 1:
                dfs(i,j,idx)
                idx+=1           

def dfs(r,c,idx):
    visited[r][c] =1
    team_index[idx].append((r,c))
    for dr, dc in zip(drs,dcs):
        nr,nc = r+dr, c+dc
        if in_range(nr,nc) and not visited[nr][nc]:
            if grid[nr][nc] == 2 or grid[nr][nc] == 3:
                dfs(nr,nc,idx)


drs, dcs = [-1,1,0,0], [0,0,-1,1]
def move():
    '''팀별 한칸 씩 이동 (dfs) '''
    global grid
    new_grid = [a[:] for a in grid]
    for i in range(m):
        team = team_index[i]
        r, c = team[0]
        for dr, dc in zip(drs,dcs):
            nr, nc = r+dr, c+dc
            if in_range(nr,nc) and grid[nr][nc] == 4:
                team.insert(0,(nr,nc))
                del_r, del_c = team.pop()
                new_grid[del_r][del_c] = 4
        for idx in range(len(team)):
            r, c = team[idx]
            if idx == 0:
                new_grid[r][c] = 1
            elif idx == len(team)-1:
                new_grid[r][c] = 3
            else:
                new_grid[r][c] = 2

    grid = new_grid
    


def calc(rnd):
    score = 0
    # dis, dcs = [0,-1,0,1], [1,0,-1,0]
    direction = (rnd//n)%4
    if direction == 0:
        i = rnd%n
        for j in range(n):
            if grid[i][j] != 0 and grid[i][j] != 4:
                return calc_score(i,j)
    elif direction == 1:
        j = rnd%n
        for i in range(n-1,-1,-1):
            score +=calc_score(i,j)
            if score:
                return score
    elif direction == 2:
        i = n-(rnd%n)-1
        for j in range(n-1,-1,-1):
            score +=calc_score(i,j)
            if score:
                return score
    elif direction == 3:
        j = n-(rnd%n)-1
        for i in range(n):
            score +=calc_score(i,j)
            if score:
                return score
    
            
def calc_score(i,j):
    for idx in range(m):
        team = team_index[idx]
        for s in range(len(team)):
            ti, tj = team[s]
            if ti == i and tj == j:
                score = (s+1)**2
                #머리 꼬리 바꾸기
                head = team[0]
                tail = team[-1]
                head, tail = tail, head
                grid[head[0]][head[1]] = 1
                grid[tail[0]][tail[1]] = 3
                team_index[idx] = deque(list(team)[::-1])
                return score
                    





#debugging 
def print_grid(grid):
    for g in grid:
        print(*g)
    print('--------')

seperate_team()
score=0
for r in range(k):
    # print(team_index)
    # print(visited)
    move()
    # print(team_index)
    # print_grid(grid)
    score+=calc(r)
    # print(score)
    # print('이동 후')
    # print(team_index)

    # print_grid(grid)
print(score)