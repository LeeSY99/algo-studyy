'''n*m 크기 격자
좌측 상단 출발 우측 하단 탈출
뱀에 물리지 않고, 뱀이 있는 칸 이동불가'''

n, m = map(int, input().split())

from collections import deque

q = deque()
dist = [[0] * m for _ in range(n)]
visited = [[0] * m for _ in range(n)]
grid = [list(map(int, input().split())) for _ in range(n)]
drs, dcs = [0,1,0,-1], [1,0,-1,0]

def in_range(r,c):
    return 0<=r<n and 0<=c<m

def push(r,c,d):
    dist[r][c] = d
    visited[r][c] = 1
    q.append((r,c))
    


def bfs():
    while q:
        r, c = q.popleft()
        for dr, dc in zip(drs, dcs):
            nr, nc = r+dr, c+dc
            if in_range(nr,nc) and not visited[nr][nc] and grid[nr][nc]:
                push(nr,nc,dist[r][c]+1)

push(0,0,0)
bfs()

# print(dist)
print(-1 if dist[n-1][m-1] == 0 else dist[n-1][m-1])
# for d in dist:
#     print(*d)

