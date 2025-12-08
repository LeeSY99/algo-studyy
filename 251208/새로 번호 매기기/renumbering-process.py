n,m = map(int, input().split())
ans = [0] * (n+1)
graph = [[] for _ in range(n+1)]
indegree = [0] * (n+1)

for _ in range(m):
    x,y = map(int, input().split())
    graph[y].append(x)
    indegree[x] += 1

import heapq
q = []
for i in range(1, n+1):
    if indegree[i] == 0:
        heapq.heappush(q, -i)

visited = [False] * (n+1)
idx =n
while q:
    x = -heapq.heappop(q)
    visited[x] = True
    ans[x] = idx
    idx -= 1

    for y in graph[x]:
        indegree[y] -= 1
        if indegree[y] == 0:
            heapq.heappush(q, -y)

is_cycle=False  
for i in range(1, n+1):
    if not visited[i]:
        is_cycle = True

if is_cycle:
    print(-1)
else:
    # print(ans)
    for i in range(1, n+1):
        print(ans[i], end = ' ')