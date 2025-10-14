n,m = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    i,j,d = map(int, input().split())
    graph[i].append((j,d))
    graph[j].append((i,d))

import heapq
def dijkstra():
    dist = [float('inf')] * (n+1)
    dist[n] = 0
    q = [(0,n)]

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

dist = dijkstra()
print(max(dist[1:]))
