import heapq

V,e = map(int, input().split())
k = int(input())
graph = [[] for _ in range(V+1)]

for i in range(e):
    u,v,w = map(int, input().split())
    graph[u].append((v,w))

def dijkstra(start):
    dist = [float('inf')] * (V+1)
    dist[start] = 0
    q = [(0, start)]

    while q:
        now_dist, now_node = heapq.heappop(q)

        if now_dist != dist[now_node]:
            continue

        for next_node, weight in graph[now_node]:
            next_dist = now_dist + weight
            if next_dist < dist[next_node]:
                dist[next_node] = next_dist
                heapq.heappush(q, (next_dist, next_node))
    return dist

dist = dijkstra(k)
# print(dist)
for i in range(1,V+1):
    if dist[i] == float('inf'):
        print("INF")
    else:
        print(dist[i])