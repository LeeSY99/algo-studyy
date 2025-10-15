n,m = map(int, input().split())

dist = [[float('inf')] * (n+1) for _ in range(n+1)]
for _ in range(m):
    u,v,d = map(int, input().split())
    dist[u][v] = min(dist[u][v], d)

for i in range(1,n+1):
    dist[i][i] = 0

for k in range(1,n+1):
    for i in range(1,n+1):
        for j in range(1,n+1):
            dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

for i in range(1,n+1):
    for j in range(1,n+1):
        if dist[i][j] == float('inf'):
            print(-1, end = ' ')
        else:
            print(dist[i][j], end = ' ')
    print()