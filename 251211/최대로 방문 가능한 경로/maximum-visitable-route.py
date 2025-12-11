n,m = map(int, input().split())
graph = [[] for _ in range(n+1)]
indegree = [0] * (n+1)

for _ in range(m):
    x,y = map(int, input().split())
    graph[y].append(x)
    indegree[x] += 1

import heapq
dp = [-1] * (n+1)
dp[n] = 0
q = []
#dp[i] : 1번에서 i번 노드까지 거치게 되는 노드 개수

for i in range(1,n+1):
    if indegree[i] == 0:
        heapq.heappush(q, i)
parent = [0] * (n+1)
visited = [False] * (n+1)
while q:
    x = heapq.heappop(q)

    for y in graph[x]:
        if dp[x] != -1:
            if dp[y] < dp[x] + 1:
                dp[y] = dp[x] + 1
                parent[y] = x
            elif dp[y] == dp[x] + 1 and parent[y] > x:
                parent[y] = x

        indegree[y] -= 1
        if indegree[y] == 0:
            heapq.heappush(q,y)



if dp[1] != -1:
    
    path = [1]
    cur = 1
    
    while cur != n:
        cur = parent[cur]
        path.append(cur)
    print(len(path))
    print(*path)
else:
    print(-1)

# print(*parent)
            
