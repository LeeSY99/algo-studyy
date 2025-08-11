n, r, q = map(int, input().split())
graph = [[] for _ in range(n+1)]
parent = [[] for _ in range(n+1)]
visited = [False] * (n+1)

for _ in range(n-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)


sub_trees = [0] * (n+1)

def dfs(x):
    visited[x] = True

    for y in graph[x]:
        if visited[y]:
            continue
        parent[y] = x
        visited[y] = True
        dfs(y)

    sub_trees[x] = 1
    for y in graph[x]:
        if parent[y] != x:
            continue
        sub_trees[x] += sub_trees[y]

dfs(r)
# print(sub_trees)
for _ in range(q):
    u = int(input())
    print(sub_trees[u])
    

