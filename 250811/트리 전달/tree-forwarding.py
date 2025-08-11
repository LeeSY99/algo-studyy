'''
i w -> i번 노드에서 점수 w획득, 
        자식노드들을 c라하면 c w연산 수행 '''


n, m = map(int, input().split())

parent = [0] + list(map(int, input().split()))
graph = [[] for _ in range(n + 1)]
dp = [0] * (n + 1)

for i in range(1,n+1):
    x = parent[i]
    y = i

    if x == -1:
        continue

    graph[x].append(y)

def dfs(x):
    for y in graph[x]:
        dp[y] += dp[x]
        dfs(y)

for _ in range(m):
    i, w = map(int, input().split())
    dp[i] += w

dfs(1)
print(*dp[1:])