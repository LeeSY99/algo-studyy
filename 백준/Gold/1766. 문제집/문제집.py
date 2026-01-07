n,m = map(int, input().split())

graph = [[] for _ in range(n+1)]
indegree = [0] *(n+1)

for _ in range(m):
    a,b = map(int, input().split())
    graph[a].append(b)
    indegree[b] += 1

import heapq
q = []
for i in range(1,n+1):
    if indegree[i] == 0:
        heapq.heappush(q,i)

solved = []
while q:
    x = heapq.heappop(q)
    solved.append(x)

    for y in graph[x]:
        indegree[y] -= 1
        if indegree[y] == 0:
            heapq.heappush(q, y)

print(*solved)