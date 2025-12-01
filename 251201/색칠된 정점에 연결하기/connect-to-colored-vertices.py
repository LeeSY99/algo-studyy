n,m,k = map(int, input().split())
colored = list(map(int, input().split()))
graph = [[] for _ in range(n+1)]

for _ in range(m):
    a,b,c = map(int, input().split())
    graph[a].append((b,c))
    graph[b].append((a,c))


import heapq
q = []
dist = [float('inf')] * (n+1)
for i in range(k):
    heapq.heappush(q,(0,colored[i]))
    dist[colored[i]] = 0
visited = [False] * (n+1)
ans = 0
while q:
    now_d, now_node = heapq.heappop(q)

    if visited[now_node]:
        continue

    visited[now_node] = True
    # print(now_d, now_node)
    ans += now_d

    for next_node, next_d in graph[now_node]:
        if dist[next_node] > next_d:
            dist[next_node] = next_d
            heapq.heappush(q, (next_d, next_node))


print(ans)