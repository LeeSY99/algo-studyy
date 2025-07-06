'''n*n격자
동일한 숫자가 상하좌우 인접해 있으면 동일 그룹
조화로움 a-b: (a 칸수+b칸수) * a숫자* b숫자 * 맞닿아 있는 변의 수
그리고 회전함
십자모양-반시계
나머지는 각각 개별적으로 시계방향
초기+1회전+2회전+3회전이후 예술점수 합
'''

from collections import deque
drs, dcs = [-1,1,0,0], [0,0,-1,1]

def in_range(r,c):
    return 0<=r<n and 0<=c<n
def group():
    groups = []
    group_num = []
    q= deque()
    visited = [[0]*n for _ in range(n)]
    group_all = [[0]*n for _ in range(n)]
    seperate = 0
    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                now_value = grid[i][j]
                groups.append(now_value)
                count = 0
                q.append((i,j))
                visited[i][j] = 1
                while q:
                    count+=1
                    r, c = q.popleft()
                    group_all[r][c] = seperate
                    for dr, dc in zip(drs,dcs):
                        nr, nc = r+dr, c+dc
                        if in_range(nr,nc) and not visited[nr][nc] and grid[nr][nc] == now_value:
                            visited[nr][nc] = 1
                            q.append((nr,nc))
                group_num.append(count)
                seperate += 1
    return groups, group_num, group_all


def calc_score(groups, group_num, group_all):
    g = len(groups)
    contact = [[0]*g for _ in range(g)]
    visited = [[0]*n for _ in range(n)]

    for r in range(n):
        for c in range(n):
            g1 = group_all[r][c]
            for dr, dc in zip(drs,dcs):
                nr, nc = r+dr, c+dc
                if not in_range(nr,nc):
                    continue
                g2 = group_all[nr][nc]
                if g1==g2:
                    continue
                a, b = (g1,g2) if g1<g2 else (g2,g1)
                contact[a][b] +=1
                
    score = 0
    for a in range(g):
        for b in range(a+1,g):
            cnt = contact[a][b]
            if cnt:
                score += (group_num[a] + group_num[b]) * groups[a] * groups[b] *cnt //2
    return score


def cross_rotate():
    for dist in range(1,n//2+1):
        temp = grid[center-dist][center]
        grid[center-dist][center] = grid[center][center+dist]
        grid[center][center+dist] = grid[center+dist][center]
        grid[center+dist][center] = grid[center][center-dist]
        grid[center][center-dist] = temp


def rotate():
    global grid
    new = [a[:] for a in grid]
    for i in range(center):
        for j in range(center):
            new[j][center-1-i] = grid[i][j]

    for i in range(center):
        for j in range(center+1,n):
            new[j-center-1][n-1-i] = grid[i][j]

    for i in range(center+1,n):
        for j in range(center):
            new[center+j+1][n-i-1] = grid[i][j]

    for i in range(center+1,n):
        for j in range(center+1,n):
            new[j][n-i+center] = grid[i][j]

    grid = new

n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

ans = 0

center = n//2
def print_grid():
    for a in grid:
        print(*a)
for _ in range(4):
    groups,group_num, group_all= group()
    # print(groups,group_num, group_all)
    # for a in group_all:
    #     print(*a)
    score = calc_score(groups,group_num,group_all)
    ans += score

    cross_rotate()
    rotate()
    # print_grid()
print(ans)

