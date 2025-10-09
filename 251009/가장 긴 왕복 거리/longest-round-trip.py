n,m,x = map(int, input().split())
import heapq
graph = [[] for _ in range(n+1)]

for _ in range(m):
    u,v,w = map(int, input().split())
    graph[u].append((v,w))

INF = float('inf')
def dijkstra(start):
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
distx = dijkstra(x)
for i in range(1,n+1):
    if i == x:
        continue
    dist = dijkstra(i)
    ans = max(ans, dist[x] + distx[i])
print(ans)