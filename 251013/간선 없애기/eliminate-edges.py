n,m = map(int, input().split())
graph = [[0]*(n+1) for _ in range(n+1)]
for _ in range(m):
    u,v,w = map(int, input().split())
    graph[u][v] = w
    graph[v][u] = w

import heapq
def dijkstra():
    dist = [float('inf')] * (n+1)
    dist[1] = 0
    q = [(0, 1)]
    path = [0] * (n+1)

    while q:
        now_d, now_node = heapq.heappop(q)

        if now_d != dist[now_node]:
            continue
        
        for next_node in range(1, n+1):
            if not graph[now_node][next_node]:
                continue
            next_d = now_d + graph[now_node][next_node]
            if next_d < dist[next_node]:
                dist[next_node] = next_d
                heapq.heappush(q, (next_d, next_node))
                path[next_node] = now_node

    return dist[n], path

now_dist, path = dijkstra()

x = n
verc = [x]
while x != 1:
    x = path[x]
    verc.append(x)
verc = verc[::-1]

ans = 0
for i in range(len(verc)-1):
    temp = graph[verc[i]][verc[i+1]]
    graph[verc[i]][verc[i+1]] = 0
    next_dist, _ = dijkstra()
    if now_dist != next_dist:
        ans += 1
    graph[verc[i]][verc[i+1]] = temp
print(ans)

        
