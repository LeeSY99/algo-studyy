n,d = map(int, input().split())
graph = [[] for _ in range(n+1)]

for _ in range(n-1):
    a,b,w = map(int, input().split())
    graph[a].append((b,w))
    graph[b].append((a,w))

## 가장 많은 간선 찾기
def dfs(x):
    for y,w in graph[x]:
        if not visited[y]:
            visited[y] = True
            edges[y] = edges[x]+1
            dist[y] = dist[x] + w
            dfs(y)

visited = [False] * (n+1)
visited[1] = True
edges = [0] * (n+1)
dist = [0] * (n+1)
dfs(1)
largest_edge = 0
largest_dist = float('inf')
largest_node = None
for i in range(1,n+1):
    if (edges[i], -dist[i]) > (largest_edge, -largest_dist):
        largest_dist = dist[i]
        largest_edge = edges[i]
        largest_node = i
# print(largest_node)

visited = [False] * (n+1)
visited[largest_node] = True
edges = [0] * (n+1)
dist = [0] * (n+1)
dfs(largest_node)

largest_edge = 0
largest_dist = float('inf')
largest_node = None
for i in range(1,n+1):
    if (edges[i], -dist[i]) > (largest_edge, -largest_dist):
        largest_dist = dist[i]
        largest_edge = edges[i]
        largest_node = i

# print(edges)
# print(dist, largest_node)
print((dist[largest_node] + d - 1)//d)
