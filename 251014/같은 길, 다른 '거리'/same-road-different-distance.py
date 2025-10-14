n,m = map(int, input().split())
graph_a = [[] for _ in range(n+1)]
graph_b = [[] for _ in range(n+1)]
graph_a_r = [[] for _ in range(n+1)]
graph_b_r = [[] for _ in range(n+1)]

for _ in range(m):
    u,v, w1, w2 = map(int, input().split())
    graph_a[u].append((v,w1))
    graph_b[u].append((v,w2))
    graph_a_r[v].append((u,w1))
    graph_b_r[v].append((u,w2))
    # graph_a[u].sort(key = lambda x: x[1])
    # graph_b[u].sort(key = lambda x: x[1])

import heapq

def dijkstra(start,graph):
    dist = [float('inf')] * (n+1)
    dist[start] = 0
    q = [(0,start)]

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

def calc(dist_a, dist_b):
    dist = [float('inf')] * (n+1)
    dist[1] = 0
    q = [(0,1)]

    while q:
        now_d, now_node = heapq.heappop(q)

        if now_d != dist[now_node]:
            continue

        length = len(graph_a[now_node])
        for j in range(length):
            next_node, weight_a = graph_a[now_node][j]
            next_node, weight_b = graph_b[now_node][j]
            
            target_dist = 0
            if dist_a[next_node] + weight_a != dist_a[now_node]:
                target_dist += 1
            if dist_b[next_node] + weight_b != dist_b[now_node]:
                target_dist += 1

            new_dist = dist[now_node] + target_dist
            if new_dist < dist[next_node]:
                dist[next_node] = new_dist
                heapq.heappush(q, (new_dist, next_node))
    # print(dist)
    return dist[n]

dist_a = dijkstra(n, graph_a_r)
dist_b = dijkstra(n, graph_b_r)
print(calc(dist_a, dist_b))
