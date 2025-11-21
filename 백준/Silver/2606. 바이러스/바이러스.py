import sys
n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
graph = [[] for _ in range(n+1)]

for _ in range(m):
    a,b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(x):
    visited[x] = True
    for y in graph[x]:
        if visited[y]: continue
        dfs(y)

visited = [False] * (n+1)
dfs(1)
print(sum(visited)-1)