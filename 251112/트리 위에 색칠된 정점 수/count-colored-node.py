n = int(input())
graph = [[] for _ in range(n+1)]
for _ in range(n-1):
    a,b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

k = int(input())
colored = [False] * (n+1)
for _ in range(k):
    a = int(input())
    colored[a] = True

def dfs(x):
    visited[x] = True
    for y in graph[x]:
        if visited[y]: continue
        parent[0][y] = x
        if colored[y]:
            c_count[y] = c_count[x] + 1
        else:
            c_count[y] = c_count[x]
        depth[y] = depth[x] + 1
        dfs(y)

import math
MAX_H = int(math.log(100000,2)) + 1
c_count = [0] * (n+1)
if colored[1]:
    c_count[1] = 1
parent = [[0] * (n+1) for _ in range(MAX_H + 1)]
visited = [False] * (n+1)
depth = [0] * (n+1)

dfs(1)

for h in range(1,MAX_H+1):
    for i in range(1, n+1):
        parent[h][i] = parent[h-1][parent[h-1][i]]

def lca(a,b):
    if depth[a] <  depth[b]:
        return lca(b,a)
    
    for h in range(MAX_H, -1, -1):
        if depth[a] - depth[b] >= (1<<h):
            a = parent[h][a]
    
    if a == b:
        return a

    for h in range(MAX_H, -1, -1):
        if parent[h][a] != parent[h][b]:
            a = parent[h][a]
            b = parent[h][b]
    
    return parent[0][a]
# print(colored)
# print(c_count)
q = int(input())
for _ in range(q):
    a,b = map(int, input().split())
    l = lca(a,b)
    print(c_count[a] + c_count[b] - 2*c_count[l] + colored[l])