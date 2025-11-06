import sys
sys.setrecursionlimit(1000000)
n,m = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(n-1):
    a,b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

a = list(map(int, input().split()))
a = set(a)
dp = [[0]*2 for _ in range(n+1)]
for node in a:
    dp[node][1] += 1

def dfs(x):
    visited[x] = True
    must_pick = (x in a)

    dp[x][1] = 0 if must_pick else 1
    dp[x][0] = float('inf') if must_pick else 0

    for y in graph[x]:
        if visited[y]: continue
        dfs(y)
        if dp[x][0] < float('inf'):
            dp[x][0] += dp[y][1]
        dp[x][1] += min(dp[y][0], dp[y][1])

visited = [False]*(n+1)
dfs(1)
print(min(dp[1]))
