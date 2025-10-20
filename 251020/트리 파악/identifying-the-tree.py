n = int(input())
edges = [[] for _ in range(n+1)]
import sys
sys.setrecursionlimit(100000)
for _ in range(n-1):
    u,v = map(int, input().split())
    edges[u].append(v)
    edges[v].append(u)

marker = []
def dfs(x, depth):
    cnt = 0
    for y in edges[x]:
        if not visited[y]:
            visited[y] = True
            cnt += 1
            dfs(y,depth + 1)
    if cnt == 0:
        marker.append((x, depth))
visited = [False] * (n+1)
visited[1] = True
dfs(1,0)

ans = 0
for _, depth in marker:
    ans += depth
print(ans%2)
