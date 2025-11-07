import sys
sys.setrecursionlimit(10000)
n = int(input())
graph = [[] for _ in range(n+1)]
parent = [0] * (n+1)
for _ in range(n-1):
    a,b = map(int, input().split())
    graph[a].append(b)
    parent[b] = a

for i in range(1,n+1):
    if parent[i] == 0:
        root = i
        break
a,b = map(int, input().split())
depth = [0] * (n+1)

def dfs(x):
    for y in graph[x]:
        depth[y] = depth[x] +1
        dfs(y)

def get_lca(a,b):
    while depth[a] != depth[b]:
        if depth[a] > depth[b]:
            a = parent[a]
        else:
            b = parent[b]
    while a != b:
        a = parent[a]
        b = parent[b]
    return a


dfs(root)
print(get_lca(a,b))
