from collections import deque
n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
'''
1: 도시
상하좌우 인접해있는 1은 같은 도시
'''

city = [[0] * m for _ in range(n)]

drs,dcs = [0,1,0,-1],[1,0,-1,0]
city_num = 1
visited = [[False]*m for _ in range(n)]

def in_range(r,c):
    return 0<=r<n and 0<=c<m

def get_city(r,c,city_num):
    q = deque([(r,c)])
    visited[r][c] = True
    city[r][c] = city_num

    while q:
        cr,cc = q.popleft()

        for dr, dc in zip(drs,dcs):
            nr, nc = cr+dr, cc+dc
            if in_range(nr,nc) and not visited[nr][nc] and grid[nr][nc] == 1:
                q.append((nr,nc))
                visited[nr][nc] = True
                city[nr][nc] = city_num


for i in range(n):
    for j in range(m):
        if grid[i][j] == 1 and not visited[i][j]:
            get_city(i,j,city_num)
            city_num += 1

def get_dist(r,c):
    for i in range(n):
        if i == r:
            continue
        if city[i][c] != 0 and city[i][c] != city[r][c]:
            before = city[r][c]
            after = city[i][c]
            graph[before][after] = min(graph[before][after], abs(i-r)-1)
            graph[after][before] = min(graph[after][before], abs(i-r)-1)
    
    for j in range(m):
        if j == c:
            continue
        if city[r][j] != 0 and city[r][j] != city[r][c]:
            before = city[r][c]
            after = city[r][j]
            graph[before][after] = min(graph[before][after], abs(j-c)-1)
            graph[after][before] = min(graph[after][before], abs(j-c)-1)


graph = [[float('inf')]*city_num for _ in range(city_num)]
edges = []
for i in range(n):
    for j in range(m):
        if city[i][j] != 0:
            get_dist(i,j)

ans = 0
dist = [float('inf')] * (n+1)
dist[1] = 0
visited = [False] * (n+1)
for i in range(1,n+1):
    min_index = -1
    for j in range(1,n+1):
        if visited[j]: continue
        if min_index == -1 or dist[min_index]>dist[j]:
            min_index = j
    
    visited[min_index] = True
    ans += dist[min_index]

    for j in range(1,n+1):
        if graph[min_index][j] == float('inf'):
            continue
        dist[j] = min(dist[j], graph[min_index][j])

# print(dist)
if ans == float('inf'):
    ans = -1
print(ans)


# for c in city:
#     print(*c)
# print('---')
# for d in dist:
#     print(*d)