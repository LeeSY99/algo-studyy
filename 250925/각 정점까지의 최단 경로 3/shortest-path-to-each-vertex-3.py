import heapq, sys

n,m = map(int, input().split())
graph = [[] for _ in range(n+1)]
distance = [float('inf')] * (n+1)


for _ in range(m):
    u,v,w = map(int, input().split())
    graph[u].append((v, w))


def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        now_d, now_node = heapq.heappop(q)
        if now_d != distance[now_node]:
            continue
        
        for next_node, weight in graph[now_node]:
            next_d = now_d + weight
            if next_d < distance[next_node]:
                distance[next_node] = next_d
                heapq.heappush(q,(next_d, next_node))

dijkstra(1)
for i in range(2, n+1):
    if distance[i] == float('inf'):
        print(-1)
    else:
        print(distance[i])



