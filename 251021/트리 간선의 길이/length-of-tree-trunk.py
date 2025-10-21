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


for i in range(1,n+1):
    visited = [False] * (n+1)
    visited[i] = True
    search(i, i)


ans = 0
for d in dist:
    d_max = max(d)
    ans = max(ans, d_max)
print(ans)