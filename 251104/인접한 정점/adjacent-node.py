import sys
sys.setrecursionlimit(10000)
n = int(input())
nums = [0] + list(map(int, input().split()))

graph = [[] for _ in range(n+1)]
for _ in range(n-1):
    a,b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

#dp[i][0] : i번 정점 선택안하고 합 최대
#dp[i][1] : i번 정점 선택하고 합 최대
dp = [[0] * 2 for _ in range(n+1)]


def dfs(x):
    visited[x] = True
    dp[x][1] = nums[x]
    for y in graph[x]:
        if visited[y] : continue
        dfs(y)
        dp[x][0] += max(dp[y][0], dp[y][1])
        dp[x][1] +=  dp[y][0] 
        # dfs(y)

visited = [False] * (n+1)
dfs(1)
# for d in dp:
#     print(*d)
print(max(dp[1]))
