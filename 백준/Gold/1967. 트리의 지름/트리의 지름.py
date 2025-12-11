import sys
sys.setrecursionlimit(100000)
n = int(input())
graph = [[] for _ in range(n+1)]

for _ in range(n-1):
    a,b,d = map(int, input().split())
    graph[a].append((b,d))
    graph[b].append((a,d))


def dfs(x):
    visited[x] = True
    for y, d in graph[x]:
        if visited[y]: continue
        dist[y] = dist[x] + d
        dfs(y)

dist = [0] * (n+1)
visited = [False] * (n+1)
dfs(1)

max_node = 0
max_dist = 0
for i in range(1,n+1):
    if dist[i] > max_dist:
        max_node = i
        max_dist = dist[i]

dist = [0] * (n+1)
visited = [False] * (n+1)
dfs(max_node)

print(max(dist))




