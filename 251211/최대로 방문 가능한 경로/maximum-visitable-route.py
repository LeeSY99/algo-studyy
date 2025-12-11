n,m = map(int, input().split())
graph = [[] for _ in range(n+1)]
indegree = [0] * (n+1)

for _ in range(m):
    x,y = map(int, input().split())
    graph[x].append(y)
    indegree[y] += 1

import heapq
dp = [0] * (n+1)
dp[1] = 1
q = []
#dp[i] : 1번에서 i번 노드까지 거치게 되는 노드 개수

for i in range(1,n+1):
    if indegree[i] == 0:
        heapq.heappush(q, i)
parent = [0] * (n+1)
visited = [False] * (n+1)
while q:
    x = heapq.heappop(q)
    visited[x] = True

    for y in graph[x]:
        if dp[y] < dp[x] + 1 and dp[x] > 0:
            dp[y] = dp[x] + 1
            parent[y] = x

        indegree[y] -= 1
        if indegree[y] == 0:
            heapq.heappush(q,y)


# print(*dp)
if dp[n] == 0:
    print(-1)
else:
    print(dp[n])
    if dp[n] != 0:
        path = []
        
        cur = n
        while cur != 0:
            path.append(cur)
            cur = parent[cur]
        path.reverse()
        print(*path)


# print(*parent)
            
