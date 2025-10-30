n = int(input())
graph = [[] for _ in range(n+1)]
for _ in range(n-1):
    a,b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
# i번 노드까지 고려
#dp[i][0] = i노드에 물건 놓지 않음
#dp[i][1] = i노드에 물건 놓음
dp = [[float('inf')]*(2) for _ in range(n+1)]
dp[1][0] = 0
dp[1][1] = 1
visited = [False] * (n+1)
parent = [0] * (n + 1)

def dfs(x):
    visited[x] = True
    for y in graph[x]:
        if not visited[y]:
            parent[y] = x
            dfs(y)

    dp[x][0] = 0
    dp[x][1] = 1

    for y in graph[x]:
        if parent[y] != x: continue

        dp[x][0] += dp[y][1]
        dp[x][1] += min(dp[y][0], dp[y][1])

dfs(1)
print(min(dp[1]))
