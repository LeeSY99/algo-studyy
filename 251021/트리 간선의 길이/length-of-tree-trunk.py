n = int(input())
edges = [[] for _ in range(n+1)]

for _ in range(n-1):
    a,b,w = map(int, input().split())
    edges[a].append((b,w))
    edges[b].append((a,w))


dist = [[0] * (n+1) for _ in range(n+1)]

# start 에서 모든 접접 사이의 거리
def search(start, x):
    for y,d in edges[x]:
        if not visited[y]:
            visited[y] = True
            dist[start][y] = dist[start][x] + d
            search(start,y)

visited = [False] * (n+1)
search(1, 1)
fatherest = 0
fatherest_node = 0
for i in range(1,n+1):
    if dist[1][i] > fatherest:
        fatherest_node = i

visited = [False] * (n+1)
dist = [[0] * (n+1) for _ in range(n+1)]
search(fatherest_node, fatherest_node)
ans = max(dist[fatherest_node])
print(ans)

