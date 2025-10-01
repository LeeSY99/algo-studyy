n,a,b = map(int, input().split())
grid = [list(input()) for _ in range(n)]
graph = [[[] for _ in range(n)] for _ in range(n)]
drs, dcs = [0,1,0,-1],[-1,0,1,0]
def in_range(i,j):
    return 0<=i<n and 0<=j<n
for r in range(n):
    for c in range(n):
        for dr, dc in zip(drs,dcs):
            nr, nc = r+dr, c+dc
            if not in_range(nr, nc):
                continue
            if grid[nr][nc] == grid[r][c]:
                graph[r][c].append((nr,nc,a))
            else:
                graph[r][c].append((nr,nc,b))


INF = float('inf')
import heapq

def dijkstra():
    dist = [[INF]*n for _ in range(n)]
    dist[0][0] = 0
    q = [(0, 0, 0)] # 거리 r c 순서

    while q:
        now_d, now_r, now_c = heapq.heappop(q)

        if now_d != dist[now_r][now_c]:
            continue
        
        for next_r, next_c, w in graph[now_r][now_c]:
            next_d = now_d + w
            if next_d < dist[next_r][next_c]:
                dist[next_r][next_c] = next_d
                heapq.heappush(q, (next_d, next_r, next_c))
    
    return dist[n-1][n-1]

print(dijkstra())
