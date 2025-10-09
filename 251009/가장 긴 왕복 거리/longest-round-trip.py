n,m,x = map(int, input().split())
import heapq
graph = [[] for _ in range(n+1)]
r_graph = [[] for _ in range(n+1)]
edges = []
for _ in range(m):
    u,v,w = map(int, input().split())
    graph[u].append((v,w))
    r_graph[v].append((u,w))

INF = float('inf')
def dijkstra(start, graph):
    dist = [INF]*(n+1)
    dist[start] = 0
    q = [(0,start)]

    while q:
        now_d, now_node = heapq.heappop(q)

        if now_d != dist[now_node]:
            continue

        for next_node, weight in graph[now_node]:
            next_d = now_d + weight
            if next_d < dist[next_node]:
                dist[next_node] = next_d
                heapq.heappush(q, (next_d, next_node))

    return dist

ans = 0
# x -> i
dist_to_i = dijkstra(x, graph)
# i -> x
dist_to_x = dijkstra(x, r_graph)
for i in range(1,n+1):
    if i == x:
        continue
    ans = max(ans, dist_to_i[i] + dist_to_x[i])
print(ans)

## 다른 풀이
## x -> i 다익스트라 1번
## i -> x 간선 뒤집어서 다익스트라 1번
## dist1[i] + dist[i]
## 인접 리스트로 풀기