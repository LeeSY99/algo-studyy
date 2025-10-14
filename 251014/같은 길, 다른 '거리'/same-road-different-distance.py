n,m = map(int, input().split())
graph_a = [[] for _ in range(n+1)]
graph_b = [[] for _ in range(n+1)]

for _ in range(m):
    u,v, w1, w2 = map(int, input().split())
    graph_a[u].append((v,w1))
    graph_b[u].append((v,w2))
    # graph_a[u].sort(key = lambda x: x[1])
    # graph_b[u].sort(key = lambda x: x[1])

import heapq

def dijkstra(graph):
    dist = [float('inf')] * (n+1)
    dist[1] = 0
    q = [(0,1)]
    path = [0] * (n+1)

    while q:
        now_d, now_node = heapq.heappop(q)

        if now_d != dist[now_node]:
            continue

        for next_node, weight in graph[now_node]:
            next_d = now_d + weight
            if next_d < dist[next_node]:
                dist[next_node] = next_d
                heapq.heappush(q, (next_d, next_node))
                path[next_node] = now_node
    
    return path
            
path_a = dijkstra(graph_a)
path_b = dijkstra(graph_b)
x = n
vertices_a = [x]
while x != 1:
    x = path_a[x]
    vertices_a.append(x)
# print(vertices_a)

x = n
vertices_b = [x]
while x != 1:
    x = path_b[x]
    vertices_b.append(x)
# print(vertices_b)

warning_a = 0
for i in range(len(vertices_b)-1, 0, -1):
    u = vertices_b[i]
    v = vertices_b[i-1]

    short = float('inf')
    for next_node, weight in graph_a[u]:
        if weight < short:
            short = weight
    ok = False
    for next_node, weight in graph_a[u]:
        if (next_node, weight) == (v, short):
            ok = True
    if not ok:
        warning_a += 1

warning_b = 0
for i in range(len(vertices_a)-1, 0, -1):
    u = vertices_a[i]
    v = vertices_a[i-1]

    short = float('inf')
    for next_node, weight in graph_b[u]:
        if weight < short:
            short = weight
    ok = False
    for next_node, weight in graph_b[u]:
        if (next_node, weight) == (v, short):
            ok = True
    if not ok:
        warning_b += 1


# print(warning_a, warning_b)
print(min(warning_a, warning_b))