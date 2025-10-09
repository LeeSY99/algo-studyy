n,m = map(int, input().split())
r1, r2 = map(int, input().split())
graph = [[] for _ in range(n+1)]
INF = float('inf')
import heapq

for _ in range(m):
    i,j,v = map(int, input().split())
    graph[i].append((j, v))
    graph[j].append((i, v))

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
    
    return dist

dist1 = dijkstra(r1)
dist2 = dijkstra(r2)
ans = INF

for i in range(1, n+1):
    if i == r1 or i == r2:
        continue
    #검정 i -> r1 -> r2 -> 검정i
    ans = min(ans, dist1[i]+dist1[r2]+dist2[i])
    #검정 i -> r2 -> r1 -> 검정 i
    ans = min(ans, dist2[i]+dist2[r1]+dist1[i])

if ans == INF:
    ans = -1
print(ans)
