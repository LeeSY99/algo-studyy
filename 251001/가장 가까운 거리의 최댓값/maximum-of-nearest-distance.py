n,m = map(int, input().split())
a,b,c = map(int, input().split())
graph = [[] for _ in range(n+1)]
INF = float('inf')
for _ in range(m):
    s,e,w = map(int, input().split())
    graph[s].append((e,w))
    graph[e].append((s,w))

import heapq
def dijkstra(start):
    dist = [INF] * (n+1)
    dist[start] = 0
    q = [(0, start)]

    while q:
        now_d, now_node = heapq.heappop(q)

        if now_d != dist[now_node]:
            continue

        for next_node, w in graph[now_node]:
            next_d = now_d + w
            if next_d < dist[next_node]:
                dist[next_node] = next_d
                heapq.heappush(q, (next_d, next_node))

    min_dist = INF
    for i in range(1,n+1):
        if i == start:
            continue
        min_dist = min(min_dist, dist[i])
    return dist


ans = 0

dist_a = dijkstra(a)
dist_b = dijkstra(b)
dist_c = dijkstra(c)

for i in range(1,n+1):
    ans = max(ans, min(dist_a[i], dist_b[i], dist_c[i]))
# print(dijkstra(a),dijkstra(b),dijkstra(c))
print(ans)