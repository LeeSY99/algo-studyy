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
            if grid[r][c] == 1 and grid[nr][nc] == 2:
                dfs(nr,nc,idx)
            elif grid[r][c] == 2 and grid[nr][nc] in (2,3):
                dfs(nr,nc,idx)
            


drs, dcs = [-1,1,0,0], [0,0,-1,1]
def move():
    '''팀별 한칸 씩 이동 (dfs)
    새 머리 좌표 + 꼬리 제외 나머지 
    list로 가능함. insert생각해서 deque를 사용했지만 '''
    global grid
    new_grid = [a[:] for a in grid]
    for i in range(m):
        team = team_index[i]
        r, c = team[0]
        for dr, dc in zip(drs,dcs):
            nr, nc = r+dr, c+dc
            ### 다음칸이 0이나 2가 아니면 머리는 이동가능
            ### 결국은 3,4 찾는거랑 같을지도?
            if in_range(nr,nc) and grid[nr][nc] in (3,4):
                new_rc = (nr,nc)
                removed = team.pop()
                team.appendleft(new_rc)

                if removed != new_rc:
                    new_grid[removed[0]][removed[1]] = 4
                break
                    
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
    # 0: 오른, 1:위 2:왼, 3:아래
    d = (rnd//n)%4
    offset = rnd%n

    if d==0:
        r,c,dr,dc = offset, 0,0,1
    elif d==1:
        r,c,dr,dc = n-1,offset,-1,0
    elif d==2:
        r,c,dr,dc = n-offset-1,n-1,0,-1
    else:
        r,c,dr,dc = 0,n-offset-1,1,0

    while in_range(r,c):
        if grid[r][c] in (1,2,3):
            return calc_score(r,c)
        r +=dr
        c +=dc
    return 0
    
    
            
def calc_score(i,j):
    for idx, team in enumerate(team_index):
        for s,(ti, tj) in enumerate(team):
            if ti == i and tj == j:
                score = (s+1)**2
                #머리 꼬리 바꾸기 ->> 그냥 리스트 뒤집으면 됨
                reversed_team = deque(list(team)[::-1])
                team_index[idx] = reversed_team     

                for k, (rr,cc) in enumerate(reversed_team):
                    if k == 0:
                        grid[rr][cc] = 1
                    elif k == len(reversed_team)-1:
                        grid[rr][cc] = 3
                    else:
                        grid[rr][cc] = 2           
                return score
    return 0
                    





#debugging 
def print_grid(grid):
    for g in grid:
        print(*g)
    print('--------')

seperate_team()
# print(team_index)
score=0
for r in range(k):
    # print(f'{r+1}턴')
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