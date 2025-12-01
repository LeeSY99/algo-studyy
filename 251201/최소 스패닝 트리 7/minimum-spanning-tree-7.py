import sys
sys.setrecursionlimit(40000)
n,m = map(int, input().split())
graph = [[] for _ in range(n+1)]

for _ in range(m):
    a,b,c = map(int, input().split())
    graph[a].append((b,c))
    graph[b].append((a,c))

import heapq
dist = [float('inf')] * (n+1)
dist[1] = 0
q = [(0, 1)]
visited = [False] * (n+1)
cost = 0
mst_edges = []
mst_graph = [[] for _ in range(n+1)]
dist_from = [0] * (n+1)

while q:
    now_d, now_node = heapq.heappop(q)

    if visited[now_node]: continue

    visited[now_node] = True
    cost += now_d

    if now_node != 1:
        mst_edges.append((min(dist_from[now_node], now_node),
        max(dist_from[now_node], now_node),dist[now_node]))

    for next_node, next_d in graph[now_node]:
        if dist[next_node] > next_d:
            dist[next_node] = next_d
            heapq.heappush(q, (next_d, next_node))
            dist_from[next_node] = now_node

print(cost)


def dfs(x):
    global last_node, max_dist
    visited[x] = True
    for y, d in mst_graph[x]:
        if visited[y]: continue
        dist[y] = dist[x] + d
        if dist[y] > max_dist:
            max_dist = dist[y]
            last_node = y
        dfs(y)

for x, y, d in mst_edges:
    mst_graph[x].append((y, d))
    mst_graph[y].append((x, d))
    
max_dist = 0
visited = [False] * (n+1)
dist = [0]* (n+1)
last_node = 0
dfs(1)

visited = [False] * (n+1)
dist = [0]* (n+1)
dfs(last_node)
print(max_dist)
