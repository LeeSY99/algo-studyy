n = int(input())

graph = [[] for _ in range(n+1)]
indegree = [0] * (n+1)
times = [0] * (n+1)

for i in range(1,n+1):
    time, pre, *pre_num = map(int, input().split())
    times[i] = time
    for p in pre_num:
        graph[p].append((i))
        indegree[i] += 1

import heapq
q = []
# dp = [float('inf')] * (n+1)
dp = [0] * (n+1)
# print(indegree)
for i in range(1,n+1):
    if indegree[i] == 0:
        heapq.heappush(q, i)
        dp[i] = times[i]

while q:
    x = heapq.heappop(q)
    for y in graph[x]:
        indegree[y] -= 1
        dp[y] = max(dp[y], dp[x] + times[y])
        if indegree[y] == 0:
            heapq.heappush(q,y)

# print(dp)
print(max(dp[1:]))




