n,m,k = map(int, input().split())
cost_from_center = [0] + list(map(int, input().split()))
graph = [[] for _ in range(n+1)]
blocked = [False] * (n+1)

for i in range(1,n+1):
    graph[0].append((i, cost_from_center[i]))
    graph[i].append((0, cost_from_center[0]))

for _ in range(m):
    a,b = map(int, input().split())
    if a>b:
        a,b = b,a

    if a==1 and b == n:
        blocked[b] = True
    else:
        blocked[a] = True

for i in range(1, n+1):
    if blocked[i]:
        continue
    a = i
    b = i+1
    if a == n:
        b = 1
    graph[a].append((b, 0))
    graph[b].append((a, 0))

import heapq

def prim():
    q = [(0,0)]
    dist = [float('inf')] * (n+1)
    visited = [False] * (n+1)
    dist[0] = 0
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
if m <= 1:
    print(1)
    exit(0)

if prim() > k:
    print(0)
else:
    print(1)
# print(prim())
    


