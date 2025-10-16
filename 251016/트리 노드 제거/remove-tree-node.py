n = int(input())
parent = list(map(int, input().split()))
delete = int(input())

edges = [[] for _ in range(n)]
for x in range(1,n):
    y = parent[x]
    edges[x].append(y)

def dfs(x):
    global ans
    if x == delete:
        return
    if len(edges[x]) == 0:
        ans += 1
    for y in edges[x]:
        if not visited[y]:
            visited = y
            ans += 1
            dfs(y)
visited = [False] * n
visited[0] = True
ans = 0
dfs(0)
print(ans)


