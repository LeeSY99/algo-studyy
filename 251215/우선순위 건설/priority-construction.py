n = int(input())

graph = [[] for _ in range(n+1)]
indegree = [0] * (n+1)
times = [0] * (n+1)

for i in range(1,n+1):
    t, *pre = map(int, input().split())
    if pre[0] == -1:
        times[i] = t
        continue
    for p in pre:
        if p == -1:
            break
        graph[p].append((i,t))
        indegree[i] += 1

from collections import deque
q = deque()
dp = [float('-inf')] * (n+1)

for i in range(1,n+1):
    if indegree[i] == 0:
        q.append(i)
        dp[i] = times[i]

while q:
    x = q.popleft()
    for y, t in graph[x]:
        dp[y] = max(dp[y], dp[x] + t)
        indegree[y] -= 1
        if indegree[y] == 0:
            q.append(y)

for i in range(1,n+1):
    print(dp[i])


