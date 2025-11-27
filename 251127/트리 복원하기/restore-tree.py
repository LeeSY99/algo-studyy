n = int(input())
graph = [[0]*(n+1) for _ in range(n+1)]

# Please write your code here.
for i in range(1,n+1):
    arr = [0] + list(map(int, input().split()))
    for j in range(1,n+1):
        graph[i][j] = arr[j]

dist = [float('inf')] * (n+1)
visited = [False] * (n+1)
dist[1] = 0
ans = 0
dist_from = [0] * (n + 1)
edges = []
for i in range(1,n+1):
    min_index = -1
    for j in range(1,n+1):
        if visited[j] : continue
        if min_index == -1 or dist[min_index] > dist[j]:
            min_index = j

    visited[min_index]=True
    
    if min_index != 1:
        edges.append((min(min_index, dist_from[min_index]),
        max(min_index, dist_from[min_index]), 
        dist[min_index]))
    ans += dist[min_index]

    for j in range(1,n+1):
        if graph[min_index][j] == 0:
            continue
        if dist[j] > graph[min_index][j]:
            dist[j] = graph[min_index][j]
            dist_from[j] = min_index

edges.sort()
for a,b,w, in edges:
    print(a,b,w)

