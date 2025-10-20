n, m = map(int, input().split())

edges = [tuple(map(int, input().split())) for _ in range(n - 1)]
queries = [tuple(map(int, input().split())) for _ in range(m)]

# Please write your code here.
dist = [[] for _ in range(n+1)]
for u,v,d in edges:
    dist[u].append((v,d))
    dist[v].append((u,d))

def dfs(x, visited, target, ans):
    if x == target:
        print(ans)
        return
    for y,d in dist[x]:
        if not visited[y]:
            visited[y] = True
            dfs(y, visited, target, ans+d)

def get_dist(a,b):
    visited = [False] * (n+1)
    visited[a] = True
    # print(f'{a} -> {b}')
    dfs(a,visited,b,0)

    

    
for a, b in queries:
    get_dist(a,b)
    