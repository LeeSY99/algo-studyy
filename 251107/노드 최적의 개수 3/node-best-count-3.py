import sys
sys.setrecursionlimit(100000)
n = int(input())
graph = [[] for _ in range(n+1)]
for _ in range(n-1):
    a,b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

dp = [[[0]*2 for _ in range(2)] for _ in range(n+1)]
parent = [0] * (n+1)
def dfs(x):
    visited[x] = True
    for y in graph[x]:
        if not visited[y]:
            visited[y] = True
            parent[y] = x
            dfs(y)
    dp[x][0][0] = 0
    dp[x][1][0] = 0
    dp[x][1][1] = 1

    for y in graph[x]:
        if parent[y] != x:
            continue
        dp[x][0][0] += dp[y][1][0]
        dp[x][1][0] += min(dp[y][1][1], dp[y][1][0])
        dp[x][1][1] += min(min(dp[y][0][0], dp[y][1][0]), dp[y][1][1])

    if dp[x][1][0] == 0:
        dp[x][1][0] = float('inf')
    else:
        best = float('inf')
        for y in graph[x]:
            if parent[y] != x:
                continue
            best = min(best, dp[x][1][0] - min(dp[y][1][1], dp[y][1][0]) + dp[y][1][1])
        dp[x][1][0] = best    
        
    
visited = [False] * (n+1)
dfs(1)
print(min(dp[1][1][0], dp[1][1][1]))
