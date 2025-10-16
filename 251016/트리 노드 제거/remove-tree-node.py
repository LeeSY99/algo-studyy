n = int(input())
parent = list(map(int, input().split()))
delete = int(input())

edges = [[] for _ in range(n)]
for x in range(n):
    y = parent[x]
    if y == -1:
        continue
    if x == delete or y == delete:
        continue
    edges[y].append(x)

# print(edges)
def dfs(x):
    global ans
    if x == delete:
        return
    if len(edges[x]) == 0:
        # print(x, len(edges[x]))
        ans += 1
    for y in edges[x]:
        if not visited[y]:
            visited[y] = True
            dfs(y)

visited = [False] * n
for i in range(n):
    if parent[i] == -1:
        root = i
# print('root', root)
visited[root] = True
ans = 0
dfs(root)
print(ans)


