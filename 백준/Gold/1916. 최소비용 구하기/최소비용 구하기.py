n = int(input())
m = int(input())

graph = [[] for _ in range(n+1)]

for _ in range(m):
    a,b,c = map(int, input().split())
    graph[a].append((b,c))

s,e = map(int, input().split())
import heapq
def dijkstra(start):
    dist = [float('inf')] * (n+1)
    dist[start] = 0
    q = []
    heapq.heappush(q, (0, start))

    while q:
        now_dist, now_node = heapq.heappop(q)
        if dist[now_node] != now_dist:
            continue

        for next_node, weight in graph[now_node]:
            next_dist = now_dist + weight
            if next_dist < dist[next_node]:
                heapq.heappush(q, (next_dist, next_node))
                dist[next_node] = next_dist

    return dist


dist = dijkstra(s)
print(dist[e])