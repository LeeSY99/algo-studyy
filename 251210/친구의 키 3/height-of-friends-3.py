n,m = map(int, input().split())

graph = [[] for _ in range(n+1)]
indegree = [0] * (n+1)

for _ in range(m):
    a,b = map(int, input().split())
    graph[a].append(b)
    indegree[b] += 1

import heapq
q = []

for i in range(1,n+1):
    if indegree[i] == 0:
        heapq.heappush(q,i)

ans = []
visited = [False] * (n+1)
while q:
    x = heapq.heappop(q)

    ans.append(x)
    visited[x] = True
    for y in graph[x]:
        indegree[y] -= 1
        if indegree[y] == 0:
            heapq.heappush(q,y)

is_cycle=False
for i in range(1,n+1):
    if not visited[i]:
        is_cycle=True

if is_cycle:
    print(-1)
else:
    print(*ans)