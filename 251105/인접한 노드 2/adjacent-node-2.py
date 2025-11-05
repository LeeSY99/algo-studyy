n = int(input())
nums = [0] + list(map(int, input().split()))
graph = [[] for _ in range(n+1)]
for _ in range(n-1):
    a,b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

#dp[i][0] : i번 블록 선택 안함
#dp[i][1] : i번 블록 선택 함 -> 리프에서부터 올라오면서 최대 
dp = [[0] * 2 for _ in range(n+1)]
selected = []
def dfs(x):
    visited[x] = True
    dp[x][1] = nums[x]
    for y in graph[x]:
        if visited[y]: continue
        dfs(y)

        dp[x][0] += max(dp[y][0], dp[y][1])
        dp[x][1] += dp[y][0]

visited = [False] * (n+1)
dfs(1)
print(max(dp[1]))


def recover(x, p_choose):
    visited[x] = True
    if p_choose:
        c_choose = False
    else:
        c_choose = dp[x][0] < dp[x][1]

    if c_choose:
        selected.append(x)
        for y in graph[x]:
            if visited[y]: continue
            recover(y, True)
    else:
        for y in graph[x]:
            if visited[y]: continue
            recover(y, False)
visited = [False] * (n+1)
recover(1, False)
selected.sort()
print(*selected)

