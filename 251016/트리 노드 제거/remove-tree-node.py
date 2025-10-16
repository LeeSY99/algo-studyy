n = int(input())
parent = list(map(int, input().split()))
delete = int(input())
is_deleted = [False] * (n)

edges = [[] for _ in range(n)]
for x in range(n):
    y = parent[x]
    if y == -1:
        root = x
        continue
    edges[y].append(x)

# print(edges)
def dfs(x):
    global ans
    if is_deleted[x]:
        return

    is_leaf = True
    for y in edges[x]:
        if is_deleted[y]:
            continue
        dfs(y)
        is_leaf = False
    if is_leaf:
        ans += 1


is_deleted[delete] = True
ans = 0
dfs(root)
print(ans)


