n,m = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    s,e,w = map(int, input().split())
    graph[s].append((e,w))
    graph[e].append((s,w))

A, B = map(int, input().split())
import heapq

def dijkstra(start):
    dist = [float('inf')] * (n+1)
    dist[start] = 0
    q = []
    heapq.heappush(q, (0, start))

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

dist = dijkstra(B)
route = []
x = A
while True:
    route.append(x)
    if x == B:
        break
    nxt = None
    best = 1001
    for v, w in graph[x]:
        if dist[x] == w + dist[v]:
            if v < best:
                best = v
                nxt = v
    if nxt is None:
        break
    x = nxt

# print(dist)
print(dist[A])
print(*route)