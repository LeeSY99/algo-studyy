n,m = map(int, input().split())
import heapq
graph = [[False] * (n+1) for _ in range(n+1)]
for _ in range(m):
    a,b,v = map(int, input().split())
    graph[a][b] = v
    graph[b][a] = v



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

dist,path = dijkstra()
# print(dist)
x = n
vertices =[x]
while x != 1:
    x = path[x]
    vertices.append(x)
vertices = vertices[::-1]

max_dist = 0
for i in range(len(vertices)-1):
    prev, next = vertices[i], vertices[i+1]
    graph[prev][next] *= 2
    now_dist, _ = dijkstra()
    max_dist = max(max_dist, now_dist)
    graph[prev][next] //= 2
    

print(max_dist - dist)