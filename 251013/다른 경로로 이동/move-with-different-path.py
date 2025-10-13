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
    q = [(0,1)]
    # path = [0]*(n+1)

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

    return dist

dist_A = dijkstra()
x = n
path_A = [x]
while x != 1:
    for i in range(1, n+1):
        if graph[i][x] == 0:
            continue
        
        if dist_A[i] + graph[i][x] == dist_A[x]:
            x = i
            break
    
    path_A.append(x)
path_A = path_A[::-1]

for i in range(len(path_A)-1):
    x = path_A[i]
    y = path_A[i+1]
    graph[x][y] = 0
    graph[y][x] = 0

dist_B = dijkstra()
ans = dist_B[n]
if ans == float('inf'):
    ans = -1

print(ans)



        

        