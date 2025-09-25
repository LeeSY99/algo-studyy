import heapq
n,m = map(int, input().split())
graph = [[] for _ in range(n+1)]

for _ in range(m):
    s, e, w = map(int, input().split())
    graph[e].append((s,w))
# print(graph)
def dijkstra():
    dist = [float('inf')] * (n+1)
    dist[n] = 0
    q = []
    heapq.heappush(q, (0, n))
    # print(q)
    while q:
        now_d, now_node = heapq.heappop(q)

        if dist[now_node] != now_d:
            continue

        for next_node, weight in graph[now_node]:
            next_d = now_d + weight
            if next_d < dist[next_node]:
                dist[next_node] = next_d
                heapq.heappush(q, (next_d, next_node))

    return dist

dist = dijkstra()
ans = 0
for i in range(1,n):
    if dist[i] == float('inf'):
        continue
    ans = max(ans, dist[i])
# print(dist)
print(ans)