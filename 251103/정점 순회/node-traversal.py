n, s, d = map(int, input().split())
import sys
sys.setrecursionlimit(100000)
graph = [[] for _ in range(n+1)]
for _ in range(n-1):
    a,b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

colored = [False] * (n+1)
#가장 먼 리프노드 까지의 거리
dist = [0] * (n+1)
visited = [False]*(n+1)

def dfs(x):
    visited[x] = True
    for y in graph[x]:
        if visited[y]: continue
        dfs(y)
        dist[x] = max(dist[x], 1+dist[y])

dfs(s)
# print(dist)

ans = 0
for i in range(1, n+1):
    if i == s:
        continue
    if dist[i] >= d:
        ans += 1
print(2*ans)

    






