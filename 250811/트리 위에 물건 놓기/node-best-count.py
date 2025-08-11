n = int(input())
graph = [[] for _ in range(n+1)]
parent = [0] * (n + 1)
visited = [False] * (n + 1)
import sys
sys.setrecursionlimit(100000)

for _ in range(n-1):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

import sys
#dp[i][0] 물건 안놓음 dp[i][1] 놓음
dp = [[0]*2 for _ in range(n+1)]

def dfs(u):
    for v in graph[u]:
        if not visited[v]:
            visited[v] = True
            parent[v] = u
            dfs(v)

    dp[u][0] = 0
    dp[u][1] = 1

    for v in graph[u]:
        if parent[v] != u:
            continue

        dp[u][0] += dp[v][1]
        dp[u][1] += min(dp[v][0], dp[v][1])

visited[1] = True
dfs(1)


print(min(dp[1][0], dp[1][1]))