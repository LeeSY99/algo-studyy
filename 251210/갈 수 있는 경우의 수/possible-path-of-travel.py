n,m = map(int, input().split())

graph = [[] for _ in range(n+1)]
indegree = [0] * (n+1)

for _ in range(m):
    x,y = map(int, input().split())
    graph[x].append(y)
    indegree[y] += 1

import heapq
q = []
dp = [0] * (n+1)
for i in range(1,n+1):
    if indegree[i] == 0:
        heapq.heappush(q, i)
dp[1] = 1
A = 1000000007
while q:
    x = heapq.heappop(q)
    for y in graph[x]:
        indegree[y] -= 1
        dp[y] = (dp[y] + dp[x]) % A
        if indegree[y] == 0:
            
            heapq.heappush(q, y)

print(dp[n])
