import math, sys
sys.setrecursionlimit(50000)
n = int(input())
MAX_H = int(math.log(50000, 2)) + 1

graph = [[] for _ in range(n+1)]
for _ in range(n-1):
    a,b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(x):
    visited[x] = True

    for y in graph[x]:
        if visited[y]: continue
        parent[0][y] = x
        depth[y] = depth[x] + 1
        dfs(y)

parent = [[0] * (n+1) for _ in range(MAX_H+1)]
visited = [False] * (n+1)
depth = [0] * (n+1)
dfs(1)

def lca(a,b):
    if depth[a] <  depth[b]:
        return lca(b,a)

    for h in range(MAX_H-1,-1,-1):
        if depth[a] - depth[b] >= (1<<h):
            a = parent[h][a]
    if a == b:
        return a
    
    for h in range(MAX_H-1,-1,-1):
        if parent[h][a] != parent[h][b]:
            a = parent[h][a]
            b = parent[h][b]
    return parent[0][a]

for h in range(1, MAX_H + 1):
    for i in range(1, n+1):
        parent[h][i] = parent[h-1][parent[h-1][i]]

q = int(input())
for _ in range(q):
    a,b,c = map(int, input().split())
    print(lca(lca(a,b),c))