n,m,k = map(int, input().split())
cost_from_center = [0] + list(map(int, input().split()))
graph = [[] for _ in range(n+1)]

for _ in range(m):
    a,b = map(int, input().split())
    cost = cost_from_center[a]+cost_from_center[b]
    graph[a].append((b, cost))

import heapq

def prim():
    q = [(0,1)]
    dist = [float('inf')] * (n+1)
    visited = [False] * (n+1)
    dist[1] = 0
    cost =0

    while q:
        now_d, now_node = heapq.heappop(q)

        if visited[now_node]:
            continue
        
        visited[now_node] = True
        cost += now_d

        for next_node, next_d in graph[now_node]:
            if dist[next_node] > next_d:
                dist[next_node] = next_d
                heapq.heappush(q, (next_d, next_node))
    return cost

if prim() > k:
    print(0)
else:
    print(1)
# print(prim())
    


