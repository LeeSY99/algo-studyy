n,m = map(int, input().split())

graph = [[] for _ in range(n+1)]
indegree =[0] *(n+1)
use_edge = [False] * (n+1)

for _ in range(m):
    a, b, d = map(int, input().split())
    graph[a].append((b,d))
    indegree[b] += 1

from collections import deque
q = deque()
dist = [0] * (n+1)
parent = [[] for _ in range(n+1)]
for i in range(1, n+1):
    if indegree[i] == 0:
        q.append(i)

while q:
    x = q.popleft()
    for y, d in graph[x]:
        if dist[x] + d > dist[y]:
            parent[y] = [x]
            dist[y] = dist[x] + d
        elif dist[x] + d == dist[y]:
            parent[y].append(x)
        indegree[y] -= 1
        if indegree[y] == 0:
            q.append(y)

ans = 0
# print(parent)
for p in parent:
    ans += len(p)
print(dist[n], ans)


