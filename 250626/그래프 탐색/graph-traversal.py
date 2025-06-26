n, m = map(int, input().split())

visited = [0] * (n+1)
graph = [[] for _ in range(n+1)]

for _ in range(m):
    start, end = map(int, input().split())
    graph[start].append(end)
    graph[end].append(start)


count = 0
def dfs(v):
    global count
    visited[v] = 1
    count +=1

    for neighbor in graph[v]:
        if visited[neighbor] == 0:
            dfs(neighbor)

dfs(1)
print(count-1)
        
    