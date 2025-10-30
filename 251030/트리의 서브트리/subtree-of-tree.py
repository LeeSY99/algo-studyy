n,r,q = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(n-1):
    a,b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

parent = [0] * (n+1)
sub_cnt = [1] * (n+1)
def dfs(x):
    visited[x] = True
    for y in graph[x]:
        if not visited[y]:
            parent[y] = x
            dfs(y)
    
    for y in graph[x]:
        if parent[y] != x:
            continue
        sub_cnt[x] += sub_cnt[y]

visited = [False] * (n+1)
dfs(r)
for _ in range(q):
    node = int(input())
    print(sub_cnt[node])
    

