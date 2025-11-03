n, s, d = map(int, input().split())

graph = [[] for _ in range(n+1)]
for _ in range(n-1):
    a,b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

colored = [False] * (n+1)
dist = [0] * (n+1)
visited = [False]*(n+1)

def dfs(x, f):
    dist[x] = f
    visited[x] = True
    for y in graph[x]:
        if visited[y]: continue
        dfs(y, f+1)

dfs(s, 0)
# print(dist)

visited = [False]*(n+1)
# ans = 0
# def search(x, f):
#     visited[x] = True
#     for y in graph[x]:
#         if visited[y]: continue
#         dist[y] -= 1
ans = max(dist)-d
if ans <= 0:
    print(0)
else:
    print(2*ans)


    






