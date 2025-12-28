from collections import deque
n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

sr,sc = 0,0
for i in range(n):
    for j in range(n):
        if grid[i][j] == 9:
            sr = i
            sc = j

def find_eat():
    count = 0
    for i in range(n):
        for j in range(n):
            if grid[i][j] == 0 or grid[i][j] == 9:
                continue
            if grid[i][j] < size:
                count+=1

    return count
drs, dcs = [0,1,0,-1],[1,0,-1,0]
def in_range(r,c):
    return 0<=r<n and 0<=c<n

def get_dist(r,c):
    dist = [[float('inf')]*n for _ in range(n)]
    dist[r][c] = 0
    q = deque()
    q.append((r,c))

    while q:
        r,c = q.popleft()
        for dr, dc in zip(drs,dcs):
            nr = r+dr
            nc = c+dc
            if in_range(nr,nc) and grid[nr][nc] <= size and dist[nr][nc] == float('inf'):
                q.append((nr,nc))
                dist[nr][nc] = dist[r][c] + 1
    # for d in dist:
    #     print(*d)
    min_dist = float('inf')
    count = 0
    gi,gj = None, None
    for i in range(n):
        for j in range(n):
            if grid[i][j] == 0 or grid[i][j] == 9:
                continue
            if dist[i][j] < min_dist and grid[i][j] < size:
                count += 1
                min_dist = dist[i][j]
                gi, gj = i,j
    return count, gi, gj, min_dist






size = 2
eat = 0

time = 0
while True:
    can_eat, gr, gc, dist = get_dist(sr,sc)
    # print(can_eat, gr, gc, dist)
    if can_eat == 0:
        break
    grid[sr][sc] = 0
    grid[gr][gc] = 9
    eat += 1
    time += dist
    sr = gr
    sc = gc

    # print(time)
    # print('----')
    if eat == size:
        size += 1
        eat = 0
print(time)