n,m = map(int, input().split())

dist = [[float('inf')] * (n+1) for _ in range(n+1)]
for _ in range(m):
    a,b,d = map(int, input().split())
    dist[a][b] = d

for i in range(1,n+1):
    dist[i][i] = 0

for k in range(1,n+1):
    for i in range(1,n+1):
        for j in range(1,n+1):
            dist[i][j] = min(dist[i][j], dist[i][k]+dist[k][j])

ans = float('inf')
for i in range(1,n+1):
    for j in range(i+1, n+1):
        ans = min(ans, dist[i][j]+dist[j][i])

print(ans)
