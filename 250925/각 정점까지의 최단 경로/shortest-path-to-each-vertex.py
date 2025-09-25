import heapq
n,m = map(int, input().split())
k = int(input())

graph = [[] for _ in range(n+1)]
for _ in range(m):
    s, e, w = map(int, input().split())
    graph[s].append((e,w))
    graph[e].append((s,w))

def dijkstra(start):
    dist = [float('inf')] * (n+1)
    q = []
    heapq.heappush(q, (0, start))
    dist[start] = 0

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

dist = dijkstra(k)
for i in range(1,n+1):
    if dist[i] == float('inf'):
        print(-1)
    else:
        print(dist[i])