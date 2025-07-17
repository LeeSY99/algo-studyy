'''
m명 사람 1번사람 1분, 2번사람은 2분에 ... 출발
n*n격자, 각각 원하는 편의점 다름

1분동안
    1. 가고싶은 방향으로 1칸 움직임 최단거리
        상,좌,우,하 순
    사람에서 상하좌우 에서 출발한 후 가장 가까운 경로 선택 -> 우선순위방향 구하기
    그런데 편의점(도착지)에서 bfs로 구하면 1번에 시작점 상하좌우 까지의 거리를 구할 수 있다
    원래라면 상하좌우 시작해서 4번 구해야 함
    보니깐 분마다 계속 최단거리를 구하야할듯? 가다가 막힐 수 있기 때문

    2. 편의점에 도착하면 멈춤
        그 이후로 편의점이 있는 칸을 지나갈 수 없음

    3. t분일때 t<m이면
        t번사람은 자신이 가고싶은 편의점과 가장 가까이 있는 베이스캠프로
        행, 열이 가장 가까운 곳
        베이스캠프 이동시 시간소요 x
        그 이후 베이스캠프가 있는 칸을 지나갈 수 없음.
사람 위치, 편의점 -> list
베이스캠프 -> 배열

'''
from collections import deque

drs, dcs = [-1,0,0,1],[0,-1,1,0]

n,m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
conv = [tuple(map(lambda x: int(x)-1, input().split())) for _ in range(m)]
position = [] #사람 위치
cango = [[1]*n for _ in range(n)]


def in_range(r,c):
    return 0<=r<n and 0<=c<n

def bfs(r,c):
    visited = [[0] *n for _ in range(n)]
    dist = [[n*n] *n for _ in range(n)]
    dist[r][c] = 0
    q = deque()
    q.append((r,c))
    visited[r][c] = 1
    while q:
        r,c = q.popleft()
        for dr, dc in zip(drs,dcs):
            nr, nc = r+dr, c+dc
            if in_range(nr,nc) and not visited[nr][nc] and cango[nr][nc]:
                dist[nr][nc] = dist[r][c]+1
                visited[nr][nc] = 1
                q.append((nr,nc))
    return dist

def find_nearest_basecamp(t):
    conv_r, conv_c = conv[t-1]
    # print(conv_r,conv_c)
    dist = bfs(conv_r, conv_c)

    # print('-find nearest basecamp--')
    # for d in dist:
    #     print(*d)
    min_dist = n*n
    min_r, min_c = 0,0
    for i in range(n):
        for j in range(n):
            if grid[i][j] == 1:
                if dist[i][j] < min_dist:
                    min_dist = dist[i][j]
                    min_r = i
                    min_c = j
    position.append((min_r,min_c))
    # print(min_r,min_c)
    # for d in dist:
        # print(*d)
    
    cango[min_r][min_c] = 0

def move():
    for i, (cur_r,cur_c) in enumerate(position):
        if position[i] == conv[i]:
            continue
        max_dist = n*n
        # print(cur_r)
        # print(cur_c)
        # exit()
        sr, sc = conv[i]
        dist = bfs(sr,sc)
        # for d in dist:
        #     print(*d)

        for dr, dc in zip(drs, dcs):
            nr, nc = cur_r+dr, cur_c+dc
            if in_range(nr,nc) and cango[nr][nc]:
                if dist[nr][nc] < max_dist:
                    max_dist = dist[nr][nc]
                    position[i] = (nr,nc)
        

def check():
    for i, (cur_r,cur_c) in enumerate(position):
        if position[i] == conv[i]:
            cango[cur_r][cur_c] = 0


def end():
    if len(position) != m:
        return False
    for i in range(m):
        if position[i] != conv[i]:
            return False
    return True

t = 0
arrived = 0
while 1:
    t += 1
    # print(f'{t}분')
    
    move()

    check()

    if t<=m:
        find_nearest_basecamp(t)
    
    
    # print(position)
    # if t == 1:
    #     break
    # print(end())
    if end():
        break

print(t)