n,m = map(int, input().split())

graph = [[] for _ in range(n+1)]
indegree = [0] * (n+1)

for _ in range(m):
    a,b = map(int, input().split())
    graph[a].append(b)
    indegree[b] += 1

import heapq
q = []
dp = [0] * (n+1)
count = [0] * (n+1)

for i in range(1, n+1):
    if indegree[i] == 0:
        heapq.heappush(q,i)
        dp[i] = 1


while q:
    x = heapq.heappop(q)
    for y in graph[x]:
        indegree[y] -= 1
        if dp[x] > dp[y]:
            dp[y] = dp[x]
            count[y] = 1
        elif dp[x] == dp[y]:
            count[y] += 1

        # print(count[y])
        # print('---')
        if indegree[y] == 0:
            if count[y] >= 2:
                dp[y] +=1
            heapq.heappush(q, y)

# print(count)
print(max(dp[1:]))