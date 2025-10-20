n = int(input())
edges = [[] for _ in range(n+1)]
import sys
sys.setrecursionlimit(100000)
for _ in range(n-1):
    u,v = map(int, input().split())
    edges[u].append(v)
    edges[v].append(u)

def dfs(x, depth):
    global ans
    cnt = 0
    for y in edges[x]:
        if not visited[y]:
            visited[y] = True
            cnt += 1
            dfs(y,depth + 1)
    if cnt == 0:
        ans += depth

visited = [False] * (n+1)
visited[1] = True
ans = 0
dfs(1,0)
print(ans%2)
