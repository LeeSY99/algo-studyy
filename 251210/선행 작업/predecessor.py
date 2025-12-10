n = int(input())

graph = [[] for _ in range(n+1)]
indegree = [0] * (n+1)
info = [(-1,-1,-1)]

for i in range(1,n+1):
    time, pre, *pre_num = map(int, input().split())
    info.append((time, pre, pre_num))
    for p in pre_num:
        graph[p].append((i, time))
        indegree[i] += 1

import heapq
q = []
dp = [float('inf')] * (n+1)
# print(indegree)
for i in range(1,n+1):
    if indegree[i] == 0:
        heapq.heappush(q, i)
        dp[i] = info[i][0]

while q:
    x = heapq.heappop(q)

    for y, time in graph[x]:
        indegree[y] -= 1
        if indegree[y] == 0:
            dp[y] = min(dp[y], dp[x] + time)
            heapq.heappush(q,y)

print(max(dp[1:]))




