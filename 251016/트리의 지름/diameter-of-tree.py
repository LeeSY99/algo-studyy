n = int(input())
edges =[[] for _ in range(n + 1)]
visited = [False] * (n + 1)
dist = [0] * (n + 1)

for _ in range(n - 1):
    x, y, d = tuple(map(int, input().split()))
    # 간선 정보를 인접리스트에 넣어줍니다.
    edges[x].append((y, d))
    edges[y].append((x, d))

def dfs(x, total_dist):
    for y, d in edges[x]:
        if not visited[y]:
            visited[y] = True
            dist[y] = total_dist + d
            dfs(y, total_dist + d)

def calc(x):
    for i in range(1,n+1):
        visited[i] = False
        dist[i] = 0

    visited[x] = True
    dist[x] = 0
    dfs(x,0)

    fatherest = 0
    fatherest_node = None
    for i in range(1,n+1):
        if dist[i] > fatherest:
            fatherest = dist[i]
            fatherest_node = i
    return fatherest_node, fatherest

fatherest_node, _ = calc(1)
_, ans = calc(fatherest_node)
print(ans)