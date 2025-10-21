n = int(input())
edges = [[] for _ in range(n+1)]
for _ in range(n-1):
    a,b = map(int, input().split())
    edges[a].append(b)
    edges[b].append(a)

def search(x):
    global max_dist, max_node
    for y in edges[x]:
        if visited[y]: continue
        visited[y] = True
        dist[y] = dist[x] + 1
        if dist[y] > max_dist:
            max_dist = dist[y]
            max_node = y
        search(y)

ans = float('inf')
for i in range(1,n+1):
    visited = [False] * (n+1)
    visited[i] = True
    dist = [0] * (n+1)
    max_dist = 0
    max_node = 0
    search(i)
    ans = min(ans, max_dist)

print(ans)