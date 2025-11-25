import sys
sys.setrecursionlimit(1000000)
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
        dfs(y)

visited = [False] * (n+1)
parent = [0] * (n+1)

dfs(1)
for i in range(2,n+1):
    print(parent[i])