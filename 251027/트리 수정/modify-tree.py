import sys
sys.setrecursionlimit(2000)
n = int(input())
graph = [[] for _ in range(n)]
removed = [[False]*n for _ in range(n)]
edges = []

visited = [False] * n
dist = [0] * n
max_dist = 0
fatherest = None

for _ in range(n-1):
    a,b,w = map(int, input().split())
    graph[a].append((b,w))
    graph[b].append((a,w))
    edges.append((a,b,w))

def dfs(x):
    global max_dist, fatherest
    for y,d in graph[x]:
        if removed[x][y]:
            continue
        if visited[y]:
            continue
        visited[y] = True
        dist[y] = dist[x] + d
        if dist[y] > max_dist:
            max_dist = dist[y]
            fatherest = y

        dfs(y)

def get_diameter(x):
    global max_dist, fatherest
    for i in range(n):
        visited[i] = False
        dist[i] = 0
    max_dist = 0
    fatherest = x

    visited[x] = True
    dfs(x)

    for i in range(n):
        visited[i] = False
        dist[i] = 0
    visited[fatherest] = True
    dfs(fatherest)

    return max_dist

ans = 0
for i in range(n-1):
    u,v,d = edges[i]
    removed[u][v] = True
    removed[v][u] = True

    # print(get_diameter(u) , get_diameter(v))
    max_diameter = d + get_diameter(u) + get_diameter(v)
    ans = max(ans, max_diameter)

    removed[u][v] = False
    removed[v][u] = False

print(ans)

