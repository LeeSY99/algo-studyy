n,m,k = map(int, input().split())

graph = [[] for _ in range(n+1)]
for _ in range(m):
    a,b,d = map(int, input().split())
    graph[a].append((b,d))
    graph[b].append((a,d))

import heapq
q = [(0, 1)]
dist = [float('inf')] * (n+1)
dist[1] = 0
visited = [False] * (n+1)
count = 0
ans = 0

while q:
    now_d, now_node = heapq.heappop(q)
    if visited[now_node]: continue

    visited[now_node] = True
    ans += now_d + count * k
    if now_d != 0:
        count += 1

    for next_node, next_d in graph[now_node]:
        if dist[next_node] > next_d:
            dist[next_node] = next_d
            heapq.heappush(q, (next_d, next_node))

print(ans)
