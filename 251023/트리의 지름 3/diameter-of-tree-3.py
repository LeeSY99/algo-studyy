n = int(input())
graph = [[] for _ in range(n+1)]

for _ in range(n-1):
    a,b,w = map(int, input().split())
    graph[a].append((b, w))
    graph[b].append((a, w))


def dfs(x, ignore_num):
    global fatherest, fatherest_node
    visited[x] = True

    for y,d in graph[x]:
        if visited[y]:
            continue
        visited[y] = True
        dist[y] = dist[x] + d
        if dist[y] > fatherest and y != ignore_num:
            fatherest = dist[y]
            fatherest_node = y
        dfs(y, ignore_num)
        

visited = [False] * (n+1)
dist = [0] * (n+1)
fatherest = 0
fatherest_node = None
dfs(1,0)
a = fatherest_node


visited = [False] * (n+1)
dist = [0] * (n+1)
fatherest = 0
dfs(a,0)

b = fatherest_node

ans = 0
##2번째
visited = [False] * (n+1)
dist = [0] * (n+1)
fatherest = 0
dfs(a, b)

ans = max(ans, fatherest)

visited = [False] * (n+1)
dist = [0] * (n+1)
fatherest = 0
dfs(b, a)
ans = max(ans, fatherest)

print(ans)
