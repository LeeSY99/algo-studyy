import math
n = int(input())
graph = [[] for _ in range(n+1)]
for _ in range(n-1):
    a,b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)


def dfs(x):
    visited[x] = True
    for y in graph[x]:
        if visited[y]: continue
        parent[y] = x
        depth[y] = depth[x] + 1
        dfs(y)
MAX_H = int(math.log(100000,2)) + 1
print(MAX_H)
visited = [False] * (n+1)
parent = [[0] * (n+1) for _ in range(MAX_H)]  
depth = [0] * (n+1)

q = int(input())

for _ in range(q):
    a,b = map(int, input().split())