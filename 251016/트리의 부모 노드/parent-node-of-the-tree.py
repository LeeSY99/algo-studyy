n = int(input())
parent = [0] * (n+1)
edges = [[] for _ in range(n + 1)]
visited = [False] * (n+1)

for _ in range(n-1):
    a,b = map(int, input().split())
    edges[a].append(b)
    edges[b].append(a)

def search(x):
    for y in edges[x]:
        if not visited[y]:
            visited[y] = True
            parent[y] = x
            search(y)

visited[1] = True
search(1)
for i in range(2,n+1):
    print(parent[i])